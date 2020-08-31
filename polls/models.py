from django.db import models
from django.contrib.auth.models import User

#
# class Answer(models.Model):
#     question = models.ForeignKey('Question', on_delete=models.CASCADE, related_name='questions')
#     option = models.CharField(max_length=100)
#     is_correct = models.BooleanField(default=False)
#
#     def __str__(self):
#         return self.option
#
#
# class Question(models.Model):
#     question = models.CharField(max_length=200)
#     answer = models.CharField(max_length=200)
#
#     def __str__(self):
#         return self.question
#
#
# class UserAnswer(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     answer = models.CharField(max_length=200)
#
#     def __str__(self):
#         return self.answer


class Questions(models.Model):
    question = models.CharField(max_length=200)
    option1 = models.CharField(max_length=200)
    option2 = models.CharField(max_length=200)
    option3 = models.CharField(max_length=200)
    option4 = models.CharField(max_length=200)
    answer = models.CharField(max_length=200)
    # has_answered_questions = models.BooleanField(default=False)
    def __str__(self):
        return self.question


# class UserAnswer(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     question = models.ForeignKey(Questions, on_delete=models.CASCADE)
#     answer = models.CharField(max_length=200)
#
#     def __str__(self):
#         return self.answer

class UserScore(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    score = models.BigIntegerField(default=0)

    def __str__(self):
        return str(self.score)