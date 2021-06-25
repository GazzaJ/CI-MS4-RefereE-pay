from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver


def update_on_save(sender, instance, created, **kwargs):
    """
    Updates the order total o