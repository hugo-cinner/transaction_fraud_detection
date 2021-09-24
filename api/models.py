from django.db import models
import uuid
# Create your models here.

class Transaction(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, null=True, blank=True)
    step = models.CharField(max_length=255, null=True, blank=True)
    type = models.CharField(max_length=255, null=True, blank=True)
    amount = models.CharField(max_length=255, null=True, blank=True)
    nameOrig = models.CharField(max_length=255, null=True, blank=True)
    oldbalanceOrig = models.CharField(max_length=255, null=True, blank=True)
    newbalanceOrig = models.CharField(max_length=255, null=True, blank=True)
    nameDest = models.CharField(max_length=255, null=True, blank=True)
    oldbalanceDest = models.CharField(max_length=255, null=True, blank=True)
    newbalanceDest = models.CharField(max_length=255, null=True, blank=True)
    isFraud = models.BooleanField(default=False)
    verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s" % self.name
