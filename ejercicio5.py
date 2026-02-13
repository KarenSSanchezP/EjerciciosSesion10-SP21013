import os

class Usuario: # Clase que representa a un usuario
    def __init__(self, nombre, apellido, email, cuenta, saldo, contrasena):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__email = email
        self.__cuenta = cuenta
        self.__saldo = float(saldo) 
        self.__contrasena = contrasena  

    @property
    def nombre_completo(self):
        return self.__nombre + " " + self.__apellido
    
    @property
    def email(self): return self.__email
    @property
    def cuenta(self): return self.__cuenta
    @property
    def saldo(self): return self.__saldo
    @property
    def contrasena(self): return self.__contrasena
    
    def validar_login(self, pass_input):
        return self.__contrasena == pass_input

    def abonar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
            return True
        return False

    def retirar(self, cantidad):
        if 0 < cantidad <= self.__saldo:
            self.__saldo -= cantidad
            return True
        return False

    def to_csv_line(self):
        return f"{self.__nombre},{self.__apellido},{self.__email},{self.__cuenta},{self.__saldo},{self.__contrasena}\n"

    def __str__(self):
        return f"Cliente: {self.nombre_completo} | Cuenta: {self.__cuenta} | Saldo: ${self.__saldo}"

class Banco: # Clase que sirve para manejar el archivo de usuarios
    archivo = "usuarios_db.csv" # Nombre del archivo
    usuarios = [] # Lista de usuarios

    @classmethod
    def cargar_datos(cls): # Carga los datos del archivo a la lista de usuarios
        cls.usuarios = [] # Limpiar lista
        if os.path.exists(cls.archivo): # Comprobar si existe el archivo
            with open(cls.archivo, "r") as file:
                next(file, None) # Saltar la cabecera si existe
                for linea in file: # Recorrer cada linea del archivo
                    datos = linea.strip().split(",") # Separar por comas
                    if len(datos) == 6: # Comprobar si tiene 6 datos
                        # Reconstruimos el objeto Usuario desde el texto
                        usuario = Usuario(datos[0], datos[1], datos[2], datos[3], datos[4], datos[5])
                        cls.usuarios.append(usuario)

    @classmethod
    def guardar_datos(cls): # Guarda los datos del archivo desde la lista de usuarios
        with open(cls.archivo, "w") as file:
            file.write("Nombre,Apellido,Email,Cuenta,Saldo,Password\n") # Cabecera
            for usuario in cls.usuarios:
                file.write(usuario.to_csv_line())

    @classmethod
    def registrar_usuario(cls): # Método para registrar un usuario
        print("\n--- REGISTRO ---")
        nombre = input("Nombre: ")
        apellido = input("Apellido: ")
        email = input("Email: ")
        cuenta = input("No. Cuenta: ")
        contrasena = input("Contraseña: ")
        # Creamos usuario nuevo con saldo 0
        nuevo = Usuario(nombre, apellido, email, cuenta, 0, contrasena)
        cls.usuarios.append(nuevo)
        cls.guardar_datos()
        print("¡Usuario registrado con éxito!")

    @classmethod
    def login(cls): # Método para iniciar sesión
        cuenta = input("Ingrese No. Cuenta: ")
        contrasena = input("Ingrese Contraseña: ")
        for usuario in cls.usuarios: # Recorrer la lista de usuarios
            # Comprobar si la cuenta y contraseña coinciden
            if usuario.cuenta == cuenta and usuario.validar_login(contrasena):
                return usuario
        return None

def main():
    # Cargamos la "Base de datos" al iniciar el programa
    Banco.cargar_datos()
    
    while True: # Menú principal del programa 
        print("\n1. Iniciar Sesión\n2. Registrarse\n3. Salir")
        opcion = input("Opción: ") # Opción seleccionada por el usuario

        if opcion == "1":
            usuario_logueado = Banco.login() # Inicia sesión
            if usuario_logueado: # Comprobar si se ha iniciado sesión
                print(f"\nBienvenido {usuario_logueado.nombre_completo}")
                while True: # Menú de sesión del usuario
                    print(f"\nSaldo Actual: ${usuario_logueado.saldo}")
                    print("a. Abonar\nb. Retirar\nc. Cerrar Sesión") # Menú de opciones
                    sub_opcion = input("Opción: ") # Opción seleccionada por el usuario
                    
                    if sub_opcion == "a": # Si se selecciona "Abonar"
                        monto = float(input("Cantidad a depositar: ")) # Pedimos la cantidad a depositar
                        usuario_logueado.abonar(monto) # La aplicamos al usuario
                        Banco.guardar_datos() # Guardamos cambios inmediatamente
                        print("Abono realizado.")
                    
                    elif sub_opcion == "b": # Si se selecciona "Retirar"
                        monto = float(input("Cantidad a retirar: ")) # Pedimos la cantidad a retirar
                        if usuario_logueado.retirar(monto): # La aplicamos al usuario
                            Banco.guardar_datos() # Guardamos cambios inmediatamente
                            print("Retiro realizado.")
                        else:
                            print("Saldo insuficiente. Intente con una cantidad menor.")
                    
                    elif sub_opcion == "c": # Si se selecciona "Cerrar Sesión"
                        break # Salimos del ciclo de sesión
            else: # Si no se ha iniciado sesión correctamente
                print("Credenciales incorrectas. Intente de nuevo.") 

        elif opcion == "2": # Si se selecciona "Registrarse"
            Banco.registrar_usuario() # Llamamos al método para registrar un usuario

        elif opcion == "3": # Si se selecciona "Salir"
            print("Gracias por visitarnos. Hasta pronto.")
            break # Salimos del programa

main()