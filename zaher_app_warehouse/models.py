from django.db import models

# Create your models here.
class StockManagement(models.Model):
    product_name = models.CharField(max_length=200)
    product_image = models.ImageField(upload_to='product-images/')
    product_price = models.CharField(max_length=10)
    product_description = models.TextField(max_length=1000)
    warehouse_name = models.ForeignKey("Warehouse", on_delete=models.CASCADE, null=True, related_name="warehouse")

    def __str__(self):
        return self.product_name

    class Meta:
        verbose_name_plural = "Stock Management"
        
class Warehouse(models.Model):
    warehouse_name = models.CharField(max_length=100)

    def __str__(self):
        return self.warehouse_name

    class Meta:
        verbose_name_plural = "Add or Remove Warehouse"