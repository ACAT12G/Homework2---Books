from models1e import *

libro1 = Libro(101, "Aprende Python", 2026, True, "Guido van Rossum", "123-456", "Educación")
libro2 = Libro(102, "Cien Años de Soledad", 1967, True, "Gabriel Garcia Marquez", "978-030", "Ficción")
libro3 = Libro(103, "El Principito", 1943, True, "Antoine de Saint-Exupery", "978-015", "Infantil")
libro4 = Libro(104, "1984", 1949, True, "George Orwell", "978-045", "Ciencia Ficción")
libro5 = Libro(105, "Don Quijote de la Mancha", 1605, True, "Miguel de Cervantes", "978-842", "Clásico")
libro6 = Libro(106, "Orgullo y Prejuicio", 1813, False, "Jane Austen", "978-014", "Romance")
libro7 = Libro(107, "Matar a un Ruiseñor", 1960, True, "Harper Lee", "978-006", "Drama")
libro8 = Libro(108, "El Hobbit", 1937, True, "J.R.R. Tolkien", "978-054", "Fantasía")
libro9 = Libro(109, "Fahrenheit 451", 1953, False, "Ray Bradbury", "978-145", "Ciencia Ficción")
libro10 = Libro(110, "Crimen y Castigo", 1866, True, "Fiodor Dostoyevski", "978-014", "Novela Psicologica")

CU = Sucursal(1, "CU")
CU2 = Sucursal(2, "CU2")
catalog = Catalogo([CU, CU2])

CU.catalogoLocal.extend([libro1, libro2, libro3, libro4, libro5])
CU2.catalogoLocal.extend([libro6, libro7, libro8, libro9, libro10])

biblio = Bilbliotecario()

print("Bienvenido a la biblioteca! Quien eres?")

while True:
    try:
        rol = int(input("1 = Usuario; 2 = Bibliotecario; 3 = Cerrar el programa: "))
    except ValueError:
        print("Usa solo números.")
        continue

    match rol:
        case 1:
            nombre = str(input("Escriba el nombre de su perfil: "))
            print(f"Bienvenido {nombre}.")
            print("Usted tiene un limite de 3 prestamos.")
            user = Usuario(3, nombre)
            
            while True:
                try:
                    elecuser = int(input("Puedes revisar el catalogo disponible con 1, o pedir un prestamo con 2. 3 para salir: "))
                except ValueError:
                    print("Usa solo números.")
                    continue

                match elecuser:
                    case 1:
                        busqueda = input("Qué estas buscando? ")
                        catalog.buscarEnTodasSucursales(busqueda)
                    case 2:
                        elec = input("Qué libro quiere? ")
                        libro_encontrado = None
                        for sucursal in catalog.sucursales:
                            for material in sucursal.catalogoLocal:
                                if material.titulo.lower() == elec.lower():
                                    libro_encontrado = material
                                    break
                        
                        if libro_encontrado:
                            biblio.gestionarPrestamos(user, libro_encontrado)
                        else:
                            print("Libro no encontrado.")
                    case 3:
                        print("Gracias por usar nuestro servicio.")
                        break
                    case _:
                        print("Opción inválida.")
        
        case 2:
            print("Bienvenid@. Las sucursales actuales son CU y CU2.")
            while True:
                try:
                    empleado = int(input("1 para transferir, 2 para salir: "))
                except ValueError:
                    print("Usa solo números.")
                    continue

                match empleado:
                    case 1:
                        objetivo = input("Qué libro quiere transferir? ")
                        sucursalini = input("De que sucursal se va a tomar este libro, CU o CU2? ")
                        sucursalfinal = input("Y cual sera el destino? ")
                        
                        libro_obj = None
                        suc_origen = None
                        suc_destino = None

                        for suc in catalog.sucursales:
                            if suc.nombre.lower() == sucursalini.lower():
                                suc_origen = suc
                            if suc.nombre.lower() == sucursalfinal.lower():
                                suc_destino = suc

                        if suc_origen:
                            for material in suc_origen.catalogoLocal:
                                if material.titulo.lower() == objetivo.lower():
                                    libro_obj = material
                                    break

                        if libro_obj and suc_origen and suc_destino:
                            biblio.transferirMaterial(libro_obj, suc_origen, suc_destino)
                        else:
                            print("Datos incorrectos.")
                    case 2:
                        print("Gracias por su trabajo.")
                        break
                    case _:
                        print("Opción inválida.")
        case 3:
            print("Adios.")
            break
        case _:
            print("Opción inválida.")


