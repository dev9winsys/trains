# Generated by Django 2.2.1 on 2019-08-21 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TrainLine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trainID', models.CharField(max_length=5)),
                ('trainName', models.CharField(max_length=200)),
                ('trainNameEng', models.CharField(max_length=200)),
                ('trainCompany', models.CharField(max_length=200)),
            ],
        ),
    ]
