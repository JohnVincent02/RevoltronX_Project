from django.shortcuts import render,redirect
from Guest.models import *
from User.models import *

def homepage(request):
    if 'uid' in request.session:
        user = tbl_user.objects.get(id=request.session['uid'])  # get only logged-in user
        return render(request, 'User/homepage.html', {'user': user})
    else:
        return redirect('login')  # redirect if not logged in




