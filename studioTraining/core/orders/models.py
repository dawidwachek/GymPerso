from django.db import models

class Orders(models.Model):
    
    slug = models.SlugField(max_length=255, unique=True),
    
    email_adress = models.CharField(max_length=255)
    name_coupon = models.CharField(max_length=15),
    original_price = models.DecimalField(max_digits=5, decimal_places=2),
    pay_price = models.DecimalField(max_digits=5, decimal_places=2),
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    editor_email = models.CharField(max_length=255)

    class Meta:
        ordering = ('-created_at')
    def __str__(self):
        return self.slug
    

class Items(models.Model):
    slug = models.SlugField(max_length=255, unique=True)
    def __str__(self):
        return self.slug