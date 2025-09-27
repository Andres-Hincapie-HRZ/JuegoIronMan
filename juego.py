# Importar librerías necesarias
import math  # Importa la librería matemática para cálculos como la raíz cuadrada
import random  # Importa la librería random para generar números aleatorios
import pygame  # Importa la librería pygame para crear el juego
from pygame import mixer  # Importa el módulo mixer de pygame para manejar sonidos

# Inicializar la librería pygame
pygame.init()  # Inicializa todos los módulos de pygame

# Crear la pantalla del juego
pantalla = pygame.display.set_mode((900, 600))  # Crea una ventana de 900x600 píxeles

# Establecer imagen de fondo del juego
fondo = pygame.image.load('fondo.png')  # Carga la imagen de fondo

# Establecer música de fondo del juego
mixer.music.load("musica_fondo.wav")  # Carga el archivo de música de fondo
mixer.music.play(-1)  # Reproduce la música en bucle infinito

# Título del juego y el icono del juego
pygame.display.set_caption("IRON MAN EN EL ESPACIO")  # Establece el título de la ventana
icono = pygame.image.load('icono.ico')  # Carga el icono del juego
pygame.display.set_icon(icono)  # Establece el icono de la ventana

# Establecer jugador (imagen 64x64 formato png) + movimientos del Jugador
jugador_img = pygame.image.load('jugador.png')  # Carga la imagen del jugador
jugadorX = 370  # Posición inicial en X del jugador
jugadorY = 480  # Posición inicial en Y del jugador
jugadorX_cambio = 0  # Cambio en X del jugador (velocidad)

# Establecer enemigo y movimientos del enemigo y cantidad de enemigos
enemigo_img = []  # Lista para almacenar las imágenes de los enemigos
enemigoX = []  # Lista para almacenar la posición X de los enemigos
enemigoY = []  # Lista para almacenar la posición Y de los enemigos
enemigoX_cambio = []  # Lista para almacenar el cambio en X de los enemigos
enemigoY_cambio = []  # Lista para almacenar el cambio en Y de los enemigos
num_de_enemigos = 6  # Número de enemigos en el juego

# Movimiento del enemigo de izquierda a derecha (imagen 70x70 formato png)
for i in range(num_de_enemigos):  # Bucle para crear cada enemigo
    enemigo_img.append(pygame.image.load('enemigo.png'))  # Carga la imagen del enemigo
    enemigoX.append(random.randint(0, 736))  # Posición X aleatoria del enemigo
    enemigoY.append(random.randint(50, 150))  # Posición Y aleatoria del enemigo
    enemigoX_cambio.append(0.5)  # Velocidad horizontal del enemigo
    enemigoY_cambio.append(40)  # Cambio vertical cuando el enemigo toca el borde

# Establecer cohete o bala (imagen 32x32 formato png) + movimiento vertical de las balas
bala_img = pygame.image.load('bala.png')  # Carga la imagen de la bala
balas = []  # Lista para almacenar las balas activas
balaY_cambio = 2  # Velocidad vertical de la bala

# Puntuación del jugador
valor_puntuacion = 0  # Inicializa la puntuación en cero
fuente = pygame.font.Font('freesansbold.ttf', 32)  # Fuente para mostrar la puntuación
textoX = 10  # Posición X del texto de puntuación
textoY = 10  # Posición Y del texto de puntuación

# Pantalla final Game Over
fuente_game_over = pygame.font.Font('freesansbold.ttf', 64)  # Fuente para el texto de Game Over

# Variables para el sistema de pausa
pausa = False  # Variable para saber si el juego está en pausa
fuente_pausa = pygame.font.Font('freesansbold.ttf', 64)  # Fuente para el texto de pausa
fuente_boton = pygame.font.Font('freesansbold.ttf', 32)  # Fuente para el botón de pausa
fuente_play = pygame.font.Font('freesansbold.ttf', 48)  # Fuente para el texto de play
boton_pausa_rect = pygame.Rect(850, 10, 32, 32)  # Rectángulo para el botón de pausa

def mostrar_puntuacion(x, y):
    # Muestra la puntuación en pantalla
    puntuacion = fuente.render("PUNTAJE : " + str(valor_puntuacion), True, (255, 255, 255))  # Renderiza el texto de puntuación
    pantalla.blit(puntuacion, (x, y))  # Dibuja el texto en la pantalla

def texto_game_over():
    # Muestra el texto de Game Over en pantalla
    texto_game_over = fuente_game_over.render("GAME OVER", True, (255, 255, 255))  # Renderiza el texto de Game Over
    pantalla.blit(texto_game_over, (200, 250))  # Dibuja el texto en la pantalla

