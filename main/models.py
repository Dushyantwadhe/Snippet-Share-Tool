from django.db import models
import uuid
from uuid import uuid4
from django.conf import settings
from django.contrib.auth.models import User

class TextSnippet(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    text = models.TextField()

class SecretKey(models.Model):
    id= models.UUIDField(primary_key=True, default=uuid4, editable=False)
    text_id = models.ForeignKey(TextSnippet, on_delete=models.CASCADE)
