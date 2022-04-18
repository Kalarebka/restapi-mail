from .models import Mailbox, Template, Email
from rest_framework import serializers
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

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
    class Meta:
        model = Email
        fields = ['id', 'mailbox', 'template', 'to', 'cc', 'bcc', 'reply_to', 'sent_date', 'date']

    def create(self, validated_data):
        return Email(**validated_data)



    # def clean_to(self):
    #     data = self.cleaned_data['to']
    #     for email in data:
    #         if not validate_email(email):
    #             raise ValidationError('Invalid email {}'.format(email))  # or raise serializers.ValidationError
    #     return data


