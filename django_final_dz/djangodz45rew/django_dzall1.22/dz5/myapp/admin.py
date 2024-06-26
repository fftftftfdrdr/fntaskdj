from django.contrib import admin
from .models import Client, Product, Order

# Register your models here.
@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone_number', 'registration_date')
    search_fields = ('name', 'email')
    list_filter = ('registration_date',)
    fields = ('name', 'email', 'phone_number', 'address', 'registration_date')
    readonly_fields = ('registration_date',)

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return self.readonly_fields + ('email',)
        return self.readonly_fields

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'added_date')
    search_fields = ('name',)
    list_filter = ('added_date',)
    fields = ('name', 'description', 'price', 'quantity', 'photo', 'added_date')
    readonly_fields = ('added_date',)

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return self.readonly_fields + ('photo',)
        return self.readonly_fields

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'client', 'total_amount', 'order_date')
    search_fields = ('client__name', 'client__email')
    list_filter = ('order_date',)
    fields = ('client', 'products', 'total_amount', 'order_date')
    readonly_fields = ('order_date',)

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return self.readonly_fields + ('client', 'total_amount')
        return self.readonly_fields


