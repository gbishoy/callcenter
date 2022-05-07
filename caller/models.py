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

    class Meta:
        managed = False
        db_table = 'cfmerchant'