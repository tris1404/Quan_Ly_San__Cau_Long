from django.db import models

class Court(models.Model):
    STATUS_CHOICES = [
        ('Available', 'Available'),
        ('Maintenance', 'Maintenance'),
        ('Closed', 'Closed'),
    ]

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    location = models.CharField(max_length=255)
    opening_time = models.TimeField()
    closing_time = models.TimeField()
    price_per_hour = models.DecimalField(max_digits=10, decimal_places=0)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Available')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.opening_time:
            self.opening_time = self.opening_time.replace(microsecond=0)
        if self.closing_time:
            self.closing_time = self.closing_time.replace(microsecond=0)
        super().save(*args, **kwargs)

class Customer(models.Model):
    name = models.CharField(max_length=225)
    phone = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True, null=True, blank=True)
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female')], null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=20, choices=[('Active', 'Active'), ('Inactive', 'Inactive')], default='Active')
    
    payment_account = models.CharField(max_length=255, null=True, blank=True)
    bank_name = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name

class Booking(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='bookings')
    court = models.ForeignKey(Court, on_delete=models.CASCADE)
    date = models.DateField()
    time_slot = models.TimeField()
    duration = models.IntegerField()

    def __str__(self):
        return f"Booking for {self.customer.name} at {self.court.name} on {self.date} from {self.time_slot}"
