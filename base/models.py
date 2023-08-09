from django.db import models
from django.contrib.auth.models import User


class Note(models.Model):
    # link to poster, cascade deletion
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, null=True)
    description = models.TextField(max_length=200, null=True, blank=True)

    updated = models.DateField(auto_now=True)
    created = models.DateField(auto_now_add=True)

    # specify metadata
    class Meta:
        ordering = ["-updated", "-created"]

    # reference
    def __str__(self):
        return self.title
