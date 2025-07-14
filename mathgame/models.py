from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class MathQuestion(models.Model):
    MODULE_CHOICES = [
        ('addition', 'Addition'),
        ('subtraction', 'Subtraction'),
        ('multiplication', 'Multiplication'),
        ('division', 'Division'),
        ('pemdas', 'PEMDAS'),
    ]
    question_text = models.CharField(max_length=100)
    correct_answer = models.IntegerField()
    module = models.CharField(max_length=20, choices=MODULE_CHOICES)

    def __str__(self):
        return f"{self.question_text} [{self.module}]"


