# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'BJCPGuideline'
        db.create_table(u'bjcp_bjcpguideline', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('year', self.gf('django.db.models.fields.PositiveIntegerField')()),
        ))
        db.send_create_signal(u'bjcp', ['BJCPGuideline'])

        # Adding model 'Category'
        db.create_table(u'bjcp_category', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('guideline', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bjcp.BJCPGuideline'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'bjcp', ['Category'])

        # Adding model 'Style'
        db.create_table(u'bjcp_style', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bjcp.Category'])),
            ('subcategory', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('aroma', self.gf('django.db.models.fields.TextField')()),
            ('appearance', self.gf('django.db.models.fields.TextField')()),
            ('flavor', self.gf('django.db.models.fields.TextField')()),
            ('mouthfeel', self.gf('django.db.models.fields.TextField')()),
            ('impression', self.gf('django.db.models.fields.TextField')()),
            ('comments', self.gf('django.db.models.fields.TextField')()),
            ('history', self.gf('django.db.models.fields.TextField')()),
            ('ingredients', self.gf('django.db.models.fields.TextField')()),
            ('examples', self.gf('django.db.models.fields.TextField')()),
            ('low_og', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('high_og', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('low_fg', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('high_fg', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('low_abv', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('high_abv', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('low_ibu', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('high_ibu', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('low_srm', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('high_srm', self.gf('django.db.models.fields.CharField')(max_length=5)),
        ))
        db.send_create_signal(u'bjcp', ['Style'])


    def backwards(self, orm):
        # Deleting model 'BJCPGuideline'
        db.delete_table(u'bjcp_bjcpguideline')

        # Deleting model 'Category'
        db.delete_table(u'bjcp_category')

        # Deleting model 'Style'
        db.delete_table(u'bjcp_style')


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
            'flavor': ('django.db.models.fields.TextField', [], {}),
            'high_abv': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'high_fg': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'high_ibu': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'high_og': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'high_srm': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'history': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'impression': ('django.db.models.fields.TextField', [], {}),
            'ingredients': ('django.db.models.fields.TextField', [], {}),
            'low_abv': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'low_fg': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'low_ibu': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'low_og': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'low_srm': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'mouthfeel': ('django.db.models.fields.TextField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'subcategory': ('django.db.models.fields.CharField', [], {'max_length': '3'})
        }
    }

    complete_apps = ['bjcp']