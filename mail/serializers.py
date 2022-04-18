from .models import Mailbox, Template, Email
from rest_framework import serializers
from rest_framework.fields import ListField


class StringArrayField(ListField):
    """
    String representation of an array field.
    """
    def to_representation(self, obj):
        obj = super().to_representation(obj)
        return ",".join([str(element) for element in obj])

    def to_internal_value(self, data):
        # data = data.split(",")
        return super().to_internal_value(data)


class MailboxSerializer(serializers.ModelSerializer):
    sent = serializers.ReadOnlyField()

    class Meta:
        model = Mailbox
        fields = ['id', 'host', 'port', 'login', 'password', 'email_from', 'use_ssl', 'is_active', 'date', 'last_update', 'sent']


class TemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Template
        fields = ['id', 'subject', 'text', 'attachment', 'date', 'last_update']


class EmailSerializer(serializers.ModelSerializer):
    to = StringArrayField()
    cc = StringArrayField(required=False)
    bcc = StringArrayField(required=False)

    class Meta:
        model = Email
        fields = ['id', 'mailbox', 'template', 'to', 'cc', 'bcc', 'reply_to', 'sent_date', 'date']

    def create(self, validated_data):
        return Email(**validated_data)



