# Generated by Django 3.1.2 on 2020-10-15 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20201011_2212'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='totalAmount',
            field=models.IntegerField(default=0),
        ),
    ]
