from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.views.generic import View

class ExtraDataView(View):

	def get(self, request, *args, **Kwargs):
		return render(request, 'users/extra_data.html')
		

def LogOut(request):
    logout(request)
    return redirect('/')
