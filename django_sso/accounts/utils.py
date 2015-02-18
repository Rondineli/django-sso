import ldap

from django.conf import settings


class LdapManipulation(object):
    """
    The class for manipulation in data user for active directory
    """
    def __init__(self, tls=True):
        self.ldap = ldap.initialize(settings.AUTH_LDAP_SERVER_URI)
        self.ldap.simple_bind_s(
            settings.AUTH_LDAP_BIND_DN,
            settings.AUTH_LDAP_BIND_PASSWORD
        )
        self.tls = tls
        if self.tls:
            self.ldap.set_option(ldap.OPT_X_TLS_DEMAND, True)
            self.ldap.set_option(ldap.OPT_DEBUG_LEVEL, 255)

    def renew_connection(self):
        try:
            self.ldap.simple_bind_s(
                settings.AUTH_LDAP_BIND_DN,
                settings.AUTH_LDAP_BIND_PASSWORD
            )
        except Exception as e:
            return e
        else:
            return True

    @renew_connection
    def search_s(self, **kwargs):
        self.ldap.search_s()

    @renew_connection
    def replace_password(self, username, new_password):
        new_password = '\"{}\"'.format(new_password)
        unicode_pass = new_password.encode('iso-8859-1')
        pass_value = unicode_pass.encode('utf-16-le')
        add_pass = [(ldap.MOD_REPLACE, 'unicodePwd', [pass_value])]
        if self.tls:
            try:
                user_dn = self.ldap.search_s(
                    settings.AUTH_LDAP_USER_SEARCH,
                    ldap.SCOPE_SUBTREE,
                    "(SAMAccountName={})".format(username)
                )
            except Exception as e:
                return e
            else:
                try:
                    self.ldap.modify_s(user_dn[0][0], add_pass)
                except Exception as e:
                    return e
                else:
                    return True
        else:
            raise Exception("Replace password is necessary ldaps connection")
