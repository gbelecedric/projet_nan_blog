# Generated by Django 2.2.6 on 2019-10-27 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20191027_2106'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='nb_coment',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='article',
            name='nb_like',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
    ]
