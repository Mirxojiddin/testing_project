import json


from django.shortcuts import render
import requests

import inspect

import requests
from django.views import View

API_URL = "http://127.0.0.1:8000/api/rooms"


def test_get_room_availability_specific_date():
    frame = inspect.currentframe()
    test_name = frame.f_code.co_name
    room_id = 1
    date = "30-06-2023"
    url = f"{API_URL}/{room_id}/availability?date={date}"
    response = requests.get(url)
    result = response.status_code == 200
    if not result:
        return {
            'test_name': test_name,
            "error": "statsu code not 200"
        }
    data = response.json()

    result = isinstance(data, list)
    if not result:
        return {
            'test_name': test_name,
            "error": "Not a list"
        }
    else:

        return {
            'test_name': test_name,
            "status": "Ok"
        }


def test_get_available_rooms_with_search():
    params = {"search": "workly"}
    response = requests.get(API_URL, params=params)
    frame = inspect.currentframe()
    test_name = frame.f_code.co_name
    result = response.status_code == 200
    if not result:
        return {
            'test_name': test_name,
            "error": "statsu code not 200"
        }
    else:
        return {
            'test_name': test_name,
            "status": "Ok"
        }


def test_get_rooms_with_filter():
    params = {"type": "conference"}
    response = requests.get(API_URL, params=params)
    frame = inspect.currentframe()
    test_name = frame.f_code.co_name
    result = response.status_code == 200
    if not result:
        return {
            'test_name': test_name,
            "error": "statsu code not 200"
        }
    else:
        return {
            'test_name': test_name,
            "status": "Ok"
        }


def test_get_room_by_id_existent():
    room_id = 1
    url = f"{API_URL}/{room_id}"
    response = requests.get(url)
    frame = inspect.currentframe()
    test_name = frame.f_code.co_name
    result = response.status_code == 200
    if not result:
        return {
            'test_name': test_name,
            "error": "statsu code not 200"
        }
    else:
        return {
            'test_name': test_name,
            "status": "Ok"
        }


class TestingSampleView(View):
    def get(self, request):
        results = {}
        counter = 0
        results[counter] = test_get_room_availability_specific_date()
        counter += 1
        results[counter] = test_get_room_by_id_existent()
        counter += 1
        results[counter] = test_get_available_rooms_with_search()
        counter += 1
        results[counter] = test_get_rooms_with_filter()
        context = {
            'results': results
        }
        # data = [i for i in results.values()]
        # results = json.dumps(data)
        print(results)

        return render(request, 'testing/testing_sample.html', context)






