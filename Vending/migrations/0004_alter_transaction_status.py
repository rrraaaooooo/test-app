# Generated by Django 4.2.2 on 2023-06-30 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Vending', '0003_alter_transaction_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='status',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
