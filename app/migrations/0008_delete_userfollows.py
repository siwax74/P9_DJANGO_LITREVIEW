# Generated by Django 5.1.3 on 2024-12-27 09:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0007_alter_review_rating"),
    ]

    operations = [
        migrations.DeleteModel(
            name="UserFollows",
        ),
    ]
