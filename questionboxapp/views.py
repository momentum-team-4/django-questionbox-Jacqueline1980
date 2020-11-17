from django.shortcuts import render
from .models import Question, Answer, User
from .forms import QuestionForm, AnswerForm


def questionbox(request):
    return render (request, 'questionbox/home.html')
    

def question_ask():
    pass

def question_all():
    pass

def question_search():
    pass

def question_user():
    pass

def answer_create():
    pass

def answer_user():
    pass