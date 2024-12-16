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
        self.stacks = [Stack(37.5,287.5),Stack(172.5,287.5),Stack(302.5,287.5),Stack(435.5,287.5),Stack(571,287.5),Stack(702,287.5),Stack(830,287.5)]
        self.debug = False
        self.endstacks = [EndStack(430,35,'hearts'),EndStack(561,35,"diamonds"),EndStack(695,35,"clubs"),EndStack(830,35,"spades")]
        self.gamewin = False
        self.highscore = None
        self.moves = 0
        self.font = pygame.font.SysFont(None,36)
    def start(self):
        self.moves = 0
        self.gamewin = False
        self.cardslist = []
        self.deck = []
        self.discard = []
        self.stacks = [Stack(37.5,287.5),Stack(172.5,287.5),Stack(302.5,287.5),Stack(435.5,287.5),Stack(571,287.5),Stack(702,287.5),Stack(834,287.5)]
        self.endstacks = [EndStack(430,35,'hearts'),EndStack(561,35,"diamonds"),EndStack(692.5,35,"clubs"),EndStack(827.5,35,"spades")]
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
        for i in range(8):
            i+=2
            cardname = "card_spades_0"
            cardname += str(i)
            self.cardslist.append(Card(f"imgs\\cards\\{cardname}.png",i,"spades"))
        self.cardslist.append(Card(f"imgs\\cards\\card_spades_10.png",10,"spades"))
        self.cardslist.append(Card(f"imgs\\cards\\card_spades_A.png",1,"spades"))
        self.cardslist.append(Card(f"imgs\\cards\\card_spades_J.png",11,"spades"))
        self.cardslist.append(Card(f"imgs\\cards\\card_spades_Q.png",12,"spades"))
        self.cardslist.append(Card(f"imgs\\cards\\card_spades_K.png",13,"spades"))
        for i in range(8):
            i+=2
            cardname = "card_diamonds_0"
            cardname += str(i)
            self.cardslist.append(Card(f"imgs\\cards\\{cardname}.png",i,"diamonds"))
        self.cardslist.append(Card(f"imgs\\cards\\card_diamonds_10.png",10,"diamonds"))
        self.cardslist.append(Card(f"imgs\\cards\\card_diamonds_A.png",1,"diamonds"))
        self.cardslist.append(Card(f"imgs\\cards\\card_diamonds_J.png",11,"diamonds"))
        self.cardslist.append(Card(f"imgs\\cards\\card_diamonds_Q.png",12,"diamonds"))
        self.cardslist.append(Card(f"imgs\\cards\\card_diamonds_K.png",13,"diamonds"))
        for card in self.cardslist:
            self.deck.append(card)
            card.visible = False
        self.deckshuffle()
        self.dealer()

    def resize_images(self):
        self.background = pygame.transform.scale(self.background,(1024,720))
        self.cardback = pygame.transform.scale(self.cardback,(100,200))
        self.deckrect = self.cardback.get_rect(center = (87.5,140))

    def show_background(self,screen):
        screen.blit(self.background,(0,0))
    
    def showdeck(self,screen):
        if self.deck != []:
            screen.blit(self.cardback,(37.5,35))

    def updatecards(self,screen,movingcard=None):
        for stack in self.stacks:
            stack.update(screen)
            #pygame.draw.rect(screen, "black", pygame.Rect(stack.rect))
        for card in self.cardslist:
            if card.moving and self.debug:
                print(f"{card} is moving")
            card.update()
            if card.instack == None and card not in self.discard:
                if card.visible and not card.moving:
                    screen.blit(card.img,(card.x,card.y))
                else:
                    screen.blit(card.back,(card.x,card.y))
            #pygame.draw.rect(screen, "black", pygame.Rect(card.rect))
        #pygame.draw.rect(screen, "black", pygame.Rect(self.deckrect))
        for stack in self.endstacks:
            stack.update(screen)
        for stack in self.stacks:
            stack.update(screen)
        if self.discard != []:
            for i in self.discard:
                if not i.moving:
                    i.x = 2000
                    i.y = 2000
                i.visible = False
                i.moveable = False
            if len(self.discard) > 1:
                card = self.discard[-2]
                card.x = 147.5
                card.y = 35
                screen.blit(card.img,(card.x,card.y))
                self.discard[-2].visible = True
            self.discard[-1].moveable = True
            self.discard[-1].visible = True
            card = self.discard[-1]
            if not card.moving:
                    card.x = 147.5
                    card.y = 35
            screen.blit(card.img,(card.x,card.y))
        if movingcard:
            screen.blit(movingcard.img,(movingcard.x,movingcard.y))
            for card in movingcard.cardsontop:
                screen.blit(card.img,(card.x,card.y))
        self.gamewin = True
        for stack in self.endstacks:
            if stack.nextValue != 14:
                self.gamewin = False
    
        
    def deckshuffle(self):
        for card in self.discard:
            self.deck.append(card)
            card.indeck = True
            card.visbile = False
            card.moveable = False
        self.discard = []
        random.shuffle(self.deck)

    def drawcard(self,stack=None):
      if self.debug:
          print(f"Deck clicked, drawing card from these: {self.deck}")
          print(f"Cards in discard: {self.discard}")
      try:
        if self.deck == []:
            self.deckshuffle()
            print("Deck shuffled")
        else:
            card = self.deck.pop()
            card.indeck = False
            card.visible = False
            card.x = 147.5
            card.y = 35
            if self.debug:
                print(f"{card} removed from deck")
        if stack:
            stack.cards.append(card)
            card.instack = stack
            if self.debug:
                print(f"{card} added to stack")
        else:
            self.discard.append(card)
            if self.debug:
                print(f"added {card} to discard")
      except:
          if self.debug:
              print("error in card draw")

    def checkvalid(self,card):
        valid = False
        for stack in self.stacks:
            if card.rect.colliderect(stack.rect):
                if self.debug:
                    print("collided with stack")
                if card.value == stack.nextValue:
                    if self.debug:
                        print('correct value')
                        print(f"color is {card.suit}, stack wants {stack.nextColor}")
                    if card.suit == "spades" or card.suit == "clubs":
                        if stack.nextColor == "black" or stack.nextValue == 13:
                            if self.debug:
                                print("correct color")
                            stack.nextColor = "red"
                            if card.instack:
                                card.instack.cards.pop()
                                stack.cards.append(card)
                                card.instack = stack
                                if self.debug:
                                    print(f"added {card} to stack")
                                for card2 in card.cardsontop:
                                    card2.instack.cards.pop()
                                    card2.instack = stack
                                    stack.cards.append(card2)
                                    if self.debug:
                                        print(f"added {card2} to stack")
                            else:
                                self.discard.pop()
                                stack.cards.append(card)
                                if self.debug:
                                    print(f"added {card} to stack")
                                card.instack = stack
                            valid = True
                    if card.suit == "hearts" or card.suit == "diamonds":
                        if stack.nextColor == "red" or stack.nextValue == 13:
                            if self.debug:
                                print("correct color")
                            stack.nextColor = "black"
                            if card.instack:
                                card.instack.cards.pop()
                                stack.cards.append(card)
                                card.instack = stack
                                if self.debug:
                                    print(f"added {card} to stack")
                                for card2 in card.cardsontop:
                                    card2.instack.cards.pop()
                                    card2.instack = stack
                                    stack.cards.append(card2)
                                    if self.debug:
                                        print(f"added {card2} to stack")
                            else:
                                self.discard.pop()
                                stack.cards.append(card)
                                if self.debug:
                                    print(f"added {card} to stack")
                                card.instack = stack
                            valid = True
        for stack in self.endstacks:
            if card.rect.colliderect(stack.rect):
                if self.debug:
                    print("collided with endstack")
                if card.value == stack.nextValue and card.suit == stack.nextColor and card.cardsontop == []:
                    if card.instack:
                        card.instack.cards.pop()
                    else:
                        self.discard.pop()
                    stack.cards.append(card)
                    card.x = stack.x-70
                    card.y = stack.y
                    card.instack = stack
                    valid = True
                else:
                  if self.debug:
                    if card.value != stack.nextValue:
                        print(f"Wrong value, stack wants {stack.nextValue}")
                    if card.suit != stack.nextColor:
                        print(f"Wrong suit, stack wants {stack.nextColor}")
                    if card.cardsontop != []:
                        print(f"Card has cards on top of it")
        if valid:
            for card in self.cardslist:
                card.cardsontop = []
        for card in self.cardslist:
            card.moving = False
        return valid

    def showmoves(self,screen):
        score_surface = self.font.render(str(self.moves)+ " moves", True, (0,0,0))
        score_rect = score_surface.get_rect(center = (340,50))
        screen.blit(score_surface,score_rect)
        high = self.font.render("High score:", True, (0,0,0))
        high_rect = high.get_rect(center = (355,100))
        screen.blit(high,high_rect)
        if self.highscore:
            highscore = self.font.render(str(self.highscore) + " moves", True, (0,0,0))
            highscore_rect = highscore.get_rect(center = (340,125))
            screen.blit(highscore,highscore_rect)
        else:
            highscore = self.font.render("Not played", True, (0,0,0))
            highscore_rect = score_surface.get_rect(center = (340,125))
            screen.blit(highscore,highscore_rect)
        restart = self.font.render("Press space", True, (0,0,0))
        restart_rect = restart.get_rect(center = (355,170))
        screen.blit(restart,restart_rect)
        restart2 = self.font.render("to restart",True,(0,0,0))
        restart2_rect = restart2.get_rect(center = (340,195))
        screen.blit(restart2,restart2_rect)

    def dealer(self):
        for num,stack in enumerate(self.stacks):
            num += 1
            for i in range(num):
                self.drawcard(stack)
        for i in self.cardslist:
            i.visible = False
            i.moveable = False
        for stack in self.stacks:
            stack.cards.sort()

    def won(self,screen):
        if not self.highscore:
            self.highscore = 9999999
        if self.moves < self.highscore:
            self.highscore = self.moves
        wintext = pygame.font.SysFont(None,128).render("You won!", True, (0,0,0))
        wintext_rect = wintext.get_rect(center = (480,512))
        screen.blit(wintext,wintext_rect)
        playagaintext = pygame.font.SysFont(None,64).render("Press space to play again.", True, (0,0,0))
        playagaintext_rect = playagaintext.get_rect(center = (480,700))
        screen.blit(playagaintext,playagaintext_rect)



