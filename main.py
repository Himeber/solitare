import pygame
import sys
from game import Game

pygame.init()
screen = pygame.display.set_mode((1024,720))
clock = pygame.time.Clock()
game = Game("imgs\\solitare_board.png","imgs\\card-back.png")
game.resize_images()
carddragging = False
cardbeinggrabbed = None
deck = game.deckrect
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            print(f"mousedown at {event.pos}")
            if event.button == 1:      
                for card in game.cardslist:
                    if card.rect.collidepoint(event.pos):
                        carddragging = True
                        cardbeinggrabbed = card
                        mouse_x, mouse_y = event.pos
                        offset_x = card.x - mouse_x
                        offset_y = card.y - mouse_y
                        print(f"Grabbed {card}")
                if cardbeinggrabbed == None:
                    if deck.collidepoint(event.pos):
                        game.drawcard()

        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:            
                carddragging = False
                print("let go")
                game.checkvalid(cardbeinggrabbed)
                cardbeinggrabbed = None

        elif event.type == pygame.MOUSEMOTION:
            if carddragging and cardbeinggrabbed:
                card = cardbeinggrabbed
                mouse_x, mouse_y = event.pos
                card.x = mouse_x + offset_x
                card.y = mouse_y + offset_y
    
    game.show_background(screen)
    game.showdeck(screen)
    game.updatecards(screen)
    pygame.display.update()
    clock.tick(120)