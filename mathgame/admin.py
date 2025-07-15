from django.contrib import admin
from .models import MathQuestion, Module, QuestionType

# Register models here.
admin.site.register(MathQuestion)
admin.site.register(Module)
admin.site.register(QuestionType)


