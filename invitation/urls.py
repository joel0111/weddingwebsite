from django.urls import path
from . import views

urlpatterns = [
    path('', views.heart_gate, name='heart_gate'),
    path('home/', views.home, name='home'),
    path('rsvp/', views.rsvp, name='rsvp'),
    path('rsvp/thanks/', views.rsvp_thanks, name='rsvp_thanks'),
    path('volunteer/', views.volunteer, name='volunteer'),
    path('volunteer/thanks/', views.volunteer_thanks, name='volunteer_thanks'),
    path('freebies/', views.freebies, name='freebies'),
]
