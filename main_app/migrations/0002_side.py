# Generated by Django 3.2.6 on 2021-08-31 01:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Side',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=250)),
                ('isVegan', models.BooleanField(default=False)),
                ('price', models.IntegerField(default=0)),
            ],
        ),
    ]
