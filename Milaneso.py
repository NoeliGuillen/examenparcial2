from vpython import *
import math

# Crear una escena
scene = canvas(title="Prueba Teclado") 

# Diccionario de objetos
objetos = {}

# Crear dos objetos (cubo y cubo2) y almacenarlos en el diccionario
objetos['cilindrop'] = cylinder(pos=vector(-16.5, 5, -10), axis=vector(0, 0, 0), radius=1.5, color=color.red)
objetos['cilindro2'] = cylinder(pos=vector(16.5, 5, -10), axis=vector(0, 0, 0), radius=1.5, color=color.red)
objetos['cilindro3'] = cylinder(pos=vector(-5, -10, -10), axis=vector(0, 0, 0), radius=2, color=color.blue)
objetos['cilindro4'] = cylinder(pos=vector(5, -10, -10), axis=vector(0, 0, 0), radius=2, color=color.blue)

# Bolitas de los brazos
objetos['bolita1'] = sphere(color=color.blue, pos=vector(-16.5, 5, -10), radius=1.5)
objetos['bolita2'] = sphere(color=color.blue, pos=vector(16.5, 5, -10), radius=1.5)

# Cabeza
objetos['cabeza'] = sphere(color=color.cyan, pos=vector(0, 16, -10), radius=7)
objetos['ojo1'] = sphere(color=color.white, pos=vector(0.75, 16, -8.5), radius=5.5)
objetos['ojo2'] = sphere(color=color.white, pos=vector(-0.75, 16, -8.5), radius=5.5)
objetos['ojo1p'] = sphere(color=color.black, pos=vector(2.8, 15.5, -4), radius=1.5)
objetos['ojo2p'] = sphere(color=color.black, pos=vector(-2.8, 15.5, -4), radius=1.5)
objetos['antena1'] = cylinder(pos=vector(6, 16, -10), axis=vector(1.5, 0, 0), radius=4, color=color.red)
objetos['antena2'] = cylinder(pos=vector(-6, 16, -10), axis=vector(-1.5, 0, 0), radius=4, color=color.red)
objetos['palo1'] = box(pos=vector(8, 19, -10), size=vector(1, 10, 1), color=color.blue)
objetos['palo2'] = box(pos=vector(-8, 19, -10), size=vector(1, 10, 1), color=color.blue)
objetos['ball1'] = sphere(color=color.red, pos=vector(8, 24, -10), radius=1.5)
objetos['ball2'] = sphere(color=color.red, pos=vector(-8, 24, -10), radius=1.5)
objetos['boca'] = cylinder(pos=vector(0, 12.8, -5.5), axis=vector(0, 0.5, 1), radius=2, color=color.black)
objetos['base'] = cylinder(pos=vector(0, 22, -10), axis=vector(0, 1.5, 0), radius=5.5, color=color.red)
objetos['copa'] = cylinder(pos=vector(0, 23, -10), axis=vector(0, 3.5, 0), radius=4, color=color.red)

# Creación del cubo
objetos['cubo1'] = box(pos=vector(0, 0, -10), size=vector(30, 20, 15), color=color.blue)
objetos['cubo2'] = box(pos=vector(-8, 5, -2), size=vector(7, 5, 1), color=color.green)
objetos['cubo3'] = box(pos=vector(0, 5, -2), size=vector(2, 2, 1), color=color.red)
objetos['cubo4'] = box(pos=vector(-10, -5, -2), size=vector(3, 5, 1), color=color.yellow)
objetos['cubo5'] = box(pos=vector(-5, -5, -2), size=vector(3, 5, 1), color=color.black)
objetos['cubo6'] = box(pos=vector(0, -5, -2), size=vector(3, 5, 1), color=color.purple)
objetos['cubo7'] = box(pos=vector(8, 7, -2), size=vector(10, 1, 1), color=color.black)
objetos['cubo8'] = box(pos=vector(8, -7, -2), size=vector(10, 1, 1), color=color.black)
objetos['cubo9'] = box(pos=vector(3, 0, -2), size=vector(1, 15, 1), color=color.black)
objetos['cubo10'] = box(pos=vector(13, 0, -2), size=vector(1, 15, 1), color=color.black)
objetos['cubo11'] = box(pos=vector(5, 3, -2), size=vector(1, 1, 1), color=color.orange)
objetos['cubo12'] = box(pos=vector(8, 2, -2), size=vector(1, 1, 1), color=color.white)
objetos['cubo13'] = box(pos=vector(11, 1, -2), size=vector(1, 1, 1), color=color.cyan)

# Cuadritos
objetos['cubo14'] = box(pos=vector(-13, 8, -2), size=vector(1, 1, 1), color=color.white)
objetos['cubo15'] = box(pos=vector(-13, -8, -2), size=vector(1, 1, 1), color=color.white)
objetos['cubo16'] = box(pos=vector(13, 8, -2), size=vector(1, 1, 1), color=color.white)
objetos['cubo17'] = box(pos=vector(13, -8, -2), size=vector(1, 1, 1), color=color.white)


