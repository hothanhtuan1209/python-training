from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.utils import timezone
from django.db.models import QuerySet
from django.urls import reverse
from django.shortcuts import get_object_or_404, render

from .models import Question, Choice


class IndexView(generic.ListView):
    """
    View for displaying the list of the latest questions.

    Attributes:
        template_name (str): The name of the template to be rendered.
        context_object_name (str): The name of the context variable to store the list of questions.
    """

    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """

        return Question.objects.filter(pub_date__lte=timezone.now()).order_by(
            "-pub_date"
        )[:5]


class DetailView(generic.DetailView):
    """
    View for displaying details of a specific question.

    Attributes:
        model (Model): The model used for the detail view.
        template_name (str): The name of the template to be rendered.
    """

    model = Question
    template_name = "polls/detail.html"

    def get_queryset(self) -> QuerySet[Question]:
        """
        Return the queryset for the detail view.

        Returns:
            QuerySet[Question]: The queryset containing the questions that are published.
        """

        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    """
    View for displaying results of a specific question.

    Attributes:
        model (Model): The model used for the detail view.
        template_name (str): The name of the template to be rendered.
    """

    model = Question
    template_name = "polls/results.html"


def vote(request, question_id):
    """
    View for voting on a specific question.

    Args:
        request (HttpRequest): The HTTP request object.
        question_id (int): The ID of the question to vote on.

    Returns:
        HttpResponse: The HTTP response.
    """

    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))


def get_queryset():
    """
    Return the last five published questions (not including those set to be
    published in the future).
    """

    return Question.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[:5]
