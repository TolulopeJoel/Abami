# Generated by Django 5.0 on 2024-01-04 20:36

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("posts", "0016_post_audio"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="summarised",
            field=models.BooleanField(default=False),
        ),
    ]