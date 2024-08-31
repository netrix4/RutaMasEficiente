# Encontrar el numero aleda;o menor para moverse, no tiene que llegar en menos movimientos sino en menos costo
# asi que eventualmente va a llegar al final sabiendo que el inicio puede ser aleatorio y el final es fijo

# checar si el paso que va a dar no sea uno donde ya estuvo

from random import randint

tablero = []
opcionesAledanas=[]
movements = []
# position = [2,3]    #Primero y hacia abjo y luego x a la derecha
position = [1,2]    #Primero y hacia abjo y luego x a la derecha
meta = [11, 6]
isOnFinalScore = False

#For random generation
# for i in range(13):
#     for j in range(13):
#         rows.append(randint(-5, 5))
#     tablero.append(rows)
#     rows=[]
    
tablero = [
    [-3,-3,2,-3,3,-2,-2,1,2,0,2,0,1],   #1
    [2,3,99,-1,-1,3,2,0,-3,-3,2,2,1],   #2
    [1,-3,-3,2,3,1,3,3,2,1,-2,-2,-3],   #3
    [0,0,3,0,3,-3,-2,-3,0,2,2,1,1],     #4
    [2,-1,-1,-3,3,3,0,-3,1,-2,2,0,1],   #5
    [0,3,-1,1,-1,-2,2,-2,2,-1,-2,-3,0], #6
    [0,3,2,0,1,1,2,3,-1,-1,0,0,-2],     #7
    [3,3,-3,-2,3,-3,-1,-3,3,-2,2,-2,-1],#8
    [-2,-2,1,0,-1,0,3,0,0,-2,2,-3,-1],  #9
    [-3,3,0,-1,-3,1,2,-3,2,-3,0,2,-2],  #10
    [-3,-3,-3,3,-2,0,-2,-3,1,0,1,-1,-2],#11
    [-1,0,1,2,1,0,100,0,-3,3,3,-2,1],   #12
    [1,-3,1,0,1,2,3,1,-2,3,3,0,3],      #13
]

class Cursor:
    Value = 0 
    Cordinates = [0,0]

def getSurroundedValues():
    """
    Purpose: Get cursor's surrounded values
    """
    posIzquierda = [] 
    posDerecha = []
    posSuperior = [] 
    posInferior = []
    
    posIzquierda.append(tablero[position[0]][position[1]-1])
    posIzquierda.append([position[0], position[1]-1])
    
    posDerecha.append(tablero[position[0]][position[1]+1])
    posDerecha.append([position[0], position[1]+1])
    
    posSuperior.append(tablero[position[0]-1][position[1]])
    posSuperior.append([position[0]-1, position[1]])
    
    posInferior.append(tablero[position[0]+1][position[1]])
    posInferior.append([position[0]+1, position[1]])

    # posSuperior.append(tablero[position[0]-2][position[1]-1])
    # posSuperior.append([position[0]-2, position[1]-1])
    # posInferior.append(tablero[position[0]][position[1]-1])
    # posInferior.append([position[0], position[1]-1])
    
    opcionesAledanas.append(posIzquierda)
    opcionesAledanas.append(posDerecha)
    opcionesAledanas.append(posSuperior)
    opcionesAledanas.append(posInferior)
    print("Estoes al final de la funcion: ", opcionesAledanas)

    # print("Posicion al final iteracion", position[0]+1, position[1]+1)
print("Este es el tablero:")

# simpler dash print
# for i in tablero:
#     print(i)

for i in tablero:
    for j in i:
        print("\t", j, end="")
    print("")

while not isOnFinalScore:
    print("Posicion al Inicio iteracion", position[0]+1, position[1]+1)
    
    getSurroundedValues()
        
    # print(menor)
    menor = opcionesAledanas[0]
    print("menor despues de calcular aledanos: ",menor)
    
    for opcion in opcionesAledanas:
        #Aqui evalua cual es la opcion mas barata de las 4 aledanas
        if opcion[0] < menor[0] and (opcion not in movements):
            menor = opcion
            print("Nuevo menor", menor, "Con opcion: ", opcion)
    
    movements.append(menor)
    # position = [menor[1][0]+1, menor[1][1]+1]
    position = menor[1]
    opcionesAledanas = []

    # print("este es el menor", menor)
    
    print("Posicion al final iteracion", position[0]+1, position[1]+1)
    print(meta)
    print()
    if(position == meta): 
        isOnFinalScore = True


#For input by user
# print("Enter your start: ")

# user_start_x_axis = input("X-axis, a number (_, ): ")
# # user_start_x_axis = input("X-axis, a letter (_, N): ")
# # user_start_x_axis = str.upper(user_start_x_axis)

# user_start_y_axis = input("y-axis,a number (0, _): ")

# user_start= (user_start_x_axis, user_start_y_axis)

# print(user_start)

# while (bandera):
    


