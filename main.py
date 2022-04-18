import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}

class Card:

  def __init__(self, suit, rank):
    self.suit = suit
    self.rank = rank
    self.value = values[rank]

  def __str__(self):
    return self.rank + ' of ' + self.suit

# print(suits[0])
# print(ranks[0])
two_hearts = Card(suits[0], ranks[0])

# print(two_hearts)
# print(two_hearts.rank)
# print(values[two_hearts.rank])


class Deck:

  def __init__(self):
    self.all_cards = []

    for suit in suits:
      for rank in ranks:
        self.all_cards.append(Card(suit, rank))

  def shuffle(self):
    random.shuffle(self.all_cards)

  def deal_one(self):
    return self.all_cards.pop()


my_deck = Deck()
# print(len(my_deck.all_cards))

# print(my_deck.all_cards[0])
my_deck.shuffle()
# print(my_deck.all_cards[0])

my_card = my_deck.deal_one()


class Player:

  def __init__(self, name):
    self.name = name
    self.all_cards = []

  def remove_one(self):
    return self.all_cards.pop(0)

  def add_cards(self, new_cards):
    if type(new_cards) == type([]):
      self.all_cards.extend(new_cards)
    else:
      self.all_cards.append(new_cards)

  def __str__(self):
    return 'Player {} has {} cards'.format(self.name,len(self.all_cards))


# palistha = Player("palistha")

# palistha.add_cards([two_hearts, two_hearts, two_hearts])
# print(palistha)

#game logic

p1 = Player('Jivan')
p2 = Player('Palistha')

#setup new game

new_deck = Deck()
new_deck.shuffle()

#split the deck between players

for x in range(26):
  p1.add_cards(new_deck.deal_one())
  p2.add_cards(new_deck.deal_one())

game_on = True

#play game - logic
round_num = 0

while game_on:
  round_num += 1

  print(f"Round {round_num}")

  #check to see if player is out of cards

  if len(p1.all_cards) == 0:
    print("Player One out of cards! Game Over")
    print("Player Two Wins!")

    game_on = False
    break

  if len(p2.all_cards) == 0:
    print("Player Two out of cards! Game Over")
    print("Player One Wins!")
    
    game_on = False
    break

  #otherwise the game is still on.... start a new round and reset current cards on the table

  player_1_cards = []
  player_1_cards.append(p1.remove_one())

  player_2_cards = []
  player_2_cards.append(p2.remove_one())

  at_war = True

  while at_war:
    if player_1_cards[-1].value > player_2_cards[-1].value:
      #player 1 gets the card
      p1.add_cards(player_1_cards)
      p1.add_cards(player_2_cards)

      at_war = False

    elif player_2_cards[-1].value > player_1_cards[-1].value:
      p2.add_cards(player_1_cards)
      p2.add_cards(player_2_cards)

      at_war = False
    else:
      print('WAR!!!!')

      # when the cards are equal
      #first we need to check if the player is out of cards

      if len(p1.all_cards) < 5:
        print("Player One unable to play war! Game Over at War")
        print("Player Two Wins! Player One Loses!")
        game_on = False
        break
      elif len(p2.all_cards) < 5:
        print("Player Two unable to play war! Game Over at War")
        print("Player One Wins! Player One Loses!")
        game_on = False
        break
      else:
        for num in range(5):
          player_1_cards.append(p1.remove_one())
          player_2_cards.append(p2.remove_one())
  