# Generated by Django 3.0.7 on 2020-07-07 03:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_reserva_odontologo'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrdenCompra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_orden', models.IntegerField(max_length=10)),
                ('fecha_emision', models.DateField()),
                ('proveedor', models.CharField(max_length=30)),
                ('cantidad', models.IntegerField(max_length=5)),
                ('precio', models.IntegerField(max_length=8)),
                ('insumo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Insumo')),
            ],
        ),
    ]