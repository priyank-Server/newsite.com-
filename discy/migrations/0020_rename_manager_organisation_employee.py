# Generated by Django 4.0.5 on 2022-08-17 05:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('discy', '0019_organisation_delete_employee'),
    ]

    operations = [
        migrations.RenameField(
            model_name='organisation',
            old_name='manager',
            new_name='employee',
        ),
    ]
