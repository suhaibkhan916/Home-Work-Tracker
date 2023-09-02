
from django.contrib import admin
from .models import Subject, Task
@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name',)
    # Add any additional configuration options as needed

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'due_date', 'status')
    list_filter = ('status', 'priority', 'subject')
    search_fields = ('title', 'user__username', 'subject__name')
    list_editable = ('status',)
    date_hierarchy = 'due_date'
    # Add any additional configuration options as needed
