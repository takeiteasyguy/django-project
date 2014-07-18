from django.views import generic
from catalog.models import Section, Commodity, ColorScheme
from django.template.context import RequestContext
from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404

# Create your views here.


class CatalogView(generic.ListView):
    template_name = 'catalog/sections.html'
    context_object_name = 'section_list'
    allow_empty = True

    def get_queryset(self):
        return Section.objects.all()


def commodity_view(request, latin_name):
    section = get_object_or_404(Section, latin_name=latin_name)
    commodities = Commodity.objects.filter(section_id=section.id)
    context = RequestContext(request, {'commodities': commodities, 'section': section})
    return render_to_response('catalog/commodities.html', context)


def detail_view(request, section, latin_name):
    sec = get_object_or_404(Section, latin_name=section)
    current_commodity = get_object_or_404(Commodity, latin_name=latin_name)
    color_schemes = ColorScheme.objects.filter(commodity_id=current_commodity.id)
    context = RequestContext(request, {'color_schemes': color_schemes, 'commodity': current_commodity,
                                       'section': sec})
    return render_to_response('catalog/detail.html', context)

