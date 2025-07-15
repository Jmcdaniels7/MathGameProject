from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here
'''const modules = [
  { title: '➕ Module 1: Addition', path: '/modules/add', color: '#FCD5CE' },
  { title: '➖ Module 2: Subtraction', path: '/modules/sub', color: '#D0F4DE' },
  { title: '✖️ Module 3: Multiplication', path: '/modules/multi', color: '#B5EAD7' },
  { title: '➗ Module 4: Division', path: '/modules/div', color: '#C7CEEA' },
  { title: '🧠 Module 5: PEMDAS', path: '/modules/pemdas', color: '#FFDAC1' },
] as const;'''

class Module(models.Model):
    title = models.CharField(max_length=50)
    path = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    color = models.CharField(max_length=50)


class MathQuestion(models.Model):
    module = models.ForeignKey(Module, on_delete=models.CASCADE, related_name='questions')
    options = models.JSONField(blank=True, null=True)
    question_text = models.CharField(max_length=100)
    correct_answer = models.IntegerField()

    def __str__(self):
        return f"{self.question_text} [{self.module}]"


class QuestionType(models.Model):
    math_question = models.ForeignKey(MathQuestion, on_delete=models.CASCADE, related_name='question_types')
    name = models.CharField(max_length=50)  # e.g., "multiple_choice", "true_false"

    def __str__(self):
        return f"{self.name} ({self.math_question})"