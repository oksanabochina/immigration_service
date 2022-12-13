from django.contrib import admin
from django.db.models import Count
from django.urls import reverse
from django.utils.html import format_html
from django.utils.http import urlencode
from . import models


@admin.register(models.Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ['name', 'snippet', 'post_count']
    search_fields = ['name__istartswith']

    @admin.display(ordering='post_count')
    def post_count(self, country):
        url = (
                reverse('admin:immigration_forum_post_changelist')
                + '?'
                + urlencode({
            'country__id': str(country.id)
        }))
        return format_html('<a href="{}">{} Posts</a>', url, country.post_count)

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(post_count=Count('post'))


@admin.register(models.UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'first_name', 'last_name']
    search_fields = ['user', 'user__first_name__istartswith', 'user__last_name__istartswith']

    @admin.display(ordering='first_name')
    def first_name(self, userprofile):
        return userprofile.user.first_name

    @admin.display(ordering='last_name')
    def last_name(self, userprofile):
        return userprofile.user.last_name


@admin.register(models.ConsultantProfile)
class ConsultantProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'first_name', 'last_name', 'country', 'post_count']
    search_fields = ['user__username__istartswith', 'user__first_name__istartswith', 'user__last_name__istartswith']
    list_filter = ['country']

    @admin.display(ordering='first_name')
    def first_name(self, consultantprofile):
        return consultantprofile.user.first_name

    @admin.display(ordering='last_name')
    def last_name(self, consultantprofile):
        return consultantprofile.user.last_name

    @admin.display(ordering='post_count')
    def post_count(self, consultantprofile):
        url = (
                reverse('admin:immigration_forum_post_changelist')
                + '?'
                + urlencode({
                'consultantprofile__id': str(consultantprofile.id)
             }))
        return format_html('<a href="{}">{} Posts</a>', url, consultantprofile.post_count)

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(post_count=Count('post'))


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'country', 'date_posted']
    ordering = ['-date_posted']
    search_fields = ['title', 'body']
    list_filter = ['country', 'date_posted']


@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['body', 'post', 'author', 'date_added']
    search_fields = ['body']
    list_filter = ['date_added']