# Generated by Django 2.2.1 on 2019-08-22 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trains', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='trainline',
            name='trainSearch',
            field=models.CharField(max_length=200, null=True),
        ),
    ]