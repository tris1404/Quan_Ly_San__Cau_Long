# Generated by Django 5.1.4 on 2025-01-13 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Booking_Mng', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='court',
            name='available_slots',
        ),
        migrations.AlterField(
            model_name='court',
            name='status',
            field=models.CharField(choices=[('Available', 'Available'), ('Maintenance', 'Maintenance'), ('Closed', 'Closed')], default='Available', max_length=20),
        ),
    ]
