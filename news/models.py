#! coding: utf-8
from django.db import models
# Create your models here.


class PieceOfNews(models.Model):
    name = models.CharField(max_length=200)
    latin_name = models.CharField(max_length=200)
    img = models.ImageField(upload_to='media/images/news/')
    desc = models.TextField()
    pub_date = models.DateField(auto_now=True)

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.latin_name:
            self.latin_name = self.tr_name()
        super(PieceOfNews, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return '/news/' + self.latin_name

    def tr_name(self):
        from catalog.transliterator import ru_to_en_converter
        return ru_to_en_converter(self.name)



