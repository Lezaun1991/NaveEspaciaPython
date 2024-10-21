import pygame
import math
from enemigo import Enemigo
from pygame import mixer
import io

## VARIABLE BYTES
def fuente_bytes(fuente):
    # Abre el archivo TTF en modo lectura binaria
    with open(fuente,'rb') as transformacion:
    # Lee todos los bytes del archivo y los almacena en una variable
        ttf_bytes = transformacion.read()
    # Crea un objeto BytesIO a partir de los bytes del archivo ttf
    return io.BytesIO(ttf_bytes)

fuente_como_bytes = fuente_bytes("assets/This_Night.ttf")


## INICIALIZAR A PYGAME
pygame.init()


# CREAR LA PANTALLA
pantalla = pygame.display.set_mode((800,600))

# TITULO E ICONO
pygame.display.set_caption("Invasión Espacial")
icono_ovni = pygame.image.load("assets/ovni.png")
pygame.display.set_icon(icono_ovni)

# AGREGAR MUSICA DE FONDO
mixer.music.load('assets/MusicaFondo.mp3')
mixer.music.set_volume(0.5)
mixer.music.play(-1)

# TEXTO FINAL DEL JUEGO
fuente_final = pygame.font.Font(fuente_como_bytes, 100)

def texto_final():
    mi_fuente_final = fuente_final.render("GAME OVER", True, (255,0,0))
    pantalla.blit(mi_fuente_final, (150,280))

# CONVERTIR LA FUENTE TTF A BYTE


# IMAGEN DE FONDO
imagen_fondo = pygame.image.load("assets/Fondo.jpg")

# VARIABLES JUGADOR
icono_cohete = pygame.image.load("assets/cohete.png")
jugador_x = 368
jugador_y = 500
jugador_x_cambio = 0

# VARIABLES ENEMIGOS ANTES DE LA CLASE
# icono_enemigo = pygame.image.load("enemigo.png")
# enemigo_x = random.randint(0,736)
# enemigo_y = random.randint(50,200)
# enemigo_x_cambio = 0.6
# enemigo_y_cambio = 50

# CREAR ENEMIGO DESPUES DE CLASES
# icono_enemigo = pygame.image.load("enemigo.png")
# enemigo = Enemigo(icono_enemigo,pantalla)

# CREAR LISTA DE ENEMIGOS
icono_enemigo = pygame.image.load("assets/enemigo.png")
enemigos = [Enemigo(icono_enemigo, pantalla) for _ in range(15)]

# VARIABLES BALA
balas = []
icono_bala = pygame.image.load("assets/bala.png")
bala_x = 0
bala_y = 500
bala_y_cambio = 5
bala_visible = False

# VARIABLE PUNTAJE
puntaje = 0
fuente = pygame.font.Font(fuente_como_bytes,32)
texto_x = 10
texto_y = 10

# FUNCION MOSTRAR PUNTAJE
def mostrar_puntaje(x,y):
    texto = fuente.render(f"Puntaje: {puntaje}", True, (255,255,255))
    pantalla.blit(texto,(x,y))

# FUNCION JUGADOR
def jugador(x, y):
    pantalla.blit(icono_cohete, (x,y))

# FUNCION ENEMIGO SIN CLASE
# def enemigo(x, y):
#     pantalla.blit(icono_enemigo, (x,y))

# DISPARAR BALA
def disparar_bala(x, y):
    global bala_visible
    bala_visible = True
    pantalla.blit(icono_bala, (x + 16, y + 10))

# FUNCION DETECTAR COLISIONES
def hay_colision(x_1,y_1,x_2,y_2):
    distancia = math.sqrt(math.pow(x_2 - x_1,2) + math.pow(y_2 - y_1,2))
    if distancia < 27:
        return True
    else:
        return False

# VARIABLES PARA EL SONIDO Y PARA OCULTAR ENEMIGOS
enemigo_ha_llegado_al_final = False
sonido_game_over_reproducido = False

