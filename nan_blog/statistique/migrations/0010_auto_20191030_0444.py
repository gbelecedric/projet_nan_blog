# Generated by Django 2.2.6 on 2019-10-30 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('statistique', '0009_visitor_infose'),
    ]

    operations = [
        migrations.CreateModel(
            name='Visitor_Infos_user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_address', models.GenericIPAddressField()),
                ('page_visited', models.TextField()),
                ('event_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Visitor_Infose',
        ),
        migrations.DeleteModel(
            name='Visitor_Infoss',
        ),
    ]
