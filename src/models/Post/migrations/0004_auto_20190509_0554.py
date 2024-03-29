# Generated by Django 2.1 on 2019-05-09 05:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0003_auto_20190403_0632'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='recommendation',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='recommendations', to='Post.Post'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('Lifestyle', 'Live a better life'), ('IT', 'Help with IT problems'), ('Events', 'Help with events'), ('Tutoring', 'Learn something new'), ('Art', 'Get creative'), ('Household', 'Improve your home'), ('Labor', 'Get a hand'), ('Other', 'Anything else')], max_length=30),
        ),
        migrations.AlterField(
            model_name='post',
            name='request_type',
            field=models.CharField(choices=[('Offering', 'Offering service'), ('Requesting', 'Asking for service')], max_length=30),
        ),
    ]
