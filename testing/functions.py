import requests


def replace_param(text, string):
	array = text.replace(' ', '').split('=')
	return string.replace("{" + array[0] + "}", array[1])


def get_absulute_url(test):
	test_url = test.url
	test_param1 = test.param1
	test_param2 = test.param2
	test_param3 = test.param3
	test_param4 = test.param4
	if test_param1:
		test_url = replace_param(test_param1, test_url)
	if test_param2:
		test_url = replace_param(test_param2, test_url)
	if test_param3:
		test_url = replace_param(test_param3, test_url)
	if test_param4:
		test_url = replace_param(test_param4, test_url)
	return test_url

