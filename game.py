import pygame
import sys
import random

pygame.init()
pygame.display.set_caption("Car Game")
points = 0
window = pygame.display.set_mode((600,600))
window.fill('green')
road = pygame.Surface((200,600))
road.fill('grey')
tree1 = pygame.Surface((40,40))
tree1.fill('dark green')
car = pygame.image.load('car.png').convert_alpha()
car = pygame.transform.scale(car, (50,90))
car_rect = car.get_rect(center = (300,370))
car2 = pygame.image.load('download.png').convert_alpha()
car2 = pygame.transform.scale(car2, (90,90))
car2_rect = car2.get_rect(midbottom = (random.randint(225,375),-20))   
text = pygame.font.SysFont('Arial', 50)
text2 = pygame.font.SysFont('Arial', 20)
gameover = text.render("!! GAME OVER !!", False,'red')
retry = text.render("RESTART", False,'red')
retry_hover = text.render("RESTART", False, 'blue')  
retry_rect = retry.get_rect(center = (300,200))
clock = pygame.time.Clock()
x1 = 200
x2 = 400
x3 = 50
x4 = 550
carstop = False
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit() 
        if event.type == pygame.MOUSEBUTTONDOWN:
            if retry_rect.collidepoint(event.pos) and carstop == True:
                car2_rect = car2.get_rect(midbottom=(random.randint(225, 375), -20))
                carstop = False
                points = 0
                car_rect = car.get_rect(center=(300, 370))

    window.fill('green')        
    window.blit(road,(200,0))
    window.blit(tree1,(100,x1))  
    window.blit(tree1,(500,x2))
    window.blit(tree1,(500,x3))
    window.blit(tree1,(100,x4))
    window.blit(car,car_rect)
    window.blit(car2,(car2_rect))
    realcar = pygame.Rect(car_rect.x + 3, car_rect.y + 3, car_rect.width - 8, car_rect.height - 10)
    realcar2 = pygame.Rect(car2_rect.x + 27, car2_rect.y + 5, car2_rect.width - 55, car2_rect.height - 15)
    
    if realcar.colliderect(realcar2):
        carstop = True
        window.blit(gameover,(150,50))
        pygame.draw.rect(window, 'black', retry_rect.inflate(10,10))
        if retry_rect.collidepoint(pygame.mouse.get_pos()):
            window.blit(retry_hover, retry_rect)
        else:
            window.blit(retry,retry_rect)


    if carstop == False:          
        x1 += 2
        x2 += 2    
        x3 += 2
        x4 += 2
        car2_rect.y += 6
        if car2_rect.y > 600:
            car2_rect = car2.get_rect(midbottom = (random.randint(225,375),-20))   
            points += 1
        if x1 > 600:
            x1 = -40
        if x2 > 600:
            x2 = -40
        if x3 > 600:
            x3 = -40  
        if x4 > 600:
            x4 = -40
         
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT] and car_rect.left > 200:
            car_rect.x -= 3
        if key[pygame.K_RIGHT] and car_rect.right < 400:
            car_rect.x += 3

    score = text2.render(f'SCORE: {points}', False, 'red')
    window.blit(score, (500,500))

    
    pygame.display.update()
    clock.tick(60)
    