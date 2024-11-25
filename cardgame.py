import random
ranks = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')
suits = ('hearts', 'diamonds', 'clubs', 'spades')
deck = [(rank, suit) for rank in ranks for suit in suits]
random.shuffle(deck)
shuffled_deck = deck
middle = 52 // 2
p1_cards = shuffled_deck[:middle]
p2_cards = shuffled_deck[middle:]

def compare_cards(p1_cards, p2_cards):
  #SHUFFLES CARDS TO INSURE IT DOESNT LOOP SAME CARDS OVER AND OVER
    random.shuffle(p1_cards)
    random.shuffle(p2_cards)
    card1 = p1_cards[0]
    card2 = p2_cards[0]
    #COMPARES CARDS TO SEE WHO GETS THEM
    if ranks.index(card1[0]) > ranks.index(card2[0]):
        print('p1 has a stronger card')
        p1_cards.append(card1)
        p1_cards.append(card2)
        p1_cards.pop(0)
        p2_cards.pop(0)
    elif ranks.index(card1[0]) < ranks.index(card2[0]):
        print('p2 has a stronger card')
        p2_cards.append(card1)
        p2_cards.append(card2)
        p1_cards.pop(0)
        p2_cards.pop(0)
    #IF TIE, ADDS 3 CARDS (on top of the tie) AND COMPARES THE FOURTH, WINNER TAKES ALL
    else:
        if len(p1_cards) >= 5 and len(p2_cards) >= 5:
            print('peaceful debate time!!')
            if ranks.index(p1_cards[4][0]) == ranks.index(p2_cards[4][0]):
                p1_cards.pop(0)
                p2_cards.pop(0)
            elif ranks.index(p1_cards[4][0]) > ranks.index(p2_cards[4][0]):
                print('p1 won the debate')
                p1_cards.extend(p1_cards[:5] + p2_cards[:5])
                del p1_cards[:5]
                del p2_cards[:5]
            else:
                print('p2 won the debate')
                p2_cards.extend(p2_cards[:5] + p1_cards[:5])
                del p1_cards[:5]
                del p2_cards[:5]
        #IF THERES NOT ENOUGH CARDS TO DEBATE, IT COMPARES THE SUIT INSTEAD
        else:
            print('Not enough cards to debate... comparing suits!')
            print(card1[1])
            print(card2[1])
            if suits.index(card1[1]) > suits.index(card2[1]):
                print('p1 has a stronger card based on suit')
                p1_cards.append(card1)
                p1_cards.append(card2)
                p1_cards.pop(0)
                p2_cards.pop(0)
            elif suits.index(card1[1]) < suits.index(card2[1]):
                print('p2 has a stronger card based on suit')
                p2_cards.append(card1)
                p2_cards.append(card2)
                p1_cards.pop(0)
                p2_cards.pop(0)
while len(p1_cards) > 0 and len(p2_cards) > 0:
    compare_cards(p1_cards, p2_cards)
if len(p1_cards) == 0:
    print("p2 has won the game!")

elif len(p2_cards) == 0:
    print("p1 has won the game!")
