# Generated by Django 4.2.2 on 2023-07-04 05:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Vending', '0004_alter_transaction_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='product_id',
        ),
        migrations.AddField(
            model_name='transaction',
            name='cost_of_product',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('Transaction_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Vending.transaction')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Vending.product')),
            ],
        ),
    ]
