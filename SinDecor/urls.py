from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from contact import views as contact_views
from django.contrib import admin
from django.conf import settings
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    (r"^$", TemplateView.as_view(template_name="main.html")),
    url(r'^catalog/', include('catalog.urls', namespace="catalog")),
    url(r'^news/', include('news.urls', namespace="news")),
    url(r'^contact/', include('contact.urls', namespace='contact')),
    url(r'^sale/', TemplateView.as_view(template_name="sale.html")),
    url(r'^thanks/$', contact_views.thanks, name='thanks'),
    url(r'^search/', include('haystack.urls')),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}))
