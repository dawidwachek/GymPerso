from django.contrib import admin

from .models import Order,Item

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_id', 'email_adress','order_status','name_coupon', 'pay_price','item_order']
    readonly_fields = ("order_id","created_at", "updated_at")
    fieldsets = [
        ('Orders data', {
            'fields':('order_status', 'order_id', 'created_at')
        }),
        ('Customer data', {
            'fields':('email_adress', 'language','user_name')
        }),
        ('Price data', {
            'fields':('original_price', 'name_coupon', 'pay_price')
        }),
        ('Edit data', {
            'fields':('updated_at', 'editor_email')
        }),
        ('Edit data', {
            #'classes':
            "classes": ["extrapretty"],
            'fields':('item_order',)
        }),
        ('tests', {
            "classes": ["callapse"],
            'fields':('test',)
        })


    ]
    
@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['item_id','email_adress','item_status']