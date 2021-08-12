from django.db import models
from django.utils import timezone


class Hitokoto(models.Model):
    comment = models.CharField(max_length=100)
    name = models.CharField(max_length=20)
    posted_at = models.DateTimeField(timezone.now())
