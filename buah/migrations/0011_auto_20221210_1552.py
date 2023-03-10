# Generated by Django 3.1.14 on 2022-12-10 07:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('buah', '0010_customer_order_orderitem_product_shippingaddress'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='product',
        ),
        migrations.AddField(
            model_name='orderitem',
            name='produk',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='buah.produk'),
        ),
        migrations.AlterField(
            model_name='produk',
            name='harga',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='produk',
            name='nama',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]
