import random

intentos = 0
aux = 0
palabras = ["besties","hamburguesa"]
respuesta = []
entrada = ""
puntos = 0
cond = True
cond2 = True
aleatorio = ""




while(cond2):
    nivel = int(input("Que nivel desea\n\t1.Bajo\n\t2. Medio\n\t3. Alto"))

    while(cond):
        if(nivel ==1):
            if len(random.choice(palabras))<=5:
                aleatorio = random.choice(palabras)
                cond = False
                intentos = 4
                aux = intentos
                puntos = 2
        elif (nivel == 2):
            if len(random.choice(palabras)) <= 12:
                aleatorio = random.choice(palabras)
                cond = False
                intentos = 6
                aux = intentos
                puntos = 3
        else:
            if len(random.choice(palabras)) > 12:
                aleatorio = random.choice(palabras)
                cond = False
                intentos = 8
                aux = intentos
                puntos = 5

    for i in range(len(aleatorio)):
        respuesta.append("*")

#    if(len(aleatorio)<=5):
#        intentos = 4
#        aux = intentos
#        puntos = 2

#    elif(len(aleatorio)<=12):
#        intentos = 6
#        aux = intentos
#        puntos = 3
#    else:
#        intentos = 8
#        aux = intentos
#        puntos = 5

    while(intentos!=0):
        print("intentos: ",intentos)
        print("puntos: ",puntos)
        print(*respuesta)
        entrada = input("Ingrese una letra: ")
        entrada = entrada.lower()


        #entrada=letra

        for sal,busq in enumerate(aleatorio):
            cont=0
            if(busq == entrada):
                respuesta[sal] = entrada
            elif (respuesta == aleatorio):
                intentos=0




        #print(intentos)
        #if respuesta == aleatorio:
        #            intentos = 0

       # for k in range(len(aleatorio)):
       #     if()

    if(aux != intentos):
        if(nivel ==1 or nivel ==2):
            puntos = puntos - 1
        elif(nivel ==3):
            puntos = puntos-2
