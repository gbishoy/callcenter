from django.shortcuts import redirect, render
from django.views.generic import View
from .models import Cfmerchant,choose
from django.contrib.auth.decorators import *
from .decorators import unauthorized_user,allowed_users



@login_required(login_url='loginpage')   
@allowed_users(['teamleader'])   
def get(request):
    branch = Cfmerchant.objects.raw("SELECT distinct(branch_name) as id ,count(branch_name) as cusnum  FROM dbo.dis_in_client_damen_cf where MONTH([loan_date])=MONTH(GETDATE())-1 and c_s = 'عميل' group by branch_name order by branch_name ")
    officer = Cfmerchant.objects.raw("SELECT username as id , first_name FROM dbo.auth_user where is_superuser = 'false' and id <> 2")   
    workplan = Cfmerchant.objects.raw("select teamleader_choose.employee as id,sum(teamleader_choose.customernumber) as total from teamleader_choose where timeadd = CAST( GETDATE() AS Date ) group by teamleader_choose.employee")
    emp = Cfmerchant.objects.raw("select officer_name  ,count(officer_name) as id from dbo.dis_in_client_damen_cf where  MONTH([loan_date])=MONTH(GETDATE())-1 and c_s = 'عميل' group by officer_name ")
    if request.POST.get('customerdata'):
        branchname = request.POST['customerdata'] 
        branch = Cfmerchant.objects.raw("SELECT distinct(branch_name) as id ,count(branch_name) as cusnum  FROM dbo.dis_in_client_damen_cf where MONTH([loan_date])=MONTH(GETDATE())-1 and c_s = 'عميل' group by branch_name order by branch_name ")
        emp = Cfmerchant.objects.raw("select officer_name  ,count(officer_name) as id from dbo.dis_in_client_damen_cf where  branch_name = '{}' and MONTH([loan_date])=MONTH(GETDATE())-1 and c_s = 'عميل' group by officer_name ".format(branchname))
        # offname = request.POST['officer']
        return render(request,'teamleader/leaderpage.html',{'emp':emp,'bran':branch,'officers':officer,'workplan':workplan})
    elif request.POST.get('employee') :
        employees = request.POST.getlist('employee')
        offname = request.POST['officer']
        for i in employees:
            ch = choose(loanofficer_name=i.split(',')[0],employee=offname,customernumber=i.split(',')[1])
            ch.save()

    return render(request,'teamleader/leaderpage.html',{'emp':'','bran':branch,'officers':officer,'workplan':workplan})


@login_required(login_url='loginpage') 
@allowed_users(['teamleader']) 
def workflowview(request):
    return render(request,'teamleader/workflow.html')


def error_404_view(request, exception):
    return render(request,'404.html')