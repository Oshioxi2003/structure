"""
User signals
"""
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User


@receiver(post_save, sender=User)
def user_post_save(sender, instance, created, **kwargs):
    """
    Signal handler for User post_save
    
    Args:
        sender: Model class
        instance: User instance
        created: Boolean indicating if instance was created
    """
    if created:
        # Perform actions after user creation
        # e.g., send welcome email, create user profile, etc.
        print(f"New user created: {instance.username}")
