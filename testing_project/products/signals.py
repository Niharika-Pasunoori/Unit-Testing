from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from products.models import User

@receiver(post_save,sender=User)
def send_welcome_email(sender,instance,created,**kwargs):
    """Send a welcome email when a new user is created."""
    print("Signal fired...")
    if created:
        send_mail(
            'Welcome!',
            'Thanks for signing up!',
            'admin@django.com',  # form-email
            [instance.email], # recipient list
            fail_silently=False,
        )