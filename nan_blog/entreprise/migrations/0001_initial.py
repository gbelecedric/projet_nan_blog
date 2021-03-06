# Generated by Django 2.2.6 on 2019-10-26 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
                ('contact', models.IntegerField()),
                ('adrresse', models.CharField(max_length=250)),
                ('maps', models.CharField(max_length=200)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
                ('facebook', models.URLField()),
                ('twitter', models.URLField()),
                ('github', models.URLField()),
                ('intagram', models.URLField()),
                ('linkedin', models.URLField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
