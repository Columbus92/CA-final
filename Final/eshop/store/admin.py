from django.contrib import admin
from .models import Store

class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity')

admin.site.register(Store, StoreAdmin)

