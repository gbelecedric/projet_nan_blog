# vim: set fileencoding=utf-8 :
from django.contrib import admin

from . import models


class Visitor_Infos_userAdmin(admin.ModelAdmin):

    list_display = ('id', 'ip_address', 'page_visited', 'event_date')
    list_filter = (
        'event_date',
        'id',
        'ip_address',
        'page_visited',
        'event_date',
    )


class Visitor_InfosAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'ip_address',
        'event_date',
        'pays',
        'ville',
        'continent',
        'longitude',
        'latitude',
        'page_visited',
        'reseau_mobile',
        'status',
    )
    list_filter = (
        'event_date',
        'status',
        'id',
        'ip_address',
        'event_date',
        'pays',
        'ville',
        'continent',
        'longitude',
        'latitude',
        'page_visited',
        'reseau_mobile',
        'status',
    )


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Visitor_Infos_user, Visitor_Infos_userAdmin)
_register(models.Visitor_Infos, Visitor_InfosAdmin)
