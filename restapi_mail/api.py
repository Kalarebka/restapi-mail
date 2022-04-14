from rest_framework import routers
from mail import views as mail_views

router = routers.DefaultRouter()
router.register(r'mailbox', mail_views.MailboxViewset)
router.register(r'template', mail_views.TemplateViewset)
router.register(r'email', mail_views.EmailViewset)
