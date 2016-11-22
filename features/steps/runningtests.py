from behave import given, when, then

@given (u'"Quizes/tests.py" exists')
def step_exists(context):
    pass

@when (u'I run "python manage.py test Quizes"')
def run_command(context):
    pass

@then (u'I should see that all tests are successful')
def is_running(context):
    pass

