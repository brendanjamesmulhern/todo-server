from django.db import models
from django.contrib.auth.models import User

class Item(models.Model):
    title = models.TextField()
    description = models.TextField()
    completed = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, default=1)

    def __str__(self):
        return self.title