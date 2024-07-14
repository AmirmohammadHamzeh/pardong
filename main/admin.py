from django.contrib import admin
from .models import *
"""
from django.contrib import admin
from .models import Debt

@admin.register(Debt)
class DebtAdmin(admin.ModelAdmin):
    list_display = ('buyer', 'amount', 'description', 'matins_share_of_purchase', 'gholam_share', 'hamze_share', 'mobin_share')
    search_fields = ('buyer',)"""

# Alternatively, you can use:
admin.site.register(Purchase)