from attr import fields
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
from django.contrib.auth import logout

ofnames =''
@login_required(login_url='loginpage')
@allowed_users(['callers'])
def get(request):
    username = request.user.username
    
    dailytask = Cfmerchant.objects.raw("select distinct(branch_code) as id ,branch_name from dbo.dis_in_client_damen_cf inner join [dbo].[teamleader_choose] on dis_in_client_damen_cf.officer_name = [teamleader_choose].[loanofficer_name] and c_s = 'عميل' and [teamleader_choose].[employee] = '{}' and MONTH([dis_in_client_damen_cf].[loan_date]) = MONTH(GETDATE())-1 and f0 IS NULL order by branch_name".format(username))
    if request.POST.get('branch'):
        branchcode = request.POST['branch']
        officername = Cfmerchant.objects.raw("select distinct(officer_name) as id  from dbo.dis_in_client_damen_cf inner join [dbo].[teamleader_choose] on dis_in_client_damen_cf.officer_name = [teamleader_choose].[loanofficer_name] and c_s = 'عميل' and [teamleader_choose].[employee] = '{}' and dis_in_client_damen_cf.branch_code='{}' and MONTH([loan_date])=MONTH(GETDATE())-1 and f0 IS NULL order by dis_in_client_damen_cf.officer_name".format(username,branchcode))
        return render(request,'callist/callist.html',{'branches':dailytask,'officername':officername})
    elif request.POST.get('ofname'): 
         officernameloans = request.POST['ofname']
        
         cusnames = Cfmerchant.objects.raw("select distinct(national_id) as id , client_name from dbo.dis_in_client_damen_cf where officer_name = '{}' and MONTH([loan_date])=MONTH(GETDATE())-1 and c_s = 'عميل' and f0 IS NULL ".format(officernameloans))
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
            customerdatasmain = Cfmerchant.objects.raw("select national_id as id,client_key,client_name,add4,officer_name,tel4,branch_name ,aprv_am,consumer_finance_initial_limit,home_add_1_mem from dbo.dis_in_client_damen_cf where national_id = '{}' and MONTH([loan_date])=MONTH(GETDATE())-1 group by national_id,client_key,client_name,add4,officer_name,tel4,branch_name,aprv_am,consumer_finance_initial_limit,home_add_1_mem".format(cusnationalid))
            customerdatas = Cfmerchant.objects.raw("select national_id as id ,* from dbo.dis_in_client_damen_cf where national_id = '{}'".format(cusnationalid))
            damendatas = Cfmerchant.objects.raw("select national_id as id,tel4,client_name,add4,client_key from dbo.dis_in_client_damen_cf where c_s = 'ضامن' and loan_key in (select distinct(loan_key) from dbo.dis_in_client_damen_cf where  national_id = '{}') and MONTH([loan_date])=MONTH(GETDATE())-1 GROUP BY national_id ,client_name,tel4,add4,client_key".format(cusnationalid))
            datamain = serializers.serialize('json', customerdatasmain, fields=('id','client_key','client_name','add4','officer_name','tel4','branch_name','aprv_am','consumer_finance_initial_limit','home_add_1_mem'))
            datadetails = serializers.serialize('json', customerdatas, fields=('id','sub_category_name','category_name','client_name_m','inst','loan_am','aprv_no','loan_date'))
            damen = serializers.serialize('json', damendatas, fields=('id','client_key','client_name','add4','tel4'))
            return JsonResponse({"customer":json.loads(datamain),"details":json.loads(datadetails),"damen":json.loads(damen)})
        else:
            pass

    else:
        if request.method == 'POST':
           pass
    return render(request,'callist/callist.html',{'branches':dailytask})

@login_required(login_url='loginpage')
def add_comment(request):
    username = request.user.username
    try:
        ch = Comment(loan_code=request.POST['nationalid'],comhead=request.POST['head'],desc=request.POST['des'],caller=username,emp=request.POST['emp'])
        ch.save()
        return JsonResponse({'state':'تم اضافة الكمت بنجاح'})
    except:
        print('faild')
        return JsonResponse({'state':'يرجي اعادة ادخال الكمنت'})

@login_required(login_url='loginpage')
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

def logout_view(request):
    logout(request)
    return render(request,'loginpage.html')


# Page For recall The Customers 
@login_required(login_url='loginpage')
def edit_comments(request):
    username = request.user.username
    all_comments = Cfmerchant.objects.raw("SELECT dbo.comment.id, dbo.comment.comhead, dbo.dis_in_client_damen_cf.branch_name, dbo.dis_in_client_damen_cf.client_name, dbo.dis_in_client_damen_cf.client_key, dbo.comment.timeadd FROM     dbo.comment INNER JOIN dbo.dis_in_client_damen_cf ON dbo.comment.loan_code = dbo.dis_in_client_damen_cf.national_id where comhead <> '' and dbo.comment.caller = '{}' ".format(username))
    return render(request,'callist/editComments.html',{'comments':all_comments})

@login_required(login_url='loginpage')
def commentsFilter(request):
    username = request.user.username
    customername = request.POST['search']
    customername = customername.strip()
    filteredCustomer = Cfmerchant.objects.raw(" SELECT distinct dbo.comment.id, dbo.comment.comhead, dbo.dis_in_client_damen_cf.branch_name, dbo.dis_in_client_damen_cf.client_name, dbo.dis_in_client_damen_cf.client_key, dbo.comment.timeadd FROM     dbo.comment INNER JOIN dbo.dis_in_client_damen_cf ON dbo.comment.loan_code = dbo.dis_in_client_damen_cf.national_id where comhead <> '' and dbo.comment.caller = '{}' and dis_in_client_damen_cf.client_name like '{}%%' ".format(username,customername))
    filteredCustomerj = serializers.serialize('json',filteredCustomer,fields=('id','comhead','branch_name','client_name','client_key','timeadd'))

    return JsonResponse({'commentsf':json.loads(filteredCustomerj)})


def getcommentdetails(request):
    username = request.user.username
    comidde = request.POST['comid']
    comiddt = Cfmerchant.objects.raw("SELECT [id],[loan_code],[cus_code],[comhead],[desc],[caller],[emp],[timeadd] FROM [AuditNetworkDB].[dbo].[comment] where id = {}".format(comidde))
    comiddtj = serializers.serialize('json',comiddt,fields=('id','comhead','desc'))

    return JsonResponse({'commentsf':json.loads(comiddtj)})

def updatecomment(request):
    comidnum = request.POST['comid']
    comdescription = request.POST['comdescr']
    
    print('here is the ')
    print(comidnum)
    print(comdescription)
    try:
        with connection.cursor() as cursor:
            cursor.execute("update[AuditNetworkDB].[dbo].[comment] set [desc] = '{}' where id = {}".format(comdescription,comidnum))
            return JsonResponse({'state':'Updated Successfuly'})
    except:
        return JsonResponse({'state':'Faild To Update'})