# /usr/bin/python

# D&D Version 5e
# Sorcerer Wild Magic Surge ability

# imports
import random
import math
import itertools

def roll_fn():
  global roll
  roll = random.randrange(1,100)
  if roll in (1,2):
    print("Roll on this table at the start of each of your turns for the next minute, ignoring this result on subsequent rolls")
  elif roll in (3,4):
    print("For the next minute, you can see any invisible creature if you have line of sight to it")
  elif roll in (5,6):
    print("A modron chosen and controlled by the DM appears in an unoccupied space within 5 feet of you , then disappears 1 minute later")
  elif roll in (7,8):
    print("You cast 'fireball' as 3rd-level spell centered on yourself")
  elif roll in (9,10):
    print("You cast 'magic missile' as 5th-level spell") 
  elif roll in (13,14):
    print("You cast 'confusion' centered on yourself")
  elif roll in (15,16):
    print("For the next minute, you regain 5 hit points at the start of each of your turns")
  elif roll in (17,18):
    print("You grow a long beard made of feathers that remains until you sneeze, at which point the feathers explode out from your face")
  elif roll in (19,20):
    print("You cast 'grease' centered on yourself")
  elif roll in (21,22):
    print("Creatures have disadvantage on svaing throws against the next spell you cast in the next minute that inbolbes a saving throw")
  elif roll in (23,24):
    print("Your skin turns a vibrant shade of blue.  A 'remove curse' spell can end this effect")
  elif roll in (25,26):
    print("An eye appears on your forehead for the next minute.  During that time, you have advantage on Wisdom (Perception) checks that rely on sight")
  elif roll in (27,28):
    print("For the next minute, all your spells with a casting time of 1 action have a cating time of 1 bonus action")
  elif roll in (29,30):
    print("You teleport up to 60 feet to an unoccupied space of your choice tha tyou can see")
  elif roll in (31,32):
    print("You are transported to the Astral Plan until the end of your next turn, after which time you return to the space you previously occupied or the nearest unoccupied space if that space is occupied")
  elif roll in (33,34):
    print("Maximize the damage of the next damaging spell you cast within the next minute")
  elif roll in (41,42):
    print("You turn into a potted plant until the start of your next turn.  While a plant, you are incapacitated and have vulnerability to all damage.  If you drop to 0 hit points, your pot breaks, and your form revert")
  elif roll in (43,44):
    print("For the next minute, you can teleport up to 20 feet as a bonus action on each of your turns")
  elif roll in (45,46):
    print("You cast 'levitate' on yourself")
  elif roll in (47,48):
    print("A unicorn controlled by the DM appears in a space within 5 feet of you, then disappears 1 minute later")
  elif roll in (49,50):
    print("You can't speak for the next minute.  Whenever you try, pink bubbles float out of your mouth")
  elif roll in (51,52):
    print("A spectral shield hovers near you for the next minute, granting you a +2 bonus to AC and immunity to 'magic missile'")
  elif roll in (55,56):
    print("Your hair falls out but grows back within 24 hours")
  elif roll in (57,58):
    print("For the next minute, any flammable object you touch that isn't being worn or carried by another creature bursts into flames")
  elif roll in (59,60):
    print("You regain your lowest-level expended spell slot")
  elif roll in (61,62):
    print("For the next minute, you must shout when you speak")
  elif roll in (63,64):
    print("You cast 'fog cloud' centered on yourself")
  elif roll in (67,68):
    print("You are frightened by the nearest creature until the end of your next turn")
  elif roll in (69,70):
    print("Each creature within 30 feet of you becomes invisible for the next minute.  The invisibility ends on a creature when it attacks or casts a spell")
  elif roll in (71,72):
    print("You gain resistance to all damage for the next minute")
  elif roll in (75,76):
    print("You glow with bright light in a 30-foot radius for the next minute.  Any creature that ends its turn within 5 feet of you is blinded until the end of its next turn")
  elif roll in (77,78):
    print("You cast 'polymorph' on yourself.  If you fail the saving throw, you turn into a sheep for the spell's duration")
  elif roll in (79,80):
    print("Illusory butterflies and flower petals flutter in the air within 10 feet of you for the next minute")
  elif roll in (81,82):
    print("You can take one additional action immediately")
  elif roll in (85,86):
    print("You cast 'mirror image'")
  elif roll in (87,88):
    print("You cast 'fly' on a random creature within 60 feet of you")
  elif roll in (89,90):
    print("You become invisible for the next minute.  During that time, other creatures can't hear you.  The invisibility ends if you attack or cast a spell")
  elif roll in (91,92):
    print("If you die wihtin the next minute, you immediately come back to life as if by the 'reincarnate' spell")
  elif roll in (93,94):
    print("Your size increases by one size category for the next minute")
  elif roll in (95,96):
    print("You and all creatures within 30 feet of you gain vulnerability to piercing damage for the next minute")
  elif roll in (97,98):
    print("You are surrounded by faint, ethereal music for the next minute")
  elif roll in (99,100):
    print("You regain all expended sorcery points")
  elif roll in (11,12):
    def roll_2_fn():
      roll_2 = random.randint(1,10)
      if roll_2 in (1,3,5,7,9):
        print("You shrink ",roll_2," inches")
      else:
        print("You grow ",roll_2," inches")
    roll_2_fn()
  elif roll in (35,36):
    def roll_3_fn():
      roll_3 = random.randint(1,10)
      if roll_3 in (1,3,5,7,9):
        print ("You grow ",roll_3," years younger - minimum of one year")
      else:
        print("You grow ",roll_3," years older")
    roll_3_fn()
  elif roll in (37,38):
    def roll_4_fn():
      global roll_4
      roll_4 = random.randint(1,4)
    roll_4_fn()
    print(roll_4," flumphs controlled by the DM appear in unoccupied spaces within 60 feet of you and are firghtened of you.  They vanish after 1 minute")

  elif roll in (39,40):
    def roll_5_fn():
      global roll_5
      roll_5 = random.randint(1,10)
      roll_5 = (roll_5 * 2)
    roll_5_fn()
    print("You regain ",roll_5," hit points")
  elif roll in (53,54):
    def roll_6_fn():
      global days_n
      for _ in itertools.repeat(None,5):
        days_n = random.randrange(1,6)
    roll_6_fn()
    print("You are immiune to being intoxicated by alcohol for the next ",days_n," days")
  elif roll in (65,66):
    def roll_7_fn():
      global damage
      for _ in itertools.repeat(None,4):
        damage = random.randint(1,10)
    roll_7_fn()
    print("Up to three creatures you choose within 30 feet of you take ",damage," lightning damage")
  elif roll in (73,74):
    def roll_8_fn():
      global hours
      hours = random.randint(1,4)
    roll_8_fn()
    print("A random creature within 60 feet of you becomes poisoned for ",hours," hours")
  elif roll in (83,84):
    def roll_9_fn():
      global damage
      damage = random.randint(1,10)
    roll_9_fn()
    print("Each creature within 30 feet of you takes ",damage," necrotic damage.  You regain hit points equa to the sum damage")
  else:
    pass

roll_fn()
