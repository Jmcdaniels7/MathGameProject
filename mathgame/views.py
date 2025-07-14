from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import MathQuestion
from .serializers import MathQuestionSerializer
import random

# we need to make a math game that teaches addition, subraction, 
# multiplication, division, negative numbers, PEMDAS, and fractions
# this needs to be game like, we need a meter for xp and level.
# each type of math needs to be its own story
# utilize blue, green, white, and yellow for happy and calming colors
# we need to utilize a mobile development framework Swift or Kotlin

@api_view(['GET'])
def get_question_by_module(request, module_name):
    questions = MathQuestion.objects.filter(module=module_name)
    if not questions.exists():
        return Response({'error': 'No questions found for this module'}, status=404)

    question = random.choice(questions)
    request.session['answer'] = question.correct_answer
    request.session['question_id'] = question.id
    serializer = MathQuestionSerializer(question)
    return Response(serializer.data)

@api_view(['POST'])
def submit_answer(request):
    user_answer = float(request.data.get('answer'))
    correct_answer = request.session.get('answer')
    question_id = request.session.get('question_id')

    if correct_answer is None or question_id is None:
        return Response({'error': 'No question in session'}, status=400)

    is_correct = abs(user_answer - correct_answer) < 0.01  # float-safe comparison
    return Response({
        'result': 'correct' if is_correct else 'wrong',
        'correct': correct_answer,
        'question_id': question_id
    })








