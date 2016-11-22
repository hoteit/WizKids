from django.test import TestCase
from quizes.models import QuizAgeGroup, QuizInstance, QuizCategory, ProblemQuestion
from django.contrib.auth.models import User
from quizes.forms import ProblemQuestionForm
from django.core.exceptions import ObjectDoesNotExist
import random
import string
import factory


def random_string(length=10):
    return u''.join(random.choice(string.ascii_letters) for x in range(length))


class QuizCategoryFactory(factory.DjangoModelFactory):
    class Meta:
        model = 'Quizes.QuizCategory'
        django_get_or_create = ('category_name')

    category_name = 'math'

class ProblemQuestionFactory(factory.Factory):
    class Meta:
        model = ProblemQuestion

class UserFactory(factory.DjangoModelFactory):
    class Meta:
        model = 'auth.User'
        django_get_or_create = ('username', 'email', 'password')

    username = 'tarek'
    email = 'tarek@nkey.io'
    password = 'tarek'


class QuizesTestCase(TestCase):

    def setUp(self):
       #user = User.objects.create_user(username='tarek', email='tarek@nkey.io', password='tarek' )
       user = UserFactory()
       #User.objects.create_user(username='tarek', email='tarek@nkey.io', password='tarek' )
       categories = QuizCategory.objects.bulk_create([
           QuizCategory(category='math'),
           QuizCategory(category='science'),
           QuizCategory(category='language')
       ])
       quizAgeGroups = QuizAgeGroup.objects.bulk_create([
           QuizAgeGroup(minAgeLevel=10, maxAgeLevel=12),
           QuizAgeGroup(minAgeLevel=13, maxAgeLevel=14)
       ])

    def create_problem_question(self, category_id, ageGroup_id, question, answerChoice1, answerChoice2, answerChoice3,
                                answerChoice4, correctAnswer, illustration):
        return ProblemQuestion.objects.create(category_id=category_id, ageGroup_id=ageGroup_id, question=question,
                                              answerChoice1=answerChoice1, answerChoice2=answerChoice2,
                                              answerChoice3=answerChoice3, answerChoice4=answerChoice4,
                                              correctAnswer=correctAnswer, illustration=illustration)

    def create_quiz_instance(self, userId, userSession, problemQuestion, userAnswer, userCorrectorNot):
        return QuizInstance.objects.create(userId, userSession, problemQuestion, userAnswer, userCorrectorNot)

    def get_category(self, category):
        try:
            return QuizCategory.objects.get(category = category).pk
        except ObjectDoesNotExist:
            raise Exception('category %s not found. ' % category)
        except:
            raise Exception ("some error has occured when looking up for cateogry %s" % category)

    def get_agegroup(self, min_age):
        try:
            return QuizAgeGroup.objects.get(minAgeLevel=min_age).pk
        except ObjectDoesNotExist:
            raise Exception('minimum age group %s is not found. ' % min_age)
        except :
            raise Exception('some error occured when looking up for age group %s. ' % min_age)

    def test_problem_question_creation_form(self):
        data= {'category': self.get_category('math'), 'ageGroup': self.get_agegroup(10),
                           'question': 'what is 1+1', 'answerChoice1':2, 'answerChoice2':3, 'answerChoice3': 4,
                           'answerChoice4':5, 'correctAnswer': 1, 'illustration': None}
        #test question creation form
        problemQuestionForm = ProblemQuestionForm(data=data)
        self.assertTrue(problemQuestionForm.is_valid())

        print (problemQuestionForm.errors)

    def test_problem_question_creation_object(self):
        problemQuestion = self.create_problem_question(
            category_id=self.get_category('math'), ageGroup_id=self.get_agegroup(10), question='what is 1+1',
            answerChoice1=2, answerChoice2=3, answerChoice3=4, answerChoice4=4, correctAnswer=1, illustration=None)
        self.assertTrue(isinstance(problemQuestion, ProblemQuestion))
