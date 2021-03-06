# Generated by Django 4.0.4 on 2022-05-03 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cfmerchant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('issue_date', models.DateTimeField(blank=True, null=True)),
                ('loan_key', models.BigIntegerField(blank=True, null=True)),
                ('loan_status', models.TextField(blank=True, null=True)),
                ('loanofficer_name', models.TextField(blank=True, null=True)),
                ('loanofficer_id', models.TextField(blank=True, null=True)),
                ('customer_id', models.TextField(blank=True, null=True)),
                ('customer_name', models.TextField(blank=True, null=True)),
                ('customer_national_id', models.BigIntegerField(blank=True, null=True)),
                ('key', models.BigIntegerField(blank=True, null=True)),
                ('gender', models.TextField(blank=True, null=True)),
                ('mobile_phone_number', models.BigIntegerField(blank=True, null=True)),
                ('gov', models.TextField(blank=True, db_column='Gov', null=True)),
                ('branch_name', models.TextField(blank=True, db_column='Branch-Name', null=True)),
                ('company', models.TextField(blank=True, db_column='Company', null=True)),
                ('product_price', models.FloatField(blank=True, null=True)),
                ('principal_paid', models.FloatField(blank=True, null=True)),
                ('first_installment_date', models.TextField(blank=True, null=True)),
                ('total_installment', models.FloatField(blank=True, null=True)),
                ('tenure', models.BigIntegerField(blank=True, null=True)),
                ('approved_limit', models.BigIntegerField(blank=True, null=True)),
                ('utilized_limit', models.FloatField(blank=True, null=True)),
                ('available_limit', models.FloatField(blank=True, null=True)),
                ('interest_rate', models.BigIntegerField(blank=True, null=True)),
                ('item_transaction_id', models.TextField(blank=True, null=True)),
                ('vendor_id', models.TextField(blank=True, null=True)),
                ('merchant_name', models.TextField(blank=True, null=True)),
                ('category_name', models.TextField(blank=True, null=True)),
                ('sub_category_name', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'cfmerchant',
                'managed': False,
            },
        ),
    ]
