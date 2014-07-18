from django.contrib import admin
from catalog.models import Section, Commodity, ColorScheme
# Register your models here.


class ColorInline(admin.TabularInline):
    model = ColorScheme
    extra = 1


class SectionAdmin(admin.ModelAdmin):
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


class CommodityAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['section']}),
        (None, {'fields': ['name']}),
        (None, {'fields': ['img']}),
        (None, {'fields': ['desc']}),
    ]
    inlines = [
        ColorInline
    ]

    class Media:
        js = (
            '/static/tiny_mce/tiny_mce.js',
            '/static/tiny_mce/tiny_mce_init.js',
        )

    list_display = ('name', 'section')


admin.site.register(Section, SectionAdmin)
admin.site.register(Commodity, CommodityAdmin)