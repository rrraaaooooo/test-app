# Generated by Django 4.2.2 on 2023-07-04 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Vending', '0005_remove_transaction_product_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='price',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
