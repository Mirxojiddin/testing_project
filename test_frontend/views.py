from bs4 import BeautifulSoup
import requests
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View

from test_frontend.models import TestingFrontend

from testing.models import Testes


class FrontendTestRunnerView(LoginRequiredMixin, View):
    def get(self, request, id):
        testes = Testes.objects.get(pk=id)
        return render(request, 'test_frontend/run_test.html', {"testes": testes})

    def post(self, request, id):
        base_url = request.POST.get('base_url')
        results = {}
        counter = 0
        tests = TestingFrontend.objects.filter(test_id=id).order_by('id')
        string = ''
        session = requests.Session()
        for test in tests:
            test_url = test.url
            params = {}
            if test.param:
                params = test.param
            test_name = test.name
            test_method = test.method
            try:
                if test_method == 'get':
                    response = session.get(f"{base_url}{test_url}", params=params)
                elif test_method == 'post':
                    response = session.post(f"{base_url}{test_url}", data=test.json, params=params)
            except ConnectionError as e:
                return render(request, 'testing/run_test.html', {"error": "serverga ulanishga xatolik"})
            
            soup = BeautifulSoup(response.text, 'html.parser')
            check = False
            if test.title:
                if test.title not in soup.title.text: 
                    check = True
                    results[counter] = {
                        'test_name': test_name,
                        'url': f"{base_url}{test_url}",
                        "error": f"Sahifa title {test.title} ga teng emas"
                    }
                    counter+=1
            
            if test.is_contain:
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

            if test.paired_tag:    
                for  key, val  in test.paired_tag.items():
                    is_null = True
                    tags = soup.find_all(key)
                    for tag in tags:
                        if val in tag.text:
                            is_null= False  
                    if  is_null:
                        check = True
                        results[counter] = {
                            'test_name': test_name,
                            'url': f"{base_url}{test_url}",
                            "error": f"Sahifada bunday {val} {key} teglari  yo'q"
                        }
                        counter += 1
            if test.single_tag:    
                for  key in test.single_tag.values():
                    is_null = True
                    if len(soup.find_all(key)) == 0:
                        check = True
                        results[counter] = {
                            'test_name': test_name,
                            'url': f"{base_url}{test_url}",
                            "error": f"Sahifada bunday {key} tagi  yo'q"
                        }
                        counter += 1 
            
            if test.id_name:    
                for  key in test.id_name.values():
                    if len(soup.find_all(id=key)) == 0:
                        check = True
                        results[counter] = {
                            'test_name': test_name,
                            'url': f"{base_url}{test_url}",
                            "error": f"Sahifada bunday {key} id yo'q"
                        }
                        counter += 1
            if test.class_name:    
                for key in test.class_name.values():
                    if len(soup.find_all(class_=key)) == 0:
                        check = True
                        results[counter] = {
                            'test_name': test_name,
                            'url': f"{base_url}{test_url}",
                            "error": f"Sahifada bunday {key} class yo'q"
                        }
                        counter += 1
            if check:
                continue
            results[counter] = {
                'test_name': test_name,
                "message": "Ok"
            }
            counter += 1
        context = {
            'results': results
        }
        return render(request, 'test_frontend/run_test.html', context)
# Create your views here.
