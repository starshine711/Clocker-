# Generated by Django 3.0.5 on 2020-07-06 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BlogApp', '0016_auto_20200706_2052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='at_article',
            field=models.IntegerField(default=3),
        ),
    ]
