from .models import Member_info
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from common.forms import Member_info, Member_infoModyForm
from django.contrib import messages
from django.http import JsonResponse

def signup(request):
    context = {'title': '회원가입'}
    return render(request, 'common/signup.html', context)