# Generated by Django 3.0.5 on 2020-08-06 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BlogApp', '0020_comment_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='email',
            field=models.CharField(default='3342391860@qq.com', max_length=50, verbose_name='文本'),
        ),
    ]
