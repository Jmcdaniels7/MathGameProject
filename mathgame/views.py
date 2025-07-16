from rest_framework.views import APIView
from rest_framework.response import Response
from .models import MathQuestion
from .serializers import MathQuestionSerializer

# we need to make a math game that teaches addition, subraction, 
# multiplication, division, negative numbers, PEMDAS, and fractions
# this needs to be game like, we need a meter for xp and level.
# each type of math needs to be its own story
# utilize blue, green, white, and yellow for happy and calming colors
# we need to utilize a mobile development framework Swift or Kotlin

class ModuleMultipleChoiceQuestions(APIView):
    def get(self, request, slug):
        questions = MathQuestion.objects.filter(
            module__slug=slug,
            question_types__name='multiple_choice'
        ).distinct().prefetch_related('answer_options')

        serializer = MathQuestionSerializer(questions, many=True)
        return Response(serializer.data)









