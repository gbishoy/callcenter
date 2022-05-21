from django.shortcuts import redirect, render
from django.views.generic import View
from django.contrib.auth.decorators import *
from sqlalchemy import values
from .decorators import unauthorized_user,allowed_users
from .models import Cfmerchant ,Comment
from django.contrib import messages


@login_required(login_url='loginpage')
@allowed_users(['callers'])

def get(request):
    username = request.user.username
    dailytask = Cfmerchant.objects.raw("select distinct(national_id) as id ,client_name from dbo.dis_in_client_damen_cf inner join [dbo].[teamleader_choose] on dis_in_client_damen_cf.officer_name = [teamleader_choose].[loanofficer_name] and c_s = 'عميل' and [teamleader_choose].[employee] = '{}' order by client_name".format(username))
    if request.POST.get('customerdata'):
        customercode = request.POST['customerdata']
        customerloans = Cfmerchant.objects.raw("select loan_key as id from dbo.dis_in_client_damen_cf where national_id = '{}'".format(customercode))
        return render(request,'callist/callist.html',{'customers':dailytask,'customerloan':customerloans})
    elif request.POST.get('loan'): 
         loankey = request.POST['loan']
         commentsty = Cfmerchant.objects.raw("select comment_text as id from comments where ComCate = 'cf'")
         customerdatas = Cfmerchant.objects.raw("select branch_code as id ,* from dbo.dis_in_client_damen_cf where c_s = 'عميل' and loan_key = '{}'".format(loankey))
         damendatas = Cfmerchant.objects.raw("select branch_code as id, * from dbo.dis_in_client_damen_cf where c_s = 'ضامن' and loan_key = '{}'".format(loankey))
         return render(request,'callist/loandetails.html',{'customerdata':customerdatas,'damendata':damendatas,'com':commentsty}) 
    else:
        if request.method == 'POST':
            commentt = {}
            username = request.user.username
            for key , value in request.POST.items():
                if (key != 'mycheckbox' or key != 'csrfmiddlewaretoken') and key != '' :
                    if key == 'com1t':
                        ch = Comment(loan_code=request.POST['mycheckbox'],comhead=request.POST['com1'],desc=value,caller=username)
                        ch.save()
                    if key == 'com2t':
                        ch = Comment(loan_code=request.POST['mycheckbox'],comhead=request.POST['com2'],desc=value,caller=username)
                        ch.save()
                    if key == 'com3t':
                        ch = Comment(loan_code=request.POST['mycheckbox'],comhead=request.POST['com3'],desc=value,caller=username)
                        ch.save()
                    if key == 'com4t':
                        ch = Comment(loan_code=request.POST['mycheckbox'],comhead=request.POST['com4'],desc=value,caller=username)
                        ch.save()
                    if key == 'com5t':
                        ch = Comment(loan_code=request.POST['mycheckbox'],comhead=request.POST['com5'],desc=value,caller=username)
                        ch.save()
                    if key == 'com6t':
                        ch = Comment(loan_code=request.POST['mycheckbox'],comhead=request.POST['com6'],desc=value,caller=username)
                        ch.save()
                    if key == 'com7t':
                        ch = Comment(loan_code=request.POST['mycheckbox'],comhead=request.POST['com7'],desc=value,caller=username)
                        ch.save()
                    if key == 'com8t':
                        ch = Comment(loan_code=request.POST['mycheckbox'],comhead=request.POST['com8'],desc=value,caller=username)
                        ch.save()
                    if key == 'com9t':
                        ch = Comment(loan_code=request.POST['mycheckbox'],comhead=request.POST['com9'],desc=value,caller=username)
                        ch.save()
                    if key == 'com10t':
                        ch = Comment(loan_code=request.POST['mycheckbox'],comhead=request.POST['com10'],desc=value,caller=username)
                        ch.save()
                    if key == 'com11t':
                        ch = Comment(loan_code=request.POST['mycheckbox'],comhead=request.POST['com11'],desc=value,caller=username)
                        ch.save()
                    if key == 'com12t':
                        ch = Comment(loan_code=request.POST['mycheckbox'],comhead=request.POST['com12'],desc=value,caller=username)
                        ch.save()
                    if key == 'com13t':
                        ch = Comment(loan_code=request.POST['mycheckbox'],comhead=request.POST['com13'],desc=value,caller=username)
                        ch.save()
                    if key == 'com14t':
                        ch = Comment(loan_code=request.POST['mycheckbox'],comhead=request.POST['com14'],desc=value,caller=username)
                        ch.save()
                    if key == 'com15t':
                        ch = Comment(loan_code=request.POST['mycheckbox'],comhead=request.POST['com15'],desc=value,caller=username)
                        ch.save()
                    if key == 'com16t':
                        ch = Comment(loan_code=request.POST['mycheckbox'],comhead=request.POST['com16'],desc=value,caller=username)
                        ch.save()
                    if key == 'com17t':
                        ch = Comment(loan_code=request.POST['mycheckbox'],comhead=request.POST['com17'],desc=value,caller=username)
                        ch.save()
            messages.info(request, 'Your comment have been added successfully!')
            return render(request,'callist/callist.html',{'customers':dailytask})
                    # ch = Comment(loan_code=request.POST['mycheckbox'][0],cus_code=request.POST['mycheckbox'][2],comhead=key,desc=value,caller=username,emp=request.POST['mycheckbox'][1])
                    # ch.save()
    return render(request,'callist/callist.html',{'customers':dailytask})