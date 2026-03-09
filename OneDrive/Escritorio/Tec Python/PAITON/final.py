import pygame
import math

SCREEN_WIDTH, SCREEN_HEIGHT = 1800, 1000

WHITE  = (255, 255, 255)
BLACK  = (0, 0, 0)
GREEN  = (0, 200, 0)
YELLOW = (230, 200, 0)
RED    = (220, 0, 0)
GRIS = (176, 176, 176)
YELLOW_Ivana = (237, 194, 50)

pygame.init()
pygame.display.set_caption("Traffic simple")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
running = True
clock = pygame.time.Clock()

# Posición y movimiento del carro
x = 0
y = 190
velocidad = 0

# Dirección visual del carro
angulo_carro = 0   # 0 = derecha, 90 = abajo

# Control del recorrido
tramo = "horizontal"   # horizontal, curva, vertical
Vel_angular = -math.pi / 2

# Semáforo
estado = "VERDE"
t_estado = pygame.time.get_ticks()
verde_on = True
t_parp = pygame.time.get_ticks()
parpadeos = 0


def carro(x, y, angulo):
    # Superficie transparente para dibujar el carro
    carro_surface = pygame.Surface((100, 60), pygame.SRCALPHA)

    # Cuerpo del carro
    pygame.draw.rect(carro_surface, RED, (10, 10, 80, 30))
    pygame.draw.circle(carro_surface, BLACK, (30, 40), 10)
    pygame.draw.circle(carro_surface, BLACK, (70, 40), 10)

    # Rotar carro
    carro_rotado = pygame.transform.rotate(carro_surface, -angulo)

    # Mantener el centro al rotar
    rect_rotado = carro_rotado.get_rect(center=(x + 50, y + 30))
    screen.blit(carro_rotado, rect_rotado.topleft)


def semaforo(estado, verde_on):
    pygame.draw.rect(screen, BLACK, (480, 25, 40, 100), 0)
    pygame.draw.rect(screen, BLACK, (493, 100, 15, 50), 0)

    ROJO_OFF = (60, 0, 0)
    AMAR_OFF = (80, 80, 0)
    VERD_OFF = (0, 60, 0)

    if estado == "ROJO":
        pygame.draw.circle(screen, RED, (500, 50), 10)
    else:
        pygame.draw.circle(screen, ROJO_OFF, (500, 50), 10)

    if estado == "AMARILLO":
        pygame.draw.circle(screen, YELLOW, (500, 75), 10)
    else:
        pygame.draw.circle(screen, AMAR_OFF, (500, 75), 10)

    if estado == "VERDE":
        pygame.draw.circle(screen, GREEN, (500, 100), 10)
    elif estado == "VERDE_PARPADEO" and verde_on:
        pygame.draw.circle(screen, GREEN, (500, 100), 10)
    else:
        pygame.draw.circle(screen, VERD_OFF, (500, 100), 10)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    ahora = pygame.time.get_ticks()

    # Lógica del semáforo
    if estado == "VERDE":
        if ahora - t_estado >= 5000:
            estado = "VERDE_PARPADEO"
            t_estado = ahora
            verde_on = True
            t_parp = ahora
            parpadeos = 0

    elif estado == "VERDE_PARPADEO":
        if ahora - t_parp >= 300:
            verde_on = not verde_on
            t_parp = ahora

            if verde_on:
                parpadeos += 1

            if parpadeos >= 3:
                estado = "AMARILLO"
                t_estado = ahora

    elif estado == "AMARILLO":
        if ahora - t_estado >= 3000:
            estado = "ROJO"
            t_estado = ahora

    elif estado == "ROJO":
        if ahora - t_estado >= 5000:
            estado = "VERDE"
            t_estado = ahora

    # Movimiento del carro
    if tramo == "horizontal":
        angulo_carro = 0

        if x > SCREEN_WIDTH:
            x = -80
            y = 190
            tramo = "horizontal"
            velocidad = 0
            angulo_carro = 0

        if (estado == "ROJO" or estado == "AMARILLO") and x < 380:
            if velocidad > 2:
                velocidad -= 0.05
            x += velocidad

        elif (estado == "ROJO" or estado == "AMARILLO") and 380 <= x < 460:
            velocidad = 0

        else:
            if velocidad < 5:
                velocidad += 0.02
            x += velocidad

        # Entrada a la curva
        if x >= 1260:
            x = 1260
            tramo = "curva"
            angulo_curva = -math.pi / 2

    elif tramo == "curva":
        centro_x = 1350
        centro_y = 545
        radio = 345

        if velocidad < 5:
            velocidad += 0.02

        Vel_angular += velocidad / radio

        x = centro_x + radio * math.cos(Vel_angular) - 40
        y = centro_y + radio * math.sin(Vel_angular) - 15

        # Giro visual del carro en la curva
        angulo_carro = math.degrees(Vel_angular) + 90

        if Vel_angular >= 0:
            tramo = "vertical"
            x = 1655
            y = 530
            angulo_carro = 90

    elif tramo == "vertical":
        angulo_carro = 90

        if velocidad < 5:
            velocidad += 0.02

        y += velocidad

        if y > SCREEN_HEIGHT:
            x = 0
            y = 190
            tramo = "horizontal"
            angulo_carro = 0

    # Dibujo
    screen.fill(WHITE)

    semaforo(estado, verde_on)

    # Calle horizontal
    pygame.draw.rect(screen, GRIS, (0, 150, 1350, 100))

    # Bordes rectos
    pygame.draw.rect(screen, YELLOW_Ivana, (0, 145, 1350, 5))
    pygame.draw.rect(screen, YELLOW_Ivana, (0, 250, 1350, 5))

    # Curva
    pygame.draw.arc(screen, YELLOW_Ivana, (950, 145, 800, 800), 0, 1.57, 5)
    pygame.draw.arc(screen, GRIS, (955, 150, 790, 790), 0, 1.57, 100)
    pygame.draw.arc(screen, YELLOW_Ivana, (1055, 250, 590, 590), 0, 1.57, 5)
    pygame.draw.arc(screen, WHITE, (1002, 197, 695, 695), 0, 1.57, 5)

    # Parte vertical
    pygame.draw.rect(screen, YELLOW_Ivana, (1745, 545, 5, 500))
    pygame.draw.rect(screen, GRIS, (1645, 545, 100, 500))
    pygame.draw.rect(screen, YELLOW_Ivana, (1640, 545, 5, 500))

    # Líneas verticales del centro
    for j in range(555, 1045, 90):
        pygame.draw.rect(screen, WHITE, (1690, j, 5, 40), 0)

    # Línea de alto
    pygame.draw.rect(screen, WHITE, (460, 150, 5, 100))

    # Líneas horizontales del centro
    for i in range(10, 1350, 90):
        pygame.draw.rect(screen, WHITE, (i, 195, 40, 5), 0)

    # Carro
    carro(int(x), int(y), angulo_carro)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()