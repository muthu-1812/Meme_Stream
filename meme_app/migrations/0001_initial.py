# Generated by Django 3.1.6 on 2021-02-09 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Meme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meme_author', models.CharField(max_length=200)),
                ('meme_url', models.CharField(max_length=200)),
                ('meme_caption', models.CharField(max_length=200)),
            ],
        ),
    ]
