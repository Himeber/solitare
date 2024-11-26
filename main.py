import pygame
import sys
from game import Game

pygame.init()
screen = pygame.display.set_mode((1024,720))
clock = pygame.time.Clock()
game = Game("imgs\\solitare_board.png","imgs\\card-back.png")
game.resize_images()
carddragging = False
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:      
                for card in game.cardslist:
                    if card.rect.collidepoint(event.pos):
                        carddragging = True
                        mouse_x, mouse_y = event.pos
                        offset_x = card.x - mouse_x
                        offset_y = card.y - mouse_y

        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:            
                carddragging = False

        elif event.type == pygame.MOUSEMOTION:
            if carddragging:
                mouse_x, mouse_y = event.pos
                card.x = mouse_x + offset_x
                card.y = mouse_y + offset_y
    
    game.show_background(screen)
    game.showdeck(screen)
    game.updatecards(screen)
    pygame.display.update()
    clock.tick(120)