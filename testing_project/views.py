import time

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View
import requests

from testing.models import Testes


class IndexView(View):
	def get(self, request):
		tests = Testes.objects.all()
		# payload = {'login': 'mirxojiddinotajonov', 'password': '3121123um'}
		# for i in range(41):
		# 	response = requests.post("https://login.emaktab.uz/",payload)
		#
		# 	if response.text.find("Otajonov M.K.")== -1:
		# 		print(response.text)
		# 		print(str(i) + 'tizimga kirdi chiqdi')
		# 		break
		# 	print(str(i))
		# 	time.sleep(2)
		return render(request, 'index.html', {'tests': tests})


class NewView(View):
	def get(self, request):
		tests = Testes.objects.all()
		array = [
			['oyatilloabdulazizov1', 'Namuna1234'],
			['xmraqulov', 'Namuna1234'],
			['botirjon_muqimov', 'Namuna1234'],
			['adhamjonovabbosbek', 'Namuna1234'],
			['azizbek.alijonov1701', 'Namuna1234'],
			['shaxriyor.alijonov05', 'Namuna1234'],
			['avazbekov.shodiyorbe', 'Namuna1234'],
			['bahodirovanaziraxon', 'Namuna1234'],
			['ergashevamuxtasar200', 'Namuna1234'],
			['abdulloh.erkaboyev', 'Namuna1234'],
			['xikmatullogulomjonov', 'Namuna1234'],
			['zulfiyaxon.ismoiljon', 'Namuna1234'],
			['muhammadrizoj2906200', 'Namuna1234'],
			['zulfiyaxonkamolova', 'Namuna1234'],
			['mamirjonova_rayxona', 'Namuna1234'],
			['odiljon.mamirov02200', 'Namuna1234'],
			['malohatmuhammadmusay', 'Namuna1234'],
			['odiljonova.gulzoda', 'Namuna1234'],
			['qobuljonovabdulaziz', 'Namuna1234'],
			['roziyabonu_z', 'Namuna1234'],
			['rshaxobiddinova07200', 'Namuna1234'],

		]
		string = ''
		for i in array:
			payload = {'login': i[0], 'password': i[1]}
			response = requests.post("https://login.emaktab.uz/", payload)
			if response.text.find("https://schools.emaktab.uz/v2/class") == -1:
				string += response.text
			time.sleep(2)
		if string == '':
			return render(request, 'new.html', {'tests': 'ishladi' })
		else:
			return render(request, 'new.html', {'tests': string})


	def post (self, request):

		ress = request.POST.get('comment')
		payload = {'language': 'py', 'code': ress, 'input': ""}
		response = requests.post("https://api.codex.jaagrav.in/", json=payload)
		print(response.json())
		return render(request, 'new.html', {"ress": response.json()['output']})

