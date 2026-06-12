import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()
running = True
pos = [250, 250]
dt = 0
vel = 0
gravity = 0.3
bounce = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("#ADD8E6")
    pygame.draw.circle(screen, "orange", pos, 30)
    pygame.draw.circle(screen, "yellow", (400,65), 50)
    pygame.draw.rect(screen, "#7CFC00", (0, 480, 500, 20))
    
    vel += gravity
    pos[1] += vel

    if pos[1] >= 450:
        pos[1] = 450
        vel = -8 + bounce
        bounce += 1

    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()
