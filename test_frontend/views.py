import re
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
                    response = session.post(f"{base_url}{test_url}", data=test.data, params=params)
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
                for val in test.is_contain.values():
                    if data.find(val) == -1:
                        check = True
                        results[counter] = {
                            'test_name': test_name,
                            'url': f"{base_url}{test_url}",
                            "error": f"not exist {val} text in data"
                        }
                        counter += 1

            if test.paired_tag:    
                for  key, val  in test.paired_tag.items():
                    is_null = True
                    if key[0]=='h' and len(key)<3:
                        new_string=key
                    else:
                        new_string = ''.join(filter(lambda x: not x.isdigit(), key))
                    if len(soup.find_all(new_string, text= re.compile(val))) == 0:
                        check = True
                        results[counter] = {
                            'test_name': test_name,
                            'url': f"{base_url}{test_url}",
                            "error": f"Sahifada bunday {val} {key} teglari  yo'q"
                        }
                        counter += 1
            if test.single_tag:    
                for  val in test.single_tag.values():
                    is_null = True
                    if len(soup.find_all(val)) == 0:
                        check = True
                        results[counter] = {
                            'test_name': test_name,
                            'url': f"{base_url}{test_url}",
                            "error": f"Sahifada bunday {val} tagi  yo'q"
                        }
                        counter += 1 
            
            if test.id_name:    
                for val in test.id_name.values():
                    if len(soup.find_all(id=val)) == 0:
                        check = True
                        results[counter] = {
                            'test_name': test_name,
                            'url': f"{base_url}{test_url}",
                            "error": f"Sahifada bunday {val} id yo'q"
                        }
                        counter += 1
            if test.attrs:    
                for  key, val in test.attrs.items():
                    new_string = ''.join(filter(lambda x: not x.isdigit(), key))
                    if len(soup.find_all(attrs={new_string:val})) == 0:
                        check = True
                        results[counter] = {
                            'test_name': test_name,
                            'url': f"{base_url}{test_url}",
                            "error": f"Sahifada bunday {val} atrubit yo'q"
                        }
                        counter += 1
            if test.href:    
                for  val in test.href.values():
                    if test_name == "Profile edit get":
                        print(soup.find_all('a'))
                    if len(soup.find_all(href=re.compile(val))) == 0:
                        check = True
                        results[counter] = {
                            'test_name': test_name,
                            'url': f"{base_url}{test_url}",
                            "error": f"Sahifada bunday {val} link yo'q"
                        }
                        counter += 1
            if test.tag_class:    
                for  key, val  in test.tag_class.items():
                    if  len(soup.find_all(key, class_=re.compile(val)))==0:
                        check = True
                        results[counter] = {
                            'test_name': test_name,
                            'url': f"{base_url}{test_url}",
                            "error": f"Sahifada bunday {val} {key} teglari  yo'q"
                        }
                        counter += 1
            if test.class_name:    
                for val in test.class_name.values():
                    if len(soup.find_all(class_=re.compile(val))) == 0:
                        check = True
                        results[counter] = {
                            'test_name': test_name,
                            'url': f"{base_url}{test_url}",
                            "error": f"Sahifada bunday {val} class yo'q"
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

