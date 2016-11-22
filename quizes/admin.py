from django.contrib import admin
from quizes.models import QuizAgeGroup, QuizCategory, QuizInstance, ProblemQuestion
admin.site.register(QuizAgeGroup)
admin.site.register(QuizCategory)
admin.site.register(ProblemQuestion)
admin.site.register(QuizInstance)

