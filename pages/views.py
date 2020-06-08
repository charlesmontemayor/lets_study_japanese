from allauth.account.views import PasswordChangeView
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'home.html'


class AboutPageView(TemplateView):
    template_name = 'about.html'


class CustomPasswordChangeView(PasswordChangeView):
    success_url = '/accounts/password/reset/key/done'
