from rest_framework import permissions
from django.contrib.auth.models import User
from .models import FinancialRecordsSpent, FinancialRecordsIncome
from django.shortcuts import get_object_or_404


class CanUpdateDestroyFinancialRecordsSpent(permissions.BasePermission):
    """
    custom FinancialRecordSpent to check if the user can update or delete project
    """

    def has_permission(self, request, view):
        user = request.user
        financialRecordsSpent_id = view.kwargs.get('pk')
        financialRecordsSpent = get_object_or_404(FinancialRecordsSpent, id=financialRecordsSpent_id)

        try:
            if user == financialRecordsSpent.who_created:
                return True
        except user.DoesNotExist or financialRecordsSpent.DoesNotExist:
            pass
        return False

class CanUpdateDestroyFinancialRecordsIncome(permissions.BasePermission):
    """
    custom FinancialRecordsIncome to check if the user can update or delete project
    """

    def has_permission(self, request, view):
        user = request.user
        financialRecordsIncome_id = view.kwargs.get('pk')
        financialRecordsIncome = get_object_or_404(FinancialRecordsIncome, id=financialRecordsIncome_id)

        try:
            if user == financialRecordsIncome.who_created:
                return True
        except user.DoesNotExist or financialRecordsIncome.DoesNotExist:
            pass
        return False