from django.db import models

class Brand(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class ProductType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Seller(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Earphone(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    product_type = models.ForeignKey(ProductType, on_delete=models.CASCADE)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    warranty_period = models.IntegerField()
    image = models.ImageField(upload_to='earphone_images', default='path/to/default/image.jpg')
  # Add this line

    def __str__(self):
        return self.name

   
