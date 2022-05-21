from django.shortcuts import redirect, render
from django.views.generic import View
from .models import Cfmerchant,choose,Employee
from django.contrib.auth.decorators import *
from .decorators import unauthorized_user,allowed_users



@login_required(login_url='loginpage')   
@allowed_users(['teamleader'])   
def get(request):
    branch = Cfmerchant.objects.raw("SELECT distinct(branch_name1) as id FROM public.cfmerchant")
    officer = Employee.objects.raw("SELECT username as id , first_name FROM public.auth_user where is_superuser = 'false' and id <> 2")   
    workplan = choose.objects.raw("select * from teamleader_choose where timeadd = current_date")
    emp = Cfmerchant.objects.raw("select officer_name2  ,count(officer_name2) as id from cfmerchant where timeadd < current_date group by officer_name2 ")

    if request.POST.get('customerdata') :
        branchname = request.POST['customerdata'] 
        branch = Cfmerchant.objects.raw("SELECT distinct(branch_name1) as id FROM public.cfmerchant")
        emp = Cfmerchant.objects.raw("select officer_name2  ,count(officer_name2) as id from cfmerchant where  branch_name1 = '{}' and timeadd < current_date group by officer_name2 ".format(branchname))
        # offname = request.POST['officer']
        return render(request,'teamleader/leaderpage.html',{'emp':emp,'bran':branch,'officers':officer,'workplan':workplan})
    elif request.POST.get('employee') :
        employees = request.POST.getlist('employee')
        offname = request.POST['officer']
        for i in employees:
            print(i)
            ch = choose(loanofficer_name=i,employee=offname)
            ch.save()

    return render(request,'teamleader/leaderpage.html',{'emp':'','bran':branch,'officers':officer,'workplan':workplan})


@login_required(login_url='loginpage') 
@allowed_users(['teamleader']) 
def workflowview(request):
    return render(request,'teamleader/workflow.html')