# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Beer'
        db.create_table(u'brewery_beer', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'brewery', ['Beer'])

        # Adding model 'Batch'
        db.create_table(u'brewery_batch', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('beer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['brewery.Beer'])),
            ('quantity', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('brewday', self.gf('django.db.models.fields.DateField')()),
            ('status', self.gf('django.db.models.fields.PositiveIntegerField')(default=1)),
        ))
        db.send_create_signal(u'brewery', ['Batch'])


    def backwards(self, orm):
        # Deleting model 'Beer'
        db.delete_table(u'brewery_beer')

        # Deleting model 'Batch'
        db.delete_table(u'brewery_batch')


    models = {
        u'brewery.batch': {
            'Meta': {'ordering': "('-brewday', 'beer')", 'object_name': 'Batch'},
            'beer': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['brewery.Beer']"}),
            'brewday': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'quantity': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'status': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1'})
        },
        u'brewery.beer': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Beer'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['brewery']