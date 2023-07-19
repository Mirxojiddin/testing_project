from django.contrib.auth.models import AbstractUser
from django.db import models


class CostumeUser(AbstractUser):
	course = models.CharField(max_length=50)

	def __str__(self):
		return f"{self.username} {self.last_name}"
