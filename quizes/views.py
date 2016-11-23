from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.core import urlresolvers
from django.shortcuts import render_to_response
from django.views import generic
import pytz
from django.core.urlresolvers import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import user_passes_test
from .forms import QuizAgeGroupForm, QuizCategoryForm, QuizInstanceForm, LoginForm, ProblemQuestionForm
from .models import QuizCategory, ProblemQuestion, UserPreferences, QuizAgeGroup, QuizInstance
from django.db.models import Count

def requires_login(view):
    def protected_view(request, *args, **kwargs):
        if not request.user.is_authenticated():
            return HttpResponseRedirect(urlresolvers.reverse('login'))
        return view(request, *args, **kwargs)
    return protected_view


def is_superuser(user):
    #return user.groups.filter(name='Manager').exists()
    return True


def logout_user(request):
    logout(request)
    return HttpResponseRedirect(urlresolvers.reverse('login'))


def notauthorized(request):
    logout(request)
    return HttpResponseRedirect(urlresolvers.reverse('notauthorized'))  # TODO: make sure to have a template


def nodata(request):
    return render_to_response('quizes/nodatafound.html',context=RequestContext(request))


def dataerror(request):
   return render_to_response('quizes/dataerror.html', context=RequestContext(request))


def set_timezone(request):
    #TODO: set the timezone in user profile and create unit test cases

    if request.method == 'POST':
        request.session['django_timezone'] = request.POST['timezone']
        return redirect('/')
    else:
        return render(request, 'quizes/timezone.html', {'timezones': pytz.common_timezones})


def login_user(request):
    auth_message = "Please log in below "
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    auth_message = "You're successfully logged in."
                    return HttpResponseRedirect(urlresolvers.reverse('index'))
                else:
                    auth_message = "Your account is not active. Please contact your administrator."
            else:
                auth_message = "Your username and/or password is incorrect. Please try again."

    else:
        login_form = LoginForm()
    context = {'login_form': login_form, 'auth_message': auth_message}

    return render(request, 'quizes/login.html', context)


@requires_login
def problemsCntReport(request):
    #show the list of customer and number of projects
    problems = ProblemQuestion.objects.annotate(num_problems=Count('problemQuestion'))
    context = {'problems': problems}
    return render(request, 'quizes/index.html', context)


class ProblemCategoryNew(generic.CreateView):
    template_name = 'quizes/problemCategory_new.html'
    form_class = QuizCategoryForm
    model = QuizCategory


class ProblemCategoryEdit(generic.UpdateView):
    model = QuizCategory
    template_name = 'quizes/problemCategory_edit.html'
    form_class = QuizCategoryForm


class ProblemCategoryView(generic.DetailView):
    model = QuizCategory
    template_name = 'quizes/problemCategory_view.html'


class ProblemCategoriesList(generic.ListView):
    context_object_name = 'catgories'
    model = QuizCategory
    template_name = 'quizes/problemCategories_list.html'


class ProblemCategoryDelete(generic.DeleteView):
    model = QuizCategory
    template_name = 'quizes/problemCategory_confirm_delete.html'
    success_url = reverse_lazy('categories_list')

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super(ProblemCategoryDelete, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(ProblemCategoryDelete, self).get_context_data(**kwargs)
        context['is_super_user'] = is_superuser(self.request.user)


class ProblemAgeGroupNew(generic.CreateView):
    template_name = 'quizes/problemAgeGroup_new.html'
    form_class = QuizAgeGroupForm
    model = QuizAgeGroup


class ProblemAgeGroupEdit(generic.UpdateView):
    model = QuizAgeGroup
    template_name = 'quizes/problemAgeGroup_edit.html'
    form_class = QuizAgeGroupForm


class ProblemAgeGroupView(generic.DetailView):
    model = QuizAgeGroup
    template_name = 'quizes/problemAgeGroup_view.html'


class ProblemAgeGroupsList(generic.ListView):
    context_object_name = 'agegroups'
    model = QuizAgeGroup
    template_name = 'quizes/problemAgeGroups_list.html'


class ProblemAgeGroupDelete(generic.DeleteView):
    model = QuizAgeGroup
    template_name = 'quizes/problemAgeGroup_confirm_delete.html'
    success_url = reverse_lazy('agegroups_list')


    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super(ProblemAgeGroupDelete, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(ProblemAgeGroupDelete, self).get_context_data(**kwargs)
        context['is_super_user'] = is_superuser(self.request.user)


class ProblemQuestionNew(generic.CreateView):
    template_name = 'quizes/problemQuestion_new.html'
    form_class = ProblemQuestionForm
    model = ProblemQuestion


class ProblemQuestionEdit(generic.UpdateView):
    model = ProblemQuestion
    template_name = 'quizes/problemQuestion_edit.html'
    form_class = ProblemQuestionForm


class ProblemQuestionView(generic.DetailView):
    model = ProblemQuestion
    template_name = 'quizes/problemQuestion_view.html'


class ProblemQuestionsList(generic.ListView):
    context_object_name = 'questions'
    model = ProblemQuestion
    template_name = 'quizes/problemQuestions_list.html'


class ProblemQuestionDelete(generic.DeleteView):
    model = ProblemQuestion
    template_name = 'quizes/problemQuestion_confirm_delete.html'
    success_url = reverse_lazy('questions_list')

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super(ProblemQuestionDelete, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(ProblemQuestionDelete, self).get_context_data(**kwargs)
        context['is_super_user'] = is_superuser(self.request.user)
