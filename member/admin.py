from django.contrib import admin
from .models import *

@admin.register(Bio)
class BioAdmin(admin.ModelAdmin):
    list_display = ('user', 'reg_number', 'programme', 'linked_in', 'github')
    search_fields = ('user__username', 'reg_number', 'programme')

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_date', 'end_date', 'is_completed')
    search_fields = ('title', 'description')

@admin.register(ProjectFile)
class ProjectFileAdmin(admin.ModelAdmin):
    list_display = ('project', 'description', 'uploaded_by', 'uploaded_at')
    search_fields = ('project__title', 'description')