from mail import tasks
from mail.models import Mailbox, Template, Email
from mail.serializers import MailboxSerializer, TemplateSerializer, EmailSerializer
from rest_framework import generics, mixins
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


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

    def get_queryset(self):
        """
        Optionally filters emails according to date of creation (date) and/or sent status (True/False)
        """
        queryset = Email.objects.all()
        date = self.request.query_params.get('date')
        sent_status = self.request.query_params.get('sent_status')
        if date is not None:
            queryset = queryset.filter(date__date=date)
        if sent_status is not None:
            if sent_status == "True":
                queryset = queryset.exclude(sent_date__isnull=True)
            else:
                queryset = queryset.exclude(sent_date__isnull=False)
        return queryset

    def get(self):
        queryset = self.get_queryset()
        serializer = EmailSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = EmailSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.create(serializer.validated_data)
            if not email.mailbox.is_active:
                return Response({"Fail": "mailbox inactive"}, status=status.HTTP_400_BAD_REQUEST)
            email.save()
            serializer = EmailSerializer(instance=email)
            tasks.send_email.delay(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
