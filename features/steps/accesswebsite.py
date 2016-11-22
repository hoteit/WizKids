from behave import *
from django.contrib.auth.models import User

#use_step_matcher("re")
use_step_matcher("parse")


@given(u'a user "{username}" exists')
def createuser(context, username):
    """
    :type context: behave.runner.Context
    """
    User.objects.create_user(username=username, password=username)
    pass


@when('I visit "homepage"')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@then("I should login")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@then("get to the problem questions page")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@then("I should get to the problem questions page")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


