# Instructions on how to install pygame on Windows 11 with a new version of Python are in this conversation
# https://gemini.google.com/share/763e5d1b8a21

import pygame
import time
import random

# Initialize pygame
pygame.init()

# Define screen dimensions
width = 600
height = 400
display = pygame.display.set_mode((width, height))
pygame.display.set_caption('Classic Snake Game')

# Define colors (R, G, B)
black = (0, 0, 0)
white = (255, 255, 255)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Define game variables
clock = pygame.time.Clock()
snake_block = 10  # The size of the snake and food blocks
snake_speed = 15  # Frames per second

# Set up fonts
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

def display_score(score):
    """Renders the current score on the screen."""
    value = score_font.render("Score: " + str(score), True, white)
    display.blit(value, [0, 0])

def draw_snake(snake_block, snake_list):
    """Draws each segment of the snake's body."""
    for x in snake_list:
        pygame.draw.rect(display, green, [x[0], x[1], snake_block, snake_block])

def display_message(msg, color):
    """Displays the game over message."""
    mesg = font_style.render(msg, True, color)
    display.blit(mesg, [width / 6, height / 3])

def game_loop():
    """Main function containing the game loop."""
    game_over = False
    game_close = False

    # Starting coordinates for the snake (center of screen)
    x1 = width / 2
    y1 = height / 2

    # Change in coordinates
    x1_change = 0
    y1_change = 0

    snake_list = []
    length_of_snake = 1

    # Spawn the first apple randomly (aligned to the 10-pixel grid)
    foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0

    while not game_over:

        # Screen shown when the player loses
        while game_close:
            display.fill(black)
            display_message("You Lost! Press Q-Quit or C-Play Again", red)
            display_score(length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop() # Restart the game

        # Event handling (keyboard inputs)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                # Prevent the snake from reversing directly into itself
                if event.key == pygame.K_LEFT and x1_change == 0:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT and x1_change == 0:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP and y1_change == 0:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN and y1_change == 0:
                    y1_change = snake_block
                    x1_change = 0

        # Boundary collision check
        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True

        # Update snake head coordinates
        x1 += x1_change
        y1 += y1_change
        display.fill(blue) # Background color
        
        # Draw the apple
        pygame.draw.rect(display, red, [foodx, foody, snake_block, snake_block])
        
        # Update snake body
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        
        # Keep the snake list the same size as the snake's length
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        # Self-collision check
        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        draw_snake(snake_block, snake_list)
        display_score(length_of_snake - 1)

        pygame.display.update()

        # Check if the snake ate the food
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
            length_of_snake += 1

        # Control the speed of the game
        clock.tick(snake_speed)

    pygame.quit()
    quit()

if __name__ == "__main__":
    game_loop()