# Generated by Django 3.1.1 on 2021-02-18 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Participants',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('inst', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=40)),
                ('contnum', models.CharField(max_length=15)),
            ],
        ),
    ]
