# Invasión Espacial

¡Bienvenido a **Invasión Espacial**! Este es un juego creado en Python utilizando la librería `pygame`. El objetivo es controlar una nave espacial y defender la Tierra destruyendo oleadas de enemigos que intentan llegar a la superficie.

## Requisitos del Sistema

Antes de ejecutar el juego, asegúrate de tener instalados los siguientes componentes:

- Python 3.x
- Pygame 2.x (`pip install pygame`)

## Instalación

1. Clona este repositorio en tu máquina local:

   ```bash
   git clone https://github.com/Lezaun1991/Nave_espacial_python.git
   cd invasion-espacial
2. Instala las dependencias necesarias (principalmente pygame):
   ```
   pip install pygame
   
## Ejecución del Juego
Para iniciar el juego, simplemente ejecuta el archivo main.py:
python main.py

## Controles del Juego
  * Flecha Izquierda: Mover la nave a la izquierda.
  * Flecha Derecha: Mover la nave a la derecha.
  * Espacio: Disparar un proyectil hacia los enemigos.

## Mecánica del Juego
Controla una nave espacial que se mueve de izquierda a derecha en la parte inferior de la pantalla.
El objetivo es disparar a los enemigos que descienden desde la parte superior de la pantalla antes de que lleguen al borde inferior.
Cuando disparas a un enemigo, este desaparece y reaparece en una posición aleatoria en la parte superior.
Si un enemigo llega a la parte inferior de la pantalla, el juego termina.

## Enemigos
Los enemigos son entidades que se mueven de lado a lado y descienden cada vez que tocan un borde. Si uno de ellos alcanza el límite inferior de la pantalla, el juego termina con un "GAME OVER".

## Colisiones
Si una bala que disparas golpea a un enemigo, el enemigo es destruido y se reinicia en una posición aleatoria en la parte superior de la pantalla. Aumenta en uno el puntaje por cada enemigo destruido.

## Música y Sonidos
Música de Fondo: Durante el juego, suena una música de fondo.
Sonido de Disparo: Cada vez que disparas, se reproduce un sonido.
Sonido de Impacto: Al destruir un enemigo, escucharás un sonido de impacto.

## Archivos Importantes
* main.py: Archivo principal que controla la lógica del juego.
* enemigo.py: Clase que representa a los enemigos del juego.
* assets/: Contiene imágenes y sonidos utilizados en el juego.
    * cohete.png: Imagen de la nave del jugador.
    * enemigo.png: Imagen de los enemigos.
    * bala.png: Imagen de la bala.
    * Fondo.jpg: Imagen de fondo del juego.
    * MusicaFondo.mp3: Música de fondo del juego.
    * disparo.mp3: Sonido de disparo.
    * Golpe.mp3: Sonido de impacto.
    * game-over-160612.mp3: Sonido de fin del juego.
 
## Estado del Juego
A continuación, se muestran las imágenes del juego en diferentes estados:

Estado inicial del juego (ImagenesJuego/InicioJuego.png)

La nave disparando a los enemigos (ImagenesJuego/impactoBala.png)

Estado cuando el juego termina (ImagenesJuego/finJuego.png)

El juego finaliza si una nave enemiga llega al borde inferior de la pantalla.

## Créditos
Este juego fue desarrollado por Víctor Alarcón Lezaun usando Pygame.
