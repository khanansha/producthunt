from django.shortcuts import render ,HttpResponse ,redirect
# Create your views here.
from django.contrib.auth.models import User

from django.contrib import auth
from .forms import SignupForm 
from django.http import HttpResponseRedirect



def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            confirm_password = form.cleaned_data['confirm_password']
            user = User.objects.create_user(username=username,password=password)
            auth.login(request,user)
            return redirect('home')
    else:
        form = SignupForm()
    return render(request, 'account/signup.html',{'form': form})

        


def login(request):

    if request.method == 'POST':

        user = auth.authenticate(username=request.POST['username'],password=request.POST['password'])

        if user is not None:

            auth.login(request, user)

            return redirect('home')

        else:

            return render(request, 'account/login.html',{'error':'username or password is incorrect.'})

    else:

        return render(request, 'account/login.html')
   

def logout(request):
    if request.method == 'POST':

        auth.logout(request)

        return redirect('home')