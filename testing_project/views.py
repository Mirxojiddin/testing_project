from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View

from testing.models import Testes


class IndexView(View):
	def get(self, request):
		tests = Testes.objects.all()

		return render(request, 'index.html', {'tests': tests})


