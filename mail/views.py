from mail import tasks
from mail.models import Mailbox, Template, Email
from mail.serializers import MailboxSerializer, TemplateSerializer, EmailSerializer
from rest_framework import generics, mixins
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django_filters import rest_framework as filters


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
class EmailList(mixins.ListModelMixin, APIView):
    """ GET a list of all emails, POST and send a single email"""
    queryset = Email.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('category', 'in_stock')

    # def get(self, request):
    #     queryset = Email.objects.all()
    #     serializer = EmailSerializer(emails, many=True)
    #     return Response(serializer.data)

    def post(self, request):
        serializer = EmailSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.create(serializer.validated_data)
            if not email.mailbox.is_active:
                return Response({"Fail": "mailbox inactive"}, status=status.HTTP_400_BAD_REQUEST)
            email.save()
            tasks.send_email.delay(email)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# FilterSet:
class EmailFilter(filters.FilterSet):
    class Meta:
        model = Email
        fields = ('sent_date', 'date')
