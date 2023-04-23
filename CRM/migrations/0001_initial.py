# Generated by Django 4.2 on 2023-04-21 10:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=25)),
                ('last_name', models.CharField(max_length=25)),
                ('email', models.EmailField(max_length=100)),
                ('phone', models.CharField(max_length=10)),
                ('mobile', models.CharField(max_length=10)),
                ('date_created', models.DateField()),
                ('date_updated', models.DateField()),
                ('sales_contact', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateField()),
                ('date_updated', models.DateField()),
                ('status', models.BooleanField(default=False)),
                ('amount', models.FloatField()),
                ('payement_due', models.DateField()),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CRM.client')),
                ('sales_contact', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateField()),
                ('date_updated', models.DateField()),
                ('attendees', models.IntegerField()),
                ('event_date', models.DateTimeField()),
                ('note', models.TextField(max_length=500)),
                ('client', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='CRM.client')),
                ('event_status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CRM.contract')),
                ('support_contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='StatusEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('event_id', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='CRM.event')),
            ],
        ),
        migrations.CreateModel(
            name='Prospect',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=25)),
                ('last_name', models.CharField(max_length=25)),
                ('email', models.EmailField(max_length=100)),
                ('phone', models.CharField(max_length=10)),
                ('mobile', models.CharField(max_length=10)),
                ('date_created', models.DateField()),
                ('date_updated', models.DateField()),
                ('sales_contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
