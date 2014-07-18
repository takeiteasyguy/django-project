from django.conf.urls import patterns, url
from news import views

urlpatterns = patterns('',
    url(r'^$', views.NewsView.as_view(), name='news'),
    url(r'(?P<latin_name>[\w\W]+)$', views.detail_view, name='detail'),
)
