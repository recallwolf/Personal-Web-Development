from django.db import models

# Create your models here.

class Article(models.Model):  
	tip1 = models.TextField(null=True)  
	tip2 = models.TextField(null=True)


class Message(models.Model):
	name = models.TextField(max_length=30)
	email = models.TextField(max_length=100)
	comments = models.TextField(null=True)
