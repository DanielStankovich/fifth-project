# Generated by Django 2.2.4 on 2019-11-13 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forumapp', '0008_auto_20191113_1251'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='category',
        ),
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.ManyToManyField(default=True, to='forumapp.Category'),
        ),
    ]
