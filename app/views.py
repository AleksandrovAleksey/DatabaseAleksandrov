from django.shortcuts import render

from app.models import Question


def index(request):
    questions = Question.objects.all()
    return render(request, 'index.html', context={'questions': questions})