class Stack:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.img = pygame.image.load("imgs\\stack-back.png").convert_alpha()
        self.img = pygame.transform.scale(self.img,(100,200))
        self.rect = pygame.Rect(self.x, self.y, 100, 500)
        self.cards = []
        self.nextValue = 13
        
        self.nextColor = "any"
    
    def update(self,screen):
        x = self.x - 25
        y = self.y
        for cardnum,card in enumerate(self.cards):
            if not card.moving:
                card.x = x
                card.y = y
                y += 50
                toppagelist = []
                for card2 in self.cards[cardnum+1:]:
                    toppagelist.append(card2)
                card.cardsontop = toppagelist
        x += 25
        self.rect = pygame.Rect(self.x, self.y, 100, ((len(self.cards)+1)*50)+100)
        #screen.blit(pygame.Surface((self.rect.width,self.rect.height)),(self.x,self.y))
        if self.cards != []:
            self.nextValue = self.cards[-1].value -1   
            self.cards[-1].visible = True
            if self.cards[-1].suit == "hearts" or self.cards[-1].suit == "diamonds":
                self.nextColor = "black"
            else:
                self.nextColor = "red"
        else:
            self.nextValue = 13
            self.nextColor = "any"
        for card in self.cards:
            card.smallhitbox = True
            self.cards[-1].smallhitbox = False
            if card.visible:
              if not card.moving:
                screen.blit(card.img,(card.x,card.y))
                card.moveable = True
                #screen.blit(pygame.Surface((card.rect.width,card.rect.height)),(card.x,card.y))
            else:
                screen.blit(card.back,(card.x+25,card.y))
                card.moveable = False
        

