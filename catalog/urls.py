from django.conf.urls import patterns, url
from catalog import views

urlpatterns = patterns('',
    url(r'^$', views.CatalogView.as_view(), name='catalog'),
    url(r'(?P<latin_name>[\w_ ]+)$', views.commodity_view, name='commodity'),
    url(r'(?P<section>[\W\w]+)/(?P<latin_name>[\W\w]+)/$', views.detail_view, name='detail'),
)
