# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'EmailSubscriber'
        db.create_table(u'email_subscription_emailsubscriber', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('activation_key', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('is_activated', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('activation_request_sent_at', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
        ))
        db.send_create_signal(u'email_subscription', ['EmailSubscriber'])


    def backwards(self, orm):
        # Deleting model 'EmailSubscriber'
        db.delete_table(u'email_subscription_emailsubscriber')


    models = {
        u'email_subscription.emailsubscriber': {
            'Meta': {'object_name': 'EmailSubscriber'},
            'activation_key': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'activation_request_sent_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_activated': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        }
    }

    complete_apps = ['email_subscription']