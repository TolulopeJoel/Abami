# Generated by Django 5.0 on 2023-12-20 17:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Source",
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
                ("name", models.CharField(max_length=255)),
                ("domain", models.URLField(max_length=255)),
                ("news_page", models.URLField()),
                ("active", models.BooleanField(default=True)),
                ("html_tag", models.CharField(max_length=255)),
                ("html_tag_classes", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="Post",
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
                ("title", models.CharField(max_length=255)),
                ("content", models.TextField()),
                ("image", models.URLField(blank=True)),
                ("published", models.BooleanField(default=False)),
                ("published_date", models.DateTimeField(blank=True, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "news_source",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="posts",
                        to="posts.source",
                    ),
                ),
            ],
            options={
                "ordering": ("created_at",),
                "unique_together": {("news_source", "title")},
            },
        ),
    ]
