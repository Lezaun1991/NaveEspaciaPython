import random
import pygame



class Enemigo:
    def __init__(self, imagen, pantalla):
        self.imagen = imagen
        self.pantalla = pantalla
        self.enemigo_x = random.randint(0, 736)
        self.enemigo_y = random.randint(50, 200)
        self.enemigo_x_cambio = 0.6
        self.enemigo_y_cambio = 50

    def mover(self):
        self.enemigo_x += self.enemigo_x_cambio

        # Limitar movimiento en los bordes
        if self.enemigo_x <= 0:
            self.enemigo_x_cambio = 0.6
            self.enemigo_y += self.enemigo_y_cambio
        elif self.enemigo_x >= 736:
            self.enemigo_x_cambio = -0.6
            self.enemigo_y += self.enemigo_y_cambio

    def dibujar(self):
        self.pantalla.blit(self.imagen, (self.enemigo_x, self.enemigo_y))

    def reiniciar(self):
        self.enemigo_x = random.randint(0, 736)
        self.enemigo_y = random.randint(50, 200)
    def final_juego(self):
        if self.enemigo_y > 455:
            return True
        else:
            return False
    def ocultar(self):
        self.enemigo_y = 1000


