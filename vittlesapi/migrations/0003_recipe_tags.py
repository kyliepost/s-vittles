# Generated by Django 3.2.10 on 2021-12-13 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vittlesapi', '0002_alter_family_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='tags',
            field=models.ManyToManyField(related_name='Recipe', through='vittlesapi.recipeTag', to='vittlesapi.Tag'),
        ),
    ]