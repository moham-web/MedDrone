from django.db import models
from django.contrib.auth.models import User  # Import User model
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class UserData(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    MANAGER = 'MGR'
    EMPLOYEE = 'EMP'
    
    ROLE_CHOICES = [
        (MANAGER, 'Manager'),
        (EMPLOYEE, 'Employee'),
    ]
    
    name = models.CharField(max_length=100, default="default")
    role = models.CharField(
        max_length=3,
        choices=ROLE_CHOICES,
        default=EMPLOYEE,
    )

        
    SECTION_CHOICES = [
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
    ]

    section = models.CharField(
        max_length=1,
        choices=SECTION_CHOICES,
        default='',  # Default value if not set
        blank=True
    )



    def __str__(self):
            return f"{self.user.username}'s Profile"
    


def create_user_data(sender,instance, created, **kwargs):
        if created:
            UserData.objects.create(user=instance)
            print('Created ')

post_save.connect(create_user_data, sender=User)