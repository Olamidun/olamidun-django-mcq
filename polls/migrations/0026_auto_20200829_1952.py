# Generated by Django 2.2.6 on 2020-08-29 18:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0025_auto_20200829_1624'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Answers',
        ),
        migrations.DeleteModel(
            name='Questions',
        ),
    ]
