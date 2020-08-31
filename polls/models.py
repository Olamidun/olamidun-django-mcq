from django.db import models
from django.contrib.auth.models import User


class Quiz(models.Model):
    story = models.TextField()


class Questions(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    question = models.CharField(max_length=200)
    option1 = models.CharField(max_length=200)
    option2 = models.CharField(max_length=200)
    option3 = models.CharField(max_length=200)
    option4 = models.CharField(max_length=200)
    answer = models.CharField(max_length=200)
    # has_answered_questions = models.BooleanField(default=False)

    def __str__(self):
        return self.question


class QuizTaker(models.Model):
    # quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, null=True, blank=True)
    quiz_taker = models.OneToOneField(User, on_delete=models.CASCADE)
    score = models.BigIntegerField(default=0)

    def __str__(self):
        return str(self.score)