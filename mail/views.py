from mail.models import Mailbox, Template, Email
from mail.serializers import MailboxSerializer, TemplateSerializer, EmailSerializer
from rest_framework import generics, mixins

# For api/mailbox/
class MailboxList(generics.ListCreateAPIView):
    """ POST a new mailbox, GET all mailboxes data"""
    queryset = Mailbox.objects.all()
    serializer_class = MailboxSerializer


# For api/mailbox/:id/
class MailboxDetail(generics.RetrieveUpdateDestroyAPIView):
    """ GET, PUT, PATCH, DELETE a single mailbox"""
    queryset = Mailbox.objects.all()
    serializer_class = MailboxSerializer


# For api/template/
class TemplateList(generics.ListCreateAPIView):
    """ POST a new template, GET all templates"""
    queryset = Template.objects.all()
    serializer_class = TemplateSerializer


# For api/template/:id/
class TemplateDetail(generics.RetrieveUpdateDestroyAPIView):
    """ GET, PUT, PATCH, DELETE a single template"""
    queryset = Template.objects.all()
    serializer_class = TemplateSerializer


# For api/email/
class EmailList(generics.GenericAPIView, mixins.ListModelMixin): # Or ListCreateAPIView?
    queryset = Email.objects.all()
    serializer_class = EmailSerializer

