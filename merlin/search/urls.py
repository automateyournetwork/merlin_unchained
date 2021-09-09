from django.urls import path
from .views import SearchView, SearchResultView

urlpatterns = [
    path('Search/', SearchView.as_view(), name="search"),
    path('Search/results/', SearchResultView.as_view(), name="search_results"),
]