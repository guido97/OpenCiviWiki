# Generated by Django 2.2.16 on 2021-05-26 14:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0036_auto_20210526_1834'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='ai_interests',
        ),
        migrations.DeleteModel(
            name='Hashtag',
        ),
    ]