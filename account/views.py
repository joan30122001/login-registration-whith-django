from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class LoginView():
    authentification_form = None
    template_name = 'registration/login.html'

    
class DashboardView(TemplateView):
    template_name = "account/dashboard.html"
