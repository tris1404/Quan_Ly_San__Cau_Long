# Generated by Django 5.1.4 on 2025-01-13 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Booking_Mng', '0004_booking'),
        ('Customers_Mng', '0002_guest_remove_customer_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='address',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='birth_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='booking_history',
            field=models.ManyToManyField(blank=True, related_name='customers', to='Booking_Mng.booking'),
        ),
        migrations.AddField(
            model_name='customer',
            name='email',
            field=models.EmailField(blank=True, max_length=255, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='gender',
            field=models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='payment_account',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='status',
            field=models.CharField(choices=[('Active', 'Active'), ('Inactive', 'Inactive')], default='Active', max_length=20),
        ),
    ]
