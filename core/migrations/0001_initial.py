# Generated by Django 3.0.7 on 2020-06-08 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rut', models.CharField(max_length=12)),
                ('nombre1', models.CharField(max_length=20)),
                ('nombre2', models.CharField(max_length=20)),
                ('apellido_pat', models.CharField(max_length=20)),
                ('apellido_mat', models.CharField(max_length=20)),
                ('fecha_nacimiento', models.DateField()),
                ('correo', models.CharField(max_length=50)),
                ('telefono', models.IntegerField(max_length=10)),
                ('direccion', models.CharField(max_length=100)),
            ],
        ),
    ]
