from django.db import models


class Problem(models.Model):
	name = models.CharField(max_length=100)
	description = models.CharField(max_length=255)

	def __str__(self):
		return self.name


class Language(models.Model):
	name = models.CharField(max_length=20)
	short_name = models.CharField(max_length=10)
	version = models.CharField(max_length=100)

	def __str__(self):
		return f"{self.name}  {self.version}"


class ProblemCodeContains(models.Model):
	contain = models.CharField(max_length=255)
	language = models.ForeignKey(Language, on_delete=models.CASCADE)
	problem = models.ForeignKey(Problem, on_delete=models.CASCADE)

	def __str__(self):
		return f"{self.problem.name} {self.language.name}"


class ProblemInput(models.Model):
	problem = models.ForeignKey(Problem, on_delete= models.CASCADE)
	input = models.CharField(max_length=100, null=True, blank=True)
	answer = models.CharField(max_length=100)

	def __str__(self):
		return f"{self.problem.name} ning input qismi"