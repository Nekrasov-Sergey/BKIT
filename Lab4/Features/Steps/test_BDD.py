from behave import *  # импортировать всё из behave

from test_TDD import *  # импортировать всё из test_TDD


@given('Shop_Builder')
def first_step(context):
    context.a = Shop_Test_Builder()


@when('test_magnit_builder return OK')
def test_magnit_builder(context):
    context.a.test_magnit_builder()


@when('test_magnit_cosmetic_builder return OK')
def test_magnit_cosmetic_builder(context):
    context.a.test_magnit_cosmetic_builder()


@then('Successfully')
def last_step(context):
    pass
