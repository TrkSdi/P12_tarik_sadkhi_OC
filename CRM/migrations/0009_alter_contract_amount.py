# Generated by Django 4.2 on 2023-05-16 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CRM', '0008_alter_client_sales_contact_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='amount',
            field=models.FloatField(default=0.0, verbose_name='Montant'),
        ),
    ]