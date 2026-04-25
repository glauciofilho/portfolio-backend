from django.contrib import admin
from .models import Project, Stack, StackProject, File, Profile


class StackProjectInline(admin.TabularInline):
    model = StackProject
    extra = 1


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    inlines = [StackProjectInline]
    list_display = ("id", "name_pt", "created_at")


@admin.register(Stack)
class StackAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "badge_url")


@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    list_display = ("id", "path", "project")



@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("id", "resume_pdf_pt", "resume_pdf_en")