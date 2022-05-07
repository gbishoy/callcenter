from django.shortcuts import redirect, render
from django.views.generic import View
from .models import Cfmerchant,choose,Employee
from django.contrib.auth.decorators import *
from .decorators import unauthorized_user,allowed_users



@login_required(login_url='loginpage')   
@allowed_users(['teamleader'])   
def get(request):
    emp = Cfmerchant.objects.raw("select officer_name2  ,count(officer_name2) as id from cfmerchant where timeadd = current_date group by officer_name2 ")
    officer = Employee.objects.raw("SELECT username as id , first_name FROM public.auth_user where is_superuser = 'false' and id <> 2")   
    workplan = choose.objects.raw("select * from teamleader_choose where timeadd = current_date")
    if request.method == "POST" :
        employees = request.POST['employee']   
        offname = request.POST['officer']
        ch = choose(loanofficer_name=employees,employee=offname)
        ch.save()
        return redirect('teamleader')

    return render(request,'teamleader/leaderpage.html',{'emp':emp,'officers':officer,'workplan':workplan})

@login_required(login_url='loginpage') 
@allowed_users(['teamleader']) 
def workflowview(request):
    
    return render(request,'teamleader/workflow.html')