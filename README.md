Trabajo Práctico Integrador (TPI) - Programación 1
Gestión de Datos de Países en Python

¡ACLARACIÓN!
En el trabajo se había anotado un desconocido conmigo y hablamos brevemente de hacer el trabajo juntos, pero cuando llegó la hora de empezar a desarrollarlo me dijo que había dejado la carrera así que lo terminé haciendo sola.


📌 Objetivo
Este proyecto implementa una aplicación en Python 3.14 para gestionar información sobre países.
Permite realizar búsquedas, filtros, ordenamientos y estadísticas a partir de un dataset en formato CSV.



⚙️ Funcionalidades principales
- Agregar un país con todos sus datos.

\- Actualizar población y superficie de un país existente.

\- Buscar países por nombre (coincidencia parcial o exacta).

\- Filtrar países por:

Continente

Rango de población

Rango de superficie

Ordenar países por:

Nombre

Población

Superficie (ascendente o descendente)

\- Mostrar estadísticas:

País con mayor y menor población

Promedio de población

Promedio de superficie

Cantidad de países por continente



📂 Estructura del repositorio
Código
├── main.py          # Código fuente principal
├── paises.csv       # Dataset base de países
├── README.md        # Documentación del proyecto
└── docs/            # Informe PDF 



▶️ Ejecución

Clonar el repositorio:

git clone https://github.com/candelariaguzzetti/tpi-paises.git
cd tpi-paises

Ejecutar el programa:

python main.py



📊 Ejemplo de uso

Menú principal:

\--- MENÚ ---

1. Agregar país
2. Actualizar país
3. Buscar país
4. Filtrar por continente
5. Filtrar por población
6. Filtrar por superficie
7. Ordenar países
8. Estadísticas
9. Salir
Ejemplo de búsqueda:

Seleccione opción: 3
Ingrese nombre a buscar: Argentina
{'nombre': 'Argentina', 'poblacion': 45376763, 'superficie': 2780400, 'continente': 'América'}



👥 Integrantes
Candelaria Guzzetti



📹 Video demostración
(https://youtu.be/LxkYfl5G5j4)



📑 Documentación
El informe académico y técnico se encuentra en la carpeta docs/ o en el siguiente enlace:
(https://docs.google.com/document/d/13JT1l-7b2luBkhlV-z0G58ceg3TqyiF6VAlC6-_fClI/edit?usp=sharing)

