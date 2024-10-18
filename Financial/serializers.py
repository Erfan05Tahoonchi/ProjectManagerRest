from rest_framework import serializers
from .models import FinancialRecordsSpent, FinancialRecordsIncome
from abc import ABC
from Projects.models import Project, Task, SubTask
from Projects.serializers import ProjectSerializers, TaskSerializers, SubTaskSerializers
from django.utils import timezone


class FinancialRecordRelatedField(serializers.RelatedField, ABC):
    def to_representation(self, value):
        if isinstance(value, Project):
            serializer = ProjectSerializers(value)
        elif isinstance(value, Task):
            serializer = TaskSerializers(value)
        elif isinstance(value, SubTask):
            serializer = SubTaskSerializers(value)
        else:
            raise Exception("Unexpected type of object")
        return serializer.data


class FinancialRecordsSpentSerializer(serializers.ModelSerializer):
    content_object = FinancialRecordRelatedField(read_only=True)

    class Meta:
        model = FinancialRecordsSpent
        fields = ['pk', 'who_created', 'spent_by', 'title', 'spent_type', 'price', 'description', 'status', 'spent_date', 'created_at', 'updated_at', 'content_type', 'object_id', 'content_object']
        extra_kwargs = {
            'who_created': {'read_only': True},
            'created_at': {'read_only': True},
            'updated_at': {'read_only': True},
        }

    def update(self, instance, validated_data):
        status_changed = 'status' in validated_data and validated_data['status'] != instance.status
        spent_by_changed = 'spent_by' in validated_data and validated_data['spent_by'] != instance.spent_by
        spent_type = 'spent_type' in validated_data and validated_data['spent_type'] != instance.spent_type
        spent_date = 'spent_date' in validated_data and validated_data['spent_date'] != instance.spent_date
        content_type_changed = 'content_type' in validated_data and validated_data['content_type'] != instance.content_type
        object_id_changed = 'object_id' in validated_data and validated_data['object_id'] != instance.object_id

        if instance.status in ['canceled', 'paid']:
            raise serializers.ValidationError(
                "This record has been marked as 'canceled' or 'paid' and cannot be updated.")
        elif spent_by_changed:
            raise serializers.ValidationError(
                "This record 'spent_by' cannot be updated."
            )
        elif spent_type:
            raise serializers.ValidationError(
                "This record 'spent_type' cannot be updated."
            )
        elif spent_date:
            raise serializers.ValidationError(
                "This record 'spent_date' cannot be updated."
            )
        elif content_type_changed:
            raise serializers.ValidationError(
                "This record 'content_type' cannot be updated."
            )
        elif object_id_changed:
            raise serializers.ValidationError(
                "This record 'object_id' cannot be updated."
            )

        instance.title = validated_data.get('title', instance.title)
        instance.price = validated_data.get('price', instance.price)
        instance.description = validated_data.get('description', instance.description)
        instance.status = validated_data.get('status', instance.status)

        if not status_changed or validated_data['status'] in ['canceled', 'paid']:
            instance.updated_at = timezone.now()

        instance.save()
        return instance


class FinancialRecordsIncomeSerializer(serializers.ModelSerializer):
    content_object = FinancialRecordRelatedField(read_only=True)

    class Meta:
        model = FinancialRecordsIncome
        fields = ['pk', 'who_created', 'received_by', 'title', 'income_type', 'price', 'completion_percentage',
                  'description', 'status', 'receive_date', 'created_at', 'updated_at', 'status', 'receive_date',
                  'created_at', 'updated_at', 'content_type', 'object_id', 'content_object']

        extra_kwargs = {
            'who_created': {'read_only': True},
            'created_at': {'read_only': True},
            'updated_at': {'read_only': True},
        }

    def update(self, instance, validated_data):
        status_changed = 'status' in validated_data and validated_data['status'] != instance.status
        received_by_changed = 'received_by' in validated_data and validated_data['received_by'] != instance.received_by
        income_type_changed = 'income_type' in validated_data and validated_data['income_type'] != instance.income_type
        received_date_changed = 'received_date' in validated_data and validated_data['received_date'] != instance.received_date
        content_type_changed = 'content_type' in validated_data and validated_data['content_type'] != instance.content_type
        object_id_changed = 'object_id' in validated_data and validated_data['object_id'] != instance.object_id

        if instance.status in ['canceled', 'received']:
            raise serializers.ValidationError(
                "This record has been marked as 'canceled' or 'received' and cannot be updated.")
        elif received_by_changed:
            raise serializers.ValidationError(
                "This record 'received_by' cannot be updated."
            )
        elif income_type_changed:
            raise serializers.ValidationError(
                "This record 'income_type' cannot be updated."
            )
        elif received_date_changed:
            raise serializers.ValidationError(
                "This record 'received_date' cannot be updated."
            )
        elif content_type_changed:
            raise serializers.ValidationError(
                "This record 'content_type' cannot be updated."
            )
        elif object_id_changed:
            raise serializers.ValidationError(
                "This record 'object_id' cannot be updated."
            )

        instance.title = validated_data.get('title', instance.title)
        instance.price = validated_data.get('price', instance.price)
        instance.completion_percentage = validated_data.get('completion_percentage', instance.completion_percentage)
        instance.description = validated_data.get('description', instance.description)
        instance.status = validated_data.get('status', instance.status)

        if instance.completion_percentage == 100:
            instance.status = 'received'

        if instance.status == 'received':
            instance.completion_percentage = 100
        elif instance.status == 'canceled':
            instance.completion_percentage = 0

        if not status_changed or validated_data['status'] in ['canceled', 'received']:
            instance.updated_at = timezone.now()

        instance.save()
        return instance
