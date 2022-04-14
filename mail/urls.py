from django.urls import path

from . import views

app_name = "board"
urlpatterns = [
    path('mailbox/', views.MailboxList.as_view(), name='mailbox_list'),
    path('mailbox/<id>/', views.MailboxDetail.as_view(), name='mailbox_detail'),
    path('template/', views.TemplateList.as_view(), name='template_list'),
    path('template/<id>/', views.TemplateDetail.as_view(), name='template_list'),
    path('email/', views.EmailList.as_view(), name='email_list'),
]
