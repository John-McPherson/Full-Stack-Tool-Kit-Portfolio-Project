# Generated by Django 3.2 on 2022-03-14 11:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Ingredients",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "ingredient_name",
                    models.CharField(max_length=200, unique=True),
                ),
                (
                    "ingredient_type",
                    models.IntegerField(
                        choices=[(0, "Base"), (1, "Modifier")], default=0
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="UserData",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("user_ingredients", models.TextField()),
                ("user_modifers", models.TextField()),
                ("user_drinks", models.TextField()),
                ("user_favs", models.TextField()),
                ("user_dislikes", models.TextField()),
                (
                    "user_name",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="user_name",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Recipes",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("recipe_name", models.CharField(max_length=200, unique=True)),
                (
                    "drink_type",
                    models.IntegerField(
                        choices=[(0, "Up"), (1, "On The Rocks"), (2, "Long")],
                        default=0,
                    ),
                ),
                ("recipe_steps", models.TextField()),
                ("ingredients_list", models.TextField()),
                ("modifiers", models.TextField()),
                ("ingredients", models.TextField()),
                (
                    "approved",
                    models.IntegerField(
                        choices=[(0, "Awaiting Approval"), (1, "Approved")],
                        default=0,
                    ),
                ),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="author",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