# Definir los movimientos en el eje X y Z
incremento_x = 0
incremento_y = 0
incremento_z = 0

limite_x = 20  # Límite de movimiento en X
limite_y = 6
limite_z = 5

incremento2 = vector(0, -0.3, 0)
incremento3 = vector(0, 0.4, 0)
incremento4 = vector(0, 0.5, 0)

amplitud = 45  # Ángulo máximo de inclinación
amplitud2 = -45
frecuencia = 0.2  # Control de la velocidad del balanceo
tiempo = 0

#CAMARA
camara_inclinacion = 0
camara_rotacion = 4.7
camara_distancia = 50

def mover_camara(evt):
    global camara_inclinacion, camara_rotacion
    if evt.key == 'w':  # Mover hacia adelante
        camara_inclinacion += 0.1
    elif evt.key == 's':  # Mover hacia atrás
        camara_inclinacion -= 0.1
    elif evt.key == 'd':  # Rotar hacia la izquierda
        camara_rotacion += 0.1
    elif evt.key == 'a':  # Rotar hacia la derecha
        camara_rotacion -= 0.1

# Enlazar los eventos de teclado
scene.bind('keydown', mover_camara)

# Función para mover los objetos según las teclas presionadas
def mover_objetos(evt):
    global incremento_x, incremento_z, incremento_y
    if evt.key == 'left':
        incremento_x = -0.6
    elif evt.key == 'right':
        incremento_x = 0.6
    elif evt.key == 'up':
        incremento_z = 0.6  # Subir cuando presionas "up" (salto)
    elif evt.key == 'down':
        incremento_z = -0.6  # Bajar cuando presionas "down"

# Función para detener el movimiento cuando se suelta la tecla
def detener_objetos(evt):
    global incremento_x, incremento_z, incremento_y
    if evt.key == 'left' or evt.key == 'right':
        incremento_x = 0
    elif evt.key == 'up' or evt.key == 'down':
        incremento_z = 0
        incremento_y = 0  # Detener el salto al soltar la tecla

# Enlazar los eventos de teclado
scene.bind('keydown', mover_objetos)
scene.bind('keyup', detener_objetos)
# Bucle de animación
while True:
    rate(30)  # Control de la tasa de actualización

    scene.forward = vector(math.cos(camara_rotacion) * math.cos(camara_inclinacion),
                           math.sin(camara_inclinacion),
                           math.sin(camara_rotacion) * math.cos(camara_inclinacion))

    for objeto in objetos.values():
        objeto.pos.x += incremento_x  
        objeto.pos.y += incremento_y 
        objeto.pos.z += incremento_z

    # Mover las esferas en los ejes y
    objetos['cubo2'].pos += incremento2
    objetos['cubo3'].pos += incremento3
    objetos['cubo4'].pos += incremento4

    if objetos['cubo2'].pos.y > limite_y or objetos['cubo2'].pos.y < -limite_y:
        incremento2.y = -incremento2.y
    if objetos['cubo3'].pos.y > limite_y or objetos['cubo3'].pos.y < -limite_y:
        incremento3.y = -incremento3.y
    if objetos['cubo4'].pos.y > limite_y or objetos['cubo4'].pos.y < -limite_y:
        incremento4.y = -incremento4.y

    # BRAZOS (continuación del movimiento)
    angulo = amplitud * math.sin(frecuencia * tiempo)
    objetos['cilindrop'].axis = vector(0, 10, 0)
    objetos['cilindrop'].rotate(angle=math.radians(angulo), axis=vector(2, 1, 1), origin=objetos['cilindrop'].pos)
    tiempo += 0.1

    angulo = amplitud2 * math.sin(frecuencia * tiempo)
    objetos['cilindro2'].axis = vector(0, -10, 0)
    objetos['cilindro2'].rotate(angle=math.radians(angulo), axis=vector(1, 0, 0), origin=objetos['cilindro2'].pos)
    tiempo += 0.1

    angulo = amplitud * math.sin(frecuencia * tiempo)
    objetos['cilindro3'].axis = vector(0, -12, 0)
    objetos['cilindro3'].rotate(angle=math.radians(angulo), axis=vector(1, 0, 0), origin=objetos['cilindro3'].pos)
    tiempo += 0.1

    angulo = amplitud2 * math.sin(frecuencia * tiempo)
    objetos['cilindro4'].axis = vector(0, -12, 0)
    objetos['cilindro4'].rotate(angle=math.radians(angulo), axis=vector(1, 0, 0), origin=objetos['cilindro4'].pos)
    tiempo += 0.1





