# Encontrar el numero aleda;o menor para moverse, no tiene que llegar en menos movimientos sino en menos costo
# asi que eventualmente va a llegar al final sabiendo que el inicio puede ser aleatorio y el final es fijo

from random import randint

tablero = []
opcionesAledanas=[]
movements = []
position=[2,3]
isOnFinalScore = False

class Cursor:
    Value = 0 
    Cordinates = [0,0]

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

print("\nEsto es la poscision inicial: ", position)
print("Este es el tablero:")

# simpler dash print
# for i in tablero:
#     print(i)

for i in tablero:
    for j in i:
        print("\t", j, end="")
    print("")

while not isOnFinalScore:
    posIzquierda = [] 
    posDerecha = []
    posSuperior = [] 
    posInferior = []
    
    posIzquierda.append(tablero[position[0]-1][position[1]-2])
    posIzquierda.append([position[0]-1, position[1]-2])
    
    posDerecha.append(tablero[position[0]-1][position[1]])
    posDerecha.append([position[0]-1, position[1]])
    
    posSuperior.append(tablero[position[0]-2][position[1]-1])
    posSuperior.append([position[0]-2, position[1]-1])
    posInferior.append(tablero[position[0]][position[1]-1])
    posInferior.append([position[0], position[1]-1])
    
    opcionesAledanas.append(posIzquierda)
    opcionesAledanas.append(posDerecha)
    opcionesAledanas.append(posSuperior)
    opcionesAledanas.append(posInferior)
    
    for opcion in opcionesAledanas:
        print(opcion)
    
    if (position):
        # isOnFinalScore = True
        print("posiiton")
                
        
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
    


