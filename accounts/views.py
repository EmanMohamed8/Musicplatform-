from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
# Create your views here.


def register_user(request):
    form = UserCreationForm(request.POST)
    if form.is_valid():
        form.save()
        user = form.cleaned_data.get('username')
        messages.success(request, user + ' Created Successfully !')
        return redirect('login_user')
    context = {'form': form}
    return render(request, 'accounts/register.html', context)


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('register_user')
        else:
            messages.info(request, 'Credentials Errors')
    return render(request, 'accounts/login.html',)


def logout_user(request):
    logout(request)
    return redirect('login')
    # return render(request, 'accounts/logout.html',)
