# -*- coding: utf-8 -*-
import re
from xml.etree import ElementTree as etree

from django.core.management import BaseCommand, CommandError
from django.utils.translation import ugettext_lazy as _
from bjcp.models import Category, Style, BJCPGuideline


class Command(BaseCommand):
    args = '<xml_file>'
    help = _(u'imports bjcp style guidelines from oficial xml file')

    def _clean_text(self, text):
        if text:
            return re.sub(' +', ' ', text).strip().replace('\'', '\'\'').replace('\n', ' ')
        else:
            return u''

    def _get_min_max(self, child, kind):
        stats = child.find(kind)
        if stats is not None:
            min, max = stats.find('low').text, stats.find('high').text
            min = min if min else u''
            max = max if max else u''
            return min, max
        else:
            return u'', u''

    def _extract_text(self, node):

        node_text = node.text if node.text else u''

        for child in node:
            node_text += u'<' + child.tag + u'>' + child.text + u'</' + child.tag + u'>'
            node_text += child.tail if child.tail else u''

        node_text += node.tail

        return self._clean_text(node_text)

    def _process_file(self, file_path):
        tree = etree.parse(file_path)
        root = tree.getroot()
        for child in root:
            style_type = child.get('type')
            if style_type == 'beer':
                guideline, created = BJCPGuideline.objects.get_or_create(year=2008)
                for category_xml in child:
                    category_id = category_xml.get('id')
                    category_name = category_xml.find('name').text
                    category, created = Category.objects.get_or_create(id=category_id, guideline=guideline)
                    category.name = category_name
                    if created:
                        category.save()

                    for style_xml in category_xml.findall('subcategory'):
                        style_subcategory = style_xml.get('id')
                        style, created = Style.objects.get_or_create(category=category, subcategory=style_subcategory)
                        style.name = style_xml.find('name').text
                        style.aroma = self._extract_text(style_xml.find('aroma'))
                        style.appearance = self._extract_text(style_xml.find('appearance'))
                        style.flavor = self._extract_text(style_xml.find('flavor'))
                        style.mouthfeel = self._extract_text(style_xml.find('mouthfeel'))
                        style.impression = self._extract_text(style_xml.find('impression'))
                        style.comments = self._extract_text(style_xml.find('comments')) if style_xml.find(
                            'comments') is not None else u''
                        style.history = self._extract_text(style_xml.find('history')) if style_xml.find(
                            'history') is not None else u''
                        style.ingredients = self._extract_text(style_xml.find('ingredients')) if style_xml.find(
                            'ingredients') is not None else u''
                        style.examples = self._extract_text(style_xml.find('examples')) if style_xml.find(
                            'examples') is not None else u''
                        stats = style_xml.find('stats')
                        if stats is not None:
                            style.low_og, style.high_og = self._get_min_max(stats, 'og')
                            style.low_fg, style.high_fg = self._get_min_max(stats, 'fg')
                            style.low_abv, style.high_abv = self._get_min_max(stats, 'abv')
                            style.low_ibu, style.high_ibu = self._get_min_max(stats, 'ibu')
                            style.low_srm, style.high_srm = self._get_min_max(stats, 'srm')
                            if stats.find('exceptions') is not None:
                                style.exceptions = stats.find('exceptions').text

                        style.save()

    def handle(self, *args, **options):
        if len(args) == 1:
            self._process_file(args[0])
        else:
            raise CommandError(_(u'This command only accepts one xml file as argumento'))