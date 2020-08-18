# Generated by Django 3.0.5 on 2020-07-06 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BlogApp', '0010_auto_20200706_1801'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=50, verbose_name='发布者')),
                ('words', models.CharField(max_length=50, verbose_name='文本')),
                ('pub_time', models.DateTimeField(auto_now=True, null=True, verbose_name='发布时间')),
            ],
        ),
    ]
