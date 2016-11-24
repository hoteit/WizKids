from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Button, Submit, Field
from crispy_forms.bootstrap import FormActions
from .models import ProblemQuestion, QuizAgeGroup, QuizCategory, QuizInstance

class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=20, required=True)
    password = forms.CharField(label='Password', widget=forms.PasswordInput(), required=True)

    helper = FormHelper()
    helper.form_class = 'form-signin'
    helper.layout = Layout(
        Field('username', css_class='form-control'),
        Field('password', css_class='form-control'),
        FormActions(
            Submit('login', 'Login', css_class='btn btn-lg btn-primary btn-block')
        )

    )


class QuizCategoryForm(forms.ModelForm):
    category = forms.CharField(label='Category name', max_length=20, required=True)

    helper = FormHelper()
    helper.form_class = 'form-signin'
    helper.layout = Layout(
        Field('category', css_class='form-control'),
        FormActions(
            Submit('save', 'Save', css_class='btn btn-lg btn-primary btn-block')
        )
    )

    class Meta:
        model = QuizCategory
        fields = ['category']


class QuizAgeGroupForm(forms.ModelForm):
    minAgeLevel = forms.IntegerField(label='minimum age group', required=True)
    maxAgeLevel = forms.IntegerField(label='maximum age group', required=True)
    helper = FormHelper()
    helper.layout = Layout(
        Field('minAgeLevel', css_class='form-control'),
        Field('maxAgeLevel', css_class='form-control'),
        FormActions(
            Submit('save', 'Save', css_class='btn btn-lg btn-primary btn-block')
        )
    )

    class Meta:
        model = QuizAgeGroup
        fields = ['minAgeLevel', 'maxAgeLevel']


class ProblemQuestionForm(forms.ModelForm):
    category = forms.ModelChoiceField(label='category', queryset=QuizCategory.objects.all())
    ageGroup = forms.ModelChoiceField(label='age group', queryset=QuizAgeGroup.objects.all())
    question = forms.CharField(label='question', required=True)
    answerChoice1 = forms.CharField(label='answer1', required=True)
    answerChoice2 = forms.CharField(label='answer2', required=True)
    answerChoice3 = forms.CharField(label='answer3', required=True)
    answerChoice4 = forms.CharField(label='answer4', required=True)
    correctAnswer = forms.IntegerField(min_value=1, max_value=4, required=True)
    illustration = forms.ImageField(required=False)
    helper = FormHelper()
    helper.form_class = 'form-horizontal'
    helper.layout = Layout(
        Field('category', css_class='form-control'),
        Field('ageGroup', css_class='form-control'),
        Field('question', css_class='form-control'),
        Field('answerChoice1', css_class='form-control'),
        Field('answerChoice2', css_class='form-control'),
        Field('answerChoice3', css_class='form-control'),
        Field('answerChoice4', css_class='form-control'),
        Field('correctAnswer', css_class='form-control'),
        Field('illustration', css_class='form-control'),
        FormActions(
            Submit('save', 'Save', css_class='btn btn-lg btn-primary btn-block')
        )
    )

    class Meta:
        model = ProblemQuestion
        fields = ['category', 'ageGroup', 'question', 'answerChoice1', 'answerChoice2', 'answerChoice3', 'answerChoice4',
                  'correctAnswer', 'illustration']


class QuizInstanceForm(forms.ModelForm):
    userId = forms.CharField(label='user id', max_length=24 )
    userSession = forms.CharField(label='session id',  max_length=24)
    problemQuestion = forms.ModelChoiceField(ProblemQuestion, required=True)
    userAnswer = forms.IntegerField(min_value=1, max_value=4, required=True)
    userCorrectorNot = forms.BooleanField(required=True)
    helper = FormHelper()
    helper.layout = Layout(
        Field('userId', css_class='form-control'),
        Field('userSession', css_class='form-control'),
        Field('problemQuestion', css_class='form-control'),
        Field('userAnswer', css_class='form-control'),
        Field('userCorrectorNot', css_class='form-control'),
        FormActions(
            Submit('save', 'Save', css_class='btn btn-lg btn-primary btn-block')
        )
    )

    class Meta:
        model = QuizInstance
        fields = ['userId', 'userSession', 'problemQuestion', 'userAnswer', 'userCorrectorNot']

