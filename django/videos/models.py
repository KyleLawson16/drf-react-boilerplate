from __future__ import unicode_literals

from django.db import models

from django.conf import settings
from django.utils.crypto import get_random_string

# Create your models here.

def random_id():
    unique_id = get_random_string(length=12, allowed_chars='0123456789qwertyuiopasdfghjklzxcvbnm')
    return unique_id


class Video(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        default=1,
        max_length=120
    )
    unique_id = models.CharField(
        editable=True,
        unique=True,
        max_length=120,
        default=random_id
    )
    video_key = models.CharField(
        max_length=120
    )
