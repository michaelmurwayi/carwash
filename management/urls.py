from django.urls import path, include 
from . import views
from .views import CarWashReservation
from django.views.generic import TemplateView


urlpatterns = [
    path('', TemplateView.as_view(template_name="home.html"), name="home"),
    path('signup/', views.SignupView, name="signup"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('profile/', TemplateView.as_view(template_name="profile.html"), name="profile"),
    
]
