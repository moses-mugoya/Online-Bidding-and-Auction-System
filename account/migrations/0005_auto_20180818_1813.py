# Generated by Django 2.0.6 on 2018-08-18 15:13

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('account', '0004_auto_20180818_1801'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Account',
            new_name='Person',
        ),
    ]