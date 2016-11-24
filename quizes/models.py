from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

class Themes(models.Model):
    #relies on Bootstrap Bootswatch themes that are located in /tallysheets/static/scripts/bower_components/bootswatch
    #and will be called using UserPreferences table as
    #  <link rel="stylesheet" href="{% static "scripts/bower_components/bootswatch/simplex/bootstrap.min.css" %}">
    theme_name = models.CharField('Theme name', max_length=20)

    def __str__(self):
        return self.theme_name

class UserPreferences(models.Model):
    #table to store user preferences
    user = models.ForeignKey(User)
    theme = models.ForeignKey(Themes, null=True)

    def __str__(self):
        return self.user.username

def is_superuser(user):
    return True


class QuizCategory (models.Model):
    """
    Categories list of the problem quizes. Ex. Math, Science, ...
    """
    category = models.CharField("Category", max_length=50)

    class Meta:
        verbose_name_plural = "Quiz Categories"

    def __str__(self):
        return '%s' % self.category

    def get_absolute_url(self):
        return reverse('problemCategory_view', kwargs={'pk': self.pk})

class QuizAgeGroup (models.Model):
    """
    age group categories for the quizes and problem questions
    """
    minAgeLevel = models.IntegerField('Minimum Age Level')
    maxAgeLevel = models.IntegerField("Maximum Age Level")

    def __str__(self):
        return '%s - %s' % (self.minAgeLevel, self.maxAgeLevel)

    class Meta:
        verbose_name_plural = "Problem Questions Age Groups"

    def get_absolute_url(self):
        return reverse('problemAgeGroup_view', kwargs={'pk': self.pk})

class ProblemQuestion (models.Model):
    """
    a single problem question - with question, multiple choices, and expected answer.
    """
    category = models.ForeignKey(QuizCategory)
    ageGroup = models.ForeignKey(QuizAgeGroup)
    question = models.CharField("Problem Question", max_length=256, default=None)
    answerChoice1 = models.CharField("Answer Choice 1", max_length=100, default=None)
    answerChoice2 = models.CharField("Answer Choice 2", max_length=100, default=None)
    answerChoice3 = models.CharField("Answer Choice 3", max_length=100, default=None)
    answerChoice4 = models.CharField("Answer Choice 4", max_length=100, default=None)
    correctAnswer = models.IntegerField('Correct Answer', default=None)
    illustration = models.ImageField(upload_to="illustrations/", null=True, blank=True)

    class Meta:
        verbose_name_plural = "Problem Questions"

    def __str__(self):
        return '%s - problem question# %i' % (self.category, self.pk)

    def get_absolute_url(self):
        return reverse('problemQuestion_view', kwargs={'pk': self.pk})


class QuizInstance (models.Model):
    """ a single instance of solving a problem """
    userId = models.CharField("User identifier", max_length=24)
    userSession = models.CharField("Unique user session identifier", max_length=24)
    problemQuestion = models.ForeignKey(ProblemQuestion)
    userAnswer = models.IntegerField("User answer")
    userCorrectorNot = models.BooleanField("User got the right answer?")
    quizDate = models.DateTimeField(default=now,  blank=True)

    class Meta:
        verbose_name_plural = "Quiz Instances"

    def __str__(self):
        return 'User %s - Date# %s' % (self.userId, self.quizDate)

