from django.db import models

class Joke(models.Model):
    category = models.CharField(max_length=100)
    type = models.CharField(max_length=10)
    joke = models.TextField(null=True, blank=True)
    setup = models.TextField(null=True, blank=True)
    delivery = models.TextField(null=True, blank=True)
    nsfw = models.BooleanField(default=False)
    political = models.BooleanField(default=False)
    sexist = models.BooleanField(default=False)
    safe = models.BooleanField(default=False)
    lang = models.CharField(max_length=10)

    def __str__(self):
        return self.joke or self.setup
