from django.db import models
from django.contrib.auth.models import User



class Book(models.Model):
	title = models.CharField(max_length=100)
	author = models.CharField(max_length=100)
	publication_date = models.DateField()
	pages = models.IntegerField()
	description = models.TextField(null=True , blank=True)
	price = models.DecimalField(max_digits=10, decimal_places=3)
	image = models.ImageField(null=True)
	rating = models.IntegerField()
	sold_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="books")

	def __str__(self):
		return self.title


