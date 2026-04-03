#Ejercicio 1
nombre = input("Ingrese su nombre: ")
while nombre == "" or not nombre.isalpha():
    print("Porfavor, ingrese su nombre solo con letras y no puede estar vacio")
    nombre = input("Ingrese su nombre: ")

entrada_cantidad = input("Cuantos productos va a comprar?: ")
while not entrada_cantidad.isdigit() or int(entrada_cantidad) <= 0:
    print("Ingrese un numero mayor a 0")
    entrada_cantidad = input("Cuantos productos va a comprar?: ")

cantidad = int(entrada_cantidad)
total_sin_desc = 0
total_con_desc = 0

for i in range(cantidad):
    print(f"--- Producto {i+1} ---")
    
    precio_producto = input("Precio del producto: ")
    while not precio_producto.isdigit():
        print("Ingrese un precio valido")
        precio_producto = input("Precio del producto: ")
    
    precio = int(precio_producto)
    total_sin_desc = total_sin_desc + precio
    
    tiene_desc = input("El producto tiene algun descuento? (S/N): ").lower()
    while tiene_desc != "s" and tiene_desc != "n":
        print("Responda con S o N")
        tiene_desc = input("El producto tiene algun descuento? (S/N): ").lower()
    
    if tiene_desc == "s":
        precio_final = precio * 0.90
    else:
        precio_final = precio
    total_con_desc = total_con_desc + precio_final

ahorro = total_sin_desc - total_con_desc
promedio = total_con_desc / cantidad

print("-" * 30)
print(f"Cliente: {nombre}")
print(f"Total sin descuentos: {total_sin_desc}")
print(f"Total con descuentos: {total_con_desc}")
print(f"Ahorro total: {ahorro}")
print(f"Promedio por producto: {promedio:.2f}")

#Ejercicio 2
usuario_correcto = "alumno"
clave_correcta = "python123"
intentos = 0
acceso = False

while intentos < 3 and acceso == False:
    print(f"--- Intento {intentos + 1}/3 ---")
    usuario = input("Usuario: ")
    
    if usuario == usuario_correcto:
        clave = input("Clave: ")
        while clave != clave_correcta and intentos < 2:
            intentos = intentos + 1
            print(f"La clave que ha ingresado es incorrecta. Intento {intentos + 1}/3")
            clave = input("Ingrese la clave nuevamente: ")
        
        if clave == clave_correcta:
            acceso = True
            print("Acceso concedido.")
        else:
            intentos = 3 
    else:
        print("El usuario que ha ingresado es incorrecto.")
        intentos = intentos + 1

if acceso == False:
    print("Cuenta bloqueada")
else:
    opcion = ""
    while opcion != "4":
        print("\n--- MENU ---")
        print("1. Ver estado de la inscripcion")
        print("2. Cambiar clave")
        print("3. Mostrar mensaje motivacional")
        print("4. Salir")
        
        opcion = input("Opcion: ")
        
        while not opcion.isdigit() or int(opcion) < 1 or int(opcion) > 4:
            print("Ingrese un numero valido.")
            opcion = input("Opcion: ")
            
        if opcion == "1":
            print("Estado: Inscripto")
            input("Presione Enter para volver al menu...")
        elif opcion == "2":
            nueva_clave = input("Nueva clave: ")
            while len(nueva_clave) < 6:
                print("Deben ingresar minimo 6 caracteres.")
                nueva_clave = input("Nueva clave: ")
            
            confirmacion = input("Confirme nueva clave: ")
            if nueva_clave == confirmacion:
                clave_correcta = nueva_clave
                print("Clave cambiada con exito.")
            else:
                print("Las claves no coinciden intentelo de nuevo.")
            input("Presione Enter para volver al menu...")
        elif opcion == "3":
            print("No estas solo en esto; confia en ti mismo y sigue adelante.")
            input("Presione Enter para volver al menu...")

    print("Sesión cerrada.")
    
#Ejercicio 3
lu1 = ""
lu2 = ""
lu3 = ""
lu4 = ""

ma1 = ""
ma2 = ""
ma3 = ""

op = input("Nombre del operador: ")
while not op.isalpha() or op == "":
    print("Porfavor, ingrese un nombre valido solamente letras.")
    op = input("Nombre del operador: ")

