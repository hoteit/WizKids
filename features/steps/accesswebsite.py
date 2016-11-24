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


@when('I login as "{user} {password}"')
def step_impl(context, user, password):
    """
    :type context: behave.runner.Context
    """
    br = context.browser
    br.get(context.get_url('login'))

    # Checks for Cross-Site Request Forgery protection input
    assert br.find_element_by_name('csrfmiddlewaretoken').is_enabled()

    br.find_element_by_name('username').send_keys(user)
    br.find_element_by_name('password').send_keys(password)
    br.find_element_by_name('login').click()


@then('I should get to the "{page}"')
def step_impl(context, page):
    """
    :type context: behave.runner.Context
    """
    br = context.browser
    assert br.current_url.endswith('/index/')



