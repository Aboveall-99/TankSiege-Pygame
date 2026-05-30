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
    player_1_rect.topleft = (player_1_X, player_1_Y)
    screen.blit(player_1,player_1_rect)




#player 2(left side)
player_2 = pygame.image.load("tank_2.png")
player_2_rect = player_2.get_rect()
player_2_X = 0
player_2_Y = 507

def player_2_movement():
    screen.blit(player_2,player_2_rect)


#Bullet1 (for player 1)
bullet_1 = pygame.image.load("bullet_1.png")
bullet_1_rect = bullet_1.get_rect()

bullet_1_active = False
bullet_1_x = 0
bullet_1_y = 0
bullet_1_speed = 1

#Background
background = pygame.image.load("Background.jpg").convert()

running = True


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # fire once per SPACE press (player 1)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            if not bullet_1_active:
                bullet_1_active = True
                bullet_1_x = player_1_X - 64
                bullet_1_y = player_1_Y

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        player_1_X -= 0.4

    if keys[pygame.K_RIGHT]:
        player_1_X += 0.4


    if keys[pygame.K_a]:
        player_2_X -= 0.4

    if keys[pygame.K_d]:

        player_2_X += 0.4
    
    # update bullet position (player 1)
    if bullet_1_active:
        bullet_1_x -= bullet_1_speed
        bullet_1_rect.topleft = (bullet_1_x, bullet_1_y)

        # deactivate when it leaves screen
        if bullet_1_x < -bullet_1_rect.width:
            bullet_1_active = False




    






    screen.fill((0,0,0))
    screen.blit(background,(0,0))

    # draw players
    player_1_movement()
    player_2_movement()

    # draw bullet (player 1)
    if bullet_1_active:
        bullet_1_rect.topleft = (bullet_1_x, bullet_1_y)
        screen.blit(bullet_1, bullet_1_rect)


    # bullet will be blitted in the update section above (under movement keys)






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

    # (debug) player collision
    if player_1_rect.colliderect(player_2_rect):
        pass




    pygame.display.update()
