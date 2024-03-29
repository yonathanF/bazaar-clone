# Generated by Django 2.1 on 2019-02-05 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='', max_length=200)),
                ('last_name', models.CharField(default='', max_length=200)),
                ('rating', models.DecimalField(decimal_places=2, max_digits=3)),
                ('description', models.TextField(default='')),
                ('education', models.CharField(default='', max_length=200)),
                ('zip_code', models.IntegerField()),
            ],
        ),
    ]
