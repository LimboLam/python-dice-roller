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

    apple = Apple(random.randrange(0, 1280, 20), random.randrange(0, 720, 20), 20, (255, 0 ,0))
    snake = {0: Snake(640, 360, 20, (0, 255, 0))}
    counter = 0
    twenty = 20

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
                    if direction == 'right':
                        direction == 'right'
                    else:
                        direction = 'left'
                if event.key == pygame.K_w:
                    if direction == 'down':
                        direction == 'down'
                    else:
                        direction = 'up'
                if event.key == pygame.K_s:
                    if direction == 'up':
                        direction == 'up'
                    else:
                        direction = 'down'
                if event.key == pygame.K_d:
                    if direction == 'left':
                        direction == 'left'
                    else:
                        direction = 'right'

        if direction == 'left':
            snake.get(0).move(-speed, 0)
        elif direction == 'up':
            snake.get(0).move(0, -speed)
        elif direction == 'down':
            snake.get(0).move(0, speed)
        elif direction == 'right':
            snake.get(0).move(speed, 0)

        if snake.get(0).x == apple.x:
            if snake.get(0).y == apple.y:
                apple = Apple(random.randrange(0, 1280, 20), random.randrange(0, 720, 20), 20, (255, 0 ,0))
                counter += 1
                if direction == 'left':
                    snake[counter] = Snake(snake.get(counter - 1).x + twenty, snake.get(counter - 1).y, 20, (0, 255, 0))
                elif direction == 'right':
                    snake[counter] = Snake(snake.get(counter - 1).x - twenty, snake.get(counter - 1).y, 20, (0, 255, 0))
                elif direction == 'up':
                    snake[counter] = Snake(snake.get(counter - 1).x, snake.get(counter - 1).y + twenty, 20, (0, 255, 0))
                elif direction == 'down':
                    snake[counter] = Snake(snake.get(counter - 1).x, snake.get(counter - 1).y - twenty, 20, (0, 255, 0))

        if snake.get(0).x > width:
            running = False
        elif snake.get(0).x < 0:
            running = False
        elif snake.get(0).y > height:
            running = False
        elif snake.get(0).y < 0:
            running = False

        screen.fill((0, 0, 0))
        apple.draw(screen)
        for key in snake:
            snake.get(key).draw(screen)
        pygame.display.flip()
            
    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()