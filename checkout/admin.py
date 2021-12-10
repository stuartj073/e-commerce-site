from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInLine(admin.TabularInline):
    """ 
    Allows us to add and edit line items in admin
    from inside the order model
    """
    order = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)
    readonly_fields = ('order_number', 'date'
                       'delvier_cost', 'order_total'
                       'grand_total')

    fields = ('order_number', 'date')

    list_display = ()

    ordering = 

admin.site.register(order, OrderAdmin)
