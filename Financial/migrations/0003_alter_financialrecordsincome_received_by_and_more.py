# Generated by Django 5.1.2 on 2024-10-18 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Financial', '0002_remove_financialrecordsincome_source_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='financialrecordsincome',
            name='received_by',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='financialrecordsspent',
            name='spent_by',
            field=models.CharField(max_length=255),
        ),
    ]
