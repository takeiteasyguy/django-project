from news.models import PieceOfNews
# -*- coding: utf-8 -*-

def cont_proc(request):
    return {
        'news': PieceOfNews.objects.all(),
    }