import pandas as pd, shutil, os, os.path, sys
ciclo = 1
separador = ("*" * 20) + "\n"
lista = []
tupla = ()

#Comprueba si existe un csv y lo pasa a un DataFrame, de no ser asi utliza la copia de seguridad,
#de no haberla hace un diccionario y la pasa a un DataFrame
if os.path.exists("Equipos") == True:
    equiposDF = pd.read_csv("Equipos.csv", index_col=0)
elif os.path.exists("CopiaDeSeguridad\CopiaEquipos") == True:
    shutil.move("CopiaDeSeguridad\CopiaEquipos.csv", "Equipos.csv")
    equiposDF = pd.read_csv("Equipos.csv", index_col=0)
else:
    equipos = {'Nombre':['Tigres','America','Atlas','Cruz Azul','Tijuana'],
               'Estadio':['Universitario','Monterrey','Jalisco','Azteca','Caliente'],
               'Ciudad':['Monterrey','Ciudad de Mexico','Guadalajara','Ciudad de Mexico','Tijuana']}
    equiposDF = pd.DataFrame(equipos)
    
while ciclo == 1:
    print("¿Que quieres hacer?")
    print("1. Ver equipos")
    print("2. Añadir un nuevo equipo")
    print("3. Modificar un equipo existente")
    print("4. Eliminar un equipo")
    print("5. Realizar copia de seguridad")
    print("6. Comparar listas y tuplas")
    print("7. Salir")
    opcion = int(input("> "))
    print(separador)
    
    if opcion == 1:
        print(equiposDF)
        print(separador)
        
    elif opcion == 2:
        print("Nombre del equipo")
        nombre = input("> ")
        print("Estadio")
        estadio = input("> ")
        print("Ciudad de origen")
        ciudad = input("> ")
        print(separador)
        
        equiposDF = equiposDF.append({'Nombre':nombre, 'Estadio':estadio, 'Ciudad':ciudad}, ignore_index=True)
        
    elif opcion == 3:
        print("Cual equipo quieres modificar \n")
        print(equiposDF.Nombre.to_string(index=True))
        index = int(input("> "))
        print("Dato que quieres modificar")
        print("1. Nombre")
        print("2. Estadio")
        print("3. Ciudad")
        dato = int(input("> "))
        
        if dato == 1:
            print("Nombre del equipo")
            nombre = input("> ")
            equiposDF.loc[index, "Nombre"] = nombre
            
        elif dato == 2:
            print("Nombre del estadio")
            estadio = input("> ")
            equiposDF.loc[index, "Estadio"] = estadio
        
        elif dato == 3:
            print("Nombre de la ciudad")
            ciudad = input("> ")
            equiposDF.loc[index, "Ciudad"] = ciudad
            
        print(separador)
        
    elif opcion == 4:
        print("Cual equipo quieres eliminar \n")
        print(equiposDF.Nombre.to_string(index=True))
        index = int(input("> "))
        equiposDF = equiposDF.drop(index, axis=0)
        equiposDF = equiposDF.reset_index(drop=True)
        print(separador)
    
    elif opcion == 5:
        equiposDF.to_csv(r'Equipos.csv', index=True, header=True)
        if os.path.exists("CopiaDeSeguridad") == True:
            shutil.copy("Equipos.csv", "CopiaDeSeguridad\CopiaEquipos.csv")
            
        elif os.path.exists("CopiaDeSeguridad") == False:
            os.mkdir("CopiaDeSeguridad")
            shutil.copy("Equipos.csv", "CopiaDeSeguridad\CopiaEquipos.csv")
            
    #Los for guardan los datos del DF en una lista y una tupla respectivamente, luego compara los tamaños
    elif opcion == 6:
        for index, linea in equiposDF.iterrows():
            lista_temp = [linea.Nombre, linea.Estadio, linea.Ciudad]
            lista.append(lista_temp)
            
        for index, linea in equiposDF.iterrows():
            tupla_temp = (linea.Nombre, linea.Estadio, linea.Ciudad)
            tupla += (tupla_temp,)
        
        tam_lista=(sys.getsizeof(lista))
        tam_tupla=(sys.getsizeof(tupla))
        print(f"tamaño de la lista: {tam_lista}")
        print(f"tamaño de la tupla: {tam_tupla}")
        
        if tam_lista < tam_tupla:
            print("La lista es mas pequeña que la tupla")
        elif tam_lista > tam_tupla:
            print("La tupla es mas pequeña que la lista")
        else:
            print("Las dos son del mismo tamaño")
        print(separador)
        
    elif opcion == 7:
        ciclo = 0
        equiposDF.to_csv(r'Equipos.csv', index=True, header=True)
