# Generated by Django 4.0.5 on 2022-08-16 17:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('discy', '0008_alter_organisation_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myuser',
            name='image',
        ),
        migrations.DeleteModel(
            name='Organisation',
        ),
        migrations.DeleteModel(
            name='Role',
        ),
    ]
