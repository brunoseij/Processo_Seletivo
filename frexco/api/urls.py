from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('fruit/', include('api.fruit.urls')),
    path('region/', include('api.region.urls')),
]