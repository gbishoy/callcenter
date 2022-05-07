# Generated by Django 4.0.4 on 2022-05-07 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('caller', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('loan_code', models.CharField(blank=True, max_length=200, null=True)),
                ('cus_code', models.CharField(blank=True, max_length=200, null=True)),
                ('comhead', models.CharField(blank=True, max_length=200, null=True)),
                ('desc', models.TextField(blank=True, null=True)),
                ('caller', models.CharField(blank=True, max_length=200, null=True)),
                ('timeadd', models.DateField()),
                ('emp', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'db_table': 'comment',
                'managed': False,
            },
        ),
    ]
