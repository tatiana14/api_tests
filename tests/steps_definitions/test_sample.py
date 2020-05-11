import pytest
from pytest_bdd import scenario, given, when, then, parsers
import requests
import logging

from helper.data_generator import random_string

LOGGER = logging.getLogger(__name__)

@scenario('../features/get.feature', 'Get by designation test')
def test_get_feature():
    pass

@scenario('../features/get.feature', 'Wrong parameter test')
def test_wrong_param_error():
    pass

@pytest.fixture(scope='function')
def context():
    context = {'payload': {}}
    return context


@given("designation is equal to <des>")
def add_des_param_to_payload(des, context):
    context['payload']['des'] = des


@then(parsers.parse('the response status code is "{code:d}"'))
def step_impl(context, code):
    LOGGER.info(f"Response with status code {context['resp'].status_code} received.")
    assert context['resp'].status_code == code


@when("get Asteroids API query with parameters is executed")
def get_response(host, context):
    resp = requests.get(host, context['payload'])
    LOGGER.info(f"Get method was called with url {resp.url}")
    context['resp'] = resp


@given("date-min is equal to <date_min>")
def add_date_min_param_to_payload(date_min, context):
    context['payload']['date-min'] = date_min


@given("date-max is equal to <date_max>")
def add_date_max_param_to_payload(date_max, context):
    context['payload']['date-max'] = date_max


@given("approach distance is less or equal to <dist_max>")
def add_dist_max_param_to_payload(dist_max, context):
    context['payload']['dist-max'] = dist_max


@then("response contains only <des> objects")
def step_impl(des, context):
    response_body = context['resp'].json()
    for d in response_body["data"]:
        assert d[0] == des


@then("response contains only data where approach distance is lower than <dist_max>")
def step_impl(dist_max, context):
    response_body = context['resp'].json()
    for d in response_body["data"]:
        assert d[6] <= dist_max


@given("wrong parameter is provided")
def add_wrong_param_to_payload(context):
    param = random_string(5)
    context['payload'][param] = random_string(2)

