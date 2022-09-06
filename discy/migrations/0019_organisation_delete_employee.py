# Generated by Django 4.0.5 on 2022-08-17 05:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('discy', '0018_alter_employee_city_alter_employee_org_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Organisation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('role', models.CharField(choices=[('DVP', 'developer'), ('TST', 'tester'), ('QA', 'quality assurance'), ('MGR', 'manager'), ('TL', 'team leader')], max_length=25)),
                ('org_name', models.CharField(default='', max_length=30)),
                ('city', models.CharField(default='', max_length=30)),
                ('manager', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='employee', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'get_latest_by': 'modified',
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='Employee',
        ),
    ]
