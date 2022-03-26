from django.db import models
from django.contrib.auth.models import User

# Create your models here.
SINGLE_CHOICE = 'SG'
MULTIPLE_CHOICE = 'MP'

QUESTION_TYPES = [
    (SINGLE_CHOICE, 'Одиночный'),
    (MULTIPLE_CHOICE, 'Множественный')
]


class Questionnaires(models.Model):
    header = models.CharField(max_length=255)
    description = models.TextField()
    type = models.CharField(max_length=2, choices=QUESTION_TYPES, default=SINGLE_CHOICE)
    user = models.ForeignKey(User)

    def __str__(self):
        return self.header


class Questions(models.Model):
    question = models.ForeignKey(Questionnaires)
    text = models.CharField(max_length=255)
    right_answer = models.BooleanField(default=False)


class Surveys(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    questionnaire = models.ForeignKey(Questionnaires)
    user = models.ForeignKey(User)


class Answers(models.Model):
    survey = models.ForeignKey(Surveys)
    question = models.ForeignKey(Questions)
    answer = models.BooleanField(default=False)