menu = ""
while menu != "5":
    print("--- Agenda de Turnos ---")
    print("1- Reservar turno")
    print("2- Cancelar turno")
    print("3- Ver agenda del dia")
    print("4- Ver resumen general")
    print("5- Cerrar sistema")
    
    menu = input("Elija una opcion a realizar: ")
    while not menu.isdigit() or int(menu) < 1 or int(menu) > 5:
        print("Error: Marca del 1 al 5")
        menu = input("Elija una opcion a realizar: ")

    if menu == "1":
        dia = input("Elegir un dia (1-Lunes, 2-Martes): ")
        while dia != "1" and dia != "2":
            dia = input("Ingrese las unicas opciones 1 o 2: ")
            
        paciente = input("Nombre del paciente: ")
        while not paciente.isalpha() or paciente == "":
            print("Ingrese un nombre valido solamente letras.")
            paciente = input("Nombre del paciente: ")
        
        if dia == "1":
            if paciente == lu1 or paciente == lu2 or paciente == lu3 or paciente == lu4:
                print("El paciente ya tiene turno el lunes")
            elif lu1 == "": lu1 = paciente
            elif lu2 == "": lu2 = paciente
            elif lu3 == "": lu3 = paciente
            elif lu4 == "": lu4 = paciente
            else: print("El lunes esta completo, no hay mas lugar")
        else:
            if paciente == ma1 or paciente == ma2 or paciente == ma3:
                print("El paciente ya tiene turno el martes")
            elif ma1 == "": ma1 = paciente
            elif ma2 == "": ma2 = paciente
            elif ma3 == "": ma3 = paciente
            else: print("El martes esta completo, no hay mas lugar")
        input("Enter para volver al menu...")

    elif menu == "2":
        dia = input("Dia a cancelar turno (1-Lunes, 2-Martes): ")
        paciente = input("Nombre del paciente a cancelar el turno: ")
        
        if dia == "1":
            if lu1 == paciente: lu1 = ""
            elif lu2 == paciente: lu2 = ""
            elif lu3 == paciente: lu3 = ""
            elif lu4 == paciente: lu4 = ""
            else: print("El nombre ingresado no se encuentra en la base de datos")
        else:
            if ma1 == paciente: ma1 = ""
            elif ma2 == paciente: ma2 = ""
            elif ma3 == paciente: ma3 = ""
            else: print("El nombre ingresado no se encuentra en la base de datos")
        input("Enter para volver al menu...")

    elif menu == "3":
        dia = input("Ver agenda del dia (1-Lunes, 2-Martes): ")
        if dia == "1":
            print("Turno 1: " + (lu1 or "(libre)"))
            print("Turno 2: " + (lu2 or "(libre)"))
            print("Turno 3: " + (lu3 or "(libre)"))
            print("Turno 4: " + (lu4 or "(libre)"))
        else:
            print("Turno 1: " + (ma1 or "(libre)"))
            print("Turno 2: " + (ma2 or "(libre)"))
            print("Turno 3: " + (ma3 or "(libre)"))
        input("Enter para seguir...")

    elif menu == "4":
        llenos_lu = 0
        if lu1 != "": llenos_lu = llenos_lu + 1
        if lu2 != "": llenos_lu = llenos_lu + 1
        if lu3 != "": llenos_lu = llenos_lu + 1
        if lu4 != "": llenos_lu = llenos_lu + 1
        
        llenos_ma = 0
        if ma1 != "": llenos_ma = llenos_ma + 1
        if ma2 != "": llenos_ma = llenos_ma + 1
        if ma3 != "": llenos_ma = llenos_ma + 1
        
        print("Lunes: " + str(llenos_lu) + " ocupados y " + str(4 - llenos_lu) + " libres")
        print("Martes: " + str(llenos_ma) + " ocupados y " + str(3 - llenos_ma) + " libres")
        
        if llenos_lu == 0 and llenos_ma == 0:
            print("No hay turnos reservados en ninguno de los dias")
        elif llenos_lu > llenos_ma:
            print("Hay mas turnos reservados el lunes")
        elif llenos_ma > llenos_lu:
            print("Hay mas turnos reservados el martes")
        else:
            print("los dos dias tienen la misma cantidad de turnos reservados")
        input("Enter para seguir...")

print("Sistema cerrado, hasta luego " + op + "!")

#Ejercicio 4
energia = 100
tiempo = 12
cerraduras = 0
alarma = False
codigo_parcial = ""
forzar_cerr = 0

agente = input("Nombre del agente: ")
while not agente.isalpha() or agente == "":
    print("El nombre solo puede tener letras")
    agente = input("Nombre del agente: ")

