#! coding: utf-8
from django.db import models
from django.shortcuts import get_object_or_404
# Create your models here.


class Section(models.Model):
    name = models.CharField(max_length=200)
    latin_name = models.CharField(max_length=200)
    img = models.ImageField(upload_to='media/images/sections/')
    desc = models.TextField(blank=True)
    pub_date = models.DateField(auto_now=True)

    class Meta:
        verbose_name = 'Раздел'
        verbose_name_plural = 'Разделы каталога'

    def __unicode__(self):
        return self.latin_name

    def save(self, *args, **kwargs):
        if not self.latin_name:
            self.latin_name = self.tr_name()
        super(Section, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return '/catalog/' + self.latin_name

    def tr_name(self):
        from catalog.transliterator import ru_to_en_converter
        return ru_to_en_converter(self.name)


class Commodity(models.Model):
    name = models.CharField(max_length=200)
    latin_name = models.CharField(max_length=200)
    img = models.ImageField(upload_to='media/images/commodities/')
    desc = models.TextField()
    section = models.ForeignKey(Section)
    pub_date = models.DateField(auto_now=True)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __unicode__(self):
        return self.latin_name

    def save(self, *args, **kwargs):
        if not self.latin_name:
            self.latin_name = self.removebadchars(self.tr_name())
        super(Commodity, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return '/catalog/' + self.current_section().__unicode__() + '/' + self.latin_name + '/'

    def tr_name(self):
        from catalog.transliterator import ru_to_en_converter
        return ru_to_en_converter(self.name)

    def current_section(self):
        return self.section

    def removebadchars(self, value):
        for c in r'\/:*?"<>|':
            value = value.replace(c, '')
        return value



class ColorScheme(models.Model):
    name = models.CharField(max_length=200)
    img = models.ImageField(upload_to=lambda self, filename: 'media/images/colorschemes/{0}/pictures/{1}'.format(
        self.removebadchars(self.current_commodity().__unicode__()), self.removebadchars(filename)))
    thumbnail = models.ImageField(upload_to=lambda self, filename: 'media/images/colorschemes/{0}/thumbnail/{1}'.format(
        self.removebadchars(self.current_commodity().__unicode__()), self.removebadchars(filename)))
    commodity = models.ForeignKey(Commodity)
    pub_date = models.DateField(auto_now=True)

    class Meta:
        verbose_name = 'Цветовая схема'
        verbose_name_plural = 'Цветовые схемы'

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return '/catalog/' + self.current_section() + '/' + self.current_commodity().__unicode__() + '/'

    def current_commodity(self):
        return self.commodity

    def current_section(self):
        section_id = get_object_or_404(Commodity, latin_name=self.current_commodity()).section_id
        return get_object_or_404(Section, id=section_id).latin_name

    def removebadchars(self, value):
        for c in r'\/:*?"<>|':
            value = value.replace(c, '')
        return value
