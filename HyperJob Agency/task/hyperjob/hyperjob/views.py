from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
from resume.models import Resume
from django.core.exceptions import PermissionDenied
from vacancy.models import Vacancy


# Create your views here.
class MainView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'hyperjob/main.html', {})


class MySignupView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = 'login'
    template_name = 'hyperjob/signup.html'


class MyLoginView(LoginView):
    form_class = AuthenticationForm
    template_name = 'hyperjob/login.html'


class MyHomeView(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            context = {
                "username": request.user.get_username()
            }
        else:
            context = {
                "username": "You Are Not Logged In"
            }
        return render(request, 'hyperjob/home.html', context)


class MyResumeNew(View):
    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated: # logged in
            if not request.user.is_staff:  # not a manager
                Resume.objects.create(
                    description= request.POST.get('description'),
                    author= request.user
                )
                return redirect('/home')
            else:
                raise PermissionDenied
        else:
            raise PermissionDenied

        
class MyVacancyNew(View):
    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:  # logged in
            if request.user.is_staff:  # is a manager
                Vacancy.objects.create(
                    description=request.POST.get('description'),
                    author=request.user
                )
                return redirect('/home')
            else:
                raise PermissionDenied
        else:
            raise PermissionDenied




