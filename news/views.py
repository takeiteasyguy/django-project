from django.views import generic
from news.models import PieceOfNews
from django.template.context import RequestContext
from django.shortcuts import render_to_response, get_object_or_404

# Create your views here.


class NewsView(generic.ListView):
    template_name = 'news/news.html'
    context_object_name = 'news_list'
    allow_empty = True

    def get_queryset(self):
        return PieceOfNews.objects.all()


def detail_view(request, latin_name):
    piece = get_object_or_404(PieceOfNews, latin_name=latin_name)
    context = RequestContext(request, {'piece': piece})
    return render_to_response('news/detail.html', context)