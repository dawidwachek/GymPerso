# Generated by Django 4.2.1 on 2023-08-04 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_remove_order_test_order_test'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='test',
        ),
        migrations.AddField(
            model_name='order',
            name='test',
            field=models.ManyToManyField(blank=True, null=True, to='orders.item'),
        ),
    ]