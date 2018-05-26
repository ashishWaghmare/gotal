from behave import *

Given a calculator
  When you add number 2 and 3
    Then calculator returns 5

@given('a calculator')
def step_impl(context):
    context.calculator = Calculator()

@when('you add number 2 and 3')
def step_impl(context):

@then('calculator returns 5')
def step_impl(context):

