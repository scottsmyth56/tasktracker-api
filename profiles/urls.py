from django.urls import path
from .views import UserSearchView

urlpatterns = [
    path('search-users/', UserSearchView.as_view(), name='search-users'),
]
