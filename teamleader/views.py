from django.shortcuts import redirect, render
from django.views.generic import View
from .models import Cfmerchant,choose
from django.contrib.auth.decorators import *
from .decorators import unauthorized_user,allowed_users



@login_required(login_url='loginpage')   
@allowed_users(['teamleader'])   
def get(request):
    branch = Cfmerchant.objects.raw("SELECT distinct(branch_name) as id FROM dbo.dis_in_client_damen_cf")
    officer = Cfmerchant.objects.raw("SELECT username as id , first_name FROM public.auth_user where is_superuser = 'false' and id <> 2")   
    workplan = Cfmerchant.objects.raw("select * from teamleader_choose where timeadd = current_date")
    emp = Cfmerchant.objects.raw("select officer_name  ,count(officer_name) as id from dbo.dis_in_client_damen_cf where add_datetime < current_date group by officer_name ")

    if request.POST.get('customerdata') :
        branchname = request.POST['customerdata'] 
        branch = Cfmerchant.objects.raw("SELECT distinct(branch_name) as id FROM dbo.dis_in_client_damen_cf")
        emp = Cfmerchant.objects.raw("select officer_name  ,count(officer_name) as id from dbo.dis_in_client_damen_cf where  branch_name = '{}' and add_datetime < current_date group by officer_name ".format(branchname))
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