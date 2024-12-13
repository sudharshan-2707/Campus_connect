from django.contrib.auth import get_user_model
from celery import shared_task 
from django.core.mail import send_mail
from project import settings
@shared_task(bind=True)
def send_mail_func(self,email):
        #operations

        mail_subject="Event registration is successfully completed" 
        
        to_email=email
        
        message="venue : JERUSALEM COLLEGE OF ENGINEEERING " 
        send_mail(
        subject = mail_subject,
        message=message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[to_email],
        fail_silently=False)
        print('email sent') 
        return "Sent Email Successfully...Check your mail please"