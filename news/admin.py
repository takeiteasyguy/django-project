from django.contrib import admin
from news.models import PieceOfNews
# Register your models here.


class NewsAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name']}),
        (None, {'fields': ['img']}),
        (None, {'fields': ['desc']}),
    ]
    class Media:
        js = (
            '/static/tiny_mce/tiny_mce.js',
            '/static/tiny_mce/tiny_mce_init.js',
        )
    list_display = ('name',)

admin.site.register(PieceOfNews, NewsAdmin)