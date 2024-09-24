# Generated by Django 5.1.1 on 2024-09-23 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("agreements", "0005_remove_agreements_remaining_amount_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="agreements",
            name="agreed_amount",
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name="agreements",
            name="down_payment",
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name="agreements",
            name="total_amount_made",
            field=models.PositiveIntegerField(default=0),
        ),
    ]
