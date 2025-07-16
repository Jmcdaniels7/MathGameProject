from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User

''' 
We need to still add options for sub, multi, div, and pemdas module questions
We also need to add question types
'''
class Module(models.Model):
    title = models.CharField(max_length=50)
    path = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    color = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class MathQuestion(models.Model):
    module = models.ForeignKey(Module, on_delete=models.CASCADE, related_name='questions')
    question_text = models.CharField(max_length=100)
    correct_answer = models.IntegerField()

    def __str__(self):
        return f"{self.question_text} [{self.module.title}]"


class AnswerOptions(models.Model):
    question = models.ForeignKey(MathQuestion, on_delete=models.CASCADE, related_name='answer_options')
    option = models.CharField(max_length=100)

    def __str__(self):
        return f"Option '{self.option}' for Question: {self.question.question_text}"


class QuestionType(models.Model):
    math_question = models.ForeignKey(MathQuestion, on_delete=models.CASCADE, related_name='question_types')
    name = models.CharField(max_length=50)  # e.g., "multiple_choice", "true_false"

    def __str__(self):
        return f"{self.name} for Question: {self.math_question.question_text}"
    

'''
Query for api endpoints:

modules question:
select question_text from mathgame_module as mm join 
mathgame_mathquestion as mmq on mm.id = mmq.module_id where mm.slug = '(this will be the modulename in react native)'

questions answer options:
select option, question_text from mathgame_mathquestion as mmq join 
mathgame_answeroptions as mao on mmq.id = mao.question_id where mao.question_id = 1

multiple choice questions:
select question_text from mathgame_mathquestion as mmq 
join mathgame_questiontype as mqt on mmq.id = mqt.math_question_id 
where mqt.name = 'multiple_choice' 

sql queries for later use:
INSERT INTO mathgame_answeroptions (question_id, option) VALUES
(1, '3'), (1, '4'), (1, '5'), (1, '6'),
(2, '12'), (2, '14'), (2, '15'), (2, '16'),
(3, '13'), (3, '17'), (3, '3'), (3, '-17'),
(4, '5'), (4, '6'), (4, '0'), (4, '-6'),
(5, '164'), (5, '100'), (5, '110'), (5, '105'),
(6, '-5'), (6, '55'), (6, '5'), (6, '-55'),
(7, '1'), (7, '0'), (7, '2'), (7, '-1'),
(8, '-25'), (8, '-7'), (8, '25'), (8, '7'),
(9, '23'), (9, '24'), (9, '25'), (9, '26'),
(10, '21'), (10, '22'), (10, '23'), (10, '24');

INSERT INTO mathgame_module (title, path, slug, color) VALUES
('➕ Module 1: Addition', '/modules/add', 'add', '#FCD5CE'),
('➖ Module 2: Subtraction', '/modules/sub', 'sub', '#D0F4DE'),
('✖️ Module 3: Multiplication', '/modules/multi', 'multi', '#B5EAD7'),
('➗ Module 4: Division', '/modules/div', 'div', '#C7CEEA'),
('🧠 Module 5: PEMDAS', '/modules/pemdas', 'pemdas', '#FFDAC1');

INSERT INTO mathgame_mathquestion (module_id, question_text, correct_answer)
VALUES
(1, '2 + 3?', 5),
(1, '10 + 4?', 14),
(1, '11 + -8?', 3),
(1, '0 + 6?', 6),
(1, '60 + 45?', 105),
(1, '25 + -30?', -5),
(1, '1 + -1?', 0),
(1, '16 + -9?', 7),
(1, '13 + 12?', 25),
(1, '5 + 17?', 22);

INSERT INTO mathgame_mathquestion (module_id, question_text, correct_answer) VALUES
(2, '9 - 5?', 4),
(2, '10 - 14?', -4),
(2, '0 - 7?', -7),
(2, '-3 - 2?', -5),
(2, '20 - 25?', -5),
(2, '15 - 8?', 7),
(2, '30 - 10?', 20),
(2, '5 - 12?', -7),
(2, '-10 - 3?', -13),
(2, '-7 - (-4)?', -3);

INSERT INTO mathgame_mathquestion (module_id, question_text, correct_answer) VALUES
(3, '4 * 2?', 8),
(3, '-3 * 4?', -12),
(3, '-5 * -2?', 10),
(3, '0 * 8?', 0),
(3, '6 * 7?', 42),
(3, '9 * 3?', 27),
(3, '-4 * 3?', -12),
(3, '8 * -1?', -8),
(3, '-6 * -6?', 36),
(3, '11 * 2?', 22);

INSERT INTO mathgame_mathquestion (module_id, question_text, correct_answer) VALUES
(4, '12 / 3?', 4),
(4, '20 / 4?', 5),
(4, '9 / 3?', 3),
(4, '100 / 10?', 10),
(4, '-12 / 3?', -4),
(4, '16 / 4?', 4),
(4, '-20 / -5?', 4),
(4, '0 / 5?', 0),
(4, '18 / 2?', 9),
(4, '30 / 5?', 6);

INSERT INTO mathgame_mathquestion (module_id, question_text, correct_answer) VALUES
(5, '2 + 3 * 4?', 14),
(5, '(2 + 3) * 4?', 20),
(5, '6 + (8 / 4)?', 8),
(5, '10 - 2 * 3?', 4),
(5, '(10 - 2) * 3?', 24),
(5, '8 / (4 - 2)?', 4),
(5, '(2 + 3) * (4 + 1)?', 25),
(5, '18 / (3 + 3)?', 3),
(5, '4 + 5 * 2 - 3?', 11),
(5, '((3 + 2) * 2) + 1?', 11);


'''
