import pytest
from pytest_bdd import scenario, given, when, then, parsers
import requests
import logging
from dateutil import parser

from helper.data_generator import random_string
from helper.data_parser import parse_to_list

LOGGER = logging.getLogger(__name__)


@scenario('../features/get.feature', 'Get by designation test')
def test_get_feature():
    pass


@scenario('../features/get.feature', 'Wrong parameter test')
def test_wrong_param_error():
    pass


@scenario('../features/get.feature', 'Get by designation empty result test')
def test_empty_result():
    pass


@pytest.fixture(scope='function')
def context():
    context = {'payload': {}}
    return context


# Given steps
@given("designation is equal to <des>")
def add_des_param_to_payload(des, context):
    context['payload']['des'] = des


@given("date-min is equal to <date_min>")
def add_date_min_param_to_payload(date_min, context):
    context['payload']['date-min'] = date_min


@given("date-max is equal to <date_max>")
def add_date_max_param_to_payload(date_max, context):
    context['payload']['date-max'] = date_max


@given("approach distance is less or equal to <dist_max>")
def add_dist_max_param_to_payload(dist_max, context):
    context['payload']['dist-max'] = dist_max


@given("wrong parameter is provided")
def add_wrong_param_to_payload(context):
    param = random_string(5)
    context['payload'][param] = random_string(2)


# When steps
@when("get Asteroids API query with parameters is executed")
def get_response(host, context):
    resp = requests.get(host, context['payload'])
    LOGGER.info(f"Get method was called with url {resp.url}")
    context['resp'] = resp
    context['parsed_data'] = parse_to_list(resp.json())


# Then steps
@then(parsers.parse('the response status code is "{code:d}"'))
def verify_status_code(context, code):
    LOGGER.info(f"Response with status code {context['resp'].status_code} received.")
    assert context['resp'].status_code == code


@then("response contains only <des> objects")
def verify_des_param(des, context):
    LOGGER.info(f"Verifying des field")
    assert context['parsed_data']
    for d in context['parsed_data']:
        assert d.des == des


@then("response contains only data where approach distance is lower than <dist_max>")
def verify_dist_max_param(dist_max, context):
    LOGGER.info(f"Verifying dist_max field")
    assert context['parsed_data']
    for d in context['parsed_data']:
        assert d.dist_max <= dist_max


@then("all returned data have date between <date_min> and <date_max>")
def verify_date_in_range(date_min, date_max, context):
    LOGGER.info(f"Verifying date field")
    assert context['parsed_data']
    for d in context['parsed_data']:
        date = parser.parse(d.cd)
        assert date <= parser.parse(date_max)
        assert date >= parser.parse(date_min)


@then(parsers.parse('count of returned objects is "{comparison_op}" "{count:d}"'))
def verify_count_is_greater_than(comparison_op, count, context):
    LOGGER.info(f"Verifying count of returned objects is {comparison_op} {count}")
    switcher = {'greater than': lambda x, y:  x > y,
                'equals to': lambda x, y:  x == y,
                'less than': lambda x, y: x < y,
                }
    condition_func = switcher[comparison_op](len(context['parsed_data']), count)
    assert condition_func == True


