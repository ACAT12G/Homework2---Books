from datetime import date
import datetime

class Material:
    def __init__(self, idMaterial: int, titulo: str, añoPublicacion: int, disponible: bool):
        self.idmaterial = idMaterial
        self.titulo = titulo
        self.añoPublicacion = añoPublicacion
        self.disponible = disponible

class Libro(Material):
    def __init__(self, idMaterial, titulo, añoPublicacion, disponible, autor: str, isbn: str, genero: str):
        super().__init__(idMaterial, titulo, añoPublicacion, disponible)
        self.autor = autor
        self.isbn = isbn
        self.genero = genero

class Revista(Material):
    def __init__(self, idMaterial, titulo, añoPublicacion, disponible, edicion: int, periodicidad: str):
        super().__init__(idMaterial, titulo, añoPublicacion, disponible)
        self.edicion = edicion
        self.periodicidad = periodicidad

class MaterialDigital(Material):
    def __init__(self, idMaterial, titulo, añoPublicacion, disponible, tipoArchivo: str, urlDescarga: str, tamañoMB: float):
        super().__init__(idMaterial, titulo, añoPublicacion, disponible)
        self.tipoArchivo = tipoArchivo
        self.urlDescarga = urlDescarga
        self.tamañoMB = tamañoMB

class Persona:
    def __init__(self):
        pass

class Usuario(Persona):
    def __init__(self, limitePrestamos: int, nombre: str):
        super().__init__()
        self.limitePrestamos = limitePrestamos
        self.bloqueado = False
        self.nombre = nombre
        self.listaActiva = []

class Bilbliotecario(Persona):
    def __init__(self):
        super().__init__()

    def gestionarPrestamos(self, Usuario, Objeto):
        if Usuario.bloqueado == True:
            print("No hay acceso, perdona por las molestias.")
        else:
            if len(Usuario.listaActiva) >= Usuario.limitePrestamos:
                print("Ya no puedes obtener mas materiales.")
            else:
                if Objeto.disponible == True:
                    Objeto.disponible = False
                    objadquirido = Prestamo(1, datetime.date.today(), datetime.date.today() + datetime.timedelta(days=7), Usuario, Objeto)
                    Usuario.listaActiva.append(objadquirido)
                    print(f"Has obtenido {Objeto.titulo} a nombre de {Usuario.nombre}.")
                else: 
                    print("El material que quieres no esta disponible ahora mismo.")

    def transferirMaterial(self, Objeto, sucursalOG, sucursalFIN):
        if Objeto in sucursalOG.catalogoLocal:
            sucursalOG.catalogoLocal.remove(Objeto)
            sucursalFIN.catalogoLocal.append(Objeto)
            print(f"{Objeto.titulo} ira de {sucursalOG.nombre} a {sucursalFIN.nombre}.")
        else:
            print("Dicho objeto no se logro encontrar.")
        
class Sucursal:
    def __init__(self, idSucursal: int, nombre: str):
        self.idSucursal = idSucursal
        self.nombre = nombre
        self.catalogoLocal = []

class Prestamo:
    def __init__(self, idPrestamo: int, fechaInicio: date, fechaDevolucion: date, usuario: Usuario, material: Material):
        self.fechaInicio = fechaInicio
        self.idPrestamo = idPrestamo
        self.fechaDevolucion = fechaDevolucion
        self.usuario = usuario
        self.material = material

class Penalizacion:
    def __init__(self, monto: float, motivo: str, pagada: bool):
        self.monto = monto
        self.motivo = motivo
        self.pagada = pagada

    def calcularMulta(self, prestamo):
        diasdif = datetime.date.today() - prestamo.fechaDevolucion
        if diasdif.days > 0:
            self.pagada = False
            self.monto = diasdif.days * 10
            print(f"Tienes una multa de {self.monto} pesos.")
        else:
            print("No hay problema alguno.")
    
    def bloquearUsuario(self, Usuario):
        if Usuario.bloqueado == True:
            print("No hay acceso, perdona por las molestias.")
        else:
            if self.pagada == False:
                Usuario.bloqueado = True
                print("El usuario ha sido bloqueado.")
            else:
                print("Hay 0 problemas.")

class Catalogo:
    def __init__(self, sucursales):
        self.sucursales = sucursales

    def buscarPorAutor(self, autor_buscado):
        encontrados = []
        for sucursal in self.sucursales:
            for material in sucursal.catalogoLocal:
                if isinstance(material, Libro) and material.autor == autor_buscado:
                    encontrados.append(material)
        if len(encontrados) > 0:
            print("Se encontro el autor.")
            return encontrados
        else:
            print("No se encontro a nadie.")
            return []

    def buscarEnTodasSucursales(self, titulo_buscado):
        encontrados = []
        for sucursal in self.sucursales:
            for material in sucursal.catalogoLocal:
                if material.titulo == titulo_buscado:
                    encontrados.append(material)
        if len(encontrados) > 0:
            print("Se encontro el material.")
            return encontrados
        else:
            print("Ni idea de lo que estas buscando.")
            return []


