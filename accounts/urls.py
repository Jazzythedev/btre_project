from django.urls import path

from . import views
# first url pattern path here '' refers to /listings. second one is single listings which looks at detail of each listing.
urlpatterns = [
    path( 'login', views.login, name = 'login'),
    path('register', views.register, name = 'register'),
    path('logout', views.logout, name = 'logout'),
     path('dashboard', views.dashboard, name = 'dashboard'),
]
