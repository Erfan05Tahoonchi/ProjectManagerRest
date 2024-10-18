from django.contrib import admin
from .models import FinancialRecordsSpent,FinancialRecordsIncome

admin.site.register(FinancialRecordsSpent)
admin.site.register(FinancialRecordsIncome)
