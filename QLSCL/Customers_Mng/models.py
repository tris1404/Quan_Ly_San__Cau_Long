from django.db import models

# Create your models here.
# models.py trong Customers_Mng
# models.py trong Customers_Mng
# models.py trong Customers_Mng
class Customer(models.Model):
    name = models.CharField(max_length=225)
    phone = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True, null=True, blank=True)
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female')], null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=20, choices=[('Active', 'Active'), ('Inactive', 'Inactive')], default='Active')
    
    # Trường số tài khoản ngân hàng
    payment_account = models.CharField(max_length=255, null=True, blank=True)  # Số tài khoản ngân hàng
    
    # Trường tên ngân hàng
    bank_name = models.CharField(max_length=255, null=True, blank=True)  # Tên ngân hàng
    
    # Liên kết với model "Booking" trong ứng dụng "Booking_Mng"
    booking_history = models.ManyToManyField('Booking_Mng.Booking', blank=True, related_name='customers')

    def __str__(self):
        return self.name




    
class Guest(models.Model):
    name = models.CharField(max_length=225)
    phone = models.CharField(max_length=255)

