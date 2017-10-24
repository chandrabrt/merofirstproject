from django import forms
from django.contrib.auth.models import User
from .models import Profile


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class SignUpForm(forms.ModelForm):
    error_css_class = 'error'
    required_css_class = 'required'
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)
    Date_of_birth = forms.DateTimeField(label='Date Of Birth',
                                        widget=forms.TextInput(attrs={'placeholder': 'YYYY-MM-DD or YYYY/MM/DD'}))
    full_name = forms.CharField(max_length=100, help_text='Enter your full name')

    class Meta:
        model = User
        fields = ('username', 'full_name', 'email', 'Date_of_birth', 'password', 'password2')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']


class UserEditForm(forms.ModelForm):

    class Meta:

        model = Profile
        fields = ['photo']


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['photo']