while energia > 0 and tiempo > 0 and cerraduras < 3 and not alarma:
    print("-" * 30)
    print("ESTADO ACTUAL:")
    print("Agente:", agente)
    print("Energia:", energia, "| Tiempo:", tiempo)
    print("Cerraduras abiertas:", cerraduras)
    print("Codigo de hackeo:", codigo_parcial)
    
    print("\nMENU DE ACCIONES:")
    print("1. Forzar cerradura (-20 energia, -2 tiempo)")
    print("2. Hackear panel (-10 energia, -3 tiempo)")
    print("3. Descansar (+15 energia, -1 tiempo)")
    
    op = input("Elegi una accion: ")
    while not op.isdigit() or int(op) < 1 or int(op) > 3:
        print("Elegi un numero 1, 2 o 3")
        op = input("Elegi una accion: ")
    
    accion = int(op)

    if accion == 1:
        if energia < 40:
            print("¡CUIDADO! Tenes poca energia, hay riesgo de alarma.")
            riesgo = input("Elegi un numero del 1 al 3, cuidado una de ellas activa la alarma: ")
            while not riesgo.isdigit() or int(riesgo) < 1 or int(riesgo) > 3:
                riesgo = input("Solo los numero del 1 al 3: ")
            if int(riesgo) == 3:
                alarma = True
                print("¡MALAS NOTICIAS! Saltaron las alarmas.")

        if not alarma:
            forzar_cerr = forzar_cerr + 1
            energia = energia - 20
            tiempo = tiempo - 2
            
            if forzar_cerr == 3:
                alarma = True
                print("¡LA CERRADURA SE TRABO! Intentaste forzar demasiado.")
            else:
                cerraduras = cerraduras + 1
                print("¡Bien! Abriste una cerradura.")
                
    elif accion == 2:
        forzar_cerr = 0 
        energia = energia - 10
        tiempo = tiempo - 3
        
        print("Hackeando el sistema...")
        for i in range(4):
            codigo_parcial = codigo_parcial + "A"
            print("Cargando codigo... " + str(len(codigo_parcial) * 12) + "%")
        
        if len(codigo_parcial) >= 8 and cerraduras < 3:
            cerraduras = cerraduras + 1
            print("¡Hackeo exitoso! Se abrio una cerradura.")

    elif accion == 3:
        forzar_cerr = 0 
        descanso = 15
        tiempo = tiempo - 1
        if alarma:
            descanso = 5
            print("Debido a la alarma no has podido descanzar correctamente...")
        
        energia = energia + descanso
        if energia > 100:
            energia = 100
        print("Recuperaste algo de energia.")

    if alarma and tiempo <= 3 and cerraduras < 3:
        print("¡BLOQUEO TOTAL! El sistema de seguridad te atrapo.")
        break

print("\n" + "=" * 30)
if cerraduras == 3:
    print("¡VICTORIA! Abriste la boveda y escapaste.")
elif energia <= 0:
    print("DERROTA: Te quedaste sin fuerzas.")
elif tiempo <= 0:
    print("DERROTA: Se te acabo el tiempo.")
elif alarma:
    print("DERROTA: El sistema se bloqueo por la alarma.")
print("=" * 30)

#Ejercicio 5
vida_jugador = 100 
vida_rival = 100 
pociones = 3 
at_pesado = 15 
at_rival = 12 
turno_yo = True 

nom = input("Nombre del Gladiador: ")
while not nom.isalpha() or nom == "":
    print("Error: Solo se permiten letras")
    nom = input("Nombre del Gladiador: ")

print("=== INICIO DEL COMBATE ===")

while vida_jugador > 0 and vida_rival > 0:
    if turno_yo:
        print("\n" + nom + " (HP: " + str(vida_jugador) + ") vs Rival (HP: " + str(vida_rival) + ")")
        print("Pociones restantes: " + str(pociones))
        print("1. Ataque Pesado")
        print("2. Rafaga Veloz")
        print("3. Curar")
        
        op = input("Elegi accion: ")
        while not op.isdigit() or int(op) < 1 or int(op) > 3:
            print("Error: Ingrese un numero valido (1, 2 o 3)")
            op = input("Elegi accion: ")
        
        accion = int(op)
        
        if accion == 1:
            golpe = float(at_pesado) 
            if vida_rival < 20:
                golpe = golpe * 1.5 
                print("¡GOLPE CRITICO!")
            
            vida_rival = vida_rival - int(golpe)
            print("Atacaste al enemigo por " + str(golpe) + " de daño") 
            
        elif accion == 2:
            print(">> ¡Inicias una rafaga de golpes!")
            for i in range(3):
                vida_rival = vida_rival - 5 
                print("> Golpe conectado por 5 de daño") 
                
        elif accion == 3:
            if pociones > 0:
                vida_jugador = vida_jugador + 30 
                if vida_jugador > 100:
                    vida_jugador = 100
                pociones = pociones - 1 
                print("Te curaste. Vida actual: " + str(vida_jugador))
            else:
                print("¡No quedan pociones! Perdiste el turno") 
        
        turno_yo = False 
        
    else:
        if vida_rival > 0:
            vida_jugador = vida_jugador - at_rival 
            print("¡El enemigo te ataco por " + str(at_rival) + " puntos!") 
        turno_yo = True 

print("\n" + "=" * 25)
if vida_jugador > 0:
    print("¡VICTORIA! " + nom + " ha ganado la batalla.") 
else:
    print("DERROTA. Has caido en combate.") 
print("=" * 25)