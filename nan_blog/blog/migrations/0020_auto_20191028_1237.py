# Generated by Django 2.2.6 on 2019-10-28 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0019_auto_20191028_1228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='date_ago',
            field=models.CharField(editable=False, max_length=250),
        ),
    ]
