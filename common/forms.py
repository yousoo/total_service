from django.contrib.auth.forms import UserCreationForm
from .models import Member_info
from django import forms

"""
회원가입폼
-user 기본 제공 필드
    username : 아이디
    password1 : 패스워드
    password2 : 패스워드확인
    email : 이메일
"""
class Member_infoForm(UserCreationForm):
    class Meta:
        model = Member_info
        fields = ['username', 'password1', 'password2', 'email', 'member_name',
                  'zipcode', 'address1', 'address2', 'address3', 'phone']

"""
회원정보 수정폼
- 아이디는 제외
- 비밀번호 포함
"""
class Member_infoModyForm(UserCreationForm):
    class Meta:
        model = Member_info
        fields = ['password1', 'password2', 'email', 'member_name',
                  'zipcode', 'address1', 'address2', 'address3', 'phone']

        def clean(self):
            form_data = self.cleand