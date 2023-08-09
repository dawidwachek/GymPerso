from django.db import models

class Item(models.Model):
    item_id = models.AutoField(primary_key=True)
    email_adress = models.EmailField(max_length=255)
    item_status = models.CharField(choices=[
        ('IC', 'Item Created'),
        ('IW', 'Item Verified'),
    ], default="IC", max_length=255)
    editor_email = models.EmailField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    language = models.CharField(choices=[
        ("PL", "Polish"),
        ("EN", "English"),
    ], default="EN", max_length=255)

    def __str__(self):
        #return self.item_id
        return f'{self.item_id} {self.email_adress}'

    
    
class Order(models.Model):
    order_status = models.CharField(choices=[
        ("OC", "Order Created"),
        ("WP", "Waiting for Payment"),
        ("PA", "Payment Accepted"),
        ("PE", "Payment Error"),
        ("WA", "Waiting for Acception"),
        ("OA", "Order Accepted"),
        ("OS", "Order Sended"),
    ],default='OC', max_length=255)
    order_id = models.AutoField(primary_key=True)
    email_adress = models.EmailField(max_length=255)
    user_name = models.CharField(max_length=30, blank=True)
    language = models.CharField(choices=[
        ("PL", "Polish"),
        ("EN", "English"),
    ], default="EN", max_length=255)
    name_coupon = models.CharField(max_length=15, null=True, blank=True)
    original_price = models.DecimalField(max_digits=7, decimal_places=2)
    pay_price = models.DecimalField(max_digits=7, decimal_places=2)
    editor_email = models.EmailField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    item_order = models.ForeignKey('orders.Item', related_name="items", null=True, blank=True, on_delete=models.CASCADE)

    i1 = Item.objects.all()
    print(i1)
    test = models.ManyToManyField(Item, null=True, blank=True)
    str_test = str(test)
    

    def __int__(self):
        return self.order_id





    

    
