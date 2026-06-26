import funciones

def menuPrincipal():
    print("\n\t\t\t...::: M E N U   P R I N C I P A L :::... \n")
    opcion = input("\n\t 1.- Agregar \n\t 2.- Borrar \n\t 3.- Modificar \n\t 4.- Mostrar \n\t 5.- Buscar \n\t 6.- Limpiar \n\t 7.- Salir \n \t\tElige una Opcion: ").strip()
    return opcion

def _capturarDatos():
    """Solicita los datos de una pelicula y regresa un diccionario."""
    nombre        = input("Nombre de la pelicula   : ").upper().strip()
    categoria     = input("Categoria (Accion/Drama/etc): ").upper().strip()
    clasificacion = input("Clasificacion (A/B/B15/C): ").upper().strip()
    genero        = input("Genero (Ficcion/Comedia/etc): ").upper().strip()
    idioma        = input("Idioma (Español/Ingles/etc): ").upper().strip()
    return {
        "nombre"       : nombre,
        "categoria"    : categoria,
        "clasificacion": clasificacion,
        "genero"       : genero,
        "idioma"       : idioma,
    }

def _buscarPorNombre(pelis, nombre):
    """Regresa una lista de indices donde coincide el nombre."""
    return [i for i, p in enumerate(pelis) if p["nombre"] == nombre]

def _encabezadoTabla():
    print(f"\n\t{'COD':<6}{'NOMBRE':<30}{'CATEGORIA':<15}{'CLASIF':<10}{'GENERO':<15}{'IDIOMA'}")
    print("\t" + "-" * 85)

def _imprimirFila(codigo, peli):
    print(f"\t{codigo:<6}{peli['nombre']:<30}{peli['categoria']:<15}"
          f"{peli['clasificacion']:<10}{peli['genero']:<15}{peli['idioma']}")



def agregarPeliculas(pelis):
    print("\n\t\t\t...::: AGREGAR PELICULAS :::... \n")
    peli = _capturarDatos()
    pelis.append(peli)
    funciones.accionExitosa()

def mostrarPeliculas(pelis):
    print("\n\t\t\t...::: MOSTRAR PELICULAS :::... \n")
    if pelis:
        _encabezadoTabla()
        for i, peli in enumerate(pelis):
            _imprimirFila(i + 1, peli)
    else:
        print("... ¡No hay peliculas que Mostrar, verifique! ...")
    funciones.esperarTecla()

def buscarPeliculas(pelis):
    print("\n\t\t\t...::: BUSCAR PELICULAS :::... \n")
    nombre = input("Escribe el nombre de la pelicula a buscar: ").upper().strip()
    indices = _buscarPorNombre(pelis, nombre)
    if indices:
        _encabezadoTabla()
        for i in indices:
            _imprimirFila(i + 1, pelis[i])
        funciones.esperarTecla()
    else:
        input("\n\t... ¡No existe la pelicula a buscar, verifique! ...")

def borrarPeliculas(pelis):
    print("\n\t\t\t...::: BORRAR PELICULAS :::... \n")
    nombre = input("Escribe el nombre de la pelicula a borrar: ").upper().strip()
    indices = _buscarPorNombre(pelis, nombre)
    if indices:
        _encabezadoTabla()
        for i in indices:
            _imprimirFila(i + 1, pelis[i])
        opc = input("\n¿Estas seguro que deseas borrar la(s) pelicula(s) encontrada(s) (Si/No)? ").lower().strip()
        while opc not in ("si", "no"):
            opc = input("¿Estas seguro (Si/No)? ").lower().strip()
        if opc == "si":
            # Borrar de atras hacia adelante para no desplazar indices
            for i in sorted(indices, reverse=True):
                pelis.pop(i)
            funciones.accionExitosa()
    else:
        input("\n\t... ¡No existe la pelicula a borrar, verifique! ...")

def modificarPeliculas(pelis):
    print("\n\t\t\t...::: MODIFICAR PELICULAS :::... \n")
    nombre = input("Escribe el nombre de la pelicula a modificar: ").upper().strip()
    indices = _buscarPorNombre(pelis, nombre)
    if indices:
        _encabezadoTabla()
        for i in indices:
            _imprimirFila(i + 1, pelis[i])
        opc = input("\n¿Estas seguro que deseas modificar la pelicula (Si/No)? ").lower().strip()
        while opc not in ("si", "no"):
            opc = input("¿Estas seguro (Si/No)? ").lower().strip()
        if opc == "si":
            print("\nEscribe los nuevos datos:")
            nuevos = _capturarDatos()
            for i in indices:
                pelis[i] = nuevos
            funciones.accionExitosa()
    else:
        input("\n\t... ¡No existe la pelicula a modificar, verifique! ...")

def limpiarPeliculas(pelis):
    print("\n\t\t\t...::: BORRAR TODAS LAS PELICULAS :::... \n")
    opc = input("¿Estas seguro que deseas borrar TODAS las peliculas (Si/No)? ").lower().strip()
    while opc not in ("si", "no"):
        opc = input("¿Estas seguro (Si/No)? ").lower().strip()
    if opc == "si":
        pelis.clear()
        funciones.accionExitosa()
