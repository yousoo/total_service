from django.urls import path
from . import views

app_name = 'common'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('signup/username_check', views.username_check, name='username_check'), #아이디중복 url은 다시 아이디중복 체크를 위한 views를 불러야 한다.
    path('index/', views.index, name='index')
]