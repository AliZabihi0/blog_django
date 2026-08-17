from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

from account_app.models import Profile


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter your Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter your Password'}),
                               label="Password")

    def clean_password(self):
        user = authenticate(username=self.cleaned_data["username"], password=self.cleaned_data["password"])
        if user is not None:
            return self.cleaned_data["password"]
        raise forms.ValidationError("Username or Password is incorrect", code="incorrect")
    def clean_username(self):
        username = self.cleaned_data['username']
        return username.lower()


class SignUpForm(forms.Form):
    username = forms.CharField(max_length=100,
                               widget=forms.TextInput(attrs={'class': 'input100', 'placeholder': 'Enter Username'}))
    email = forms.EmailField(max_length=100,
                             widget=forms.EmailInput(attrs={'class': 'input100', 'placeholder': 'Enter Email'}))
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'input100', 'placeholder': 'Enter Password'}), )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'input100', 'placeholder': 'Enter Password again'}), )

    def clean_username(self):
        username = self.cleaned_data['username']

        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Username already exists")
        if username == '':
            raise forms.ValidationError("Username cannot be empty")
        if " " in username:
            raise forms.ValidationError("Username must contain only letters and numbers")
        return username.lower()

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email already exists")
        if email == '':
            raise forms.ValidationError("Email cannot be empty")
        return email

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 and password2:
            if password1 != password2:
                raise forms.ValidationError("Passwords don't match")

            if len(password1) < 8:
                raise forms.ValidationError("Password must contain at least 8 characters")

        return cleaned_data


class EditProfile(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')
        widgets = {}
