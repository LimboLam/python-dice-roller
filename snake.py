import pygame
import sys
import random

def main():
    pygame.init()
    width, height = (800, 600)
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

    apple = Apple(random.randrange(0, width, 20), random.randrange(0, height, 20), 20, (255, 0, 0))
    goldApp = Apple(random.randrange(0, width, 20,), random.randrange(0, height, 20), 20, (166, 135, 16))
    voidApp = Apple(random.randrange(0, width, 20,), random.randrange(0, height, 20), 20, (13, 0, 34))
    snakeHead = Snake(width / 2, height / 2, 20, (0, 255, 0))
    snakeBod = {}
    score = 0
    font = pygame.font.Font(None, 36)
    scoreSurface = font.render(f'Score: {score}', True, (255, 255, 255))
    scoreRect = scoreSurface.get_rect(center = (75, 40))
    overTopSurface = font.render('Game Over', True, (255, 255, 255))
    overTopRect = overTopSurface.get_rect(center = (width / 2, 200))
    overBotSurface = font.render('Press R to restart or Q to quit', True, (255, 255, 255))
    overBotRect = overBotSurface.get_rect(center = (width / 2, 450))
    nameSurface = font.render('SNAKE BUT BETTER', True, (0, 255, 0))
    nameRect = nameSurface.get_rect(center = (width / 2, 200))
    startSurface = font.render('Press Enter to start', True, (255, 255, 255))
    startRect = startSurface.get_rect(center = (width / 2, 450))
    counter = 0
    snakePosX = [width / 2]
    snakePosY = [height / 2]
    eatGapple = False
    dead = False
    start = True

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
                if event.key == pygame.K_a or pygame.K_LEFT:
                    if direction == 'right':
                        direction = 'right'
                    else:
                        direction = 'left'
                elif event.key == pygame.K_w or pygame.K_UP:
                    if direction == 'down':
                        direction = 'down'
                    else:
                        direction = 'up'
                elif event.key == pygame.K_s or pygame.K_DOWN:
                    if direction == 'up':
                        direction = 'up'
                    else:
                        direction = 'down'
                elif event.key == pygame.K_d or pygame.K_RIGHT:
                    if direction == 'left':
                        direction = 'left'
                    else:
                        direction = 'right'

            if start:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        start = False

            if dead:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        apple = Apple(random.randrange(0, width, 20), random.randrange(0, height, 20), 20, (255, 0 ,0))
                        goldApp = Apple(random.randrange(0, width, 20,), random.randrange(0, height, 20), 20, (166, 135, 16))
                        snakeHead = Snake(width / 2, height / 2, 20, (0, 255, 0))
                        snakeBod = {}
                        score = 0
                        font = pygame.font.Font(None, 36)
                        scoreSurface = font.render(f'Score: {score}', True, (255, 255, 255))
                        scoreRect = scoreSurface.get_rect(center = (75, 40))
                        overTopSurface = font.render('Game Over', True, (255, 255, 255))
                        overTopRect = overTopSurface.get_rect(center = (width / 2, 250))
                        overBotSurface = font.render('Press R to restart or Q to quit', True, (255, 255, 255))
                        overBotRect = overBotSurface.get_rect(center = (width / 2, 550))
                        counter = 0
                        snakePosX = [width / 2]
                        snakePosY = [height / 2]
                        eatGapple = False
                        direction = None
                        speed = 20
                        dead = False
                    elif event.key == pygame.K_q:
                        running = False
        
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
                apple = Apple(random.randrange(0, width, 20), random.randrange(0, height, 20), 20, (255, 0 ,0))
                for bod in snakeBod:
                    if snakeBod[bod].x == apple.x:
                        if snakeBod[bod].y == apple.y:
                            apple = Apple(random.randrange(0, width, 20), random.randrange(0, height, 20), 20, (255, 0 ,0))
                if random.random() < 0.1:
                    eatGapple = True
                    goldApp = Apple(random.randrange(0, width, 20), random.randrange(0, height, 20), 20, (166, 135,16))
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
                scoreSurface = font.render(f'Score: {score}', True, (255, 255, 255))
                counter += 1

        if snakeHead.x == goldApp.x:
            if snakeHead.y == goldApp.y:
                repeat = 0
                if random.random() <= 0.1:
                    eatGapple = True
                    goldApp = Apple(random.randrange(0, width, 20,), random.randrange(0, height, 20), 20, (166, 135, 16))
                else:
                    eatGapple = False
                    goldApp = Apple(-40, -40, 20, (166, 135, 16))
                score += 3
                if direction == 'left':
                    while repeat < 3:
                        snakeBod[counter] = Snake(snakeBod.get(counter - 1).x + 20, snakeBod.get(counter - 1).y, 20, (0, 255, 0))
                        repeat += 1
                        counter += 1
                elif direction == 'right':
                    while repeat < 3:
                        snakeBod[counter] = Snake(snakeBod.get(counter - 1).x - 20, snakeBod.get(counter - 1).y, 20, (0, 255, 0))
                        repeat += 1
                        counter += 1
                elif direction == 'up':
                    while repeat < 3:
                        snakeBod[counter] = Snake(snakeBod.get(counter - 1).x, snakeBod.get(counter - 1).y + 20, 20, (0, 255, 0))
                        repeat += 1
                        counter += 1
                elif direction == 'down':
                    while repeat < 3:
                        snakeBod[counter] = Snake(snakeBod.get(counter - 1).x, snakeBod.get(counter - 1).y - 20, 20, (0, 255, 0))
                        repeat += 1
                        counter += 1
                repeat = 0
                scoreSurface = font.render(f'Score: {score}', True, (255, 255, 255))

        if snakeHead.x == voidApp.x:
            if snakeHead.y == voidApp.y:
                if score < 50:
                    voidApp = Apple(random.randrange(0, width, 20,), random.randrange(0, height, 20), 20, (13, 0, 34))
                    score = round(score / 2)
                    scoreSurface = font.render(f'Score: {score}', True, (255, 255, 255))

        if snakeHead.x > width:
            dead = True
        elif snakeHead.x < 0:
            dead = True
        elif snakeHead.y > height:
            dead = True
        elif snakeHead.y < 0:
            dead = True
        for snake in snakeBod:
            if snakeHead.x == snakeBod[snake].x:
                if snakeHead.y == snakeBod[snake].y:
                    dead = True

        if start:
            screen.fill((0, 0, 0))
            screen.blit(nameSurface, nameRect)
            screen.blit(startSurface, startRect)
        elif dead:
            screen.fill((0, 0, 0))
            screen.blit(overTopSurface, overTopRect)
            screen.blit(overBotSurface, overBotRect)
        else:
            screen.fill((0, 0, 0))
            apple.draw(screen)
            snakeHead.draw(screen)
            if eatGapple:
                goldApp.draw(screen)
            voidApp.draw(screen)
            if len(snakeBod) > 0:
                for key in snakeBod:
                    snakeBod.get(key).draw(screen)
                    snakeBod.get(key).x = snakePosX[len(snakePosX) - key - 1]
                    snakeBod.get(key).y = snakePosY[len(snakePosY) - key - 1]
            screen.blit(scoreSurface, scoreRect)
        pygame.display.flip()
            
    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()