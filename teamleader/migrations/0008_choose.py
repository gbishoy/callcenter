# Generated by Django 4.0.4 on 2022-05-03 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teamleader', '0007_delete_choose'),
    ]

    operations = [
        migrations.CreateModel(
            name='choose',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loanofficer_name', models.TextField(blank=True, null=True)),
                ('employee', models.TextField(blank=True, null=True)),
                ('timeadd', models.DateField(auto_now_add=True)),
            ],
        ),
    ]