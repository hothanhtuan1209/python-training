from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.http import Http404
from django.views import generic

from .models import Question

# Create your views here.

class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by("-pub_date")[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"

class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." %question_id)
