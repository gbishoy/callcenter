from django.shortcuts import redirect, render
from django.views.generic import View
from django.contrib.auth.decorators import *
from sqlalchemy import null, values
from .decorators import unauthorized_user,allowed_users
from .models import Cfmerchant ,Comment
from django.contrib import messages
from django.http import  HttpResponse,JsonResponse
from django.forms.models import model_to_dict
import json
from django.core import serializers
from django.db import connection

ofnames =''
@login_required(login_url='loginpage')
@allowed_users(['callers'])

def get(request):
    username = request.user.username
    
    dailytask = Cfmerchant.objects.raw("select distinct(branch_code) as id ,branch_name from dbo.dis_in_client_damen_cf inner join [dbo].[teamleader_choose] on dis_in_client_damen_cf.officer_name = [teamleader_choose].[loanofficer_name] and c_s = 'عميل' and [teamleader_choose].[employee] = '{}' and MONTH([dis_in_client_damen_cf].[loan_date]) = MONTH(GETDATE())-1 order by branch_name".format(username))
    if request.POST.get('branch'):
        branchcode = request.POST['branch']
        officername = Cfmerchant.objects.raw("select distinct(officer_name) as id  from dbo.dis_in_client_damen_cf inner join [dbo].[teamleader_choose] on dis_in_client_damen_cf.officer_name = [teamleader_choose].[loanofficer_name] and c_s = 'عميل' and [teamleader_choose].[employee] = '{}' and dis_in_client_damen_cf.branch_code='{}' and MONTH([loan_date])=MONTH(GETDATE())-1 order by dis_in_client_damen_cf.officer_name".format(username,branchcode))
        return render(request,'callist/callist.html',{'branches':dailytask,'officername':officername})
    elif request.POST.get('ofname'): 
         officernameloans = request.POST['ofname']
        
         cusnames = Cfmerchant.objects.raw("select distinct(national_id) as id , client_name from dbo.dis_in_client_damen_cf where officer_name = '{}' and MONTH([loan_date])=MONTH(GETDATE())-1 and c_s = 'عميل' ".format(officernameloans))
         commentsty = Cfmerchant.objects.raw("select comment_text as id from comments where LoanCategory = 'cf' and comment_id not in (271,270,291)")
         return render(request,'callist/loandetails.html',{'ofloans':cusnames,'com':commentsty})
        #  customerdatas = Cfmerchant.objects.raw("select branch_code as id ,* from dbo.dis_in_client_damen_cf where c_s = 'عميل' and loan_key = '{}'".format(loankey))
        #  damendatas = Cfmerchant.objects.raw("select branch_code as id, * from dbo.dis_in_client_damen_cf where c_s = 'ضامن' and loan_key = '{}'".format(loankey))
        #  return render(request,'callist/loandetails.html',{'customerdata':customerdatas,'damendata':damendatas,'com':commentsty}) 
    elif request.headers.get('x-requested-with') == 'XMLHttpRequest':
        if request.POST['nationalid'] == null:
            pass
        elif request.POST['nationalid'] != null:
            cusnationalid = request.POST['nationalid']
            # commentsty = Cfmerchant.objects.raw("select comment_text as id from comments where ComCate = 'cf'")
            customerdatasmain = Cfmerchant.objects.raw("select national_id as id,client_key,client_name,add4,officer_name,tel4,branch_name ,aprv_am,consumer_finance_initial_limit from dbo.dis_in_client_damen_cf where national_id = '{}' and MONTH([loan_date])=MONTH(GETDATE())-1 group by national_id,client_key,client_name,add4,officer_name,tel4,branch_name,aprv_am,consumer_finance_initial_limit".format(cusnationalid))
            customerdatas = Cfmerchant.objects.raw("select national_id as id ,* from dbo.dis_in_client_damen_cf where national_id = '{}'".format(cusnationalid))
            damendatas = Cfmerchant.objects.raw("select national_id as id,tel4,client_name,add4,client_key from dbo.dis_in_client_damen_cf where c_s = 'ضامن' and loan_key in (select distinct(loan_key) from dbo.dis_in_client_damen_cf where  national_id = '{}') and MONTH([loan_date])=MONTH(GETDATE())-1 GROUP BY national_id ,client_name,tel4,add4,client_key".format(cusnationalid))
            datamain = serializers.serialize('json', customerdatasmain, fields=('id','client_key','client_name','add4','officer_name','tel4','branch_name','aprv_am','consumer_finance_initial_limit'))
            datadetails = serializers.serialize('json', customerdatas, fields=('id','sub_category_name','category_name','client_name_m','inst','loan_am','aprv_no','loan_date'))
            damen = serializers.serialize('json', damendatas, fields=('id','client_key','client_name','add4','tel4'))
            return JsonResponse({"customer":json.loads(datamain),"details":json.loads(datadetails),"damen":json.loads(damen)})
        else:
            pass

    else:
        if request.method == 'POST':
           pass
    return render(request,'callist/callist.html',{'branches':dailytask})

def add_comment(request):
    username = request.user.username
    try:
        ch = Comment(loan_code=request.POST['nationalid'],comhead=request.POST['head'],desc=request.POST['des'],caller=username,emp=request.POST['emp'])
        ch.save()
        return JsonResponse({'state':'تم اضافة الكمت بنجاح'})
    except:
        print('faild')
        return JsonResponse({'state':'يرجي اعادة ادخال الكمنت'})

def getComments(request):
    username = request.user.username
    comcate = Cfmerchant.objects.raw("SELECT  [Id] as id ,[weight],[commentCategory],[violationKind],[comment],[indvORgroop],[oneONgroop],[kind],[type] FROM [AuditNetworkDB].[mounirdb].[commentsty] where [type] = 'cf' and kind = {}".format(request.POST['cmcat']))
    comcatego = serializers.serialize('json', comcate, fields=('id','weight','commentCategory','violationKind','comment','indvORgroop','oneONgroop','kind','type'))
    return JsonResponse({'comcategory':json.loads(comcatego)})

def updatecustomerstate(request):
    username = request.user.username
    print(request.POST['nationalid'])
    print(request.POST['status'])
    with connection.cursor() as cursor:
        cursor.execute("UPDATE [AuditNetworkDB].[dbo].[dis_in_client_damen_cf] SET [f0] = {} where national_id = {}".format(request.POST['status'],request.POST['nationalid']))

    return JsonResponse({'state':'done'})


def error_404_view(request, exception):
    return render(request,'404.html')