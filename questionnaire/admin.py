from django.contrib import admin

from .models import Questionnaires, Questions, Surveys, Answers, UserAnswers
# Register your models here.0

admin.site.register(Questionnaires)
admin.site.register(Questions)
admin.site.register(Surveys)
admin.site.register(Answers)
admin.site.register(UserAnswers)
