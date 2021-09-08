from django.urls import path
from .views import SearchView, SearchLearnVLANView

urlpatterns = [
    path('Search/', SearchView.as_view(), name="search"),
    path('Search/learn_vlan/', SearchLearnVLANView.as_view(), name="learn_vlan_search_results"),
]