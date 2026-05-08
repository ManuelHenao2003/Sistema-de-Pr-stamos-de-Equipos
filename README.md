# Sistema-de-Prestamos-de-Equipos
En este proyecto desarrollé un sistema de préstamos de equipos en Python con el objetivo de simular la gestión de inventario dentro de una institución. A través de este trabajo pude aplicar de forma práctica los conceptos de listas, tuplas y diccionarios vistos durante el curso, además de mejorar mi lógica de programación y organización del código.

Para comenzar, utilicé un diccionario principal llamado equipos, donde almacené toda la información de los dispositivos registrados en el sistema. Cada equipo contiene su estado de disponibilidad y una lista de préstamos realizados. Gracias a esto pude organizar la información de manera clara y estructurada.

También implementé listas para guardar el historial de préstamos de cada equipo. Dentro de esas listas utilicé tuplas para registrar cada préstamo con el nombre del usuario y la fecha correspondiente. Elegí usar tuplas porque son inmutables y permiten mantener la integridad de la información registrada.

Desarrollé varias funciones para dividir el programa en módulos más organizados y fáciles de entender. La función mostrar_equipos() me permitió visualizar todos los equipos junto con su estado actual, indicando si estaban disponibles o prestados.

Con la función registrar_prestamo() logré que el sistema validara si un equipo existía y si estaba disponible antes de prestarlo. Luego el programa solicita el nombre del usuario, registra automáticamente la fecha actual y guarda el préstamo en el historial del equipo. Después cambia el estado del equipo a no disponible.

También implementé la función devolver_equipo(), la cual permite devolver un equipo al inventario. Esta función verifica que el equipo exista y que realmente esté prestado antes de cambiar nuevamente su estado a disponible.

Otra función importante fue ver_historial(), donde mostré todos los préstamos registrados de cada equipo, incluyendo el usuario y la fecha del préstamo. Si un equipo no tenía registros, el sistema mostraba un mensaje indicando que no existían préstamos registrados.

Además, desarrollé la función agregar_equipo(), que permite registrar nuevos equipos dentro del sistema verificando que no existan previamente en el inventario.

Finalmente, integré todo el programa mediante una función principal llamada menu(), la cual muestra un menú interactivo para que el usuario pueda navegar entre todas las opciones del sistema de manera sencilla. El programa permanece en ejecución hasta que el usuario selecciona la opción de salir.