def jugador(x, y):
    # Dibuja al jugador en la pantalla
    pantalla.blit(jugador_img, (x, y))  # Dibuja la imagen del jugador en la posición (x, y)

def enemigo(x, y, i):
    # Dibuja un enemigo en la pantalla
    pantalla.blit(enemigo_img[i], (x, y))  # Dibuja la imagen del enemigo i en la posición (x, y)

def disparar_bala(x, y):
    # Dispara una bala desde la posición (x, y)
    bala = {'x': x, 'y': y}  # Crea un diccionario con la posición de la bala
    balas.append(bala)  # Agrega la bala a la lista de balas

def colision(enemigoX, enemigoY, balaX, balaY):
    # Calcula si hay colisión entre un enemigo y una bala
    distancia = math.sqrt(math.pow(enemigoX - balaX, 2) + (math.pow(enemigoY - balaY, 2)))  # Calcula la distancia entre el enemigo y la bala
    if distancia < 27:  # Si la distancia es menor a 27, hay colisión
        return True
    else:
        return False

def mostrar_pausa():
    # Muestra la pantalla de pausa
    s = pygame.Surface((900, 600))  # Crea una superficie del tamaño de la pantalla
    s.set_alpha(128)  # Establece la transparencia de la superficie
    s.fill((0, 0, 0))  # Rellena la superficie de negro
    pantalla.blit(s, (0, 0))  # Dibuja la superficie en la pantalla
    
    # Texto PAUSA con sombra
    texto_sombra = fuente_pausa.render("PAUSA", True, (50, 50, 50))  # Renderiza la sombra del texto PAUSA
    texto_pausa = fuente_pausa.render("PAUSA", True, (255, 255, 255))  # Renderiza el texto PAUSA
    pantalla.blit(texto_sombra, (353, 253))  # Dibuja la sombra
    pantalla.blit(texto_pausa, (350, 250))  # Dibuja el texto principal
    
    # Triángulo de PLAY blanco con borde
    pygame.draw.polygon(pantalla, (255, 255, 255), [
        (400, 350),
        (400, 400),
        (450, 375)
    ], 0)  # Dibuja un triángulo blanco para indicar "play"
    
    # Texto "Click para continuar"
    texto_continuar = fuente_boton.render("Click para continuar", True, (255, 255, 255))  # Renderiza el texto de continuar
    pantalla.blit(texto_continuar, (300, 450))  # Dibuja el texto en la pantalla

def dibujar_boton_pausa():
    # Dibuja el botón de pausa en la pantalla
    color_boton = (200, 200, 200) if boton_pausa_rect.collidepoint(pygame.mouse.get_pos()) else (255, 255, 255)  # Cambia el color si el mouse está sobre el botón
    
    # Fondo del botón
    pygame.draw.rect(pantalla, (50, 50, 50), boton_pausa_rect)  # Dibuja el fondo oscuro del botón
    pygame.draw.rect(pantalla, color_boton, boton_pausa_rect, 2)  # Dibuja el borde del botón
    
    # Barras de pausa más estilizadas
    pygame.draw.rect(pantalla, color_boton, (boton_pausa_rect.x + 8, boton_pausa_rect.y + 6, 4, 20))  # Dibuja la primera barra de pausa
    pygame.draw.rect(pantalla, color_boton, (boton_pausa_rect.x + 20, boton_pausa_rect.y + 6, 4, 20))  # Dibuja la segunda barra de pausa

