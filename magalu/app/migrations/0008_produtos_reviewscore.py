# Generated by Django 3.1.3 on 2021-01-24 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20210124_0047'),
    ]

    operations = [
        migrations.AddField(
            model_name='produtos',
            name='reviewScore',
            field=models.IntegerField(null=True),
        ),
    ]
