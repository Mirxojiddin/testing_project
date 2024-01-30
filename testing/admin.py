from django.contrib import admin
from testing.models import Testes, UnitTestes, Course, Problem, ProblemInput

admin.site.register(Course)
admin.site.register(Testes)
admin.site.register(UnitTestes)
admin.site.register(Problem)
admin.site.register(ProblemInput)

# Register your models here.
