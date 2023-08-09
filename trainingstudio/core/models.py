from django.db import models

class HighLevel(models.Model):
    h_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=False)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    #objectives - list

class MediumLevel(models.Model):
    m_id = models.CharField(max_length=255, blank=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=False)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    #objectives - list

class LowLevel(models.Model):
    l_id = models.CharField(max_length=255, blank=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=False)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    #objectives - list
