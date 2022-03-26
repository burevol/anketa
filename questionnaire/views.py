from django.shortcuts import render
from django.views.generic import ListView
from .models import Questionnaires


# Create your views here.

class QuestionnaireList(ListView):
    model = Questionnaires
    template_name = 'questionnaires/questionnaire_list.html'