from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^api/countries$',views.countries_details),
    url(r'^api/countries/(?P<pk>[0-9]+)$',views.countries_details)
]