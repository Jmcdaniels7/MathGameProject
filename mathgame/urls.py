from django.urls import path
from .views import ModuleMultipleChoiceQuestions

urlpatterns = [
    path('questions/module/<slug:slug>/multiple-choice/', ModuleMultipleChoiceQuestions.as_view(), name='module-multiple-choice-questions'),
]


