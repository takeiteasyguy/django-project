# -*- coding: utf-8 -*-
from django.test import TestCase
from models import Section


class SectionTestCase(TestCase):
    def setUp(self):
        Section.objects.create(name=u'имя',
                               img='/static/catalog/img/test_news_1.jpg',
                               desc='testdesc',)

    def test_section(self):
        section = Section.objects.get(name='имя')