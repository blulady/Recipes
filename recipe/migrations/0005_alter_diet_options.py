# Generated by Django 4.1 on 2022-09-07 02:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("recipe", "0004_recipe_chef_alter_recipe_associated_recipe_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="diet",
            options={"ordering": ["name"]},
        ),
    ]