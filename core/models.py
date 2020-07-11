from django.db import models

# Create your models here.

class Usuario(models.Model):
    rut = models.CharField(max_length=12)
    nombre1 = models.CharField(max_length=20)
    nombre2 =models.CharField(max_length=20)
    apellido_pat = models.CharField(max_length=20)
    apellido_mat = models.CharField(max_length=20)
    fecha_nacimiento = models.DateField()
    correo = models.CharField(max_length=50)
    telefono = models.IntegerField
    direccion = models.CharField(max_length=100)
   

    def __str__(self):
        return self.nombre1

class Paciente(models.Model):
    usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE)
    medic_desc = models.CharField(max_length=150)
    alergia = models.CharField(max_length=50)
    enfermedad = models.CharField(max_length=50)

def __str__(self):
    return self.medic_desc
    

class Insumo(models.Model):
    codigo = models.CharField(max_length=20)
    nombre = models.CharField(max_length=30)
    marca = models.CharField(max_length=20)
    unid_medida = models.CharField(max_length=20)
    fecha_vencimiento = models.DateField()
    cantidad = models.IntegerField()

def __str__(self):
        return self.nombre

class InsumoMedico(models.Model):
    Insumos = models.ForeignKey(Insumo,on_delete=models.CASCADE)
    desc_medica = models.CharField(max_length=50)
    contraIndicacion = models.CharField(max_length=50)

#def __str__(self):
        #return self.desc_medica


class Reserva(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    correo = models.CharField(max_length=30)
    especialidad = models.CharField(max_length=20)
    fecha_atencion = models.DateField()
    hora_atencion = models.CharField(max_length=10)
    odontologo = models.CharField(max_length=20)


def __str__(self):
    return self.nombre

class Reserva1(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    correo = models.CharField(max_length=30)
    especialidad = models.CharField(max_length=20)
    fecha_atencion = models.DateField()
    hora_atencion = models.CharField(max_length=10)
    
def __str__(self):
    return self.nombre


class OrdenCompra(models.Model):
    num_orden = models.IntegerField(max_length=10)
    fecha_emision = models.DateField()
    proveedor = models.CharField(max_length=30)
    insumo = models.ForeignKey(Insumo,on_delete=models.CASCADE)
    cantidad = models.IntegerField(max_length=5)
    precio = models.IntegerField(max_length=8)

def __str__(self):
    return self.num_orden
