# Generated by Django 3.0.3 on 2020-03-17 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BlogApp', '0006_auto_20200317_2140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='number',
            field=models.IntegerField(default=0),
        ),
    ]
