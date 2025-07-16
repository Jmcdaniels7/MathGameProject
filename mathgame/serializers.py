from rest_framework import serializers
from .models import MathQuestion, AnswerOptions

#serializer used for json configuration for api endpoints
class AnswerOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnswerOptions
        fields = ['id', 'option']

class MathQuestionSerializer(serializers.ModelSerializer):
    answer_options = AnswerOptionSerializer(many=True)

    class Meta:
        model = MathQuestion
        fields = ['id', 'question_text', 'correct_answer', 'answer_options']
