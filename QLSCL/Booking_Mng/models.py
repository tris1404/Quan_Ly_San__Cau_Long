from django.db import models

# Create your models here.

from django.db import models
import datetime

class Court(models.Model):
    STATUS_CHOICES = [
        ('Available', 'Available'),
        ('Maintenance', 'Maintenance'),
        ('Closed', 'Closed'),
    ]

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    location = models.CharField(max_length=255)
    opening_time = models.TimeField()  # Định dạng thời gian
    closing_time = models.TimeField()  # Định dạng thời gian
    price_per_hour = models.DecimalField(max_digits=10, decimal_places=0)  # Giá theo giờ
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Available')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # Loại bỏ phần microseconds khi lưu thời gian
        if self.opening_time:
            self.opening_time = self.opening_time.replace(microsecond=0)
        if self.closing_time:
            self.closing_time = self.closing_time.replace(microsecond=0)
        super().save(*args, **kwargs)

    def formatted_opening_time(self):
        return self.opening_time.strftime('%H:%M:%S')

    def formatted_closing_time(self):
        return self.closing_time.strftime('%H:%M:%S')


from Customers_Mng.models import Customer  # Nếu cần, nhập khẩu Customer từ ứng dụng khác

# models.py trong Booking_Mng
class Booking(models.Model):
    customer = models.ForeignKey('Customers_Mng.Customer', on_delete=models.CASCADE, related_name='bookings')
    court = models.ForeignKey('Court', on_delete=models.CASCADE)
    date = models.DateField()
    time_slot = models.TimeField()
    duration = models.IntegerField()  # Thời gian chơi (ví dụ: số giờ)

    def __str__(self):
        return f"Booking for {self.customer.name} at {self.court.name} on {self.date} from {self.time_slot}"