class EndStack(Stack):
    def __init__(self, x, y,type):
        super().__init__(x, y)
        self.nextColor = type
        self.nextValue = 1
    
    def update(self,screen):
        self.rect = self.img.get_rect(center = (self.x,self.y))
        #screen.blit(pygame.Surface((self.rect.width,self.rect.height)),(self.x,self.y))
        for card in self.cards:
            card.visible = False
            card.moveable = False
            card.x = self.x - 25
            card.y = self.y
        if self.cards != []:
            self.nextValue = self.cards[-1].value+1
            self.cards[-1].visible = True
            if not self.cards[-1].moving:
                screen.blit(self.cards[-1].img,(self.x-15,self.y))
            
            

class Card:
    def __init__(self,img,value,suit):
        self.cardsontop = []
        self.img = pygame.image.load(img).convert_alpha()
        self.img = pygame.transform.scale(self.img,(150,200))
        self.back = pygame.image.load("imgs\\card-back.png").convert_alpha()
        self.back = pygame.transform.scale(self.back,(100,200))
        self.value = value
        self.x = 0
        self.y = 0
        self.suit = suit
        self.visible = True
        self.indeck = True
        self.rect = self.img.get_rect(center = (self.x+150,self.y-200))
        self.instack = None
        self.moving = False
        self.moveable = False
        self.smallhitbox = False

    def __lt__(self,other):
        if self.value < other.value:
            return True
        else:
            return False
    
    def update(self):
        if self.indeck:
            self.x = 999
            self.y = 999
        if self.smallhitbox:
            self.rect = pygame.Rect(self.x+25, self.y, 100, 50)
        else:
            self.rect = self.img.get_rect(center = (self.x+75,self.y+100))
        
        if self.cardsontop != []:
            y = self.y
            for card in self.cardsontop:
              if not card.moving:
                y += 50
                card.x = self.x
                card.y = y
        if not self.visible:
            self.moveable = False
        if self.moving:
            y = self.y
            for card in self.cardsontop:
                y += 50
                card.moving = True
                card.x = self.x
                card.y = y

    def __repr__(self) -> str:
        return (f"Card: {self.value} of {self.suit}")
