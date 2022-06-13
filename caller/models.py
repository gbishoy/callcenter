from django.db import models

# Create your models here.
class Cfmerchant(models.Model):
    issue_date = models.DateTimeField(blank=True, null=True)
    loan_key = models.BigIntegerField(blank=True, null=True)
    loan_status = models.TextField(blank=True, null=True)
    loanofficer_name = models.TextField(blank=True, null=True)
    loanofficer_id = models.TextField(blank=True, null=True)
    customer_id = models.TextField(blank=True, null=True)
    customer_name = models.TextField(blank=True, null=True)
    customer_national_id = models.BigIntegerField(blank=True, null=True)
    key = models.BigIntegerField(blank=True, null=True)
    gender = models.TextField(blank=True, null=True)
    mobile_phone_number = models.BigIntegerField(blank=True, null=True)
    gov = models.TextField(db_column='Gov', blank=True, null=True)  # Field name made lowercase.
    branch_name = models.TextField(db_column='Branch-Name', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    company = models.TextField(db_column='Company', blank=True, null=True)  # Field name made lowercase.
    product_price = models.FloatField(blank=True, null=True)
    principal_paid = models.FloatField(blank=True, null=True)
    first_installment_date = models.TextField(blank=True, null=True)
    total_installment = models.FloatField(blank=True, null=True)
    tenure = models.BigIntegerField(blank=True, null=True)
    approved_limit = models.BigIntegerField(blank=True, null=True)
    utilized_limit = models.FloatField(blank=True, null=True)
    available_limit = models.FloatField(blank=True, null=True)
    interest_rate = models.BigIntegerField(blank=True, null=True)
    item_transaction_id = models.TextField(blank=True, null=True)
    vendor_id = models.TextField(blank=True, null=True)
    merchant_name = models.TextField(blank=True, null=True)
    category_name = models.TextField(blank=True, null=True)
    sub_category_name = models.TextField(blank=True, null=True)
    client_key = models.TextField(blank=True, null=True)
    client_name = models.TextField(blank=True, null=True)
    add4 = models.TextField(blank=True, null=True)
    officer_name = models.TextField(blank=True, null=True)
    tel4 = models.TextField(blank=True, null=True)
    aprv_am = models.TextField(blank=True, null=True)
    aprv_no = models.TextField(blank=True, null=True)
    sub_category_name = models.TextField(blank=True, null=True)
    category_name = models.TextField(blank=True, null=True)
    client_name_m = models.TextField(blank=True, null=True)
    inst = models.TextField(blank=True, null=True)
    loan_am = models.TextField(blank=True, null=True)
    loan_date = models.TextField(blank=True, null=True)
    consumer_finance_initial_limit = models.TextField(blank=True, null=True)
    weight = models.TextField(blank=True, null=True)
    commentCategory = models.TextField(blank=True, null=True)
    violationKind = models.TextField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    indvORgroop = models.TextField(blank=True, null=True)
    oneONgroop = models.TextField(blank=True, null=True)
    kind = models.TextField(blank=True, null=True)
    type = models.TextField(blank=True, null=True)
    f0 = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cfmerchant'

class Comment(models.Model):
    loan_code = models.CharField(max_length=200, blank=True, null=True)
    cus_code = models.CharField(max_length=200, blank=True, null=True)
    comhead = models.CharField(max_length=200, blank=True, null=True)
    desc = models.TextField(blank=True, null=True)
    caller = models.CharField(max_length=200, blank=True, null=True)
    emp = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'comment'