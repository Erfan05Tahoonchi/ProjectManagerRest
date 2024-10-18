from django.urls import path
from .views import FinancialRecordsSpentListCreateView, FinancialRecordsSpentListUpdateDeleteView, \
    FinancialRecordsIncomeListCreateView, FinancialRecordsIncomeListUpdateDeleteView

app_name = 'financial'

urlpatterns = [
    path('spent/list/create/', FinancialRecordsSpentListCreateView.as_view(), name='spent_list_create'),
    path('spent/update/destroy/<int:pk>/', FinancialRecordsSpentListUpdateDeleteView.as_view(),name='spent_update_destroy'),
    path('income/list/create/', FinancialRecordsIncomeListCreateView.as_view(), name='income_list_create'),
    path('income/update/destroy/<int:pk>/', FinancialRecordsIncomeListUpdateDeleteView.as_view(),name='income_update_destroy'),
]
