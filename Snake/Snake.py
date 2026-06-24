import pygame
import random
import sys

pygame.init()

#Colors
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)

#Creating window
screen_width = 600
screen_height = 600
gameWindow = pygame.display.set_mode((screen_width, screen_height))

#Game Title
pygame.display.set_caption("Snake Game")
pygame.display.update()

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 40)

#Draw
def plot_snake(gameWindow, color, snake_list, snake_size):
    for x,y in snake_list:
        pygame.draw.rect(gameWindow, black, [x, y, snake_size, snake_size])

def show_message(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x, y])
    return


#Game Loop
def gameloop():

    #Game Specific Variables
    exit_game = False
    game_over = False

    velocity_x = 0
    velocity_y = 0

    snake_x = 45
    snake_y = 55

    food_x = random.randint(20,screen_width//2)
    food_y = random.randint(20,screen_height//2)

    score = 0
    snake_size = 10
    fps = 30

    snake_list = []
    snake_length = 1
    
    while not exit_game:
        if game_over:
            gameWindow.fill(white)
            show_message("Game Over! Press Enter To Continue", red, 50, 250)

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        gameloop()

                
        else:
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    exit_game = True


                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = 10
                        velocity_y = 0
                    
                    if event.key == pygame.K_LEFT:
                        velocity_x = - 10
                        velocity_y = 0
                    
                    if event.key == pygame.K_UP:
                        velocity_y = - 10
                        velocity_x = 0
                    
                    if event.key == pygame.K_DOWN:
                        velocity_y = 10
                        velocity_x = 0

            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y

            if abs(snake_x - food_x)<8 and abs(snake_y - food_y)<8:
                score += 10
                snake_length += 5
                
                food_x = random.randint(20,screen_width//2)
                food_y = random.randint(20,screen_height//2)


            gameWindow.fill(white)
            show_message("Score: " + str(score), red, 250, 5)
            
            head = []
            head.append(snake_x)
            head.append(snake_y)
            snake_list.append(head)

            if len(snake_list) > snake_length:
                del snake_list[0]

            if head in snake_list[: -1]:
                game_over = True

            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                game_over = True

            
            plot_snake(gameWindow, black, snake_list, snake_size)
            
            pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size])
        pygame.display.update()
        clock.tick(fps)


    pygame.quit()
    sys.exit()


gameloop()
