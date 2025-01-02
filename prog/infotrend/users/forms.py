from django import forms
from django.forms import TextInput, PasswordInput, EmailInput
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth import get_user_model

class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', 
    widget=forms.TextInput(attrs={'class':'form-control'}))

    password = forms.CharField(label='Пароль', 
    widget=forms.PasswordInput(attrs={'class':'form-control'}))



class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', 
    widget=forms.TextInput(attrs={'class':'form-control'}))

    password1 = forms.CharField(label='Пароль', 
    widget=forms.PasswordInput(attrs={'class':'form-control'}))

    password2 = forms.CharField(label='Повтор пароля', 
    widget=forms.PasswordInput(attrs={'class':'form-control'}))

    
    class Meta:
        model = get_user_model()
        fields = ['username','email','password1','password2']
        labels = {
            'email':'E-mail',
        }
        widgets ={
            
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] != cd['password2']:
            raise forms.ValidationError("Пароли должны совпадать!")
        return cd['password1']

    def clean_email(self):
        email = self.cleaned_data['email']
        if get_user_model().objects.filter(email=email).exists():
            raise forms.ValidationError("Такой E-mail уже существует")
        return email

class ProfileUserForm(forms.ModelForm):
    username = forms.CharField(disabled=True, label='Логин', 
    widget=forms.TextInput(attrs={'class':'form-control'}))

    email = forms.CharField(disabled=True, label='E-mail', 
    widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = get_user_model()
        fields =['username','email']


class UserPasswordChangeForm(PasswordChangeForm):   
    old_password = forms.CharField(label='Старый пароль', 
    widget=forms.PasswordInput(attrs={'class':'form-control'}))
    new_password1 = forms.CharField(label='Новый пароль', 
    widget=forms.PasswordInput(attrs={'class':'form-control'}))
    new_password2 = forms.CharField(label='Подтверждение пароля', 
    widget=forms.PasswordInput(attrs={'class':'form-control'}))