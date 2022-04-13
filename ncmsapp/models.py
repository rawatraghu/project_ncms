from django.db import models
from django.db.models import manager

# Create your models here.
class bill(models.Model):
    bill_number=models.IntegerField(5)
    transaction_number=models.IntegerField(6)
    paid_through=models.CharField(max_length=4)
    amount=models.DecimalField(max_digits=5,decimal_places=2)
    time_date=models.DateTimeField()
    customer_id=models.IntegerField(3)

class branch(models.Model):
    branch_id=models.IntegerField(5)
    branch_name=models.CharField(max_length=20)
    branch_address=models.CharField(max_length=20)
    manager_id=models.IntegerField(5)
    cashier_id=models.IntegerField(5)

class card(models.Model):
    card_number=models.IntegerField(3)
    customer_id=models.IntegerField(3)
    valid_till=models.DateField()

class customer(models.Model):
    customer_id=models.IntegerField(3)
    customer_name=models.CharField(max_length=20)
    address=models.CharField(max_length=40)
    email_id=models.CharField(max_length=20)
    membership_period=models.IntegerField(3)
    branch_id=models.IntegerField(5)

class employee(models.Model):
    emp_id=models.IntegerField()
    emp_name=models.CharField(max_length=20)
    gender=models.CharField(max_length=1)
    address=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    salary=models.IntegerField(5)

class item(models.Model):
    item_number=models.IntegerField(2)
    item_name=models.CharField(max_length=20)
    price=models.DecimalField(max_digits=5,decimal_places=2)

class order_placed(models.Model):
    order_number=models.IntegerField()
    item_number=models.IntegerField()
    time_order_placed=models.TimeField()
    quantity=models.IntegerField()
    customer_id=models.IntegerField()