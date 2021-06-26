from django.db import models
from django.utils import timezone
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class SubscribedUser(models.Model):
    name = models.CharField(max_length=150)
    email= models.CharField(max_length=100, null = True, unique = True, error_messages={'unique': 'Email address already exist'})
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

@receiver(post_save, sender=SubscribedUser)
def send_email(sender, instance, created, **kwargs):
	if created:
		if instance.email:
			print(f"......................................................{instance.email}")
			send_mail("Subscription Mail", "Hey, You are now a subscriber", "harveyspect60@gmail.com", [instance.email], fail_silently=True)
