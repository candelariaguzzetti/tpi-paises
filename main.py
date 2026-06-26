import csv

def cargar_paises(archivo):
    paises = []
    try:
        with open(archivo, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for fila in reader:
                paises.append({
                    "nombre": fila["nombre"],
                    "poblacion": int(fila["poblacion"]),
                    "superficie": int(fila["superficie"]),
                    "continente": fila["continente"]
                })
    except Exception as e:
        print("Error al leer el archivo:", e)
    return paises


# -------------------------------
# Funciones principales
# -------------------------------
def agregar_pais(paises):
    nombre = input("Nombre: ").strip()
    poblacion = int(input("Población: "))
    superficie = int(input("Superficie: "))
    continente = input("Continente: ").strip()
    paises.append({"nombre": nombre, "poblacion": poblacion, "superficie": superficie, "continente": continente})
    print("País agregado correctamente.")

def actualizar_pais(paises):
    nombre = input("Ingrese el país a actualizar: ").strip()
    for pais in paises:
        if pais["nombre"].lower() == nombre.lower():
            pais["poblacion"] = int(input("Nueva población: "))
            pais["superficie"] = int(input("Nueva superficie: "))
            print("Datos actualizados.")
            return
    print("País no encontrado.")

def buscar_pais(paises):
    nombre = input("Ingrese nombre a buscar: ").strip().lower()
    resultados = [p for p in paises if nombre in p["nombre"].lower()]
    if resultados:
        for r in resultados:
            print(r)
    else:
        print("No se encontraron coincidencias.")

def filtrar_por_continente(paises):
    cont = input("Ingrese continente: ").strip()
    filtrados = [p for p in paises if p["continente"].lower() == cont.lower()]
    if filtrados:
        for f in filtrados:
            print(f)
    else:
        print("No se encontraron países en ese continente.")

def filtrar_por_poblacion(paises):
    minimo = int(input("Población mínima: "))
    maximo = int(input("Población máxima: "))
    filtrados = [p for p in paises if minimo <= p["poblacion"] <= maximo]
    for f in filtrados:
        print(f)

def filtrar_por_superficie(paises):
    minimo = int(input("Superficie mínima: "))
    maximo = int(input("Superficie máxima: "))
    filtrados = [p for p in paises if minimo <= p["superficie"] <= maximo]
    for f in filtrados:
        print(f)

def ordenar_paises(paises):
    criterio = input("Ordenar por (nombre/poblacion/superficie): ").strip().lower()
    orden = input("Ascendente (asc) o descendente (desc): ").strip().lower()
    reverse = True if orden == "desc" else False
    if criterio in ["nombre", "poblacion", "superficie"]:
        ordenados = sorted(paises, key=lambda p: p[criterio], reverse=reverse)
        for o in ordenados:
            print(o)
    else:
        print("Criterio inválido.")

def estadisticas(paises):
    mayor = max(paises, key=lambda p: p["poblacion"])
    menor = min(paises, key=lambda p: p["poblacion"])
    promedio_poblacion = sum(p["poblacion"] for p in paises) / len(paises)
    promedio_superficie = sum(p["superficie"] for p in paises) / len(paises)
    continentes = {}
    for p in paises:
        continentes[p["continente"]] = continentes.get(p["continente"], 0) + 1

    print("País con mayor población:", mayor["nombre"])
    print("País con menor población:", menor["nombre"])
    print("Promedio de población:", round(promedio_poblacion))
    print("Promedio de superficie:", round(promedio_superficie))
    print("Cantidad de países por continente:", continentes)

# -------------------------------
# Menú principal
# -------------------------------
def menu():
    paises = cargar_paises("paises.csv")
    while True:
        print("\n--- MENÚ ---")
        print("1. Agregar país")
        print("2. Actualizar país")
        print("3. Buscar país")
        print("4. Filtrar por continente")
        print("5. Filtrar por población")
        print("6. Filtrar por superficie")
        print("7. Ordenar países")
        print("8. Estadísticas")
        print("9. Salir")
        opcion = input("Seleccione opción: ")
        if opcion == "1":
            agregar_pais(paises)
        elif opcion == "2":
            actualizar_pais(paises)
        elif opcion == "3":
            buscar_pais(paises)
        elif opcion == "4":
            filtrar_por_continente(paises)
        elif opcion == "5":
            filtrar_por_poblacion(paises)
        elif opcion == "6":
            filtrar_por_superficie(paises)
        elif opcion == "7":
            ordenar_paises(paises)
        elif opcion == "8":
            estadisticas(paises)
        elif opcion == "9":
            break
        else:
            print("Opción inválida.")

menu()
