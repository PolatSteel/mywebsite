from django.urls import path
from . import views


urlpatterns = [
    path("", views.information, name="information"),
    path('whatidid/',views.start, name='start'),
    path('aboutme/',views.information, name='information'),
    path('contact/',views.contact, name='contact'),
    
   
]
