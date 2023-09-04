from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from projects.models import Projects

class User(AbstractUser):
    contributor = models.ManyToManyField(Projects)
    can_be_contacted  = models.BooleanField(default=False)
    can_data_be_shared = models.BooleanField(default=False)
    age = models.IntegerField()
    date_joined = models.DateTimeField(default=timezone.now)
    REQUIRED_FIELDS = ["can_be_contacted", "can_data_be_shared", "age"] 
    def save(self, *args, **kwargs):
        if self.age<15:
            self.can_data_be_shared = False
        super().save(*args, **kwargs)
        return self
    