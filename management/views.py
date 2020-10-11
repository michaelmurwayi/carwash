from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.views.generic.base import TemplateView
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from djreservation.views import ProductReservationView
from .models import Reservation
import requests 

# Create your views here.

class HomeView(TemplateView):
    template_name = "home.html"
    
# class SignUpView(generic.CreateView):
#     form_class = UserCreationForm
#     success_url = reverse_lazy('accounts/')
#     template_name = "signup.html"

#     def post(self, request):
#         form = self.form_class(request.post)
        
#         if form.is_valid():
#             return HttpResponseRedirect('/admin/')

#             return render(request, self.template_name, {'form': form})

def SignupView(request):
    form = UserCreationForm(request.POST)
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('profile')
    return render(request, 'signup.html', {'form': form})

class CarWashReservation(ProductReservationView):
    base_model = Reservation
    amount_field = 'quantity'
