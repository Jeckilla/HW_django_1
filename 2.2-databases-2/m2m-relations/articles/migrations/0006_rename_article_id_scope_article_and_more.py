# Generated by Django 4.2.4 on 2023-09-03 20:53

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("articles", "0005_rename_article_scope_article_id_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="scope",
            old_name="article_id",
            new_name="article",
        ),
        migrations.RenameField(
            model_name="scope",
            old_name="tag_id",
            new_name="tag",
        ),
    ]