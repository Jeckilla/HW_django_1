# Generated by Django 4.2.4 on 2023-09-03 20:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("articles", "0003_alter_article_tags_alter_tag_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="scope",
            name="article",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="scopes",
                to="articles.article",
            ),
        ),
        migrations.AlterField(
            model_name="scope",
            name="tags",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="scopes",
                to="articles.tag",
            ),
        ),
    ]
