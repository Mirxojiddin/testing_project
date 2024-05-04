from django.db import models
from testing.models import Testes, Course
POST, GET = "post", 'get'


class TestingFrontend(models.Model):
	METHOD_CHOICE = (
		(POST, POST),
		(GET, GET),
	)
	test = models.ForeignKey(Testes, on_delete=models.CASCADE)
	name = models.CharField(max_length=100)
	description = models.CharField(max_length=1000)
	url = models.CharField(max_length=100)
	method = models.CharField(max_length=20, choices=METHOD_CHOICE)
	param = models.JSONField(null=True, blank=True)
	data = models.JSONField(null=True, blank=True)
	title = models.CharField(max_length=100)
	class_name = models.JSONField(null=True, blank=True)
	id_name = models.JSONField(null=True, blank=True)
	paired_tag = models.JSONField(null=True, blank=True)
	single_tag = models.JSONField(null=True, blank=True)
	is_contain = models.JSONField(null=True, blank=True)
	attrs = models.JSONField(null=True, blank=True)
	href = models.JSONField(null=True, blank=True)
	tag_class = models.JSONField(null=True, blank=True)

	def __str__(self):
		return f"{self.test.name} {self.name}"
