from os import system 
system("cls")
import random
### CREDITOS
### CEO: GERMAN PHILLIPE BONHOMME
### PROGRAMADOR SENIOR: GERMAN PHILLIPE BONHOMME
### PROGRAMADOR JUNIOR: GERMAN PHILLIPE BONHOMME
### ANALISTA PROGRAMADOR: GERMAN PHILLIPE BONHOMME
### APOYO MORAL 1: JIMI HENDRIX (THE JIMI HENDRIX EXPERIENCE)
### APOYO MORAL 2: JIMMY PAGE (LED ZEPPELIN)
### APOYO MORAL 3: LAS MINITAS DE IG
### APOYO MORAL 4: LAS CHICAS TRANS DE IG
### APOYO MORAL 5: LOS FEMBOYS DE IG
### APOYO MORAL 6: LUCIFER
### APOYO MORAL 7: CHATGPT
### APOYO MORAL 8: CAPUCCINO VAINILLA
### APOYO MORAL 9: LEFT 4 DEAD 2
### APOYO MORAL 10: SPOTIFY
def clear():
    system("cls")
def asignar():
    while True:
        clear()
        print("""
              ****************************
              ASIGNADO SUELDO ALEATORIO A:
              ****************************
              1- Juan Perez
              2- Maria Garcia
              3- Carlos Lopez
              4- Ana Martinez
              5- Pedro Rodriguez
              6- Laura Hernandez
              7- Miguel Sanchez
              8- Isabel Gomez
              9- Francisco Diaz
              10- Elena Fernandez
              *******************""")
        worker1={"nombre":"Juan Perez","sueldo":random.randint(300000,2500000)}
        worker2={"nombre":"Maria Garcia","sueldo":random.randint(300000,2500000)}
        worker3={"nombre":"Carlos Lopez","sueldo":random.randint(300000,2500000)}
        worker4={"nombre":"Ana Martinez","sueldo":random.randint(300000,2500000)}
        worker5={"nombre":"Pedro Rodriguez","sueldo":random.randint(300000,2500000)}
        worker6={"nombre":"Laura Hernandez","sueldo":random.randint(300000,2500000)}
        worker7={"nombre":"Miguel Sanchez","sueldo":random.randint(300000,2500000)}
        worker8={"nombre":"Isabel Gomez","sueldo":random.randint(300000,2500000)}
        worker9={"nombre":"Francisco Diaz","sueldo":random.randint(300000,2500000)}
        worker10={"nombre":"Elena Fernandez","sueldo":random.randint(300000,2500000)}
        #NO SUPE HACERLO CON UN FOR T-T
        trabajadores[0]=worker1
        trabajadores[1]=worker2
        trabajadores[2]=worker3
        trabajadores[3]=worker4
        trabajadores[4]=worker5
        trabajadores[5]=worker6
        trabajadores[6]=worker7
        trabajadores[7]=worker8
        trabajadores[8]=worker9
        trabajadores[9]=worker10
        print("Sueldos Asignados!")
        return trabajadores
def clasificar(trabajadores):
    clear()
    try:
        count1=0
        count2=0
        count3=0
        totalreal=0
        for trabajador in trabajadores:
            if trabajador["sueldo"]<800000:
                count1+=1
        print(f"Sueldos menores a $800.000 TOTAL: {count1}")
        print("Nombre empleado  |  Sueldo")
        for trabajador in trabajadores:
            if trabajador["sueldo"]<800000:
                print(f"{trabajador["nombre"]}  |  ${trabajador["sueldo"]}")
        for trabajador in trabajadores:
            if trabajador["sueldo"]>800000 and trabajador["sueldo"]<2000000:
                count2+=1
        print(f"Sueldos entre $800.000 y $2.000.000 TOTAL: {count2}")
        print("Nombre empleado  |  Sueldo")
        for trabajador in trabajadores:
            if trabajador["sueldo"]>800000 and trabajador["sueldo"]<2000000:
                print(f"{trabajador["nombre"]}  |  ${trabajador["sueldo"]}")
        for trabajador in trabajadores:
            if trabajador["sueldo"]>2000000:
                count3+=1
        print(f"Sueldos superiores a $2.000.000 TOTAL: {count3}")
        print("Nombre empleado  |  Sueldo")
        for trabajador in trabajadores:
            if trabajador["sueldo"]>2000000:
                print(f"{trabajador["nombre"]}  |  ${trabajador["sueldo"]}")
        for trabajador in trabajadores:
            total=trabajador["sueldo"]
            totalreal+=total
        print(f"TOTAL SUELDOS: ${totalreal}")
    except:
        print("Error! | Sueldos no asignados")

    pause()
