from django.shortcuts import render, redirect

from .models import tbl_user

def index(request):
    return render(request,'Guest/index.html')



def user_register(request):
    if request.method == 'POST':
        tbl_user.objects.create(
            user_name = request.POST['user_name'],
            user_address = request.POST['user_address'],
            user_contact = request.POST['user_contact'],
            user_email = request.POST['user_email'],
            user_gender = request.POST['user_gender'],
            user_dob = request.POST['user_dob'],
            user_password = request.POST['user_password']
        )
        # ✅ FIXED: Pass `request` to render()
        return render(request, 'Guest/user_register.html')

    return render(request, 'Guest/user_register.html')




def login(request):
    if request.method == 'POST':
        email = request.POST['user_email']
        password = request.POST['user_password']

        usercount=tbl_user.objects.filter(user_email=email,user_password=password). count()
        if usercount > 0:
            user=tbl_user.objects.get(user_email=email,user_password=password)
            request.session["uid"]=user.id
            user.save()
            return redirect('User:homepage')
        else:
            return render(request,'Guest/login.html')
    else:
        return render(request,"Guest/login.html")
