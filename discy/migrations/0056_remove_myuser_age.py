# Generated by Django 4.0.5 on 2022-08-25 10:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('discy', '0055_alter_organisation_city'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myuser',
            name='age',
        ),
    ]
