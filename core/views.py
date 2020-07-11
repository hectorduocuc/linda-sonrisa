from django.shortcuts import render, redirect
from .models import Usuario, Paciente, Insumo, Reserva, OrdenCompra
from django.contrib import messages
from django.views.generic import ListView
#from lindasonrisa.core.models import Paciente
from .forms import CustomUserForm
from django.contrib.auth import login as user_login, authenticate
from django.contrib.auth.decorators import login_required, permission_required


# Vistas
#

def inicio(request):
    return render(request, 'core/inicio.html')

def registrar(request):
    data = {
        'form':CustomUserForm()
    }

    if request.method == 'POST':
        formulario = CustomUserForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            #autenticar al usuario y redirigirlo al inicio
            username = formulario.cleaned_data['username']
            password = formulario.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            user_login(request, user)
            return redirect(to='inicio')


    return render(request, 'core/registrar.html', data)

def login(request):
    return render(request, 'core/login.html')     

def contacto(request):
    return render(request, 'core/contacto.html')       

def servicios(request):
    return render(request, 'core/servicios.html') 

@login_required(login_url='/login/')
def reserva(request):
    citas = Reserva.objects.all()
    variables = {'reserva':Reserva}

    if request.POST:
        reserva = Reserva()
        reserva.nombre = request.POST.get('txtnombre')
        reserva.apellido = request.POST.get('txtapellido')
        reserva.correo = request.POST.get('txtcorreo')
        reserva.especialidad = request.POST.get('cbxEspecialidad')
        reserva.fecha_atencion = request.POST.get('fecAtencion')
        reserva.hora_atencion = request.POST.get('cbxHora')
        reserva.odontologo = request.POST.get('cbxmedico')
        try:
            reserva.save()
            variables['mensaje']='Reserva realizada con éxito'
        except:
            variables['mensaje']= 'No se pudo realizar la reserva'



    return render(request, 'core/reserva.html', variables)   

def quienes_somos(request):
    return render(request, 'core/quienes_somos.html')       

# Vistas Administracion
       
@login_required(login_url='/login/')
def sistema_inventario(request):
    return render(request, 'core/sistema_inventario.html') 

def paciente2(request):
    personas = Usuario.objects.all()   
    variables = {'personas':Usuario}

    if request.POST:
        usuario = Usuario()
        usuario.rut = request.POST.get('txtrut')
        usuario.nombre1 = request.POST.get('txtnombre')
        usuario.apellido_pat = request.POST.get('txtapepat')
        usuario.apellido_mat = request.POST.get('txtapemat')
        usuario.fecha_nacimiento = request.POST.get('datenaci')
        usuario.direccion = request.POST.get('txtdireccion')
        usuario.telefono = request.POST.get('txttelefono')
        usuario.correo = request.POST.get('txtmail')

        try:
            usuario.save()
            variables['mensaje']='Guardado Correctamente'
        except:
            variables['mensaje']= 'No se guardó con éxito'

    return render(request, 'core/paciente2.html', variables)  



def proveedor(request):
    personas = Usuario.objects.all()
    data = {'personas':Usuario}
    return render(request, 'core/proveedor.html',{'personas':personas})  

def odontologo(request):
    return render(request, 'core/odontologo.html')

def empleado(request):
    return render(request, 'core/empleado.html')    

def insumo(request):
    insumo = Insumo.objects.all()
    
    variables = {'productos':Insumo}

    if request.POST:
        insumo = Insumo()
        insumo.codigo = request.POST.get('txtidcod')
        insumo.nombre = request.POST.get('txtnombre')
        insumo.marca = request.POST.get('txtmarca')
        insumo.unid_medida = request.POST.get('txtform')
        insumo.fecha_vencimiento = request.POST.get('fecvenc')
        insumo.cantidad = request.POST.get('txtcant')
        try:
            insumo.save()
            variables['mensaje']='Guardado Correctamente'
        except:
            variables['mensaje']= 'Insumo no se pudo Guardar'

        

    return render(request, 'core/insumo.html', variables)      




def compras(request):
    return render(request, 'core/compras.html')

def inventario(request):
    productos = Insumo.objects.all()
    data = {'productos':Insumo}
    return render(request, 'core/inventario.html',{'productos':productos})    


def ordenCompra(request):
    productos = Insumo.objects.all()
    variables = {'productos':Insumo}
    return render(request, 'core/ordenCompras.html', variables)








# Servicios

def diagnostico(request):
    return render(request, 'core/diagnostico.html') 

def perodoncia(request):
    return render(request, 'core/perodoncia.html') 

def implante(request):
    return render(request, 'core/implante.html')   

def prevencion(request):
    return render(request, 'core/prevencion.html')       

def odontopediatria(request):
    return render(request, 'core/odontopediatria.html')     

def ortodoncia(request):
    return render(request, 'core/ortodoncia.html') 

def restauradora(request):
    return render(request, 'core/restauradora.html')    

def estetica(request):
    return render(request, 'core/estetica.html')     

def endodoncia(request):
    return render(request, 'core/endodoncia.html')   

def blanqueamiento(request):
    return render(request, 'core/blanqueamiento.html')     



# Menu inferior

def terminos(request):
    return render(request, 'core/terminos.html')                


#CRUD CLIENTES


#eliminar usuario
def eliminar_usuario(request, correo):
    #buscar el usuario a eliminar
    usuario = Usuario.objects.get(correo=correo)

    try:
        usuario.delete()
        mensaje = "  Usuario Eliminado"
        messages.success(request, mensaje)
    except:
        mensaje = "  No se ha podido elminar el Usuario"
        messages.error(request, mensaje)
    return redirect('proveedor')



#eliminar insumo
def eliminar_insumo(request, codigo):
    #buscar el insumo a eliminar
    insumo = Insumo.objects.get(codigo=codigo)

    try:
        insumo.delete()
        mensaje = "  Insumo Eliminado"
        messages.success(request, mensaje)
    except:
        mensaje = "  No se ha podido elminar el insumo"
        messages.error(request.mensaje)
    return redirect('insumo')

 
 
def pacientelistar(request):
    return render(request, 'core/pacientelistar.html')

#editar Usuario
def EditarUsuario(request, rut):
    personas = Usuario.objects.get(rut=rut)
    variables = {'personas': Usuario}
    
    if request.POST:
        usuario = Usuario()
        usuario.rut = request.POST.get('txtrut')
        usuario.nombre1 = request.POST.get('txtnombre')
        usuario.apellido_pat = request.POST.get('txtapepat')
        usuario.apellido_mat = request.POST.get('txtapemat')
        usuario.fecha_nacimiento = request.POST.get('datenaci')
        usuario.direccion = request.POST.get('txtdireccion')
        usuario.telefono = request.POST.get('txttelefono')
        usuario.correo = request.POST.get('txtmail')

        try:
            usuario.save()
            messages.success(request, 'Modificado Correctamente')
        except:
            messages.error(request, 'No se pudo Modificar')
        return redirect('proveedor')

    return render(request, 'core/EditarUsuario.html', variables)


def listarReserva(request):
    citas = Reserva.objects.all()
    variables = {'reserva':citas}
    return render(request, 'core/listarReserva.html',variables)

def eliminar_reserva(request, id):
    #buscar el insumo a eliminar
    reserva = Reserva.objects.get(id=id)

    try:
        reserva.delete()
        mensaje = " Reserva Eliminada"
        messages.success(request, mensaje)
    except:
        mensaje = "  No se ha podido elminar la Reserva"
        messages.error(request.mensaje)
    return redirect('listarReserva')
