# Generated by Django 4.0.5 on 2022-08-24 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discy', '0054_alter_organisation_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organisation',
            name='city',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
