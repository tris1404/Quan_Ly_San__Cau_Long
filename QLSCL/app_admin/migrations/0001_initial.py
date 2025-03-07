# Generated by Django 5.1.4 on 2025-02-13 06:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Court',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('location', models.CharField(max_length=255)),
                ('opening_time', models.TimeField()),
                ('closing_time', models.TimeField()),
                ('price_per_hour', models.DecimalField(decimal_places=0, max_digits=10)),
                ('status', models.CharField(choices=[('Available', 'Available'), ('Maintenance', 'Maintenance'), ('Closed', 'Closed')], default='Available', max_length=20)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225)),
                ('phone', models.CharField(max_length=255)),
                ('email', models.EmailField(blank=True, max_length=255, null=True, unique=True)),
                ('gender', models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10, null=True)),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('status', models.CharField(choices=[('Active', 'Active'), ('Inactive', 'Inactive')], default='Active', max_length=20)),
                ('payment_account', models.CharField(blank=True, max_length=255, null=True)),
                ('bank_name', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time_slot', models.TimeField()),
                ('duration', models.IntegerField()),
                ('court', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_admin.court')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookings', to='app_admin.customer')),
            ],
        ),
    ]
