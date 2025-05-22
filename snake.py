import pygame
import sys
import random

def main():
    pygame.init()
    width, height = (1280, 720)
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Snake")

    class Snake:
        def __init__(self, x, y, size, color):
            self.x = x
            self.y = y
            self.color = color
            self.size = size

        def draw(self, screen):
            pygame.draw.rect(screen, self.color, (self.x, self.y, self.size, self.size))

        def move(self, dx, dy):
            self.x += dx
            self.y += dy

    class Apple:
        def __init__(self, x, y, size, color):
            self.x = x
            self.y = y
            self.color = color
            self.size = size

        def draw(self, screen):
            pygame.draw.rect(screen, self.color, (self.x, self.y, self.size, self.size))

    snake = Snake(640, 360, 20, (0, 255, 0))
    apple = Apple(random.randrange(0, 1280, 20), random.randrange(0, 720, 20), 20, (255, 0 ,0))

    clock = pygame.time.Clock()

    running = True
    speed = 5
    
    while running:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            keys = pygame.key.get_pressed()
            if keys[pygame.K_a]:
                snake.move(-speed, 0)
            if keys[pygame.K_d]:
                snake.move(speed, 0)
            if keys[pygame.K_w]:
                snake.move(0, -speed)
            if keys[pygame.K_s]:
                snake.move(0, speed)

            screen.fill((0, 0, 0))
            snake.draw(screen)
            apple.draw(screen)
            pygame.display.flip()
            
    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()