from django.contrib import admin
from .models import Post, Comment, Photography, Award, Certification, Project, Publication, Programing
from django_summernote.admin import SummernoteModelAdmin

class PostAdmin(SummernoteModelAdmin):
    list_display = ('title', 'slug', 'status','created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)

admin.site.register(Post, PostAdmin)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)

@admin.register(Photography)
class PhotographyAdmin(admin.ModelAdmin):
    list_display = ('image_name', 'place', 'author', 'created_on')
    search_fields = ('author', 'place')
    list_filter = ('created_on',)

@admin.register(Award)
class AwardsAdmin(admin.ModelAdmin):
    list_display = ('award_name', 'company', 'year', 'created_on')
    search_fields = ('award_name', 'company', 'year')
    list_filter = ('created_on',)

@admin.register(Certification)
class CertificationsAdmin(admin.ModelAdmin):
    list_display = ('certification_name', 'company', 'year', 'created_on')
    search_fields = ('certification_name', 'company', 'year')
    list_filter = ('created_on',)

@admin.register(Project)
class ProjectsAdmin(admin.ModelAdmin):
    list_display = ('project_name', 'company', 'year', 'created_on')
    search_fields = ('project_name', 'company', 'year')
    list_filter = ('created_on',)

@admin.register(Publication)
class PublicationsAdmin(admin.ModelAdmin):
    list_display = ('publication_name', 'publisher', 'year', 'created_on')
    search_fields = ('publication_name', 'publisher', 'year')
    list_filter = ('created_on',)

@admin.register(Programing)
class ProgramingAdmin(admin.ModelAdmin):
    list_display = ('programing_name', 'level', 'created_on')
    search_fields = ('programing_name', 'level')
    list_filter = ('created_on',)