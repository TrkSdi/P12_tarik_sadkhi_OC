# Generated by Django 4.2 on 2023-04-23 14:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('CRM', '0004_rename_prospect_lead_alter_client_date_created_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('status', models.BooleanField(default=False, verbose_name='Commencé')),
            ],
        ),
        migrations.AddField(
            model_name='client',
            name='company_name',
            field=models.CharField(blank=True, default=None, max_length=250, null=True, verbose_name='Compagnie'),
        ),
        migrations.AddField(
            model_name='lead',
            name='company_name',
            field=models.CharField(blank=True, default=None, max_length=250, null=True, verbose_name='Compagnie'),
        ),
        migrations.AlterField(
            model_name='client',
            name='sales_contact',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='contract',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Date de création'),
        ),
        migrations.AlterField(
            model_name='contract',
            name='date_updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Mis à jour le'),
        ),
        migrations.AlterField(
            model_name='contract',
            name='sales_contact',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='event',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Date de création'),
        ),
        migrations.AlterField(
            model_name='event',
            name='date_updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Mis à jour le'),
        ),
        migrations.AlterField(
            model_name='event',
            name='support_contact',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='lead',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Date de création'),
        ),
        migrations.AlterField(
            model_name='lead',
            name='date_updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Mis à jour le'),
        ),
        migrations.AlterField(
            model_name='lead',
            name='sales_contact',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='StatusEvent',
        ),
        migrations.AlterField(
            model_name='event',
            name='event_status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CRM.eventstatus'),
        ),
    ]
