# Generated by Django 5.1.1 on 2024-09-22 11:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("transactions", "0002_transactions_landdetail_transactions_buyer_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="transactions",
            name="LandDetail",
        ),
    ]
