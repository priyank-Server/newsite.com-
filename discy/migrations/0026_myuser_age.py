# Generated by Django 4.0.5 on 2022-08-17 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discy', '0025_alter_employee_org_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='age',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
