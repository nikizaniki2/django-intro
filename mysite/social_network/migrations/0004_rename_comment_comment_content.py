# Generated by Django 3.2.3 on 2021-05-26 11:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social_network', '0003_auto_20210526_1440'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='comment',
            new_name='content',
        ),
    ]
