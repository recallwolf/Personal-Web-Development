from django.db import models

# Create your models here.
class Article(models.Model):  
	tip1 = models.TextField(null=True)  
	tip2 = models.TextField(null=True)