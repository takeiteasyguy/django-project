#! coding: utf-8
from django.conf import settings
from django.views.generic import CreateView
from django.core.mail import send_mail
from models import ContactForm
from django.core.urlresolvers import reverse
from django.shortcuts import render


class ContactCreateView(CreateView):
    form_class = ContactForm
    template_name = 'contact/contacts.html'

    def get_success_url(self):
        return reverse('thanks')

    def form_valid(self, form):
        message = '{name} / {mail} написал: '.format(
            name=form.cleaned_data.get('name').encode('utf-8'),
            mail=form.cleaned_data.get('mail').encode('utf-8')
        )
        message += "\n\n{0}".format(form.cleaned_data.get('text').encode('utf-8'))
        send_mail(
            subject=form.cleaned_data.get('title').encode('utf-8').strip(),
            message=message,
            from_email='journalbeast@gmail.com',
            recipient_list=settings.LIST_OF_EMAIL_RECIPIENTS,
            fail_silently=False
        )
        return super(ContactCreateView, self).form_valid(form)

def thanks(request):
    return render(request, 'contact/thanks.html')