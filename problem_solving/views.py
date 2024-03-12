import requests
from django.shortcuts import render
from django.views import View

from problem_solving.models import Problem, ProblemInput


class ProblemView(View):
    def get(self, request):
        problems = Problem.objects.all()
        return render(request, 'testing/problem.html', {'problems': problems})


class ProblemDetailView(View):
    def get(self, request, problem_id):
        problem = Problem.objects.get(id=problem_id)
        return render(request, 'testing/problem-detail.html', {'problem': problem})

    def post(self, request, problem_id):
        code = request.POST.get('comment')
        problem_inputs = ProblemInput.objects.filter(problem_id=problem_id)
        url = "https://online-code-compiler.p.rapidapi.com/v1/"
        headers = {
            "content-type": "application/json",
            "X-RapidAPI-Key": "6b177d26b4msh108832346c8d435p185f17jsnabd819fc5be7",
            "X-RapidAPI-Host": "online-code-compiler.p.rapidapi.com"
        }
        for problem_input in problem_inputs:
            if problem_input.input is not None:
                inputs = problem_input.input.replace("n", '\n')
            else:
                inputs = ''
            payload = {
                "language": "python3",
                "version": "latest",
                "code": code,
                "input": inputs
            }
            response = requests.post(url, json=payload, headers=headers)
            print(response.json()['output'])
            print(problem_input.answer)

            if response.json()['output'].find(problem_input.answer) == -1:
                return render(request, 'testing/problem-detail.html', {"message": "xato"})
        return render(request, 'testing/problem-detail.html', {"message": "to'g'ri"})
