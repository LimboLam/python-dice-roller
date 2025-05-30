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
    goldApp = Apple(random.randrange(0, 1280, 20,), random.randrange(0,720, 20), 20, (166, 135, 16))
    snakeHead = Snake(640, 360, 20, (0, 255, 0))
    snakeBod = {}
    score = 0
    font = pygame.font.Font(None, 36)
    text_surface = font.render(f'Score: {score}', True, (255, 255, 255))
    text_rect = text_surface.get_rect(center=(75, 40))
    counter = 0
    snakePosX = [640]
    snakePosY = [360]
    eatGapple = False

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
            snakeHead.move(-speed, 0)
            snakePosX.append((snakeHead.x))
            snakePosY.append((snakeHead.y))
        elif direction == 'up':
            snakeHead.move(0, -speed)
            snakePosX.append((snakeHead.x))
            snakePosY.append((snakeHead.y))
        elif direction == 'down':
            snakeHead.move(0, speed)
            snakePosX.append((snakeHead.x))
            snakePosY.append((snakeHead.y))
        elif direction == 'right':
            snakeHead.move(speed, 0)
            snakePosX.append((snakeHead.x))
            snakePosY.append((snakeHead.y))

        if snakeHead.x == apple.x:
            if snakeHead.y == apple.y:
                apple = Apple(random.randrange(0, 1280, 20), random.randrange(0, 720, 20), 20, (255, 0 ,0))
                if random.random() < 0.25:
                    eatGapple = True
                    goldApp = Apple(random.randrange(0, 1280, 20,), random.randrange(0,720, 20), 20, (166, 135, 16))
                score += 1
                if direction == 'left':
                    if len(snakeBod) == 0:
                        snakeBod[0] = Snake(snakeHead.x + 20, snakeHead.y, 20, (0, 255, 0))
                    else:
                        snakeBod[counter] = Snake(snakeBod.get(counter - 1).x + 20, snakeBod.get(counter - 1).y, 20, (0, 255, 0))
                elif direction == 'right':
                    if len(snakeBod) == 0:
                        snakeBod[0] = Snake(snakeHead.x - 20, snakeHead.y, 20, (0, 255, 0))
                    else:
                        snakeBod[counter] = Snake(snakeBod.get(counter - 1).x - 20, snakeBod.get(counter - 1).y, 20, (0, 255, 0))
                elif direction == 'up':
                    if len(snakeBod) == 0:
                        snakeBod[0] = Snake(snakeHead.x, snakeHead.y + 20, 20, (0, 255, 0))
                    else:
                        snakeBod[counter] = Snake(snakeBod.get(counter - 1).x, snakeBod.get(counter - 1).y + 20, 20, (0, 255, 0))
                elif direction == 'down':
                    if len(snakeBod) == 0:
                        snakeBod[0] = Snake(snakeHead.x, snakeHead.y - 20, 20, (0, 255, 0))
                    else:
                        snakeBod[counter] = Snake(snakeBod.get(counter - 1).x, snakeBod.get(counter - 1).y - 20, 20, (0, 255, 0))
                text_surface = font.render(f'Score: {score}', True, (255, 255, 255))
                counter += 1

        if snakeHead.x == goldApp.x:
            if snakeHead.y == goldApp.y:
                repeat = 0
                if random.random() <= 0.25:
                    eatGapple = True
                    goldApp = Apple(random.randrange(0, 1280, 20,), random.randrange(0, 720, 20), 20, (166, 135, 16))
                else:
                    eatGapple = False
                    goldApp = Apple(-40, -40, 20, (166, 135, 16))
                score += 5
                if direction == 'left':
                    while repeat < 5:
                        snakeBod[counter] = Snake(snakeBod.get(counter - 1).x + 20, snakeBod.get(counter - 1).y, 20, (0, 255, 0))
                        repeat += 1
                elif direction == 'right':
                    while repeat < 5:
                        snakeBod[counter] = Snake(snakeBod.get(counter - 1).x - 20, snakeBod.get(counter - 1).y, 20, (0, 255, 0))
                        repeat += 1
                elif direction == 'up':
                    while repeat < 5:
                        snakeBod[counter] = Snake(snakeBod.get(counter - 1).x, snakeBod.get(counter - 1).y + 20, 20, (0, 255, 0))
                        repeat += 1
                elif direction == 'down':
                    while repeat < 5:
                        snakeBod[counter] = Snake(snakeBod.get(counter - 1).x, snakeBod.get(counter - 1).y - 20, 20, (0, 255, 0))
                        repeat += 1
                repeat = 0
                text_surface = font.render(f'Score: {score}', True, (255, 255, 255))
                counter += 1


        if snakeHead.x > width:
            running = False
        elif snakeHead.x < 0:
            running = False
        elif snakeHead.y > height:
            running = False
        elif snakeHead.y < 0:
            running = False
        for snake in snakeBod:
            if snakeHead.x == snakeBod[snake].x:
                if snakeHead.y == snakeBod[snake].y:
                    running = False

        screen.fill((0, 0, 0))
        apple.draw(screen)
        snakeHead.draw(screen)
        if eatGapple == True:
            goldApp.draw(screen)
        if len(snakeBod) > 0:
            for key in snakeBod:
                snakeBod.get(key).draw(screen)
                snakeBod.get(key).x = snakePosX[len(snakePosX) - key - 1]
                snakeBod.get(key).y = snakePosY[len(snakePosY) - key - 1]
        screen.blit(text_surface, text_rect)
        pygame.display.flip()
            
    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()