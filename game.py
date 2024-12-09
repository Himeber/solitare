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
        self.stacks = [Stack(37.5,287.5),Stack(172.5,287.5),Stack(302.5,287.5),Stack(435.5,287.5),Stack(571,287.5),Stack(702,287.5),Stack(830,287)]
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
            if card.visible:
                screen.blit(card.img,(card.x,card.y))
            else:
                screen.blit(card.back,(card.x,card.y))
            #pygame.draw.rect(screen, "black", pygame.Rect(card.rect))
        #pygame.draw.rect(screen, "black", pygame.Rect(self.deckrect))
        for stack in self.stacks:
            stack.update()
            screen.blit(stack.img,(stack.x,stack.y))
            #pygame.draw.rect(screen, "black", pygame.Rect(stack.rect))
    
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
        for stack in self.stacks:
            if card.rect.collidepoint(stack.rect):
                if card.value == stack.nextValue:
                    if card.suit == "spade" or card.suit == "club":
                        pass


class Stack:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.img = pygame.image.load("imgs\\card-back.png").convert_alpha()
        self.img = pygame.transform.scale(self.img,(100,200))
        self.rect = self.img.get_rect(center = (self.x+50,self.y+100))
        self.cards = []
        self.nextValue = 13
        self.nextColor = "any"
    
    def update(self):
        self.rect = self.img.get_rect(center = (self.x+50,self.y+100))


class Card:
    def __init__(self,img,value,suit):
        self.img = pygame.image.load(img).convert_alpha()
        self.img = pygame.transform.scale(self.img,(150,200))
        self.back = pygame.image.load("imgs\\card-back.png").convert_alpha()
        self.back = pygame.transform.scale(self.img,(150,200))
        self.value = value
        self.x = 0
        self.y = 0
        self.suit = suit
        self.visible = True
        self.indeck = True
        self.rect = self.img.get_rect(center = (self.x+150,self.y-200))
        self.instack = None
    
    def update(self):
        if self.indeck:
            self.x = 999
            self.y = 999
        self.rect = self.img.get_rect(center = (self.x+75,self.y+100))


    def __repr__(self) -> str:
        return (f"Card: {self.value} of {self.suit}")
