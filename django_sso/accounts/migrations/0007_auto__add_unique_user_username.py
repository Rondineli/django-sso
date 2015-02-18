# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding unique constraint on 'User', fields ['username']
        db.create_unique(u'accounts_user', ['username'])


    def backwards(self, orm):
        # Removing unique constraint on 'User', fields ['username']
        db.delete_unique(u'accounts_user', ['username'])


    models = {
        u'accounts.group': {
            'Meta': {'object_name': 'Group'},
            'creation_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modification_time': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'perspectives': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['perspectives.Perspective']", 'symmetrical': 'False'}),
            'role': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'users': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['accounts.User']", 'symmetrical': 'False'})
        },
        u'accounts.user': {
            'Meta': {'object_name': 'User'},
            'creation_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_admin': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'modification_time': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80', 'db_index': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '18', 'null': 'True'}),
            'team': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'alerts.alert': {
            'Meta': {'object_name': 'Alert', '_ormbases': [u'ceprules.CEPRule']},
            u'ceprule_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['ceprules.CEPRule']", 'unique': 'True', 'primary_key': 'True'}),
            'doc': ('django.db.models.fields.TextField', [], {}),
            'expire_time': ('django.db.models.fields.IntegerField', [], {'default': '60'}),
            'recipients': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['recipients.Recipient']", 'symmetrical': 'False'}),
            'severity': ('django.db.models.fields.CharField', [], {'max_length': '80'})
        },
        u'ceprules.ceprule': {
            'Meta': {'unique_together': "(('name', 'company'),)", 'object_name': 'CEPRule'},
            'company': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['companies.Company']"}),
            'creation_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'modification_time': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80', 'db_index': 'True'}),
            'syntax': ('django.db.models.fields.TextField', [], {})
        },
        u'companies.company': {
            'Meta': {'object_name': 'Company'},
            'api_key': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '64'}),
            'creation_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'modification_time': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'})
        },
        u'dashboards.dashboard': {
            'Meta': {'unique_together': "(('name', 'company'),)", 'object_name': 'Dashboard'},
            'alerts': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['alerts.Alert']", 'symmetrical': 'False'}),
            'company': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['companies.Company']"}),
            'creation_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'datasources': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['datasources.Datasource']", 'symmetrical': 'False'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'max_history_days': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '180'}),
            'modification_time': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'source': ('django.db.models.fields.TextField', [], {})
        },
        u'datasources.datasource': {
            'Meta': {'object_name': 'Datasource', '_ormbases': [u'ceprules.CEPRule']},
            u'ceprule_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['ceprules.CEPRule']", 'unique': 'True', 'primary_key': 'True'}),
            'flow_id': ('django.db.models.fields.CharField', [], {'max_length': '80'})
        },
        u'perspectives.perspective': {
            'Meta': {'unique_together': "(('name', 'company'),)", 'object_name': 'Perspective'},
            'alerts': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['alerts.Alert']", 'symmetrical': 'False'}),
            'company': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['companies.Company']"}),
            'creation_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'dashboards': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['dashboards.Dashboard']", 'symmetrical': 'False'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modification_time': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80'})
        },
        u'recipients.recipient': {
            'Meta': {'unique_together': "(('scheme', 'name'),)", 'object_name': 'Recipient'},
            'creation_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'destination': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modification_time': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'scheme': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['accounts']