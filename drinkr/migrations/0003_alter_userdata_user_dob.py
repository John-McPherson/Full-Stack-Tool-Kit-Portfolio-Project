# Generated by Django 3.2 on 2022-03-14 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drinkr', '0002_auto_20220314_1155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdata',
            name='user_dob',
            field=models.DateTimeField(),
        ),
    ]
