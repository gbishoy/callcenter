from django.shortcuts import redirect, render
from django.views.generic import View
from django.contrib.auth.decorators import *
from .decorators import unauthorized_user,allowed_users
from .models import Cfmerchant

@login_required(login_url='loginpage')
@allowed_users(['callers'])
def get(request):
    
    username = request.user.username
    dailytask = Cfmerchant.objects.raw("select distinct(national_id) as id ,client_name1 from public.cfmerchant inner join public.teamleader_choose on cfmerchant.officer_name2 = teamleader_choose.loanofficer_name and c_s = 'عميل' and teamleader_choose.employee = '{}' order by client_name1".format(username))
    if request.POST.get('customerdata'):
        customercode = request.POST['customerdata']
        customerloans = Cfmerchant.objects.raw("select loan_key1 as id from public.cfmerchant where national_id = '{}'".format(customercode))
        return render(request,'callist/callist.html',{'customers':dailytask,'customerloan':customerloans})
    elif request.POST.get('loan'): 
         loankey = request.POST['loan']
         customerdatas = Cfmerchant.objects.raw("select branch_code1 as id ,* from public.cfmerchant where c_s = 'عميل' and loan_key1 = '{}'".format(loankey))
         damendatas = Cfmerchant.objects.raw("select branch_code1 as id, * from public.cfmerchant where c_s = 'ضامن' and loan_key1 = '{}'".format(loankey))
         return render(request,'callist/loandetails.html',{'customerdata':customerdatas,'damendata':damendatas}) 
    return render(request,'callist/callist.html',{'customers':dailytask})