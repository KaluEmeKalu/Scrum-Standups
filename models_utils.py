from django.contrib.humanize.templatetags.humanize import naturaltime
from django.db import models


class TimeStampBaseModel(models.Model):

    timestamp = models.DateTimeField(
        editable=False, auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now=True, blank=True, null=True)

    def time_ago(self):
        return naturaltime(self.timestamp)

    def __str__(self, name=None):
        """
        If model has name set that as name.

        If model has name or name set by subclass
            Then return that name
        Else return "Class_Name object #*number* cretaed on *date*"
        """

        if name:
            return name
        else:
            return "{} object #{} created on {}".format(
                self.__class__.__name__, self.id, self.timestamp
            )

    class Meta:
        abstract = True


class NameTimeStampBaseModel(models.Model):

    name = models.CharField(max_length=80, null=True, blank=True)
    timestamp = models.DateTimeField(
        editable=False, auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now=True, blank=True, null=True)

    def time_ago(self):
        return naturaltime(self.timestamp)

    def __str__(self, name=None):
        """
        If model has name set that as name.

        If model has name or name set by subclass
            Then return that name
        Else return "Class_Name object #*number* cretaed on *date*"
        """
        if self.name:
            name = self.name

        if name:
            return name
        else:
            return "{} object #{} created on {}".format(
                self.__class__.__name__, self.id, self.timestamp
            )

    class Meta:
        abstract = True