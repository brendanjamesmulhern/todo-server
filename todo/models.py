from django.db import models

class Item(models.Model):
    title = models.TextField()
    description = models.TextField()
    completed = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title