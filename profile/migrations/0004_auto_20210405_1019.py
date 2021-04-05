# Generated by Django 3.1.7 on 2021-04-05 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile', '0003_auto_20210405_1008'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='rank',
            field=models.CharField(blank=True, choices=[(1, 'Member'), (2, 'Recruit'), (3, 'Officer'), (4, 'Sergeant'), (5, 'General')], default='none', max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='earnings',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=40, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='qualification',
            field=models.CharField(blank=True, choices=[('high_school', 'High School'), ('university', 'University'), ('none', 'Prefer Not To Say')], default='none', max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='rating',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=6, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='sales',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]