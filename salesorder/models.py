from django.db import models

# Create your models here.
class Sales(models.Model):
    sales_name = models.CharField(max_length=50)
    sales_employee_id = models.IntegerField(unique=True)

    def __str__(self):
        return self.sales_name
    
class Order(models.Model):
    customer = models.CharField(max_length=50)
    so_number = models.CharField(max_length=20)
    sales_id = models.ForeignKey(Sales, on_delete=models.PROTECT)
    artikel = models.CharField(max_length=20)
    warna = models.CharField(max_length=20)
    nomor_mesin = models.IntegerField()
    qty = models.IntegerField()

    def __str__(self):
        return self.so_number
