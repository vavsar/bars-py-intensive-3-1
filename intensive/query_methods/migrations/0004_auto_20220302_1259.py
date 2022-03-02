# Generated by Django 3.2.12 on 2022-03-02 12:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('query_methods', '0003_auto_20220302_0947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productcost',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_costs', to='query_methods.product', verbose_name='Товар'),
        ),
        migrations.AlterField(
            model_name='productcount',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_counts', to='query_methods.product', verbose_name='Товар'),
        ),
    ]
