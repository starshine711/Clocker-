# Generated by Django 3.0.5 on 2020-07-06 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BlogApp', '0009_article_like_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='like_user',
            field=models.TextField(blank=True, default=' ', null=True),
        ),
    ]
