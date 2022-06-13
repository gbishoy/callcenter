from django.contrib import messages
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login ,logout
from django.contrib.auth.decorators import login_required
from .decorators import unauthorized_user,allowed_users



@unauthorized_user
def loginpageview(request):
   if request.method == "POST" :
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request=request, user=user)
            return redirect('homepage')

        else:
            messages.success(request,'هناك خطأ في تسجيل الدخول')
            return redirect('loginpage')

   else:
       return render(request,'loginpage.html') 
    
          
    

        
@login_required(login_url='loginpage')
def homepage(request):
    return render(request,'index.html')


def error_404_view(request, exception):
    return render(request,'404.html')

def logout_view(request):
    logout(request)
    return render(request,'loginpage.html')

