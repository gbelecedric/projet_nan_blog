from django.contrib import admin

# Register your models here.
# vim: set fileencoding=utf-8 :
from django.contrib import admin

from . import models


class Visiteur_InfosAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'date_add',
        'date_update',
        'status',
        'ip_address',
        'pays',
        'ville',
        'continent',
        'longitude',
        'latitude',
        'page_visited',
        'reseau_mobile',
    )
    list_filter = (
        'date_add',
        'date_update',
        'status',
        'id',
        'date_add',
        'date_update',
        'status',
        'ip_address',
        'pays',
        'ville',
        'continent',
        'longitude',
        'latitude',
        'page_visited',
        'reseau_mobile',
    )


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Visiteur_Infos, Visiteur_InfosAdmin)
