# Generated by Django 2.2.6 on 2019-10-28 12:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0021_auto_20191028_1241'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='date_ago',
        ),
    ]
