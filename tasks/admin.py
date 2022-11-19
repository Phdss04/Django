from django.contrib import admin
from . models import Task
# Register your models here.

class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome', 'descricao', 'feito']
    list_display_links = ['id', 'nome']
    list_editable = ['feito']
    
admin.site.register(Task, TaskAdmin)