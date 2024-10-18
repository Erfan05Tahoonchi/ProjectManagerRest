from django.shortcuts import render
from .models import FinancialRecordsSpent, FinancialRecordsIncome
from .serializers import serializers, FinancialRecordsSpentSerializer, FinancialRecordsIncomeSerializer
from rest_framework import generics
from .permissions import permissions, CanUpdateDestroyFinancialRecordsSpent, CanUpdateDestroyFinancialRecordsIncome
from rest_framework.response import Response
from rest_framework import status


# FinancialRecordsSpent
class FinancialRecordsSpentListCreateView(generics.ListCreateAPIView):
    """
    this views make and show list of financial spent records
    """
    serializer_class = FinancialRecordsSpentSerializer

    def get_queryset(self):
        user = self.request.user
        return FinancialRecordsSpent.objects.filter(who_created=user).order_by('-price')

    def perform_create(self, serializer):
        user = self.request.user
        if serializer.validated_data.get('status') == 'canceled':
            raise serializers.ValidationError("You cannot create a record with status 'canceled'.")
        serializer.save(who_created=user)


class FinancialRecordsSpentListUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    """
    this views update and delete financial spent records
    """
    serializer_class = FinancialRecordsSpentSerializer
    permission_classes = [permissions.IsAuthenticated, CanUpdateDestroyFinancialRecordsSpent]
    queryset = FinancialRecordsSpent
    lookup_field = 'pk'

    def perform_update(self, serializer):
        if serializer.is_valid():
            serializer.save()

    def perform_destroy(self, instance):
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# FinancialRecordsIncome
class FinancialRecordsIncomeListCreateView(generics.ListCreateAPIView):
    """
    this views make and show list of financial income records
    """
    serializer_class = FinancialRecordsIncomeSerializer

    def get_queryset(self):
        user = self.request.user
        return FinancialRecordsIncome.objects.filter(who_created=user).order_by('-price')

    def perform_create(self, serializer):
        user = self.request.user
        if serializer.validated_data.get('status') == 'canceled':
            raise serializers.ValidationError("You cannot create a record with status 'canceled'.")
        serializer.save(who_created=user)


class FinancialRecordsIncomeListUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    """
    this views update and delete financial income records
    """
    serializer_class = FinancialRecordsIncomeSerializer
    permission_classes = [permissions.IsAuthenticated, CanUpdateDestroyFinancialRecordsIncome]
    queryset = FinancialRecordsIncome
    lookup_field = 'pk'

    def perform_update(self, serializer):
        if serializer.is_valid():
            serializer.save()

    def perform_destroy(self, instance):
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
