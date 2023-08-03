from django.db import models
import datetime
from django.utils import timezone

class Question(models.Model):
    """
    Represents a question in the poll app.

    Attributes:
        question_text (str): The text of the question.
        pub_date (datetime): The date and time when the question was published.
    """

    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        """
        Returns a string representation of the Question object.
        """
        
        return self.question_text

    def was_published_recently(self):
        """
        Returns True if the Question was published within the last 1 day;
        otherwise, returns False.
        """
        
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

class Choice(models.Model):
    """
    Represents a choice for a question in the poll app.

    Attributes:
        question (Question): The question to which this choice belongs.
        choice_text (str): The text of the choice.
        votes (int): The number of votes received for this choice.
    """

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        """
        Returns a string representation of the Choice object.
        """
        
        return self.choice_text
