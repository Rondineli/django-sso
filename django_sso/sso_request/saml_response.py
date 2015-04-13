# -*- coding: utf-8 -*-


import time
import zlib
import base64
from xml.dom.minidom import parseString

from saml2.saml import AuthnStatement, Subject, SubjectConfirmation,\
    SubjectConfirmationData, Conditions, Audience, AudienceRestriction,\
    AuthnContext, AuthnContextClassRef, Assertion, NameID, Issuer
from saml2.samlp import Response, Status, StatusCode
from saml2.utils import createID, sign
from xmldsig import Signature, SignedInfo, Reference, DigestValue, DigestMethod,\
    Transform, Transforms, SignatureMethod, CanonicalizationMethod,\
    SignatureValue

import datetime

from django_auth_ldap.backend import LDAPBackend


class SAML2Response:
    """
    Obs: rewrite code for pep8
    Class for SAML 2.0 response construction.
    Tested with Google Apps.
    See sample response at:
    http://code.google.com/p/google-apps-sso-sample/source/browse/trunk/php/SAMLTestTool/templates/SamlResponseTemplate.xml
    """

    def __init__(self, private_key_file_name, certificate_file_name):
        self.private_Key_file_name = private_key_file_name
        self.certificate_file_name = certificate_file_name

    issuer = 'HogofogoIDP'
    validityInterval = 5    # in minutes

    def get_login_response(self, request, user):
        saml_req = self._parse_saml_request(request)
        assertion = self._get_saml_assertion(user, saml_req)
        return (assertion, saml_req['ACS'])

    def _create_subject_elem(self, user,
                             saml_req, not_before,
                             not_on_or_after):
        name_id = NameID(
            format='urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress',
            text=user
        )
        scd = SubjectConfirmationData(not_before=not_before,
                                      not_on_or_after=not_on_or_after,
                                      recipient=saml_req['ACS'],
                                      in_response_to=saml_req['ID'])
        sc = SubjectConfirmation('urn:oasis:names:tc:SAML:2.0:cm:bearer',
                                 subject_confirmation_data=scd)
        subject = Subject(name_id=name_id, subject_confirmation=sc)
        return subject

    def _create_conditions_elem(self, saml_req, not_before, not_on_or_after):
        ar = AudienceRestriction(audience=Audience(text=saml_req['ACS']))
        return Conditions(not_before=not_before,
                          not_on_or_after=not_on_or_after,
                          audience_restriction=ar)

    def _create_authn_statement_elem(self, user):
        cref_str = 'urn:oasis:names:tc:SAML:2.0:ac:classes:Password'
        ac = AuthnContext(
            authn_context_class_ref=AuthnContextClassRef(
                text=cref_str
            )
        )
        print "create_auth_user => %s" % (user)
        user = LDAPBackend().populate_user(user)
        print "create_auth_user => %s" % (user)
        if user is not None:
            last_login_gmt = user.last_login.strftime("%Y-%m-%dT%H:%M:%SZ")

        else:
            last_login_gmt = not_before = time.strftime(
                "%Y-%m-%dT%H:%M:%SZ",
                time.gmtime()
            )
        ass = AuthnStatement(authn_instant=last_login_gmt,
                             authn_context=ac)
        return ass

    def _create_signature(self):
        ref = Reference(uri='',
                        transforms=Transforms(
                            transform=Transform(
                                algorithm='http://www.w3.org/2000/09/xmldsig#enveloped-signature'
                            )
                        ),
                        digest_method=DigestMethod(
                            algorithm='http://www.w3.org/2000/09/xmldsig#sha1'
                        ),
                        digest_value=DigestValue(text=''))
        s_info = SignedInfo(
            canonicalization_method=CanonicalizationMethod(
                algorithm='http://www.w3.org/TR/2001/REC-xml-c14n-20010315#WithComments'
            ),
            signature_method=SignatureMethod(
                algorithm='http://www.w3.org/2000/09/xmldsig#%s-sha1' % 'rsa'
            ),
            reference=ref
        )
        return Signature(
            signed_info=s_info,
            signature_value=SignatureValue(text='')
        )

    def _post_process(self, assertion):
        """
        Currently sign with the private key and also include the
        certificate in the SAML response.
        """
        return sign(
            str(assertion),
            self.private_Key_file_name,
            self.certificate_file_name
        )

    def _get_saml_assertion(self, user, saml_reqest):
        """
        Return a SAML assertion for the user.
        """
        # Create a conditions timeframe (period in which assertion is valid)
        not_before = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
        not_on_or_after = time.strftime(
            "%Y-%m-%dT%H:%M:%SZ",
            time.gmtime(
                time.time() + self.validityInterval
            )
        )
        subject = self._create_subject_elem(
            user,
            saml_reqest,
            not_before,
            not_on_or_after
        )
        conditions = self._create_conditions_elem(
            saml_reqest,
            not_before,
            not_on_or_after
        )
        auth_statement = self._create_authn_statement_elem(user)
        # Create the actual assertion
        assertion = Assertion(id=createID(),
                              version='2.0',
                              issue_instant=not_before,
                              issuer=Issuer(text=self.issuer),
                              subject=subject,
                              conditions=conditions,
                              authn_statement=auth_statement)
        response = Response(
            id=createID(),
            version='2.0',
            issue_instant=not_before,
            signature=self._create_signature(),
            status=Status(
                status_code=StatusCode(
                    value='urn:oasis:names:tc:SAML:2.0:status:Success'
                )
            ),
            assertion=assertion
        )

        return self._post_process(response)

    def _b64decode_and_decompress(self, encoded_data):
        decoded_data = base64.b64decode(encoded_data)
        return zlib.decompress(decoded_data, -15)

    def _parse_saml_request(self, request):
        encoded_saml_req = request.GET.get('SAMLRequest', None)
        saml_request = self._b64decode_and_decompress(encoded_saml_req)
        req_dom = parseString(saml_request)
        req = req_dom.getElementsByTagName('samlp:AuthnRequest')[0]
        return {
            'ID': req.attributes['ID'].value,
            'IssueInstant': req.attributes['IssueInstant'].value,
            'ProviderName': req.attributes['ProviderName'].value,
            'ACS': req.attributes['AssertionConsumerServiceURL'].value,
        }
