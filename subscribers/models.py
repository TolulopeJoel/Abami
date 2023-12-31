from django.db import models


class Subscriber(models.Model):
    email = models.EmailField(max_length=225, unique=True)
    verified = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
