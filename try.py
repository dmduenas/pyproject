import pygame
import time
import random
# Initialize Pygame
pygame.init()
# Screen dimensions
width, height = 800, 600
dis = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake Game')
# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
# Snake settings
snake_block = 10
snake_speed = 15
# Fonts
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)
# Display score
def display_score(score):
   value = score_font.render(f"Your Score: {score}", True, white)
   dis.blit(value, [0, 0])
# Draw the snake
def draw_snake(snake_block, snake_list):
   for x in snake_list:
       pygame.draw.rect(dis, green, [x[0], x[1], snake_block, snake_block])
# Game loop
def game_loop():
   game_over = False
   game_close = False
   x1, y1 = width // 2, height // 2
   x1_change, y1_change = 0, 0
   snake_list = []
   length_of_snake = 1
   foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
   foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
   clock = pygame.time.Clock()
   while not game_over:
       while game_close:
           dis.fill(black)
           message = font_style.render("Game Over! Press Q-Quit or C-Play Again", True, red)
           dis.blit(message, [width / 6, height / 3])
           display_score(length_of_snake - 1)
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
       if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
           game_close = True
       x1 += x1_change
       y1 += y1_change
       dis.fill(black)
       pygame.draw.rect(dis, blue, [foodx, foody, snake_block, snake_block])
       snake_head = [x1, y1]
       snake_list.append(snake_head)
       if len(snake_list) > length_of_snake:
           del snake_list[0]
       for block in snake_list[:-1]:
           if block == snake_head:
               game_close = True
       draw_snake(snake_block, snake_list)
       display_score(length_of_snake - 1)
       pygame.display.update()
       if x1 == foodx and y1 == foody:
           foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
           foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
           length_of_snake += 1
       clock.tick(snake_speed)
   pygame.quit()
   quit()
# Start the game
game_loop()