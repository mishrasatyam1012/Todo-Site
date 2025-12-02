from django.contrib import admin
from .models import Task
# Register your models here.

class TaskAdmin(admin.ModelAdmin):
    list_display = ('isCompleted','task', 'updatedAt',)


admin.site.register(Task, TaskAdmin)