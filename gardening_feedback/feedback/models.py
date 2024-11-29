from django.db import models

# Create your models here.
from django.db import models

class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])  # Rating from 1 to 5
    comments = models.TextField()

    def __str__(self):
        return f"Feedback from {self.name}"
