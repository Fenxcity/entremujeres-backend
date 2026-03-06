import pygame

SCREEN_WIDTH, SCREEN_HEIGHT = 400, 300
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

pygame.init()

pygame.display.set_caption("Traffic simple")

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(WHITE)

    pygame.draw.rect(screen, BLUE, (200, 150, 20, 12), 0)

    pygame.display.flip()
    clock.tick(8)

pygame.quit()