from django.db import models
import datetime

#category
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Categories'


#customer
class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100, unique=True)
    password=models.CharField(max_length=50)
    phone_number = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.first_name}{self.last_name}'



#product
class Product(models.Model):
    name=models.CharField(max_length=10000)
    price=models.DecimalField(default=0, decimal_places=2, max_digits=9)
    category=models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description=models.TextField(max_length=10000, default="", blank=True, null=True)
    image=models.ImageField(upload_to='uploads/products/')
    is_sale=models.BooleanField(default=False)
    sale_price=models.DecimalField(default=0, decimal_places=2, max_digits=9)

    def __str__(self):
        return f'{self.name} {self.price}'
    



#order
class Order(models.Model):
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1)
    address=models.CharField(max_length=100, default="", blank=True)
    phone=models.CharField(max_length=10, default="", blank=True)
    order_date = models.DateTimeField(default=datetime.datetime.today)
    status=models.BooleanField(default=False)

    def __str__(self):
        return self.product



# Create your models here.
#to extract and play with databases
