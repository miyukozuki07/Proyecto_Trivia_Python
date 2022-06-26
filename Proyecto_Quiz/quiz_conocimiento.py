from io import open
import random

#Leer el archivo Preguntas y extraer las lineas del archivo
archivo = open("Preguntas.txt", "r", encoding = "utf8")
preguntas = archivo.readlines()
respuestas = preguntas
archivo.close()

#Estas 3 listas van a contener solo las preguntas
facil = [] 
normal = []
dificil = []

#Convirtiendo las lineas a listas clasificando por categorias (facil, normal, dificil)
for linea in preguntas:
    campos = linea.replace("\n", "").split(";")
    if campos[0] == 'facil':
        f = []
        for i in range(len(campos)):
            if i == 1 or i == 2:
                f.append(campos[i])
                
        facil.append(f)
        
    elif campos[0] == 'normal':
        n = []
        for i in range(len(campos)):
            if i == 1 or i == 2:
                n.append(campos[i])
                
        normal.append(n)
        
    else:
        d = []
        for i in range(len(campos)):
            if i == 1 or i == 2:
                d.append(campos[i])
                
        dificil.append(d)

#Estas 3 listas van a contener solo las opciones de respuesta
a_facil = []
a_normal = []
a_dificil = []
#Convirtiendo las lineas de respuestas a listas por categorias 
for linea in respuestas:
    campos = linea.replace("\n", "").split(";")
    if campos[0] == 'facil':
        f = []
        for i in range(len(campos)):
            if i >= 3:
                f.append(campos[i])

        a_facil.append(f)
                
    elif campos[0] == 'normal':
        n = []
        for i in range(len(campos)):
            if i >= 3:
                n.append(campos[i])

        a_normal.append(n)

    else:
        d = []
        for i in range(len(campos)):
            if i >= 3:
                d.append(campos[i])

        a_dificil.append(d)
        


#Leer el archivo Respuestas y extraer las lineas del archivo
archivo = open("Respuestas.txt", "r", encoding = "utf8")
respuesta = archivo.readlines()
archivo.close()

#Listas con la respuesta a cada pregunta
r_facil = []
r_normal = []
r_dificil = []

#Convirtiendo las lineas de respuesta a listas por categorias 
for linea in respuesta:
    campos = linea.replace("\n", "").split(";")
    if campos[0] == 'facil':
        f = []
        for i in range(len(campos)):
            if i > 1:
                f.append(campos[i])

        r_facil.append(f)
                
    elif campos[0] == 'normal':
        n = []
        for i in range(len(campos)):
            if i > 1:
                n.append(campos[i])

        r_normal.append(n)

    else:
        d = []
        for i in range(len(campos)):
            if i > 1:
                d.append(campos[i])

        r_dificil.append(d)

#----------------------------------------------------------
puntuacion = 0
jugando = 0

def preg_facil():
    jugando = 0
    for i in range(len(facil)):
        for j in range(len(facil[i])):
            if j == 1:
                a = facil[i][j]
                print(a)
                for k in range(len(a_facil)):
                    for m in range(len(a_facil[i])):
                        if i == k:
                            print(a_facil[k][m])
                ans = str(input())
                print(type(ans))
                rp = evaluar(jugando,a,ans)
                print(rp)

                """if rp == True:
                    print("Correcto")
                    puntuacion = puntuacion + 1
                else:
                    print("Incorrecto")"""
                
    
        
def preg_normal():
    for i in range(len(normal)):
        for j in range(len(normal[i])):
            if j == 1:
                print(normal[i][j])
                for k in range(len(a_normal)):
                    for m in range(len(a_normal[i])):
                        if i == k:
                            print(a_normal[k][m])
                ans = input()


def preg_dificil():
    for i in range(len(dificil)):
        for j in range(len(dificil[i])):
            if j == 1:
                print(dificil[i][j])
                for k in range(len(a_dificil)):
                    for m in range(len(a_dificil[i])):
                        if i == k:
                            print(a_dificil[k][m])
                ans = input()
    

def evaluar(jug, pre, res):
    a = pre
    b = res
    c = jug
    print(f"Valor de a:{a}")
    print(f"Valor de b:{b}")
    print(f"Valor de c:{c}")
    print(r_facil)

    if c == 0:
        for i in range(len(r_facil)):   #[1,2,3,4,5]
            print(f"Primer for:{i}")
            for j in range(len(r_facil[i])):    #[1,2]
                print(f"Segundo for: {j}")
                print("Valores del IF", r_facil[i][j], a)
                if r_facil[i][j] == a:
                    print(r_facil[i][j])
                    j = j + 1
                    ev = r_facil[i][j]
                    print(ev)

        if ev == b:
            print(ev)
                    


       
   
                
                    
    
print("Bienvenido al quiz de conocimiento")

preg_facil()





               




