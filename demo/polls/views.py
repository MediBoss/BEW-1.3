from django.shortcuts import render
from django.http import HttpResponse
from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)


# View(controller) to handle the page that shows detail of a question
def detail(request, question_id):
    return HttpResponse("You're Looking at question %s." % question_id)
# View(controller) to handle the page that shows results of of a question
def results(request, question_id):

    response = "You're looking at the results of question %s."
    return HttpResponse(response, question_id)

# View(controller) to handle the page that shows the vote of a question
def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)


