from django.contrib import admin

# Register your models here.
# vim: set fileencoding=utf-8 :
from django.contrib import admin

from . import models


class LinkAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'date_add',
        'date_update',
        'status',
        'facebook',
        'twitter',
        'github',
        'intagram',
        'linkedin',
    )
    list_filter = (
        'date_add',
        'date_update',
        'status',
        'id',
        'date_add',
        'date_update',
        'status',
        'facebook',
        'twitter',
        'github',
        'intagram',
        'linkedin',
    )


class InfoAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'date_add',
        'date_update',
        'status',
        'contact',
        'adrresse',
        'maps',
    )
    list_filter = (
        'date_add',
        'date_update',
        'status',
        'id',
        'date_add',
        'date_update',
        'status',
        'contact',
        'adrresse',
        'maps',
    )


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Link, LinkAdmin)
_register(models.Info, InfoAdmin)
