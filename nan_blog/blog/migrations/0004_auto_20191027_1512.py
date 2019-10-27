# Generated by Django 2.2.6 on 2019-10-27 15:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0003_article_titre_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='nbr_comment',
        ),
        migrations.RemoveField(
            model_name='article',
            name='nbr_like',
        ),
        migrations.AlterField(
            model_name='article',
            name='categorie_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='articles', to='blog.Categorie'),
        ),
        migrations.AlterField(
            model_name='commentaire',
            name='article_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commentaires', to='blog.Article'),
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='blog.Article')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Like',
                'verbose_name_plural': 'Likes',
            },
        ),
    ]
