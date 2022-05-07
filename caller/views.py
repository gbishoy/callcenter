from django.shortcuts import redirect, render
from django.views.generic import View
from django.contrib.auth.decorators import *
from .decorators import unauthorized_user,allowed_users
from .models import Cfmerchant

@login_required(login_url='loginpage')
@allowed_users(['callers'])
def get(request):
    
    username = request.user.username
    dailytask = Cfmerchant.objects.raw("select distinct(customer_national_id) as id ,customer_name from public.cfmerchant inner join public.teamleader_choose on cfmerchant.loanofficer_name = teamleader_choose.loanofficer_name and teamleader_choose.employee = '{}' order by customer_name".format(username))
    if request.POST.get('customerdata'):
        customercode = request.POST['customerdata']
        customerloans = Cfmerchant.objects.raw("select loan_key as id from public.cfmerchant where customer_national_id = '{}'".format(customercode))
        return render(request,'callist/callist.html',{'customers':dailytask,'customerloan':customerloans})
    elif request.POST.get('loan'): 
         loankey = request.POST['loan']
         customerdatas = Cfmerchant.objects.raw("select * from public.cfmerchant where loan_key = '{}'".format(loankey))
         print(request.POST['loan'])
         return render(request,'callist/loandetails.html',{'customerdata':customerdatas})

    return render(request,'callist/callist.html',{'customers':dailytask,}) 
    
   