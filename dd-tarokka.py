# /usr/bin/python

# Dnd Version 5e
# Tarokka Deck Fortune Telling Game
# used by Madam Eva in Curse of Strahd

# imports
import random

# lists and dictionaries

card_deck = [
  'Hooded One (7)    ',
  'Enchanter (3)     ',
  'Shepherd (4)      ',
  'Tempter           ',
  'Raven             ',
  'Seer              ',
  'Swashbuckler (1)  ',
  'Executioner       ',
  'Ghost             ',
  'Warrior           ',
  'Tax Collector (8) ',
  'Anarchist (6)     ',
  'Marionette        ',
  'Miser (9)         ',
  'Torturer (9)      ',
  'Priest            ',
  'Traitor (9)       ',
  'Paladin (2)       ',
  'Thief (7)         ',
  'Beast             ',
  'Guild Member (5)  ',
  'Healer (3)        ',
  'Darklord          ',
  'Myrmidon (5)      ',
  'Elementalist (5)  ',
  'Diviner (2)       ',
  'Abjurer (4)       ',
  'Artifact          ',
  'Avenger (1)       ',
  'Beggar (6)        ',
  'Beserker (6)      ',
  'Bishop (8)        ',
  'Broken One        ',
  'Charlatan (7)     ',
  'Conjurer (9)      ',
  'Dictator (8)      ',
  'Donjon            ',
  'Druid (5)         ',
  'Evoker (6)        ',
  'Horseman          ',
  'Illusionist (7)   ',
  'Innocent          ',
  'Missionary (2)    ',
  'Mists             ',
  'Monk (1)          ',
  'Necromancer (8)   ',
  'Philanthropist (2)',
  'Rogue             ',
  'Soldier (3)       ',
  'Trader (3)        ',
  'Transmuter (1)    ',
  'Wizard            ',
  'Mercenary (4)     ',
  'Merchant (4)      '
]

# functions

def draw_cards_fn():
  global drawn_cards
  drawn_cards = random.sample(card_deck, 5)

  global pos_1
  global pos_2
  global pos_3
  global pos_4
  global pos_5

  pos_1 = random.choice(drawn_cards)
  drawn_cards.remove(pos_1)

  pos_2 = random.choice(drawn_cards)
  drawn_cards.remove(pos_2)

  pos_3 = random.choice(drawn_cards)
  drawn_cards.remove(pos_3)

  pos_4 = random.choice(drawn_cards)
  drawn_cards.remove(pos_4)

  pos_5 = random.choice(drawn_cards)
  drawn_cards.remove(pos_5)

def reveal_cards_fn():
  print("         |--------|")
  print("         |        |")
  print("         | Card 2 |")
  print("         |        |")
  print("|--------|--------|--------|")
  print("|        |        |        |")
  print("| Card 1 | Card 5 | Card 3 |")
  print("|        |        |        |")
  print("|--------|--------|--------|")
  print("         |        |")
  print("         | Card 4 |")
  print("         |        |")
  print("         |--------|")

  print("")
  print("Card 1 - ", pos_1)
  print("The Tome of Strahd (location): This card tells of history.  Knowledge of the ancient will help you better understand your enemy")

  print("")
  print("Card 2 - ", pos_2)
  print("The Holy Symbol of Ravenkind (location):  This card tells of a powerful force for good and protection, a symbol of great hope")

  print("")
  print("Card 3 - ", pos_3) 
  print("The Sunsword (location):  This is a card of power and strength.  It tells of a weapon of vengeance:  a sword of sunlight")

  print("")
  print("Card 4 - ", pos_4)
  print("Strahd's Enemy (where to find an ally:  This card sheds light on one who will help you greatly in the battle against darkness")

  print("")
  print("card 5 - ", pos_5)
  print("Strahd (location):  Your enemy is a creature of darkness, whose powers are beyond mortality.  This card will lead you to him")

draw_cards_fn()
reveal_cards_fn()
