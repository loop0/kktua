# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Beer.style'
        db.add_column(u'brewery_beer', 'style',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bjcp.Style'], null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Beer.style'
        db.delete_column(u'brewery_beer', 'style_id')


    models = {
        u'bjcp.bjcpguideline': {
            'Meta': {'ordering': "('-year',)", 'object_name': 'BJCPGuideline'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'year': ('django.db.models.fields.PositiveIntegerField', [], {})
        },
        u'bjcp.category': {
            'Meta': {'ordering': "('guideline', 'id')", 'object_name': 'Category'},
            'guideline': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['bjcp.BJCPGuideline']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'bjcp.style': {
            'Meta': {'ordering': "('category', 'subcategory')", 'object_name': 'Style'},
            'appearance': ('django.db.models.fields.TextField', [], {}),
            'aroma': ('django.db.models.fields.TextField', [], {}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['bjcp.Category']"}),
            'comments': ('django.db.models.fields.TextField', [], {}),
            'examples': ('django.db.models.fields.TextField', [], {}),
            'exceptions': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'flavor': ('django.db.models.fields.TextField', [], {}),
            'high_abv': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'high_fg': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'high_ibu': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'high_og': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'high_srm': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'history': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'impression': ('django.db.models.fields.TextField', [], {}),
            'ingredients': ('django.db.models.fields.TextField', [], {}),
            'low_abv': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'low_fg': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'low_ibu': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'low_og': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'low_srm': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'mouthfeel': ('django.db.models.fields.TextField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'subcategory': ('django.db.models.fields.CharField', [], {'max_length': '3'})
        },
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
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'style': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['bjcp.Style']", 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['brewery']