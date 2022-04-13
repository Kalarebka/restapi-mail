import uuid

from django.db import models


class Mailbox(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    host = models.CharField(max_length=100)
    port = models.IntegerField(default=465)
    login = models.CharField(max_length=50)
    # TODO How to make password secure and retrievable at the same time?
    password = models.CharField(max_length=50)
    email_from = models.CharField(max_length=100)
    use_ssl = models.BooleanField(default=True)
    is_active = models.BooleanField(default=False)
    data = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now_add=True)

    @property
    def sent(self):
        return self.email_set.count()


class Template(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    subject = models.CharField(max_length=250)
    text = models.TextField()
    # TODO Set media root and make uploads directory
    attachment = models.FileField(upload_to='uploads/')
    date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now_add=True)


class Email(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    mailbox = models.ForeignKey(Mailbox, on_delete=models.CASCADE)
    template = models.ForeignKey(Template, on_delete=models.CASCADE)
    # TODO postgres ArrayField or JSONField?
    # to =
    # cc =
    # bcc =
    reply_to = models.EmailField(default=None, null=True)
    sent_date = models.DateTimeField(default=None, null=True)
    date = models.DateTimeField(auto_now_add=True)
