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
    header = models.CharField(max_length=255, verbose_name='Header')
    description = models.TextField(verbose_name='Description')
    type = models.CharField(max_length=2, choices=QUESTION_TYPES, default=SINGLE_CHOICE,
                            verbose_name='Type')
    user = models.ForeignKey(User, verbose_name='User', on_delete=models.CASCADE)

    def __str__(self):
        return self.header


class Questions(models.Model):
    questionnaire = models.ForeignKey(Questionnaires, verbose_name='Questionnaire', on_delete=models.CASCADE)
    text = models.CharField(max_length=255, verbose_name='Question')
    right_answer = models.BooleanField(default=False, verbose_name='Right answer')

    def __str__(self):
        return self.text


class Surveys(models.Model):
    date = models.DateTimeField(auto_now_add=True, verbose_name='Surveys date')
    questionnaire = models.ForeignKey(Questionnaires, verbose_name='Questionnaire', on_delete=models.CASCADE)
    user = models.ForeignKey(User, verbose_name='User', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} {self.date}'


class Answers(models.Model):
    survey = models.ForeignKey(Surveys, verbose_name='Survey', on_delete=models.CASCADE)
    question = models.ForeignKey(Questions, verbose_name='Question', on_delete=models.CASCADE)
    answer = models.BooleanField(default=False, verbose_name='Answer')

    def __str__(self):
        return f'{self.survey.user.username} {self.survey.date} {self.question}'
