# Generated by Django 3.0.7 on 2020-06-09 01:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20200608_1406'),
    ]

    operations = [
        migrations.CreateModel(
            name='Insumo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=20)),
                ('nombre', models.CharField(max_length=30)),
                ('marca', models.CharField(max_length=20)),
                ('unid_medida', models.CharField(max_length=20)),
                ('fecha_vencimiento', models.DateField()),
                ('cantidad', models.IntegerField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='InsumoMedico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc_medica', models.CharField(max_length=50)),
                ('contraIndicacion', models.CharField(max_length=50)),
                ('Insumos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Insumo')),
            ],
        ),
    ]
