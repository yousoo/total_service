from .models import Member_info
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from common.forms import Member_infoForm, Member_infoModyForm
from django.contrib import messages
from .models import Member_info
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt, csrf_protect #csrf토큰 일시해제

@csrf_exempt #csfr토큰 일시해제한다.(주소받아오는 것)
def signup(request):
    if request.method == 'POST':
        form = Member_infoForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            zipcode = form.cleaned_data.get('zipcode')
            address1 = form.cleaned_data.get('address1')
            address2 = form.cleaned_data.get('address2')
            address3 = form.cleaned_data.get('address3')
            phone = form.cleaned_data.get('phone')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('common: index')
        else:
            print(form.errors)
    else:
        form = Member_infoForm()
    context = {'form': form, 'title': '회원가입'}
    return render(request, 'common/signup.html', context)

"""
사용자 아이디 중복체크
1. username(사용자아이디)를 템플릿에서 받아온다.
2. Member_info 모델에서 해당 username으로 검색한다.
3. 검색결과가 있으면 is_user는 yes, 없으면 no를 템플릿에 돌려준다.
"""
def username_check(request):
    username = request.GET['username']
    if Member_info.objects.filter(username=username).exists():
        user_exist = {
            "is_user": "yes",
        }
    else:
        user_exist = {
            "is_user": "no",
        }
    return JsonResponse(user_exist)

def index(request):
    return render(request, 'common/index.html')