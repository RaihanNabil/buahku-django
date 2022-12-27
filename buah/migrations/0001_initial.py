# Generated by Django 4.1.2 on 2022-10-22 12:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kategori',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Produk',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=100)),
                ('deskripsi', models.TextField()),
                ('jumlah', models.IntegerField()),
                ('harga', models.IntegerField()),
                ('diskon', models.TextField()),
                ('kategori', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='buah.kategori')),
            ],
        ),
    ]