import pygame
import random

# Initialize Pygame
pygame.init()

# Define constants
WIDTH, HEIGHT = 640, 480
FPS = 10
SNAKE_SIZE = 20
FOOD_SIZE = SNAKE_SIZE
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
BRIGHT_GREEN = (0, 200, 0)
BRIGHT_RED = (200, 0, 0)

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()

def draw_snake(snake_body):
    for block in snake_body:
        pygame.draw.rect(screen, GREEN, [block[0], block[1], SNAKE_SIZE, SNAKE_SIZE])

def draw_food(food_position):
    pygame.draw.rect(screen, RED, [food_position[0], food_position[1], FOOD_SIZE, FOOD_SIZE])

def text_objects(text, font):
    textSurface = font.render(text, True, BLACK)
    return textSurface, textSurface.get_rect()

def draw_button(msg, x, y, w, h, ic, ac, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(screen, ac, (x, y, w, h))
        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(screen, ic, (x, y, w, h))

    smallText = pygame.font.SysFont("comicsansms", 20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x + (w / 2)), (y + (h / 2)))
    screen.blit(textSurf, textRect)

def quitgame():
    pygame.quit()
    quit()

def game_loop():
    running = True
    game_close = False

    # Snake initial position
    snake_x = WIDTH // 2
    snake_y = HEIGHT // 2
    snake_body = [[snake_x, snake_y]]

    # Initial food position
    food_x = round(random.randrange(0, WIDTH - SNAKE_SIZE) / SNAKE_SIZE) * SNAKE_SIZE
    food_y = round(random.randrange(0, HEIGHT - SNAKE_SIZE) / SNAKE_SIZE) * SNAKE_SIZE
    food_position = [food_x, food_y]

    x_change, y_change = 0, 0

    while running:
        while game_close:
            screen.fill(BLACK)

            largeText = pygame.font.SysFont("comicsansms", 55)
            TextSurf, TextRect = text_objects("Game Over", largeText)
            TextRect.center = ((WIDTH / 2), (HEIGHT / 2 - 50))
            screen.blit(TextSurf, TextRect)

            draw_button("Restart", 150, 350, 100, 50, GREEN, BRIGHT_GREEN, game_loop)
            draw_button("Quit", 390, 350, 100, 50, RED, BRIGHT_RED, quitgame)

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    game_close = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -SNAKE_SIZE
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = SNAKE_SIZE
                    y_change = 0
                elif event.key == pygame.K_UP:
                    y_change = -SNAKE_SIZE
                    x_change = 0
                elif event.key == pygame.K_DOWN:
                    y_change = SNAKE_SIZE
                    x_change = 0

        snake_x += x_change
        snake_y += y_change

        if snake_x >= WIDTH or snake_x < 0 or snake_y >= HEIGHT or snake_y < 0:
            game_close = True

        snake_head = [snake_x, snake_y]
        snake_body.append(snake_head)
        if len(snake_body) > 1:
            del snake_body[0]

        if snake_x == food_x and snake_y == food_y:
            food_x = round(random.randrange(0, WIDTH - SNAKE_SIZE) / SNAKE_SIZE) * SNAKE_SIZE
            food_y = round(random.randrange(0, HEIGHT - SNAKE_SIZE) / SNAKE_SIZE) * SNAKE_SIZE
            food_position = [food_x, food_y]
            snake_body.insert(0, [snake_x, snake_y])  # Grow the snake

        screen.fill(BLACK)
        draw_food(food_position)
        draw_snake(snake_body)

        pygame.display.update()
        clock.tick(FPS)

    quitgame()

game_loop()
