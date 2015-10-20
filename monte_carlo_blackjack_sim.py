#!/usr/bin/env python2.7

from __future__ import division
import itertools
from random import shuffle
import operator



class deckOfCards():
    __deck = []
    __points={1:1,2:2,3:3,4:4,5:5,6:6,7:7,8:8,9:9,10:10,11:10,12:10,13:10}
    __disp={1:'Ace',2:'Two',3:'Three',4:'Four',5:'Five',6:'Six',7:'Seven',8:'Eight',9:'Nine',10:'Ten',11:'Jack',12:'Queen',13:'King'}
    def __init__(self):
        self.__deck=list(itertools.product(range(1,14),['Spade','Heart','Diamond','Club']))
        shuffle(self.__deck, random=None)
    def hit(self):
        card=self.__deck.pop()
        return (self.__disp[card[0]],card[1],self.__points[card[0]])

class blackjackPlayer():
    __points=0
    __hitlimit=int()

    def __init__(self,hitlim=20):
        self.__hitlimit=hitlim
        self.__cards=[]
        self.__debug=[]
        self.noAces=0

    def update(self,temp):
        self.__debug.append(temp)
        self.__cards.append((temp[0],temp[1]))
        self.__points+=temp[2]
        if temp[0] == 'Ace' and self.__points <= 11 :
            self.noAces+=1
            # print "The ACE OF SPADES!!"
            self.__points+=10

    def score(self):
        return self.__points

    def shouldIHitThat(self):
        if self.__points >= self.__hitlimit:
            return False
        else:
            return True

    def show_cards(self):
        return self.__cards

    def recalc_score(self):
        if self.noAces >= 1:
            while self.noAces>0 and self.score() >21:
                self.noAces-=1
                self.__points-=10
            return 1
        else:
            return 0

def unitSimulation():
    dealer=blackjackPlayer(hitlim=17)
    player=blackjackPlayer(hitlim=20)
    cards=deckOfCards()

    dealer.update(cards.hit())
    player.update(cards.hit())

    while (True):
        print "Dealer:", dealer.score()
        print "Player:", player.score()

        if dealer.shouldIHitThat():
            dealer.update(cards.hit())

        if dealer.score() == 21:
            print "Dealer:", dealer.score()
            print "Player:", player.score()
            print "Dealer Blackjack"
            print "Dealer:", dealer.show_cards()
            print "Player:", player.show_cards()
            return (0,1,0)

        elif dealer.score() > 21:
            recalcScore=dealer.recalc_score()
            if recalcScore == 1:
                if dealer.score() > 21:
                    print "Dealer:", dealer.score()
                    print "Player:", player.score()
                    print "Dealer Busted"
                    print "Player:", player.show_cards()
                    print "Dealer:", dealer.show_cards()
                    return (1,0,0)

            elif recalcScore == 0 :
                print "Dealer:", dealer.score()
                print "Player:", player.score()
                print "Dealer Busted"
                print "Player:", player.show_cards()
                print "Dealer:", dealer.show_cards()
                return (1,0,0)

        if player.shouldIHitThat():
            player.update(cards.hit())

        if player.score() == 21:
            print "Dealer:", dealer.score()
            print "Player:", player.score()
            print "Player Blackjack!"
            print "Player:", player.show_cards()
            print "Dealer:", dealer.show_cards()
            return (1,0,0)

        elif player.score() > 21:
            recalcScore=player.recalc_score()

            if recalcScore == 1:
                if player.score() > 21:
                    print "Dealer:", dealer.score()
                    print "Player:", player.score()
                    print "Player Busted"
                    print "Player:", player.show_cards()
                    print "Dealer:", dealer.show_cards()
                    return (0,1,0)

            elif recalcScore == 0 :
                print "Dealer:", dealer.score()
                print "Player:", player.score()
                print "Player Busted"
                print "Player:", player.show_cards()
                print "Dealer:", dealer.show_cards()
                return (0,1,0)


        if dealer.shouldIHitThat() == False  and dealer.score < player.score():
            print "Dealer:", dealer.score()
            print "Player:", player.score()
            print "Player wins"
            print "Player:", player.show_cards()
            print "Dealer:", dealer.show_cards()
            return (1,0,0)

        elif player.shouldIHitThat() == False and dealer.shouldIHitThat() == False and player.score() == dealer.score():
            print "Dealer:", dealer.score()
            print "Player:", player.score()
            print "Draw!"
            print "Player:", player.show_cards()
            print "Dealer:", dealer.show_cards()
            return (0,0,1)

        elif player.shouldIHitThat() == False and dealer.shouldIHitThat() == False and player.score() < dealer.score():
            print "Dealer:", dealer.score()
            print "Player:", player.score()
            print "Dealer Wins!"
            print "Player:", player.show_cards()
            print "Dealer:", dealer.show_cards()
            return (0,1,0)

        elif player.shouldIHitThat() == False and dealer.shouldIHitThat() == False and player.score() > dealer.score():
            print "Dealer:", dealer.score()
            print "Player:", player.score()
            print "Player Wins!"
            print "Player:", player.show_cards()
            print "Dealer:", dealer.show_cards()
            return (1,0,0)

def main():
    score = (0,0,0)
    number_of_simulations=1000
    for i in range(0,number_of_simulations):
        score =tuple(map(operator.add,score, unitSimulation()))
    print score
    print "Win:", score[0]/number_of_simulations
    print "Lose:", score[1]/number_of_simulations
    print "Draw:", score[2]/number_of_simulations

if __name__ == "__main__":
    main()
