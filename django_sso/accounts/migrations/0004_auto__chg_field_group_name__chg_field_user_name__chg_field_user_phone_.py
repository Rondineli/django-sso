# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Group.name'
        db.alter_column(u'accounts_group', 'name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=80))

        # Changing field 'User.name'
        db.alter_column(u'accounts_user', 'name', self.gf('django.db.models.fields.CharField')(max_length=80))

        # Changing field 'User.phone'
        db.alter_column(u'accounts_user', 'phone', self.gf('django.db.models.fields.CharField')(max_length=18, null=True))

        # Changing field 'User.team'
        db.alter_column(u'accounts_user', 'team', self.gf('django.db.models.fields.CharField')(max_length=40, null=True))

        # Changing field 'User.email'
        db.alter_column(u'accounts_user', 'email', self.gf('django.db.models.fields.EmailField')(unique=True, max_length=100))

    def backwards(self, orm):

        # Changing field 'Group.name'
        db.alter_column(u'accounts_group', 'name', self.gf('django.db.models.fields.CharField')(max_length=200, unique=True))

        # Changing field 'User.name'
        db.alter_column(u'accounts_user', 'name', self.gf('django.db.models.fields.CharField')(max_length=200))

        # Changing field 'User.phone'
        db.alter_column(u'accounts_user', 'phone', self.gf('django.db.models.fields.CharField')(max_length=200, null=True))

        # Changing field 'User.team'
        db.alter_column(u'accounts_user', 'team', self.gf('django.db.models.fields.CharField')(max_length=200, null=True))

        # Changing field 'User.email'
        db.alter_column(u'accounts_user', 'email', self.gf('django.db.models.fields.EmailField')(max_length=200, unique=True))

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
            'team': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True'})
        },
        u'companies.company': {
            'Meta': {'object_name': 'Company'},
            'creation_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'modification_time': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'})
        },
        u'dashboards.dashboard': {
            'Meta': {'unique_together': "(('name', 'company'),)", 'object_name': 'Dashboard'},
            'company': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['companies.Company']"}),
            'creation_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modification_time': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'}),
            'source': ('django.db.models.fields.TextField', [], {})
        },
        u'perspectives.perspective': {
            'Meta': {'unique_together': "(('name', 'company'),)", 'object_name': 'Perspective'},
            'company': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['companies.Company']"}),
            'creation_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'dashboards': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['dashboards.Dashboard']", 'symmetrical': 'False'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modification_time': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['accounts']