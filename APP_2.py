#Importar Librerias
import sqlite3

#Creación de base de datos
conn = sqlite3.connect("Registros.db")
cursor = conn.cursor()

#Crear tabla en base de datos
cursor.execute("""
    CREATE TABLE IF NOT EXISTS cuentas2 (
    correo TEXT PRIMARY KEY,
    primer_nombre TEXT,
    segundo_nombre TEXT,
    primer_apellido TEXT,
    segundo_apellido TEXT,
    telefono INTEGER,
    contraseña TEXT
)
""")
conn.commit()
conn.close()

#Declarar variables
nombre1 = ""
nombre2 = ""
apellido1 =""
apellido2 =""
correo = ""
telefono = ""
contraseña1 = ""
contraseña2 = ""
regis = "registrarme"
login = "ingresar"
nombre_buscar = ""

#Bienvenida del usuario
print("\nBienvenido Usuario\n")

#Pedir Ingresar registrarme o ingresar
registro = str(input("¿Que desea hacer? (registrarme/ingresar)\n"))

#Pedir al usuario registarse o si ya tiene cuenta ingresar
while True:
    if registro == regis:
        break
    elif registro == login:
        break
    else:
        print("Dato ingresado incorrecto")
        registro = str(input("¿Que desea hacer? (Registrarme/Ingresar)\n"))
    
#Condicion para actuar dependiendo de la desicion
while True:
    #registro
    if registro == regis:
        nombre1 = str(input("\nIngresa su primer nombre\n"))
        nombre2 = str(input("\nIngresa su segundo nombre\n"))
        apellido1 = str(input("\nIngresa su primer apellido\n"))
        apellido2 = str(input("\nIngresa su segundo apellido\n"))
        correo = str(input("\nIngresa su correo\n"))
        while True:
            try:
                telefono = int(input("\nIngresa su telefonon\n"))
                break
            except ValueError:
                print("\nIngresa solo valores numericos\n")
        contraseña1 = str(input("Introduce una contraseña"))
        contraseña2 = str(input("Repite la constraseña"))
        while True:
            if contraseña1 != contraseña2:
                print("Error la contraseñas ingresadas no coinciden")
                contraseña1 = str(input("Cree una contraseña"))
                contraseña2 = str(input("Repita la contraseña\n"))
            else:
                break
            
        #Ir a buscar en la base de datos si ya existe el correo
        conn_login = sqlite3.connect("Registros.db")
        cursor_login = conn_login.cursor()
        cursor_login.execute("SELECT * FROM cuentas2 WHERE correo=?",(correo,))
        result_login = cursor_login.fetchone()
        
        if result_login:
            print("\nEl correo " +correo+ " ya esta registrado\n")
            
        else:
            cursor_login.execute("INSERT INTO cuentas2 (correo,primer_nombre,segundo_nombre,primer_apellido,segundo_apellido,telefono,contraseña)VALUES(?,?,?,?,?,?,?)",
            (correo,nombre1,nombre2,apellido1,apellido2,telefono,contraseña2))
            print("\nRegistro con exito")
            conn_login.commit()
            conn_login.close()
            break
        
        print(f"Bienvenido ' {nombre1}''{apellido1}'")
        #Cerrar la conexion con la base de datos
        
    # Ingresar a la cuenta
    elif registro == login:
        #Ingreso de correo y contraseña
        correo = str(input("Ingresa su correo\n"))
        contraseña1 = str(input("\nIngrese su contraseña\n"))
        
        #Crea la Variable Query para buscar los datos ingresados
        conn_correo =sqlite3.connect("Registros.db")
        cursor_correo = conn_correo.cursor()
        query = """SELECT *FROM cuentas2 WHERE correo = ? AND contraseña = ?"""
        
        #Ejecutar el query para relaizar la busqueda
        cursor_correo.execute(query, (correo, contraseña1))
        result_correo = cursor_correo.fetchone()
        
        #Validación si se cuentra en la base de datos, contar las columas de la tabla para que jale la info
        if result_correo:
            print("Bienvenido " +result_correo[2]+" "+result_correo[3])
            break
        else:
            print(f"No existe ningun correo registrado como: '{correo}'\no ingreso erroneamente la contraseña ")
        
#Acceso a la Tienda en Linea
    

    
        
        
    


