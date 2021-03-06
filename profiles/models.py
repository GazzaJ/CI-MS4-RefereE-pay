from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from matches.models import Team

from django_countries.fields import CountryField


class UserProfile(models.Model):
    """
    User profile model for maintaining
    payments and payment history
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=50, null=True, blank=True)
    team = models.ForeignKey(Team, null=True, blank=True,
                             on_delete=models.SET_NULL)
    profile_phone_number = models.CharField(max_length=20, null=True,
                                            blank=True)
    profile_street_address1 = models.CharField(max_length=80, null=True,
                                               blank=True)
    profile_street_address2 = models.CharField(max_length=80, null=True,
                                               blank=True)
    profile_town_or_city = models.CharField(max_length=80, null=True,
                                            blank=True)
    profile_county = models.CharField(max_length=80, null=True,
                                      blank=True)
    profile_postcode = models.CharField(max_length=20, null=True, blank=True)
    profile_country = CountryField(blank_label='Country', null=True,
                                   blank=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Create or update the user profile
    """
    if created:
        UserProfile.objects.create(user=instance)
    # Save the profile if an existing user
    instance.userprofile.save()
