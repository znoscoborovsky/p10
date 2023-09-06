# Generated by Django 4.2.5 on 2023-09-06 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("projects", "0002_projects_created_time_issues_comments"),
    ]

    operations = [
        migrations.AddField(
            model_name="comments",
            name="title",
            field=models.CharField(
                default="", max_length=30, verbose_name="titre du commentaire"
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="issues",
            name="title",
            field=models.CharField(
                default="", max_length=30, verbose_name="titre de la tache"
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="comments",
            name="description",
            field=models.TextField(
                max_length=2048, verbose_name="description du commentaire"
            ),
        ),
        migrations.AlterField(
            model_name="issues",
            name="description",
            field=models.TextField(
                max_length=2048, verbose_name="description du probleme"
            ),
        ),
        migrations.AlterField(
            model_name="projects",
            name="description",
            field=models.TextField(
                max_length=2048, verbose_name="description du projet"
            ),
        ),
        migrations.AlterField(
            model_name="projects",
            name="title",
            field=models.CharField(max_length=30, verbose_name="titre du projet"),
        ),
        migrations.AlterField(
            model_name="projects",
            name="type",
            field=models.CharField(
                choices=[
                    ("BACK_END", "BACK_END"),
                    ("FRONT_END", "FRONT_END"),
                    ("IOS", "IOS"),
                    ("ANDROID", "ANDROID"),
                ],
                max_length=30,
                verbose_name="Type de projet",
            ),
        ),
    ]
