from django.conf.urls import url
from django.contrib.auth.views import LoginView
from .views import DashboardView

urlpatterns = [
    url('login/', view = LoginView.as_view(template_name = 'account/login.html'), name = "login"),
    url('dashboard/', view = DashboardView.as_view(), name = "dashboard"),
]
