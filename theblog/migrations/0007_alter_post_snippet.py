# Generated by Django 3.2.7 on 2021-10-14 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0006_post_snippet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='snippet',
            field=models.CharField(default='Click The Above Link To Read Blog Post..', max_length=255),
        ),
    ]