# Bucles del juego
jugando = True  # Variable para controlar el bucle principal del juego
while jugando:  # Bucle principal del juego
    pantalla.fill((0, 0, 0))  # Rellena la pantalla de negro
    pantalla.blit(fondo, (0, 0))  # Dibuja la imagen de fondo
    
    # Dibujar botón de pausa
    dibujar_boton_pausa()  # Llama a la función para dibujar el botón de pausa
    
    for evento in pygame.event.get():  # Procesa los eventos de pygame
        if evento.type == pygame.QUIT:  # Si se cierra la ventana
            jugando = False  # Termina el bucle principal
            
        if evento.type == pygame.MOUSEBUTTONDOWN:  # Si se presiona un botón del mouse
            pos_mouse = pygame.mouse.get_pos()  # Obtiene la posición del mouse
            if pausa:  # Si el juego está en pausa
                # Cualquier clic reanuda el juego cuando está en pausa
                pausa = False  # Quita la pausa
                mixer.music.unpause()  # Reanuda la música
            elif boton_pausa_rect.collidepoint(pos_mouse):  # Si se hace clic en el botón de pausa
                # Solo el botón de pausa puede pausar el juego
                pausa = True  # Pone el juego en pausa
                mixer.music.pause()  # Pausa la música

        # Solo procesar teclas si no está en pausa
        if not pausa:  # Si el juego no está en pausa
            if evento.type == pygame.KEYDOWN:  # Si se presiona una tecla
                if evento.key == pygame.K_LEFT:  # Si la tecla es flecha izquierda
                    jugadorX_cambio = -2  # Mueve el jugador a la izquierda
                if evento.key == pygame.K_RIGHT:  # Si la tecla es flecha derecha
                    jugadorX_cambio = 2  # Mueve el jugador a la derecha
                if evento.key == pygame.K_SPACE:  # Si la tecla es espacio
                    sonido_bala = mixer.Sound("disparo.wav")  # Carga el sonido de disparo
                    sonido_bala.play()  # Reproduce el sonido de disparo
                    balaX = jugadorX  # Posición X de la bala igual a la del jugador
                    disparar_bala(balaX, jugadorY)  # Dispara la bala

            if evento.type == pygame.KEYUP:  # Si se suelta una tecla
                if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:  # Si es flecha izquierda o derecha
                    jugadorX_cambio = 0  # Detiene el movimiento del jugador

    if pausa:  # Si el juego está en pausa
        mostrar_pausa()  # Muestra la pantalla de pausa
        pygame.display.update()  # Actualiza la pantalla
        continue  # Salta el resto del bucle y vuelve al inicio

    # Solo actualizar posiciones si no está en pausa
    jugadorX += jugadorX_cambio  # Actualiza la posición X del jugador
    if jugadorX <= 0:  # Si el jugador llega al borde izquierdo
        jugadorX = 0  # Lo mantiene en el borde
    elif jugadorX >= 736:  # Si el jugador llega al borde derecho
        jugadorX = 736  # Lo mantiene en el borde

    # Movimiento de los enemigos y colisión al impacto de la bala (dentro de bucles del juego)
    for i in range(num_de_enemigos):  # Para cada enemigo
        if enemigoY[i] > 440:  # Si el enemigo llega a la parte inferior
            for j in range(num_de_enemigos):  # Para todos los enemigos
                enemigoY[j] = 2000  # Los mueve fuera de la pantalla
            texto_game_over()  # Muestra el texto de Game Over
            break  # Sale del bucle de enemigos

        enemigoX[i] += enemigoX_cambio[i]  # Actualiza la posición X del enemigo
        if enemigoX[i] <= 0:  # Si el enemigo llega al borde izquierdo
            enemigoX_cambio[i] = 0.5  # Cambia la dirección a la derecha
            enemigoY[i] += enemigoY_cambio[i]  # Baja el enemigo
        elif enemigoX[i] >= 736:  # Si el enemigo llega al borde derecho
            enemigoX_cambio[i] = -0.5  # Cambia la dirección a la izquierda
            enemigoY[i] += enemigoY_cambio[i]  # Baja el enemigo

        # Impacto de las balas en los enemigos + (sonido duración 1 segundo max 2 formato wav) (dentro de bucles del juego)
        for bala in balas:  # Para cada bala activa
            colisiona = colision(enemigoX[i], enemigoY[i], bala['x'], bala['y'])  # Comprueba si hay colisión
            if colisiona:  # Si hay colisión
                sonido_explosion = mixer.Sound("explosion.wav")  # Carga el sonido de explosión
                sonido_explosion.play()  # Reproduce el sonido de explosión
                balas.remove(bala)  # Elimina la bala de la lista
                valor_puntuacion += 1  # Aumenta la puntuación
                enemigoX[i] = random.randint(0, 736)  # Reaparece el enemigo en una posición X aleatoria
                enemigoY[i] = random.randint(50, 150)  # Reaparece el enemigo en una posición Y aleatoria
                break  # Sale del bucle de balas

        enemigo(enemigoX[i], enemigoY[i], i)  # Dibuja el enemigo en pantalla

    # Movimiento y renderizado de las balas (dentro de bucles del juego)
    for bala in balas:  # Para cada bala activa
        bala['y'] -= balaY_cambio  # Mueve la bala hacia arriba
        pantalla.blit(bala_img, (bala['x'] + 16, bala['y'] + 10))  # Dibuja la bala en pantalla

    # Eliminar balas fuera de pantalla (dentro de bucles del juego)
    for bala in balas.copy():  # Copia la lista de balas para poder eliminar mientras se itera
        if bala['y'] <= 0:  # Si la bala sale de la pantalla por arriba
            balas.remove(bala)  # Elimina la bala de la lista
            
    # Mostrar jugador y puntuación
    jugador(jugadorX, jugadorY)  # Dibuja al jugador en pantalla
    mostrar_puntuacion(textoX, textoY)  # Muestra la puntuación en pantalla

    pygame.display.update()  # Actualiza la pantalla con todos los cambios
