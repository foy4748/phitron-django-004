# Generated by Django 5.1.1 on 2024-10-17 07:01

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Book",
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
                ("book_name", models.CharField(max_length=1024)),
                ("author", models.CharField(max_length=1024)),
                (
                    "book_image",
                    models.ImageField(blank=True, null=True, upload_to="book/uploads/"),
                ),
                ("description", models.TextField(max_length=5120)),
                ("quantity", models.IntegerField()),
                ("price", models.FloatField()),
                ("createdAt", models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name="BorrowedBook",
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
                ("borrowedAt", models.DateTimeField(default=django.utils.timezone.now)),
                (
                    "book",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="borrowed_books",
                        to="book.book",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="borrowed_books",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
