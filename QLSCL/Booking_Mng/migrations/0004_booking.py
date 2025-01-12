# Generated by Django 5.1.4 on 2025-01-13 05:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Booking_Mng', '0003_alter_court_price_per_hour'),
        ('Customers_Mng', '0002_guest_remove_customer_gender'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time_slot', models.TimeField()),
                ('duration', models.IntegerField()),
                ('court', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Booking_Mng.court')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookings', to='Customers_Mng.customer')),
            ],
        ),
    ]
