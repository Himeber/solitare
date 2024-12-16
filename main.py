import pygame
import sys
from game import Game

pygame.init()
screen = pygame.display.set_mode((1024,1024))
clock = pygame.time.Clock()
game = Game("imgs\\solitare_board.png","imgs\\card-back.png")
game.resize_images()
carddragging = False
cardbeinggrabbed = None
deck = game.deckrect
lastpos = 0,0
game.start()
game.debug = False
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if game.debug:
                    print(f"Click at {event.pos}")
                for card in game.cardslist:
                    if card.rect.collidepoint(event.pos) and card.moveable:
                        carddragging = True
                        cardbeinggrabbed = card
                        mouse_x, mouse_y = event.pos
                        offset_x = card.x - mouse_x
                        offset_y = card.y - mouse_y
                        if game.debug:
                            print(f"Grabbed {card}")
                        lastpos = card.x,card.y
                if cardbeinggrabbed == None:
                    if deck.collidepoint(event.pos):
                        game.drawcard()

        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:            
                carddragging = False
                if cardbeinggrabbed:
                    valid = game.checkvalid(cardbeinggrabbed)
                    if not valid:
                        card.x,card.y = lastpos
                    else:
                        game.moves += 1
                    card.moving = False
                    for card2 in card.cardsontop:
                        card2.moving = False
                cardbeinggrabbed = None

        elif event.type == pygame.MOUSEMOTION:
            if carddragging and cardbeinggrabbed:
                card = cardbeinggrabbed
                card.moving = True
                mouse_x, mouse_y = event.pos
                card.x = mouse_x + offset_x
                card.y = mouse_y + offset_y
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game.start()
        
    screen.fill((255,255,255))
    game.show_background(screen)
    game.showdeck(screen)
    game.showmoves(screen)
    game.updatecards(screen,cardbeinggrabbed)
    if game.gamewin:
        game.won(screen)
    pygame.display.update()
    clock.tick(120)