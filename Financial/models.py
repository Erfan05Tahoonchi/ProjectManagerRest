from django.contrib.auth.models import User
from django.db import models
from django.contrib.contenttypes.fields import GenericRelation, GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.utils import timezone


class FinancialRecordsSpent(models.Model):
    SPENT_TYPE_CHOICES = (
        ('salary', 'Salary'),
        ('equipment', 'Equipment'),
        ('rent', 'Rent'),
        ('utilities', 'Utilities'),
        ('tax', 'Tax'),
        ('maintenance', 'Maintenance'),
        ('travel', 'Travel'),
        ('supplies', 'Supplies'),
        ('advertising', 'Advertising'),
        ('insurance', 'Insurance'),
        ('consultant_fee', 'Consultant Fee'),
        ('loan_repayment', 'Loan Repayment'),
        ('miscellaneous', 'Miscellaneous'),
        ('other', 'Other'),
    )
    STATUS_CHOICES = (
        ('in progress', 'in progress'),
        ('paid', 'paid'),
        ('canceled', 'canceled'),
    )
    who_created = models.ForeignKey(User, on_delete=models.CASCADE)
    spent_by = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    spent_type = models.CharField(max_length=20, choices=SPENT_TYPE_CHOICES)
    price = models.FloatField()
    description = models.TextField()
    status = models.CharField(max_length=11, choices=STATUS_CHOICES)
    spent_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    def save(self, *args, **kwargs):
        if not self.pk:
            self.created_at = timezone.now()
        super(FinancialRecordsSpent, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class FinancialRecordsIncome(models.Model):
    INCOME_TYPE_CHOICES = (
        ('client_payment', 'Client Payment'),
        ('investment', 'Investment'),
        ('grant', 'Grant'),
        ('revenue', 'Revenue'),
        ('loan', 'Loan'),
        ('donation', 'Donation'),
        ('other', 'Other'),
    )
    STATUS_CHOICES = (
        ('in progress', 'in progress'),
        ('received', 'received'),
        ('canceled', 'canceled'),
    )
    who_created = models.ForeignKey(User, on_delete=models.CASCADE)
    received_by = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    income_type = models.CharField(max_length=20, choices=INCOME_TYPE_CHOICES)
    price = models.FloatField()
    completion_percentage = models.FloatField(default=0.0)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=11, choices=STATUS_CHOICES)
    receive_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    def save(self, *args, **kwargs):
        if not self.pk:
            self.created_at = timezone.now()

        if self.completion_percentage == 100.0:
            self.status = 'received'

        super(FinancialRecordsIncome, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.title}"
