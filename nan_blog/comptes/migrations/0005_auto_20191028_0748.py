# Generated by Django 2.2.6 on 2019-10-28 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comptes', '0004_auto_20191028_0724'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='imageprofile',
            field=models.ImageField(default='profileimage.png', upload_to='profile'),
        ),
    ]
