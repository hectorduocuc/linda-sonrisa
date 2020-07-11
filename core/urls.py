
from django.urls import path
from django.contrib.auth import views as auth_views
from .views import inicio, registrar, login, sistema_inventario, contacto, servicios, perodoncia, diagnostico, implante, prevencion, odontopediatria, ortodoncia, restauradora, estetica, endodoncia, blanqueamiento, paciente2, reserva, quienes_somos, terminos, proveedor, odontologo, empleado, insumo, compras, inventario,eliminar_usuario, eliminar_insumo, pacientelistar, EditarUsuario, listarReserva, eliminar_reserva, OrdenCompra

urlpatterns = [
    path('', inicio, name="inicio"),
    path('registrar/' ,registrar, name="registrar"),
    # path('iniciar_sesion/' ,iniciar_sesion, name="iniciar_sesion"),
    path('login/' ,auth_views.LoginView.as_view(template_name='core/login.html'), name="login"),
    path('logout/' ,auth_views.LogoutView.as_view(template_name='core/login.html'), name="logout"),
    path('sistema_inventario/' ,sistema_inventario, name="sistema_inventario"),
    path('contacto/' ,contacto, name="contacto"),
    path('servicios/' ,servicios, name="servicios"),
    path('perodoncia/' ,perodoncia, name="perodoncia"),
    path('diagnostico/' ,diagnostico, name="diagnostico"),
    path('implante/' ,implante, name="implante"),
    path('prevencion/' ,prevencion, name="prevencion"),
    path('odontopediatria/' ,odontopediatria, name="odontopediatria"),
    path('ortodoncia/' ,ortodoncia, name="ortodoncia"),
    path('restauradora/' ,restauradora, name="restauradora"),
    path('estetica/' ,estetica, name="estetica"),
    path('endodoncia/' ,endodoncia, name="endodoncia"),
    path('blanqueamiento/' ,blanqueamiento, name="blanqueamiento"),
    path('paciente2/' ,paciente2, name="paciente2"),
    path('reserva/' ,reserva, name="reserva"),
    path('quienes_somos/' ,quienes_somos, name="quienes_somos"),
    path('terminos/' ,terminos, name="terminos"),
    path('proveedor/' ,proveedor, name="proveedor"),
    path('odontologo/' ,odontologo, name="odontologo"),
    path('empleado/' ,empleado, name="empleado"),
    path('insumo/' ,insumo, name="insumo"),
    path('compras/' ,compras, name="compras"),
    path('inventario/' ,inventario, name="inventario"),
    path('eliminar_usuario/<correo>/', eliminar_usuario, name="eliminar_usuario"),
    path('eliminar_insumo/<codigo>/', eliminar_insumo, name="eliminar_insumo"),
    path('pacientelistar/',pacientelistar, name="pacientelistar"),
    path('EditarUsuario/<rut>/', EditarUsuario, name="EditarUsuario"),
    path('listarReserva/', listarReserva, name="listarReserva"),
    path('eliminar_reserva/<id>/', eliminar_reserva, name="eliminar_reserva"),
    path('ordenCompra/', OrdenCompra, name="ordenCompra")



]