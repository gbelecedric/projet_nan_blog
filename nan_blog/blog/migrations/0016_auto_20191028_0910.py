# Generated by Django 2.2.6 on 2019-10-28 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_auto_20191028_0903'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='nb_like',
            field=models.PositiveIntegerField(default='0', editable=False),
        ),
        migrations.AlterField(
            model_name='article',
            name='nb_com',
            field=models.PositiveIntegerField(default='0', editable=False),
        ),
    ]