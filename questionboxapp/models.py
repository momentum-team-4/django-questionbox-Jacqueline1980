from django.db import models
from users.models import User

class Question(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField(blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title}"


class Answer(models.Model):
    body = models.TextField(blank=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)


