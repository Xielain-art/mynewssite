from django.views import generic
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from .forms import RegisterForm
from django.http import JsonResponse
import random
import json
from django.contrib.auth.models import User


class SignUpView(generic.CreateView):
    form_class = RegisterForm
    success_url = reverse_lazy('login')
    template_name = 'registration/registration.html'


def user_register(request):

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save()
            user.save()

        else:
            if User.objects.filter(username=request.POST['user']).exists():
                response = {
                    'message': True
                }
            else:
                response = {
                    'message': False
                }
            return JsonResponse(response)

    else:
        form = RegisterForm()
    return render(request, 'registration/registration.html', {'form': form})


def get_num(request):
    response = {
        'message': 123
    }
    return JsonResponse(response)
