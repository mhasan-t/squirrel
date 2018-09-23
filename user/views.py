from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView, DetailView, CreateView

from user.models import Client


class IndexView(TemplateView):
    template_name = 'index.html'


class SignUpView(CreateView):
    template_name = 'signup.html'

    def get(self, request, *args, **kwargs):
        return render(request, template_name=self.template_name)

    def post(self, request, *args, **kwargs):
        data = request.POST
        d = {}
        for key, value in data.items():
            d[key] = value

        del d['csrfmiddlewaretoken']
        del d['confirm_password']
        if User.objects.filter(username= d['username']).count() or User.objects.filter(email=d['email']).count():
            error_data = {
                'error': 'Username or Email is already in use'
            }
            return render(request, self.template_name, context=error_data)
        else:
            user = Client.objects.create(**d)
            return redirect('/client/index/')


class ClientLoginView(LoginView):
    template_name = 'login.html'

    def get_success_url(self):
        return '/companies'

@method_decorator(login_required, name='dispatch')
class ClientDetail(DetailView):
    model = Client
    template_name = 'user_profile.html'
    context_object_name = 'client'
    queryset = Client.objects.all()


class ClientLogoutView(LogoutView):

    def get_next_page(self):
        return '/client/login/'
