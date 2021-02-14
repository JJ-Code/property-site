from django.urls import path

from . import views

# /listings/23 for single page. don't need to do listing/23 here bc will do it in main urls 
urlpatterns = [
    path('', views.index, name='listings'),
    path('<int:listing_id>', views.listing, name='listing'),
    path('search', views.search, name='search')
]
