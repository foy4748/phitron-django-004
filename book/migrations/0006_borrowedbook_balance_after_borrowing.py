# Generated by Django 5.1.1 on 2024-10-25 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("book", "0005_category_book_category"),
    ]

    operations = [
        migrations.AddField(
            model_name="borrowedbook",
            name="balance_after_borrowing",
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=12),
        ),
    ]