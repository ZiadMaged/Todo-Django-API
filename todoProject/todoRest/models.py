from django.db import models

class Notes(models.Model):
    title = models.CharField(max_length=200)
    body = models.CharField(max_length=500)

    def __str__(self):
        return self.title
