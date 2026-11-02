from django.db import models
from django.contrib.auth.models import AbstractUser

class Organization(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

class User(AbstractUser):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, null=True, related_name='members')

class MetricPayload(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='metrics')
    payload_type = models.CharField(max_length=50, db_index=True)
    data = models.JSONField(default=dict)
    processed = models.BooleanField(default=False, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        indexes = [
            models.Index(fields=['organization', 'processed', '-created_at']),
        ]