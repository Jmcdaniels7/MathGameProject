from django.urls import path
from .views import get_question_by_module, submit_answer

urlpatterns = [
    path('question/<str:module_name>/', get_question_by_module),
    path('answer/', submit_answer),
]
