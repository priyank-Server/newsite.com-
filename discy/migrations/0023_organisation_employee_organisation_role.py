# Generated by Django 4.0.5 on 2022-08-17 06:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('discy', '0022_role_alter_organisation_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='organisation',
            name='employee',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='organisation', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='organisation',
            name='role',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='organisation', to='discy.role'),
        ),
    ]
