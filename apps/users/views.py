from django.shortcuts import render, redirect
from django.contrib.auth import logout

def LogOut(request):
    logout(request)
    return redirect('/')
