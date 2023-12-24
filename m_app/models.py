from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import CustomUserManager
from django.contrib.auth import get_user_model

class User(AbstractUser):

    USERONLY = 'U'
    BRONZE = 'B'
    SILVER = 'S'
    GOLD = 'G'

    SUBSCRIPTION_STATUS = (
        (USERONLY, 'useronly'),
        (BRONZE, 'bronze'),
        (SILVER, 'silver'),
        (GOLD, 'gold')
    )

    username = None
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=13, unique=True)
    address = models.CharField(max_length=100)
    business_name = models.CharField(max_length=250)
    password = models.CharField(max_length=100,blank=False,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    subscription = models.CharField(max_length=1, choices=SUBSCRIPTION_STATUS, blank=True, null=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'phone_number'

    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.email
    
    





class Event(models.Model):

    class EventType(models.TextChoices):
        SOCIAL_EVENT = 'social', 'Social Event'
        EDUCATIONAL_EVENT = 'educational', 'Educational Event'
        HACKATHON = 'hackathon', 'Hackathon'
        OFFER = 'offer', 'Offer'
        OTHER = 'other', 'Other'



    title = models.CharField(max_length=255)
    description = models.CharField(max_length=400)
    latitude = models.FloatField()
    longitude = models.FloatField()
    # image = models.ImageField(upload_to="images", null=True)
    date = models.DateField(null=True)

    EventType = models.CharField(
        max_length=20,
        choices=EventType.choices,
        default=EventType.OTHER,
    )

    def __str__(self):
        return self.title
    
    # def has_passed(self):
    #     # Check if the event has already passed
    #     return self.event_datetime < timezone.now()

# @receiver(pre_delete, sender=Event)
# def delete_event_if_passed(sender, instance, **kwargs):
#     # Delete the event only if it has already passed
#     if instance.has_passed():
#         instance.delete()