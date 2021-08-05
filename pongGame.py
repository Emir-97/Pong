import pygame, sys
pygame.init()

#Colors
black = (0, 0, 0)
white = (255, 255, 255)
screen_size = (800, 600)

screen = pygame.display.set_mode(screen_size)
clock = pygame.time.Clock()

player_width = 15
player_height = 90

#Coordenadas y velocidad del jugador 1
player1_x_coord = 60
player1_y_coord = 300 - (player_height / 2)
player1_y_speed = 0

#Coordenadas y velocidad del jugador 2

player2_x_coord = 720
player2_y_coord = 300 - (player_height / 2)
player2_y_speed = 0

#Coordenadas de la pelota

ball_x = 400
ball_y = 300
ball_x_speed = 3
ball_y_speed = 3

game_over = False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            #Player 1
            if event.key == pygame.K_w:
                player1_y_speed = -3
            if event.key == pygame.K_s:
                player1_y_speed = 3
            #Player 2
            if event.key == pygame.K_UP:
                player2_y_speed = -3
            if event.key == pygame.K_DOWN:
                player2_y_speed = 3

        if event.type == pygame.KEYUP:
            #Player 1
            if event.key == pygame.K_w:
                player1_y_speed = 0
            if event.key == pygame.K_s:
                player1_y_speed = 0

            #Player 2
            if event.key ==  pygame.K_UP:
                player2_y_speed = 0
            if event.key == pygame.K_DOWN:
                player2_y_speed = 0

    #Modify this part to give moviment to the players and the ball
    player1_y_coord += player1_y_speed
    player2_y_coord += player2_y_speed

    #Ball movements
    ball_x += ball_x_speed
    ball_y += ball_y_speed

    #Prevent it from going out of the box
    if (ball_y > 590 or ball_y < 10):
        ball_y_speed *= -1

    #Check if the ball comes out of the left or right side
    if (ball_x > 800 or ball_x < 0):
        ball_x = 400
        ball_y = 300
        #If the ball comes out, reverse the direction
        ball_x_speed *= -1
        ball_y_speed *= -1

    #Prevent it from going out of the box
    if (player1_y_coord > 500 or player1_y_coord < 0):
        player1_y_speed *= -1
    if (player2_y_coord > 500 or player2_y_coord < 0):
        player2_y_speed *= -1

    screen.fill(black)
    #Draw zone
    player1 = pygame.draw.rect(screen, white, (player1_x_coord, player1_y_coord, player_width, player_height))
    player2 = pygame.draw.rect(screen, white, (player2_x_coord, player2_y_coord, player_width, player_height))
    ball = pygame.draw.circle(screen, white, (ball_x, ball_y), 10)
    #Draw zone
    #Collisions
    if (ball.colliderect(player1) or ball.colliderect(player2)):
        ball_x_speed *= -1
        

    pygame.display.flip()
    clock.tick(60)
#Me permite salir de una manera segura de la pantalla
pygame.quit()
