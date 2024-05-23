# Proyecto Coderhouse

Comision: 54135

Alumno: Alan Barbera

## Acerca del proyecto
    Será una página para que una vendedora pueda administrar sus clientes y productos. Agregar, modificar o eliminar
    un producto o cliente. 

## Aplicaciones
    Cuenta con una aplicación Cliente y otra Producto, para poder visualizar el contenido
    de la página y cumplir con algunas de las funciones básicas del mi proyecto

### Modelos
    El los modelos de la app Cliente tengo 3 clases: 
    Pais
        (una simple clase que pedirá ingresar un país, todavia no esta implementado)
    MetodosPagos
        (la clase pretenderá ser a futuro unas simples opciones para marcar si va a pagar con Crédito, Débito, transferencia o efectivo, tampoco esta implementado aún)
    Usuarios
        (la clase principal, en la que pedirá datos básicos, como nombre, apellido y un email. Tambien incorpora un ForeignKey para las clases País y MetodosPagos)

## Mejoras futuras
    Poder aplicar descuentos tanto a productos en específico, como a metodos de pagos
    Eliminar multiples productos o usuarios simultaneos, y no de a uno
    Opción de ocultar usuarios o productos
    Poder seleccionar varias productos (como si fuese un carrito de compras) asi mostrar el total, y si es que se 
        puede aplicar algun descuento. (No será un carrito de compras propiamente dicho porque la página no será para un cliente, sino para una vendedora)
    Crear un pedido de compra para mandar al proveedor

## Problemas conocidos
    -No he podido todavia implementar correctamente el ingreso de un email. En ese campo, he tenido que usar 
        un CharField en vez de un EmailField. Me da un error que no he podido solucionar

    -Las imagenes solo las he podido cargar desde el panel de Administracion Django, no desde la pagina directamente

## Otros
    La implementación de imagenes no las he hecho a modo de Avatar para un perfil, sino que implementé la función para subir una imagen de los productos

    El user y pass para el login es como se pidió:
        -admin
        -123