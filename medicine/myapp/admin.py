from django.contrib import admin
from . models import *
from django.utils.html import format_html
from django.urls import reverse

@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title','selling_price','discounted_price', 'category','product_image']

@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user','locality','city', 'state','zipcode']

@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','product','quantity']
    def products(self,obj):
        link=reverse("admin:myapp_product_change",args=[obj.product.pk])
        return format_html('<a href="{}">{}</a>',link,obj.product.title)

@admin.register(Payment)
class PaymentModelAdmin(admin.ModelAdmin):
    list_display=['id','user','amount','razorpay_order_id','razorpay_payment_status','razorpay_payment_id','paid']

@admin.register(OrderPlaced)
class OrderPlacedModelAdmin(admin.ModelAdmin):
    list_display=['id','user','customer','product','quantity','ordered_date','status','payment']
    def products(self,obj):
        link=reverse("admin:myapp_customer_change",args=[obj.customer.pk])
        return format_html('<a href="{}">{}</a>',link,obj.customer.name)
  
    def products(self,obj):
        link=reverse("admin:myapp_product_change",args=[obj.product.pk])
        return format_html('<a href="{}">{}</a>',link,obj.product.title)

    def products(self,obj):
        link=reverse("admin:myapp_payment_change",args=[obj.payment.pk])
        return format_html('<a href="{}">{}</a>',link,obj.payment.razorpay_payment_id)


@admin.register(Wishlist)
class WishlistModelAdmin(admin.ModelAdmin):
    list_display=['id','user','product']
    def products(self,obj):
        link=reverse("admin:myapp_product_change",args=[obj.product.pk])
        return format_html('<a href="{}">{}</a>',link,obj.product.title)

