from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignupForm(forms.ModelForm):
    username=forms.CharField(widget=forms.TextInput, required=True,max_length=50)
    password=forms.CharField(widget=forms.TextInput, required=True,max_length=50)
    confirm_password=forms.CharField(widget=forms.TextInput,max_length=50)
    #registration=forms.ModelChoiceField(queryset=OtpVerification.objects.all())
    #OTP=forms.CharField(widget=forms.TextInput,max_length=10)
    class Meta:  
        model = User  
        fields = ('username','password')

    def clean_username(self):
        username = self.cleaned_data.get('username')
        username_qs = User.objects.filter(username=username)
        if username_qs.exists():
            raise forms.ValidationError("This username already exists.")
        return username 

    def clean_confirm_password(self):
        password=self.cleaned_data['password']
        confirm_password=self.cleaned_data['confirm_password']
        if password != confirm_password:
            raise forms.ValidationError("password and confirm_password does not match")
        return password    
