from itertools import chain
from django.db import models
from django.contrib.auth.models import User
from . models_utils import (
    NameTimeStampBaseModel,
    TimeStampBaseModel,
)
# Create your models here.
class Standup(TimeStampBaseModel):
    yesterday = models.TextField(null=True, blank=True)
    today = models.TextField(null=True, blank=True)
    blocker = models.TextField(null=True, blank=True)
    user = models.ForeignKey(User, null=True, blank=True,
                             related_name='standups')

    def __str__(self):
        return self.today


class Company(NameTimeStampBaseModel):
    staff = models.ManyToManyField(User, blank=True, related_name='companies')
    admins = models.ManyToManyField(User, blank=True)
 
    def get_standups(self):
        """
         Returns a list of Standups
         of all staff sorted by timestamp
        """

        standups_list = []
        for the_user in self.staff.all():
            for standup in the_user.standups.all():
                standups_list.append(standup)

        result_list = sorted(
            standups_list,
            key=lambda instance: instance.timestamp)
        
        return result_list


