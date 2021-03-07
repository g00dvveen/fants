from django.db import models
import uuid

# Create your models here.
class Common(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    value = models.BooleanField()
    description = models.TextField()
