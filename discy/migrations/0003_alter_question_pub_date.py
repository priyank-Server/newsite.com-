# Generated by Django 4.0.4 on 2022-05-11 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discy', '0002_question_first_name_question_last_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
