import pygame
import sys
import random

def main():
    pygame.init()
    width, height = (1280, 720)
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Snake")

    class Snake(pygame.sprite.Sprite):
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

    class Apple(pygame.sprite.Sprite):
        def __init__(self, x, y, size, color):
            self.x = x
            self.y = y
            self.color = color
            self.size = size

        def draw(self, screen):
            pygame.draw.rect(screen, self.color, (self.x, self.y, self.size, self.size))

    snake = Snake(640, 360, 20, (0, 255, 0))
    snakePlus = Snake(snake.x - 20, snake.y, 20, (0, 255, 0))
    apple = Apple(random.randrange(0, 1280, 20), random.randrange(0, 720, 20), 20, (255, 0 ,0))

    clock = pygame.time.Clock()

    running = True
    speed = 20
    direction = None
    
    while running:
        clock.tick(15)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    direction = 'left'
                if event.key == pygame.K_w:
                    direction = 'up'
                if event.key == pygame.K_s:
                    direction = 'down'
                if event.key == pygame.K_d:
                    direction = 'right'

        if direction == 'left':
            snake.move(-speed, 0)
        elif direction == 'up':
            snake.move(0, -speed)
        elif direction == 'down':
            snake.move(0, speed)
        elif direction == 'right':
            snake.move(speed, 0)

        if snake.x == apple.x:
            if snake.y == apple.y:
                twenty = 20
                apple = Apple(random.randrange(0, 1280, 20), random.randrange(0, 720, 20), 20, (255, 0 ,0))
                # if direction == 'left':
                #     snakePlus = Snake(snake.x + twenty, snake.y, twenty, (0, 255, 0))
                # elif direction == 'right':
                #     snakePlus = Snake(snake.x - twenty, snake.y, twenty, (0, 255, 0))
                # elif direction == 'up':
                #     snakePlus = Snake(snake.x, snake.y - twenty, twenty, (0, 255, 0))
                # elif direction == 'down':
                #     snakePlus = Snake(snake.x, snake.y + twenty, twenty, (0, 255, 0))
                twenty += 20

        if snake.x > width:
            running = False
        elif snake.x < 0:
            running = False
        elif snake.y > height:
            running = False
        elif snake.y < 0:
            running = False

        screen.fill((0, 0, 0))
        snake.draw(screen)
        snakePlus.draw(screen)
        apple.draw(screen)
        pygame.display.flip()
            
    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()