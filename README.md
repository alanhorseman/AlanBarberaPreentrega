# Proyecto Coderhouse

Comision: 54135

Alumno: Alan Barbera

## Acerca del proyecto
    Será una página para que una vendedora pueda administrar sus clientes y productos. Agregar, modificar o eliminar
    un producto o cliente. 

## Aplicaciones
    Hasta ahora cuenta solamente con una aplicación Cliente y otra Producto, para poder visualizar el contenido
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
    Implementar fotos de productos
    Opción de ocultar usuarios o productos
    Poder seleccionar varias productos (como si fuese un carrito de compras) asi mostrar el total, y si es que se 
        puede aplicar algun descuento. (No será un carrito de compras propiamente dicho porque la página no será para un cliente, sino para una vendedora)
    Crear un pedido de compra para mandar al proveedor

## Problemas conocidos
    -No he podido todavia implementar correctamente el ingreso de un email. En ese campo, he tenido que usar 
        un CharField en vez de un EmailField. Me da un error que no he podido solucionar

    -Al momento de MODIFICAR un usuario o producto ya creado, si no se desea modificar y se quiere volver atras, no 
        devuelve a la lista, sino al home de la app. Se donde se encuentra el problema, pero aun no pude solucionarlo
    