def statistic(trabajadores):
    # NOTA: NO ME ACUERDO COMO HACER FUNCIONAR ESTA FUNCION, EL CODIGO ABAJO ME HA FUNCIONADO 2 VECES Y NI SE COMO
    # PROCEDO A RENDIRME F POR MI U.U :-:
    clear()
    try:
        for trabajador in trabajadores:
            sueldomaximo=2500000
            sueldominimo=300000
            sueldomasbajo=0
            if trabajador["sueldo"]<sueldomaximo:
                sueldomasbajo=trabajador["sueldo"]
        print(f"Sueldo mas bajo: ${sueldomasbajo}")
        
    except:
        print("Error! | No hay sueldos asignados")
    pause()
def report(trabajadores):
    clear()
    try:
        print("Nombre Empleado | Sueldo Base | Desc. Salud | Desc. AFP | Sueldo liquido")
        for trabajador in trabajadores:
            print(f"{trabajador["nombre"]} | ${trabajador["sueldo"]} | ${trabajador["sueldo"]*0.07:.0f} | ${trabajador["sueldo"]*0.12:.0f} | ${trabajador["sueldo"]-trabajador["sueldo"]*0.19:.0f}")
        f=open("Reporte.csv","w")
        f.write("Nombre Empleado;Sueldo Base;Desc. Salud;Desc. AFP;Sueldo liquido\n")
        for trabajador in trabajadores:
            f.write(f"{trabajador["nombre"]};${trabajador["sueldo"]};${trabajador["sueldo"]*0.07:.0f};${trabajador["sueldo"]*0.12:.0f};${trabajador["sueldo"]-trabajador["sueldo"]*0.19:.0f}\n")
        print("")
        print("Se ha impreso una plantilla en un archivo (.csv) exitosamente")
    except:
        print("Error! | No hay sueldos asignados!")
    pause()
def pause():
    input("Presione enter para continuar...")
sueldos=[] #       0               1            2             3                4               5                      6              7                  8               9         
trabajadores=["Juan Perez","Maria Garcia","Carlos Lopez","Ana Martinez","Pedro Rodriguez","Laura Hernandez","Miguel Sanchez","Isabel Gomez","Francisco Diaz","Elena Fernandez"]
while True:
    clear()
    print("""
          *****************************
          LEMON'S SALARY TOOL
          *****************************
          1- Asignar sueldos aleatorios 
          2- Clasificar sueldos
          3- Ver estadistica
          4- Reporte de sueldos
          5- Salir del programa
          *****************************""")
    op=input("Elige una opcion: ")
    match op:
        case "1":
            clear()
            asignar()
            pause()
        case "2":
            clasificar(trabajadores)
        case "3":
            clear()
            print("Proximamente! | Recuerda! este programa esta en una version beta y podria no contener aun las funciones prometidas!")
            input("Presione enter para continuar")
        case "4":
            report(trabajadores)
        case "5":
            clear()
            print("Finalizando programa...")
            print("Desarrollado por German Phillipe Bonhomme")
            print("RUT 20.730.806-4")
            import sys
            sys.exit()
        case other:
            clear()
            print("Error! | Opcion no valida")
            pause()