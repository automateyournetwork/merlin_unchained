from django.urls import path
from .views import SearchView, SearchResultAllView, SearchResultStateView, SearchResultConfigView

urlpatterns = [
    path('Search/', SearchView.as_view(), name="search"),
    path('Search/all_results/', SearchResultAllView.as_view(), name="search_results_all"),
    path('Search/state_results/', SearchResultStateView.as_view(), name="search_results_state"),
    path('Search/config_results/', SearchResultConfigView.as_view(), name="search_results_config"),
]