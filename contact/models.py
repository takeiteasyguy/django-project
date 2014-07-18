#! coding: utf-8
from django.db import models
from django.forms import ModelForm, Textarea


class Contact(models.Model):
    title = models.CharField('Тема:', max_length=100)
    name = models.CharField('Имя:', max_length=100)
    mail = models.EmailField('Электронный адрес:', max_length=100)
    text = models.TextField('Сообщение:')

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'

    def __unicode__(self):
        return '%s' % self.title


class ContactForm(ModelForm):

    class Meta:
        model = Contact
        widgets = {
            'text': Textarea(attrs={
        'cols': 100, 'rows': 6})
        }


class PurchaseContact(models.Model):
    name = models.CharField('Имя:', max_length=100)
    mail = models.EmailField('Номер телефона:', max_length=100)
    text = models.TextField('Удобное время звонка:')

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'

    def __unicode__(self):
        return '%s' % self.title


class PurchaseContactForm(ModelForm):

    class Meta:
        model = PurchaseContact
        widgets = {
            'text': Textarea(attrs={
        'cols': 100, 'rows': 6})
        }