# lOOP DEL JUEGO
se_ejecuta = True
while se_ejecuta:
    # # RGB
    # pantalla.fill((205, 144, 228))

    # IMAGEN DE FONDO
    pantalla.blit(imagen_fondo, (0,0))

    #ITERAR EVENTOS
    for evento in pygame.event.get():
        # EVENTO CERRAR PROGRAMA
        if evento.type == pygame.QUIT:
            se_ejecuta = False
        # EVENTO PRESIONAR TECLAS
        if evento.type == pygame.KEYDOWN:
            # PRESIONAR TECLA IZQUIERDA
            if evento.key == pygame.K_LEFT:
                jugador_x_cambio = -0.6
            # PRESIONAR TECLA IZQUIERDA
            if evento.key == pygame.K_RIGHT:
                jugador_x_cambio = +0.6
            if evento.key == pygame.K_SPACE:
                sonido_bala = mixer.Sound('assets/disparo.mp3')
                sonido_bala.play()
                sonido_bala.set_volume(0.3)
                nueva_bala = {
                    "x": jugador_x,
                    "y": jugador_y,
                    "velocidad": -5
                }
                balas.append(nueva_bala)

                # ESTO ERA PARA DISPARAR UNA BALA

                # if not bala_visible:
                #     bala_x = jugador_x
                #     disparar_bala(bala_x,bala_y)

        # EVENTO SOLTAR TECLA
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 0

    # MODIFICAR UBICACION JUGADOR
    jugador_x += jugador_x_cambio

    # MANTENER DENTRO DE BORDES JUGADOR
    if jugador_x <= 0:
        jugador_x = 0
    elif jugador_x >= 736:
        jugador_x = 736

    # # MODIFICAR UBICACION ENEMIGO ANTES DE CLASE
    # enemigo_x += enemigo_x_cambio
    #
    # # MANTENER DENTRO DE BORDES ENEMIGO
    # if enemigo_x <= 0:
    #     enemigo_x_cambio = 0.6
    #     enemigo_y += enemigo_y_cambio
    # elif enemigo_x >= 736:
    #     enemigo_x_cambio = -0.6
    #     enemigo_y += enemigo_y_cambio 


    # MOSTRAR PUNTAJE

    mostrar_puntaje(texto_x, texto_y)
    # DESPUES DE LA CLASE ENEMIGO


    for enemigo in enemigos:
        if enemigo.final_juego():
            enemigo_ha_llegado_al_final = True
            break

    if enemigo_ha_llegado_al_final:
        for enemigo in enemigos:
            enemigo.ocultar()
        texto_final()
        if not sonido_game_over_reproducido:
            mixer.music.stop()
            musica_game_over = mixer.Sound('assets/game-over-160612.mp3')
            musica_game_over.play()
            sonido_game_over_reproducido = True


    else:
        # MOSTRAR JUGADOR
        jugador(jugador_x, jugador_y)
        for enemigo in enemigos:
            enemigo.mover()
            enemigo.dibujar()

    if not enemigo_ha_llegado_al_final:
        # MOVIMIENTO BALA CUANDO ERA UNA SOLA BALA
        # if bala_y <= - 64:
        #         #     bala_y = 500
        #         #     bala_visible = False
        #         # if bala_visible:
        #         #     disparar_bala(bala_x,bala_y)
        #         #     bala_y -= bala_y_cambio
        for bala in balas:
            bala["y"] += bala["velocidad"]
            pantalla.blit(icono_bala,(bala["x"] + 16, bala["y"] + 10 ))
            if bala["y"] < 0:
                balas.remove(bala)

        # COLISION
            for enemigo in enemigos:
                colision = hay_colision(enemigo.enemigo_x,enemigo.enemigo_y,bala["x"],bala["y"])
                if colision:
                    sonido_golpe = mixer.Sound('assets/Golpe.mp3')
                    sonido_golpe.play()
                    sonido_golpe.set_volume(1)
                    if bala in balas:
                        balas.remove(bala)
                    puntaje += 1
                    enemigo.reiniciar()


            # POSICION DE LA NAVE Y ENEMIGO



        # ACTUALIZAR
    pygame.display.update()
