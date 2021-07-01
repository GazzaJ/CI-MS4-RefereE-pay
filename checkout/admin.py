from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInLine(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('match_fines', 'lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInLine,) 
    readonly_fields = ('order_number', 'date',
                       'order_total', 'grand_total',)

    fields = ('order_number', 'full_name', 'email', 'phone_number',
              'street_address1', 'street_address2', 'town_or_city',
              'county_or_state', 'postcode', 'country', 
              'date', 'order_total', 'grand_total',)

    list_display = ('order_number', 'date', 'full_name',
                    'order_total', 'grand_total',)

    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)
