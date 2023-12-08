from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
import inspect

import requests
from django.views import View

from testing.models import UnitTestes, Testes
API_URL = "http://127.0.0.1:8000/api/rooms"


class TestView(View):
    def get(self, request,  id):
        tests = UnitTestes.objects.filter(test_id=id).order_by('id')
        return render(request, 'testing/view.html', {'tests': tests})


class TestRunnerView(LoginRequiredMixin, View):
    def get(self, request, id):
        testes = Testes.objects.get(pk=id)
        return render(request, 'testing/run_test.html', {"testes": testes})

    def post(self, request, id):
        base_url = request.POST.get('base_url')
        results = {}
        counter = 0
        if id == 2:
            try:
                data = {
                    "username": "mirkhojiddin",
                    "first_name": 'kimdir',
                    "last_name": "kimov",
                    "email": "asdlasd@gmail.com",
                    "password": '124578'
                }
                response = requests.post(f"http://127.0.0.1:8000/users/register", json=data)
                print(response)
            except :
                return render(request, 'testing/run_test.html', {"error": "serverga ulanishga xatolik"})
        tests = UnitTestes.objects.filter(test_id=id).order_by('id')
        cookie = ''
        for test in tests:
            test_url = test.url
            if test.param:
                for key, val in test.param.items():
                    test_url = test_url.replace("{" + key + "}", str(val))
            test_name = test.name
            test_method = test.method
            payload = {'username': 'qw12', 'password': 'qw12'}
            session = requests.Session()
            session.post(base_url)

            try:
                if test.name.find("Login") != -1 or test.name.find("login") != -1:
                    response = session.post(f"{base_url}{test_url}", data=test.json)
                    cookie = session.cookies
                if test_method == 'get':
                    response = session.get(f"{base_url}{test_url}", cookies=cookie)
                elif test_method == 'post':
                    response = session.post(f"{base_url}{test_url}", data=test.json, cookies=cookie)

            except ConnectionError as e:
                return render(request, 'testing/run_test.html', {"error": "serverga ulanishga xatolik"})
            if test.status_code > 0:
                if response.status_code != test.status_code:
                    results[counter] = {
                        'test_name': test_name,
                        'url': f"{base_url}{test_url}",
                        "error": f"status code not {test.status_code}"
                    }
                    counter += 1
                    continue
            if test.is_list:
                data = response.json()
                if not isinstance(data, list):
                    results[counter] = {
                        'test_name': test_name,
                        "error": "data is not  a list"
                    }
                    counter += 1
                    continue
            check = False
            if test.key:
                for key in test.key:
                    data = response.json()
                    if key not in data:
                        check = True
                        results[counter] = {
                            'test_name': test_name,
                            "error": f"not exist {key} in data"
                        }
                        counter += 1
                        break
            if check:
                continue
            if test.is_contain:
                check = False
                data = response.text
                for key in test.is_contain.values():
                    if data.find(key) == -1:
                        check = True
                        results[counter] = {
                            'test_name': test_name,
                            'url': f"{base_url}{test_url}",
                            "error": f"not exist {key} text in data"
                        }
                        counter += 1
            if check:
                print(test.name, response.text)
                continue
            results[counter] = {
                'test_name': test_name,
                "message": "Ok"
            }
            counter += 1
        context = {
            'results': results
        }
        return render(request, 'testing/run_test.html', context)


class TestReview(View):
    def get(self, request, test):
        test = UnitTestes.objects.get(name=test)
        return render(request, 'testing/review.html', {'test': test})


class GoodreadsTestSample(View):
    def get(self, request):
        base_url = "http://127.0.0.1:8000"
        url = "/books/list"
        response = requests.get(f"{base_url}{url}")
        response_text = response.text
        payload = {'username':'qw12','password':'qw12'}
        session = requests.Session()
        session.post('http://127.0.0.1:8000/users/login', data=payload)

        response = requests.get('http://127.0.0.1:8000/users/profile_edit', cookies=session.cookies)
        print(response_text.find('Books'))

        print(response.text)
        return render(request, 'testing/run_test.html')


# import requests
#
# with requests.Session() as s:
#     res = s.get('https://httpbin.org/cookies/set/abc/123')
#     print('res: {}'.format(res.text))
#
#     res = s.get('https://httpbin.org/cookies')
#     print('res: {}'.format(res.text))
#     # Outputs
#     # res: {
#     #   "cookies": {
#     #     "abc": "123"
#     #   }
#     # }
#     print(s.cookies)  # <RequestsCookieJar[<Cookie abc=123 for httpbin.org/>]>
#     print('actual cookies: {}'.format(s.cookies.get_dict()))  # actual cookies: {'abc': '123'}
# import requests
# r1 = requests.post('http://www.yourapp.com/login')
# r2 = requests.post('http://www.yourapp.com/somepage',cookies=r1.cookies)

#
# payload = {'username':'qw12','password':'qw12'}
# session = requests.Session()
# session.post('http://127.0.0.1:8000/users/login',headers=headers,data=payload)
#
# response = requests.get('http://127.0.0.1:8000/users/profile_edit', cookies=session.cookies)
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
        # print(results)

        return render(request, 'testing/testing_sample.html', context)

