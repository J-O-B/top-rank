# Generated by Django 3.1.7 on 2021-04-06 23:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('messenger', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='custommessage',
            old_name='msg_content',
            new_name='body',
        ),
        migrations.RenameField(
            model_name='custommessage',
            old_name='created_at',
            new_name='created',
        ),
    ]
