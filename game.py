import pygame
import random

class Game:
    def __init__(self,background_img,cardback):
        self.background = pygame.image.load(background_img).convert_alpha()
        self.cardback = pygame.image.load(cardback).convert_alpha()
        self.cardslist = []
        self.deck = []
        self.deckrect = self.cardback.get_rect(center = (37.5,35))
        self.discard = []
        for i in range(8):
            i+=2
            cardname = "card_clubs_0"
            cardname += str(i)
            self.cardslist.append(Card(f"imgs\\cards\\{cardname}.png",i,"clubs"))
        self.cardslist.append(Card(f"imgs\\cards\\card_clubs_10.png",10,"clubs"))
        self.cardslist.append(Card(f"imgs\\cards\\card_clubs_A.png",1,"clubs"))
        self.cardslist.append(Card(f"imgs\\cards\\card_clubs_J.png",11,"clubs"))
        self.cardslist.append(Card(f"imgs\\cards\\card_clubs_Q.png",12,"clubs"))
        self.cardslist.append(Card(f"imgs\\cards\\card_clubs_K.png",13,"clubs"))
        for i in range(8):
            i+=2
            cardname = "card_hearts_0"
            cardname += str(i)
            self.cardslist.append(Card(f"imgs\\cards\\{cardname}.png",i,"hearts"))
        self.cardslist.append(Card(f"imgs\\cards\\card_hearts_10.png",10,"hearts"))
        self.cardslist.append(Card(f"imgs\\cards\\card_hearts_A.png",1,"hearts"))
        self.cardslist.append(Card(f"imgs\\cards\\card_hearts_J.png",11,"hearts"))
        self.cardslist.append(Card(f"imgs\\cards\\card_hearts_Q.png",12,"hearts"))
        self.cardslist.append(Card(f"imgs\\cards\\card_hearts_K.png",13,"hearts"))
        for card in self.cardslist:
            self.deck.append(card)
    def resize_images(self):
        self.background = pygame.transform.scale(self.background,(1024,720))
        self.cardback = pygame.transform.scale(self.cardback,(100,200))
        self.deckrect = self.cardback.get_rect(center = (87.5,140))

    def show_background(self,screen):
        screen.blit(self.background,(0,0))
    
    def showdeck(self,screen):
        if self.deck != []:
            screen.blit(self.cardback,(37.5,35))

    def updatecards(self,screen):
        for card in self.cardslist:
            card.update()
            screen.blit(card.img,(card.x,card.y))
            #pygame.draw.rect(screen, "black", pygame.Rect(card.rect))
        #pygame.draw.rect(screen, "black", pygame.Rect(self.deckrect))
    
    def deckshuffle(self):
        for i in range(len(self.discard)):
            self.deck.append(self.discard.pop)
        random.shuffle(self.deck)

    def drawcard(self):
        if self.deck == []:
            self.deckshuffle()
        card = self.deck.pop()
        card.indeck = False
        card.x = 147.5
        card.y = 35

    def checkvalid(self,card):
        validpositions = [(90,380),(220,380),(360,380),(480,380),(620,380),(760,380),(880,380)]

class Card:
    def __init__(self,img,value,suit):
        self.img = pygame.image.load(img).convert_alpha()
        self.img = pygame.transform.scale(self.img,(150,200))
        self.value = value
        self.x = 0
        self.y = 0
        self.suit = suit
        self.indeck = True
        self.rect = self.img.get_rect(center = (self.x+150,self.y-200))
    
    def update(self):
        if self.indeck:
            self.x = 999
            self.y = 999
        self.rect = self.img.get_rect(center = (self.x+75,self.y+100))

    def __repr__(self) -> str:
        return (f"Card: {self.value} of {self.suit}")
