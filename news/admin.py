from django.contrib import admin

from . import models


@admin.register(models.News)
class NewsAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Comment)
class AuthorAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Status)
class StatusAdmin(admin.ModelAdmin):
    pass


@admin.register(models.NewsStatus)
class NewsStatusAdmin(admin.ModelAdmin):
    pass


@admin.register(models.CommentStatus)
class CommentStatus(admin.ModelAdmin):
    pass

