from django.urls import path, include
from .views import QuestionnaireList

urlpatterns = [
    path('list/', QuestionnaireList.as_view(), name='questionnaire_list'),
]