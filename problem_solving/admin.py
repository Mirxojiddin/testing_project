from django.contrib import admin

from problem_solving.models import Problem, ProblemInput, Language, ProblemCodeContains

admin.site.register(Problem)
admin.site.register(ProblemInput)
admin.site.register(Language)
admin.site.register(ProblemCodeContains)
