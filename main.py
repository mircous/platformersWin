import pygame

#init pygame!!
pygame.init()

#display-is obieqtis gaketeba zomaze
screen = pygame.display.set_mode((920, 800))
pygame.display.set_caption("My platformer Game")

#suratis chatvirtva!
background_img = pygame.image.load("start_screen.png")

#gilakis gaketeba zomaze da suratis mimagreba!
start_btn_img = pygame.image.load("start_button.png")
button_width = 200
button_height = 100
start_btn_img = pygame.transform.scale(start_btn_img, (button_width, button_height))
start_btn_rect = start_btn_img.get_rect()
start_btn_rect.center = (400, 400)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if start_btn_rect.collidepoint(mouse_pos):
                print("Start button clicked!!!") # aq dawer shens logikas ra unda mmoxdes startze dacherisas
    #screen image-is chveneba
    screen.blit(background_img, (0, 0))

    #achvene start button-i
    screen.blit(start_btn_img, start_btn_rect)

    #ganaxleba monitoris
    pygame.display.flip()

pygame.quit()

