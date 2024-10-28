from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, SetPasswordForm
from django import forms
from . models import Profile

class UpdateUserInfo(forms.ModelForm):
    phone = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'شماره تلفن'}),
        required=False
    )    
    address = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'ادرس'}),
        required=False
    )    
    city = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'شهر'}),
        required=False
    )    
    state = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'منطقه'}),
        required=False
    )    
    zipcode = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'کدپستی'}),
        required=False
    )
    
    class Meta:
        model = Profile
        fields = ('phone', 'address', 'city', 'state', 'zipcode')
class UpdatePasswordForm(SetPasswordForm):
        new_password1 = forms.CharField(
        label="",
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'name':'password',
                'type':'password',
                'placeholder':'گذرواژه خود را وارد کنید'
                }
         )
        )
    
        new_password2 = forms.CharField(
        label="",
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'name':'password',
                'type':'password',
                'placeholder':'گذرواژه خود را مجدد وارد کنید'
                }
            )
         )
    
        class Meta:
            model = User
            fields = ('new_password1', 'new_password2')

class UpdateUserForm(UserChangeForm):
    password = None
    first_name = forms.CharField(
        label="",
        max_length=50,
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'نام خود را وارد کنید'})
    )
    
    last_name = forms.CharField(
        label="",
        max_length=50,
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'نام خانوادگی خود را وارد کنید'})
   )
    
    email = forms.EmailField(
        label="",
        max_length=80,
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'ایمیل خود را وارد کنید'})
    )
    
    username = forms.CharField(
        label="",
        max_length=20,
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'نام کاربری خود را وارد کنید'})
    )
    
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username')
class SignUpForm(UserCreationForm):
    first_name = forms.CharField(
        label="",
        max_length=50,
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'نام خود را وارد کنید'})
    )
    
    last_name = forms.CharField(
        label="",
        max_length=50,
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'نام خانوادگی خود را وارد کنید'})
   )
    
    email = forms.EmailField(
        label="",
        max_length=80,
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'ایمیل خود را وارد کنید'})
    )
    
    username = forms.CharField(
        label="",
        max_length=20,
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'نام کاربری خود را وارد کنید'})
    )
    
    password1 = forms.CharField(
        label="",
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'name':'password',
                'type':'password',
                'placeholder':'گذرواژه خود را وارد کنید'
            }
        )
    )
    
    password2 = forms.CharField(
        label="",
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'name':'password',
                'type':'password',
                'placeholder':'گذرواژه خود را مجدد وارد کنید'
            }
        )
    )
       
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password1', 'password2')
        