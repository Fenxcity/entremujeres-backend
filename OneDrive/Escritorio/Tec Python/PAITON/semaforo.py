import pygame

SCREEN_WIDTH, SCREEN_HEIGHT = 1000, 300
WHITE  = (255, 255, 255)
BLACK  = (  0,   0,   0)
GREEN  = (  0, 200,   0)
YELLOW = (230, 200,   0)
RED    = (220,   0,   0)
GRIS = (176, 176, 176)
YELLOW_Ivana = (237,194,50)

pygame.init()
pygame.display.set_caption("Traffic simple")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

running = True
clock = pygame.time.Clock()


estado = "VERDE"          
t_estado = pygame.time.get_ticks()

verde_on = True            
t_parp = pygame.time.get_ticks()
parpadeos = 0              

def semaforo(estado, verde_on):
    pygame.draw.rect(screen, BLACK, (480, 25, 40, 100), 0)
    pygame.draw.rect(screen, BLACK, (493,100, 15, 50), 0)
    ROJO_OFF = (60, 0, 0)
    AMAR_OFF = (80, 80, 0)
    VERD_OFF = (0, 60, 0)
    # rojo
    if estado == "ROJO":
        pygame.draw.circle(screen, RED, (500, 50), 10)
    else:
        pygame.draw.circle(screen, ROJO_OFF, (500, 50), 10)
    # amarillo
    if estado == "AMARILLO":
        pygame.draw.circle(screen, YELLOW, (500, 75), 10)
    else:
        pygame.draw.circle(screen, AMAR_OFF, (500, 75), 10)
    # verde (normal o parpadeando)
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

    # --- Sección lógica del semáforo ---
    if estado == "VERDE":
        if ahora - t_estado >= 10000:     # 10 segundos de tiempo en verde
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

            if parpadeos >= 3:  # 3 veces
                estado = "AMARILLO"
                t_estado = ahora

    elif estado == "AMARILLO":
        if ahora - t_estado >= 3000:      # 3 segundos en amarillo
            estado = "ROJO"
            t_estado = ahora

    elif estado == "ROJO":
        if ahora - t_estado >= 10000:     # 10 segundos en rojo
            estado = "VERDE"
            t_estado = ahora

    
    screen.fill(WHITE)

    semaforo(estado, verde_on)

    
    pygame.draw.rect(screen, GRIS, (0, 150, 1000, 100), 0)
    pygame.draw.rect(screen, YELLOW_Ivana, (0, 145, SCREEN_WIDTH, 5), 0)
    pygame.draw.rect(screen, YELLOW_Ivana, (0, 250, SCREEN_WIDTH, 5), 0)

    for x in range(10, SCREEN_WIDTH, 90):
        pygame.draw.rect(screen, WHITE, (x, 195, 40, 5), 0)

    pygame.display.flip()
    clock.tick(60)  # 60 FPS para que el tiempo sea suave


pygame.quit()