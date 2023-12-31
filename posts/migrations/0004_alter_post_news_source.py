# Generated by Django 5.0 on 2023-12-23 21:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("posts", "0003_post_link_to_news"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="news_source",
            field=models.ForeignKey(
                default="",
                on_delete=django.db.models.deletion.CASCADE,
                related_name="posts",
                to="posts.source",
            ),
            preserve_default=False,
        ),
    ]
