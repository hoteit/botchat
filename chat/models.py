from django.db import models

class Post(models.Model):
    author = models.CharField(max_length=30)
    name = models.CharField(max_length=100)
    issue_or_change = models.CharField(max_length=400)
    full_note = models.CharField(max_length=400)
    cid=models.CharField(max_length=25)
    processed_note = models.CharField(max_length=400)
    date_field = models.CharField(max_length=30)

    def publish(self):
        self.save()

    def __str__(self):
        return self.name