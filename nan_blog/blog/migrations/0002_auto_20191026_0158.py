# Generated by Django 2.2.6 on 2019-10-26 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'verbose_name': 'Article', 'verbose_name_plural': 'Article'},
        ),
        migrations.AlterModelOptions(
            name='categorie',
            options={'verbose_name': 'Categorie', 'verbose_name_plural': 'Categorie'},
        ),
        migrations.AlterModelOptions(
            name='commentaire',
            options={'verbose_name': 'Commentaire', 'verbose_name_plural': 'Commentaire des postes'},
        ),
        migrations.AlterModelOptions(
            name='favoris',
            options={'verbose_name': 'Favoris', 'verbose_name_plural': 'Favoris des utilisateurs'},
        ),
        migrations.AlterModelOptions(
            name='reply',
            options={'verbose_name': 'Reply', 'verbose_name_plural': 'reponse aux commentaires'},
        ),
        migrations.AddField(
            model_name='article',
            name='nbr_like',
            field=models.IntegerField(default='0'),
        ),
    ]
