from django.shortcuts import render
from django.contrib.auth.forms import UserreationForm
from django.urls import reverse_lazy
from django.views import generic

class register(generic.CreateView):
    from_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'account/register.html'
