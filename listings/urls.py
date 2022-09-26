from django.urls import path

from . import views
# first url pattern path here '' refers to /listings. second one is single listings which looks at detail of each listing.
urlpatterns = [
    path( '', views.index, name = 'listings'),
    path('<int:listing_id>', views.listing, name = 'listing'),
    path('search', views.search, name = 'search'),
]
