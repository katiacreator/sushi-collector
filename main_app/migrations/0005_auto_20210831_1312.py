# Generated by Django 3.2.6 on 2021-08-31 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_auto_20210831_1148'),
    ]

    operations = [
        migrations.AddField(
            model_name='side',
            name='isVegetarian',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='sushi',
            name='isVegan',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='sushi',
            name='isVegetarian',
            field=models.BooleanField(default=False),
        ),
    ]