# Generated by Django 5.0.2 on 2024-03-02 13:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("movie", "0002_alter_movie_director"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="actor",
            options={
                "ordering": ["first_name"],
                "verbose_name": "Actor",
                "verbose_name_plural": "Actors",
            },
        ),
        migrations.AlterModelOptions(
            name="director",
            options={
                "ordering": ["first_name"],
                "verbose_name": "Director",
                "verbose_name_plural": "Directors",
            },
        ),
        migrations.AlterModelOptions(
            name="movie",
            options={
                "ordering": ["title"],
                "verbose_name": "Movie",
                "verbose_name_plural": "Movies",
            },
        ),
        migrations.AlterModelTable(
            name="actor",
            table="actors",
        ),
        migrations.AlterModelTable(
            name="director",
            table="directors",
        ),
        migrations.AlterModelTable(
            name="movie",
            table="movies",
        ),
    ]