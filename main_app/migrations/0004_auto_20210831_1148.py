# Generated by Django 3.2.6 on 2021-08-31 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_auto_20210831_1019'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sushi',
            name='type',
        ),
        migrations.AddField(
            model_name='sushi',
            name='sides',
            field=models.ManyToManyField(to='main_app.Side'),
        ),
    ]
