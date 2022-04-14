from rest_framework import viewsets
from . import models
from . import serializers


class MailboxViewset(viewsets.ModelViewSet):
    queryset = models.Mailbox.objects.all()
    serializer_class = serializers.MailboxSerializer


class TemplateViewset(viewsets.ModelViewSet):
    queryset = models.Template.objects.all()
    serializer_class = serializers.TemplateSerializer


class EmailViewset(viewsets.ModelViewSet):
    queryset = models.Email.objects.all()
    serializer_class = serializers.Email
