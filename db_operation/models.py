from django.db import models

# Create your models here.

class Customer(models.Model):
    customer_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50 , blank=False)
    last_name = models.CharField(max_length=50 , blank=False)
    email = models.EmailField(max_length=100 , blank=False)
    mobile_number = models.CharField(max_length=20 ,blank=False)
    address = models.CharField(max_length=200 , blank=False)
    Status = models.CharField(max_length=20 ,default='active')

    db_table = 'my_custom_table_name'

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Customer'