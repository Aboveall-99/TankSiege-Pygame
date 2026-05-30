import pygame

pygame.init()

screen = pygame.display.set_mode((800,600),vsync=1)
pygame.display.set_caption("Tank Siege")


#player 1(right side)

player_1 = pygame.image.load("tank_1.png")
player_1_rect = player_1.get_rect()
player_1_X = 736
player_1_Y = 510

def player_1_movement():
    screen.blit(player_1,player_1_rect)



#player 2(left side)
player_2 = pygame.image.load("tank_2.png")
player_2_rect = player_2.get_rect()
player_2_X = 0
player_2_Y = 507

def player_2_movement():
    screen.blit(player_2,player_2_rect)


#Bullet1(for player 1)

bullet_1 = pygame.image.load("bullet_1.png")
bullet_1_rect = bullet_1.get_rect()
bullet_shoot_state = "off"



#Background
background = pygame.image.load("Background.jpg").convert()



running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

            
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_1_X -= 0.4

    if keys[pygame.K_RIGHT]:
        player_1_X += 0.4

    if keys[pygame.K_a]:
        player_2_X -= 0.4

    if keys[pygame.K_d]:

        player_2_X += 0.4

    






    screen.fill((0,0,0))
    screen.blit(background,(0,0))

    player_1_movement()
    player_2_movement()





    if player_1_X >= 736:
        player_1_X = 736
    
    elif player_1_X <= 0:
        player_1_X = 0


    if player_2_X >= 736:
        player_2_X = 736
    
    if player_2_X <= 0:
        player_2_X = 0

    player_1_rect.topleft = (player_1_X, player_1_Y)
    player_2_rect.topleft = (player_2_X, player_2_Y)

    if player_1_rect.colliderect(player_2_rect):
        print("hit")



    pygame.display.update()
