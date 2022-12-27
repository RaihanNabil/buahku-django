# Generated by Django 3.1.14 on 2022-12-09 14:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('buah', '0004_auto_20221209_2156'),
    ]

    operations = [
        migrations.AddField(
            model_name='shippingaddress',
            name='address',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='shippingaddress',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='shippingaddress',
            name='kodepos',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
