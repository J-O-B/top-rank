# Generated by Django 3.1.7 on 2021-04-03 00:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20210403_0045'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='languages',
            field=models.CharField(choices=[('html', 'HTML'), ('css', 'CSS')], default='html', max_length=20),
        ),
    ]