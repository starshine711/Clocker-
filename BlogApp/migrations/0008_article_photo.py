# Generated by Django 3.0.5 on 2020-05-17 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BlogApp', '0007_auto_20200317_2143'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='photo',
            field=models.TextField(blank=True, default='none', null=True),
        ),
    ]
