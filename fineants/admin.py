from django.contrib import admin
from .models import Transaction


class TransactionAdmin(admin.ModelAdmin):
    list_display = ('title', 'creditor', 'amount', 'created')
    search_fields = ['title', 'creditor', 'amount', 'created']
    fieldsets = [
        ('General', {'fields': ['title', 'creditor', 'debitors', 'amount']}),
        ('Meta',    {'fields': ['created'], 'classes': ['collapse']}),
    ]


admin.site.register(Transaction, TransactionAdmin)