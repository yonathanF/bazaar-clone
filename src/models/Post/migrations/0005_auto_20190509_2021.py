# Generated by Django 2.1 on 2019-05-09 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0004_auto_20190509_0554'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='recommendation',
        ),
        migrations.AddField(
            model_name='post',
            name='recommendations',
            field=models.ManyToManyField(blank=True, related_name='related_posts', to='Post.Post'),
        ),
    ]
