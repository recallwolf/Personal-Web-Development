from django.contrib import admin
from . import models 

# Register your models here.
class MessageAdmin(admin.ModelAdmin):
	list_display = ('name', 'email', 'comments')

admin.site.register(models.Article)
admin.site.register(models.Message, MessageAdmin)
