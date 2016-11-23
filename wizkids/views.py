from django.http import HttpResponseRedirect


def index(request):
    return HttpResponseRedirect('/quizes/index')
