from behave import *

from test_tdd.test_TDD import *


@given('bot')
def first_step(context):
    context.a = TestBot()


@when('ticket_check return OK')
def test_ticket(context):
    context.a.test_ticket()


@when('day_check return OK')
def test_day(context):
    context.a.test_day()


@when('trip_check return OK')
def test_trip(context):
    context.a.test_trip()


@then('Successfully')
def last_step(context):
    pass
