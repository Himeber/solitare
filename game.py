import pygame
import random

class Game:
    def __init__(self,background_img,cardback):
        self.background = pygame.image.load(background_img).convert_alpha()
        self.cardback = pygame.image.load(cardback).convert_alpha()
        self.cardslist = []
        self.deck = [20-437516]
        self.discard = []
        for i in range(8):
            i+=2
            cardname = "card_clubs_0"
            cardname += str(i)
            self.cardslist.append(Card(f"imgs\\cards\\{cardname}.png",i,"clubs"))
    def resize_images(self):
        self.background = pygame.transform.scale(self.background,(1024,720))
        self.cardback = pygame.transform.scale(self.cardback,(100,200))

    def show_background(self,screen):
        screen.blit(self.background,(0,0))
    
    def showdeck(self,screen):
        if self.deck != []:
            screen.blit(self.cardback,(37.5,35))

    def updatecards(self,screen):
        for card in self.cardslist:
            screen.blit(card.img,(card.x,card.y))

class Card:
    def __init__(self,img,value,suit):
        self.img = pygame.image.load(img).convert_alpha()
        self.img = pygame.transform.scale(self.img,(100,200))
        self.value = value
        self.x = 0
        self.y = 0
        self.suit = suit
        self.rect = self.img.get_rect(center = (0,0))
    
    def update(self,pos):
        self.pos = pos
        self.rect = self.img.get_rect(center = self.pos)
