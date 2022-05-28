from django.shortcuts import redirect, render
from django.views.generic import View
from django.contrib.auth.decorators import *
from sqlalchemy import values
from .decorators import unauthorized_user,allowed_users
from .models import Cfmerchant ,Comment
from django.contrib import messages
from django.http import  HttpResponse,JsonResponse
from django.forms.models import model_to_dict
import json
from django.core import serializers

ofnames =''
@login_required(login_url='loginpage')
@allowed_users(['callers'])

def get(request):
    username = request.user.username
    
    dailytask = Cfmerchant.objects.raw("select distinct(branch_code) as id ,branch_name from dbo.dis_in_client_damen_cf inner join [dbo].[teamleader_choose] on dis_in_client_damen_cf.officer_name = [teamleader_choose].[loanofficer_name] and c_s = 'عميل' and [teamleader_choose].[employee] = '{}' order by branch_name".format(username))
    if request.POST.get('branch'):
        branchcode = request.POST['branch']
        officername = Cfmerchant.objects.raw("select distinct(officer_name) as id  from dbo.dis_in_client_damen_cf inner join [dbo].[teamleader_choose] on dis_in_client_damen_cf.officer_name = [teamleader_choose].[loanofficer_name] and c_s = 'عميل' and [teamleader_choose].[employee] = '{}' and dis_in_client_damen_cf.branch_code='{}' order by dis_in_client_damen_cf.officer_name".format(username,branchcode))
        return render(request,'callist/callist.html',{'branches':dailytask,'officername':officername})
    elif request.POST.get('ofname'): 
         officernameloans = request.POST['ofname']
        
         cusnames = Cfmerchant.objects.raw("select distinct(national_id) as id , client_name from dbo.dis_in_client_damen_cf where officer_name = '{}'".format(officernameloans))
         return render(request,'callist/loandetails.html',{'ofloans':cusnames})
        #  commentsty = Cfmerchant.objects.raw("select comment_text as id from comments where ComCate = 'cf'")
        #  customerdatas = Cfmerchant.objects.raw("select branch_code as id ,* from dbo.dis_in_client_damen_cf where c_s = 'عميل' and loan_key = '{}'".format(loankey))
        #  damendatas = Cfmerchant.objects.raw("select branch_code as id, * from dbo.dis_in_client_damen_cf where c_s = 'ضامن' and loan_key = '{}'".format(loankey))
        #  return render(request,'callist/loandetails.html',{'customerdata':customerdatas,'damendata':damendatas,'com':commentsty}) 
    elif request.headers.get('x-requested-with') == 'XMLHttpRequest':
        cusnationalid = request.POST['nationalid']
        print(cusnationalid)
        # commentsty = Cfmerchant.objects.raw("select comment_text as id from comments where ComCate = 'cf'")
        customerdatasmain = Cfmerchant.objects.raw("select national_id as id,client_key,client_name,add4,officer_name,tel4,branch_name ,aprv_am,consumer_finance_initial_limit from dbo.dis_in_client_damen_cf where national_id = '{}' group by national_id,client_key,client_name,add4,officer_name,tel4,branch_name,aprv_am,consumer_finance_initial_limit".format(cusnationalid))
        customerdatas = Cfmerchant.objects.raw("select national_id as id ,* from dbo.dis_in_client_damen_cf where national_id = '{}'".format(cusnationalid))
        damendatas = Cfmerchant.objects.raw("select national_id as id,tel4,client_name,add4,client_key from dbo.dis_in_client_damen_cf where c_s = 'ضامن' and loan_key in (select distinct(loan_key) from dbo.dis_in_client_damen_cf where  national_id = '{}') GROUP BY national_id ,client_name,tel4,add4,client_key".format(cusnationalid))
        
        datamain = serializers.serialize('json', customerdatasmain, fields=('id','client_key','client_name','add4','officer_name','tel4','branch_name','aprv_am','consumer_finance_initial_limit'))
        datadetails = serializers.serialize('json', customerdatas, fields=('id','sub_category_name','category_name','client_name_m','inst','loan_am','aprv_no','loan_date'))
        damen = serializers.serialize('json', damendatas, fields=('id','client_key','client_name','add4','tel4'))

        return JsonResponse({"customer":json.loads(datamain),"details":json.loads(datadetails),"damen":json.loads(damen)})

    else:
        if request.method == 'POST':
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
            return render(request,'callist/callist.html',{'branches':dailytask})
                    # ch = Comment(loan_code=request.POST['mycheckbox'][0],cus_code=request.POST['mycheckbox'][2],comhead=key,desc=value,caller=username,emp=request.POST['mycheckbox'][1])
                    # ch.save()
    return render(request,'callist/callist.html',{'branches':dailytask})


# def getcustomerdata(request):
#     if request.method == 'POST':
#         cusnationalid = request.POST['customerdata']
#         commentsty = Cfmerchant.objects.raw("select comment_text as id from comments where ComCate = 'cf'")
#         customerdatas = Cfmerchant.objects.raw("select national_id as id ,* from dbo.dis_in_client_damen_cf where national_id = '{}'".format(cusnationalid))
#         damendatas = Cfmerchant.objects.raw("select branch_code as id,* from dbo.dis_in_client_damen_cf where c_s = 'ضامن' and loan_key in (select loan_key from dbo.dis_in_client_damen_cf where  national_id = '{}')".format(cusnationalid))
#         return JsonResponse({'customerdata':model_to_dict(customerdatas),'damendata':model_to_dict(damendatas),'com':model_to_dict(commentsty)})

