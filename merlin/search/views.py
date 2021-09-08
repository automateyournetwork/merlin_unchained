from django.views.generic import TemplateView, ListView
from django.db.models import Q
from merlin.models import LearnVLAN

class SearchView(TemplateView):
    template_name = 'Search/search.html'

class SearchLearnVLANView(ListView):
    model = LearnVLAN
    template_name = 'Search/LearnVLAN/learn_vlan_search_results.html'

    def get_queryset(self): # new
        query = self.request.GET.get('q')
        object_list = LearnVLAN.objects.filter(
            Q(pyats_alias=query) | Q(os=query) | Q(vlan=query) | Q(interfaces=query) | Q(mode=query) | Q(name=query) | Q(shutdown=query) | Q(state=query)
        )
        return object_list    