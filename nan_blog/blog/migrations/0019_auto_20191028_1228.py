# Generated by Django 2.2.6 on 2019-10-28 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0018_auto_20191028_1225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='date_ago',
            field=models.CharField(max_length=250),
        ),
    ]