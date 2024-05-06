import pygame
import time
import random

# Initialize Pygame
pygame.init()

# Set the dimensions of the screen
width = 800
height = 800
block_size = 20

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)

# Set up the display
game_display = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake")

clock = pygame.time.Clock()

font_style = pygame.font.SysFont(None, 50)

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    game_display.blit(mesg, [(width - mesg.get_width()) / 2, (height - mesg.get_height()) / 2])


def game_loop():
    game_over = False
    game_close = False

    # Initial position of the snake
    x_snake = width / 2
    y_snake = height / 2

    # Initial speed and direction of the snake
    x_change = 0
    y_change = 0

    # Initial position of the food
    x_food = round(random.randrange(0, width - block_size) / 20.0) * 20.0
    y_food = round(random.randrange(0, height - block_size) / 20.0) * 20.0

    snake_list = []
    snake_length = 1

    while not game_over:

        while game_close:
            game_display.fill(black)
            message("Game Over! Press Q to Quit or C to Continue", green)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -block_size
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = block_size
                    y_change = 0
                elif event.key == pygame.K_UP:
                    x_change = 0
                    y_change = -block_size
                elif event.key == pygame.K_DOWN:
                    x_change = 0
                    y_change = block_size

        if x_snake >= width or x_snake < 0 or y_snake >= height or y_snake < 0:
            game_close = True

        x_snake += x_change
        y_snake += y_change
        game_display.fill(black)
        pygame.draw.rect(game_display, green, [x_food, y_food, block_size, block_size])

        snake_head = []
        snake_head.append(x_snake)
        snake_head.append(y_snake)
        snake_list.append(snake_head)

        if len(snake_list) > snake_length:
            del snake_list[0]

        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_close = True

        # Draw the snake
        for segment in snake_list:
            pygame.draw.rect(game_display, white, [segment[0], segment[1], block_size, block_size])

        pygame.display.update()

        if x_snake == x_food and y_snake == y_food:
            x_food = round(random.randrange(0, width - block_size) / 20.0) * 20.0
            y_food = round(random.randrange(0, height - block_size) / 20.0) * 20.0
            snake_length += 1

        clock.tick(10)

    pygame.quit()
    quit()

game_loop()
