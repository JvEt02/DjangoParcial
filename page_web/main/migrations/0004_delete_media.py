# Generated by Django 4.1.1 on 2022-09-21 22:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0003_delete_certificate_delete_portfolio_and_more"),
    ]

    operations = [
        migrations.DeleteModel(name="Media",),
    ]
