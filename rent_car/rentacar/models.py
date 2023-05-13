from django.db import models


class Car(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="car_images")
    capacity = models.IntegerField()
    fuel = models.CharField(max_length=10)
    price = models.DecimalField(decimal_places=2, max_digits=12)
    power = models.IntegerField()
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    number = models.IntegerField(unique=True)
    car = models.ForeignKey(Car, on_delete=models.PROTECT)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    price = models.DecimalField(decimal_places=2, max_digits=12)
    customer_name = models.CharField(max_length=50, null=True)
    phone = models.CharField(max_length=50, null=True)
    email = models.CharField(max_length=100, null=True)
    text = models.CharField(max_length=400, null=True)

    def __str__(self):
        return f"Order: {self.number}"
