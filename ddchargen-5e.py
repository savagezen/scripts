# /usr/bin/python
# Character Generator for Dungeons and Dragons 5e

# Imports
import random
import math
import itertools

# Lists and Dictionaries
races = [
  "Dwarf",
  "Mountain Dwarf",
  "Hill Dwarf",
  "Elf",
  "Wood Elf",
  "High Elf",
  "Drow",
  "Halfling",
  "Lightfoot Halfling",
  "Stout Halfling",
  "Human",
  "Dragonborn",
  "Gnome",
  "Forest Gnome",
  "Half-Elf",
  "Half-Orc",
  "Tiefling"
]

avg_stats = [
  "   Race        Hieght  Weight        Lifespan",
  "   ====        ======  ======        ========",
  "   Dwarf:      4-5'    150 lbs.      350 years",
  "   Elf:        5-6'+   150-170 lbs.  750 years",
  "   Halfling:   3-4'    40 lbs.       150 years",
  "   Human:      5-6'    130-200 lbs.  < 100 years",
  "   Dragonborn: > 6'    250 lbs.      < 100 years",
  "   Gnome:      3-4'    40 lbs.       350 years",
  "   Half-Elf:   5-6'    130-170 lbs.  180 years",
  "   Half-Orc:   5-6'+   150-230 lbs.  < 80 years",
  "   Tiefling:   5-6'    130-200 lbs.  100 years"
]

classes = [
  "Barbarian",
  "Bard",
  "Cleric",
  "Druid",
  "Fighter",
  "Monk",
  "Paladin",
  "Ranger",
  "Rogue",
  "Sorcerer",
  "Warlock",
  "Wizard"
  ]
  
abilities = [
  "   Strength:      natural athleticism, bodily power",
  "   Dexterity:     physical agility, reflexes, balance, poise",
  "   Constitution:  health, stamina, vital force",
  "   Intelligence:  mental acuity, information recall, analytical skill",
  "   Wisdom:        awareness, intuition, insight",
  "   Charisma:      confidence, eloquence, leadership",
  ]

# Functions
def start():
  print('#############################################')
  print('D&D 5e Character Generator by Austin Haedicke')
  print('#############################################')
  print('-- Feel Free to Use, Edit, and Distribute! --')
  print('')
  print('          (R)oll Dice                        ')
  print('          (C)reate Charcter                  ')
  print('')
  option = input('What would you like to do? ')
  if option in ('R', 'r'):
    dice = int(input('How many dice? '))
    sides = int(input('How many sides on each die? '))
    for _ in itertools.repeat(None, dice):
      print(random.randrange(1,sides))
  elif option in ('C', 'c'):
    pass
  else:
    start()

def race_fn():
  global char_race
  print('Available Races Include:')
  for race in races:
    print(race)
  char_race = input('Enter Your Race: ')
  if char_race in races:
    pass
  else:
    print('Race not available')
    race_fn()

def class_fn():
  def choose_class():
    global char_class
    print('Available Classes for the', char_race, 'Class Inclue:')
    for char_class in classes:
      print(char_class)
    char_class = input('Enter Your Class: ')
    if char_class not in classes:
      print('Class not available')
      choose_class()
    else:
      pass
  choose_class()
  
def misc_fn():
  global char_heightft
  global char_heightin
  global char_weight
  global char_gender
  global char_age
  print('Now we need to select some miscelaneous stats:')
  for entry in avg_stats:
    print(entry)
  print('The race you selected was', char_race)
  height = int(input('Enter Your Height in Total Inches (12 in / foot): '))
  char_weight = int(input('Enter Your Weight in Pounds (lbs): '))
  char_age = int(input('Enter Your Age: '))
  char_gender = input('Enter Your Gender: ')
  char_heightft = math.trunc(height/12)
  char_heightin = height % 12

def name_fn():
  global char_name
  global plyr_name
  plyr_name = input('Enter Player Name: ')
  char_name = input('Enter Character Name: ')

def abilities_fn():
  def stat_roll():
	    d1 = random.randrange(1,6)
	    d2 = random.randrange(1,6)
	    d3 = random.randrange(1,6)
	    d4 = random.randrange(1,6)
	    raw_rolls = [d1,d2,d3,d4]
	    sorted_rolls = sorted(raw_rolls)
	    del sorted_rolls[0]
	    total = sum(sorted_rolls)
	    return total
  def strength():
    global abl_str
    abl_str = int(input('Enter the score to use for Strength: '))
    if abl_str not in abl_scores:
      print('Score not valid')
      strength()
    else:
      abl_scores.remove(abl_str)
  def dexterity():
	  print('Remaining Scores: ', abl_scores)
	  global abl_dex
	  abl_dex = int(input('Enter the score to use for Dexterity: '))
	  if abl_dex not in abl_scores:
	     print('Score not valid')
	     dexterity()
	  else:
	     abl_scores.remove(abl_dex)
  def constitution():
	  print('Remaining Scores: ', abl_scores)
	  global abl_con
	  abl_con = int(input('Enter the score to use for Constitution: '))
	  if abl_con not in abl_scores:
	    print('Score not valid')
	    constitution()
	  else:
	     abl_scores.remove(abl_con)
  def intelligence():
	  print('Remaining Scores: ', abl_scores)
	  global abl_int
	  abl_int = int(input('Enter the score to use for Intelligence: '))
	  if abl_int not in abl_scores:
	    print('Score not valid')
	    intelligence()
	  else:
	    abl_scores.remove(abl_int)
  def wisdom():
	  print('Remaining Scores: ', abl_scores)
	  global abl_wis
	  abl_wis = int(input('Entere the score to use for Wisdom: '))
	  if abl_wis not in abl_scores:
	    print('Score not valid')
	    wisdom()
	  else:
	    abl_scores.remove(abl_wis)
  def charisma():
	  print('Remaining Scores: ', abl_scores)
	  global abl_cha
	  abl_cha = int(input('Enter the score to use for Charisma: '))
	  if abl_cha not in abl_scores:
	    print('Score not valid')
	    charisma()
	  else:
	    abl_scores.remove(abl_cha)
  def assign():
    strength()
    dexterity()
    constitution()
    intelligence()
    wisdom()
    charisma()
  print('Now we need to roll and assign the 6 ability scores.')
  score1 = stat_roll()
  score2 = stat_roll()
  score3 = stat_roll()
  score4 = stat_roll()
  score5 = stat_roll()
  score6 = stat_roll()
  abl_scores = [score1,score2,score3,score4,score5,score6]
  print('Your Rolles Scores Are: ', abl_scores)
  reroll = input('Do You Want to [C]ontinue or [R]eroll? ')
  if reroll in ('C', 'c', 'Continue', 'continue'):
    assign()
    print('The Scores You Assigned Were:')
    print('   Strength: ', abl_str)
    print('   Dexterity: ', abl_dex)
    print('   Constitution: ', abl_con)
    print('   Intelligence: ', abl_int)
    print('   Wisdom: ', abl_wis)
    print('   Charisma: ', abl_cha)
    choice = input('Do you want to (C)ontinue, Re(A)ssign, or (R)eroll? ')
    if choice in ('R', 'r', 'Reroll', 'reroll'):
      abilities_fn()
    elif choice in ('A', 'a', 'Reassign', 'reassign', 'ReAssign'):
      assign()
    else:
      pass
  else:
    abilities_fn()

def race_bonus_fn():
  global abl_str
  global abl_dex
  global abl_con
  global abl_int
  global abl_wis
  global abl_cha
  print('Specific races give bonuses to certain ability scores.')
  print('The race you selected was: ', char_race,)
  print('Checking for Strength Bonus...')
  if char_race in ('Mountain Dwarf', 'Dragonborn', 'Half-Orc', 'Human'):
    print('   ... you got a bonus!')
    if char_race == 'Human':
      abl_str = abl_str + 1
    else:
      abl_str = abl_str + 2
  else:
    pass
  print('Checking for Dexterity Bonus...')
  if char_race in ('Elf', 'Wood Elf', 'High Elf', 'Drow', 'Halfling', 'Lightfoot Halfling', 'Forest Gnome', 'Human'):
    print('   ... you got a bonus!')
    if char_race == 'Human':
      abl_dex = abl_dex + 1
    else:
      abl_dex = abl_dex + 2
  else:
    pass
  print('Checking for Constitution Bonus...')
  if char_race in ('Dwarf', 'Mountain Dwarf', 'Hill Dwarf', 'Stout Halfling', 'Rock Gnome', 'Half-Orc', 'Human'):
    print('   ... you got a bonus!')
    if char_race in ('Dwarf', 'Mountain Dwarf', 'Hill Dwarf'):
      abl_con = abl_con + 2
    else:
      abl_con = abl_con + 1
  else:
    pass
  print('Checking for Intelligence Bonus...')
  if char_race in ('High Elf', 'Gnome', 'Forest Gnome', 'Tiefling', 'Human'):
    print('   ... you got a bonus!')
    if char_race in ('Gnome', 'Forest Gnome'):
      abl_int = abl_int + 2
    else:
      abl_int = abl_int + 1
  else:
    pass
  print('Checking for Wisdom Bonus...')
  if char_race in ('Hill Dwarf', 'Wood Elf', 'Human'):
    print('   ... you got a bonus!')
    abl_wis = abl_wis + 1
  else:
    pass
  print('Checking for Charisma Bonus...')
  if char_race in ('Half-Elf', 'Drow', 'Lightfoot Halfling', 'Dragonborn', 'Human', 'Tiefling'):
    print('   ... you got a bonus!')
    if char_race in ('Half-Elf', 'Tiefling'):
      abl_cha = abl_cha + 2
    else:
      abl_cha = abl_cha + 2
  else:
    pass

def modifiers_fn():
  global mod_str
  global mod_dex
  global mod_con
  global mod_int
  global mod_wis
  global mod_cha
  global char_ac
  global prim_stat
  global atk_bonus
  print('Each ability score provides a modier score which benefits certain attributes.')
  def mod(ability):
    if ability == 1:
      mod = -5
      return mod
    elif ability in (2,3):
      mod = -4
      return mod
    elif ability in (4,5):
      mod = -3
      return mod
    elif ability in (6,7):
      mod = -2
      return mod
    elif ability in (8,9):
      mod = -1
      return mod
    elif ability in (10,11):
      mod = +0
      return mod
    elif ability in (12,13):
      mod = 1
      return mod
    elif ability in (14,15):
      mod = 2
      return mod
    elif ability in (16,17):
      mod = 3
      return mod
    elif ability in (18,10):
      mod = 4
      return mod
    elif ability in (20,21):
      mod = 5
      return mod
    elif ability in (22,23):
      mod = 6
      return mod
    elif ability in (24,25):
      mod = 7
      return mod
    elif ability in (26,27):
      mod = 8
      return mod
    elif ability in (28,29):
      mod = 9
      return mod
    elif ability == 30:
      mod = 10
      return mod
    else:
      pass
  mod_str = mod(abl_str)
  mod_dex = mod(abl_dex)
  mod_con = mod(abl_con)
  mod_int = mod(abl_int)
  mod_wis = mod(abl_wis)
  mod_cha = mod(abl_cha)
  char_ac = mod_dex + 10
  print('Here are your Ability Scores and (Modifier):')
  print('   Armor Class ', char_ac)
  print('   Strength    ', mod_str)
  print('   Dexterity   ', mod_dex)
  print('   Constitution', mod_con)
  print('   Intelligence', mod_int)
  print('   Wisdom      ', mod_wis)
  print('   Charisma    ', mod_cha)
  print('Each character also gets an atck modifier based on their proficiency bonus + main stat modifier')
  print('The proficiency bonus for Lvl 1 characters is 2')
  print('Your class is: ', char_class, '. Calculating attack bonus...')
  if char_class in ('Barbarian'):
    prim_stat = 'Strength'
  elif char_class in ('Bard', 'Sorcerer', 'Warlock'):
    prim_stat = 'Charisma'
  elif char_class in ('Cleric', 'Druid'):
    prim_stat = 'Wisdom'
  elif char_class == 'Fighter':
    prim_stat = input('Choose (S)trength or (D)exterity: ')
    if prim_stat in ('S', 's', 'Strength', 'strength'):
      prim_stat = 'Strength'
    elif prim_stat in ('D', 'd', 'Dexterity', 'dexterity'):
      prim_stat = 'Dexterity'
    else:
      print('Choice not valid')
      modifiers_fn()
  elif char_class in ('Monk', 'Ranger'):
    prim_stat = input('Choose (D)exterity or (W)isdom: ')
    if prim_stat in ('D', 'd', 'Dexterity', 'dexterity'):
      prim_stat = 'Dexterity'
    elif prim_stat in ('W', 'w', 'Wisdom', 'wisdom'):
      prim_stat = 'Wisdom'
    else:
      print('Choice not valid')
      modifiers_fn()
  elif char_class == 'Paladin':
    # str or cha
    prim_stat = input('Choose between (S)trength and (C)harisma: ')
    if prim_stat in ('S', 's', 'Strength', 'strength'):
      prim_stat = 'Strength'
    elif prim_stat in ('C', 'c', 'Charisma', 'charisma'):
      prim_stat = 'Charisma'
  elif char_class == 'Rogue':
    prim_stat = 'Dexterity'
  else:
    # Wizard
    prim_stat = 'Intelligence'
  if prim_stat == 'Strength':
    atk_bonus = mod_str + 2
  if prim_stat == 'Dexterity':
    atk_bonus = mod_dex + 2
  if prim_stat == 'Intelligence':
    atk_bonus = mod_int + 2
  if prim_stat == 'Wisdom':
    atk_bonus = mod_wis + 2
  if prim_stat == 'Charisma':
    atk_bonus = mod_cha + 2
  print('Your primary stat is: ', prim_stat)
  print('Your attack bonus is: ', atk_bonus)
  
def hp_fn():
  global char_hp
  print('Now we need to calculate hit points.')
  if char_class in ('Barbarian'):
    hit_die = random.randint(1,12)
    char_hp = mod_con + hit_die
    print('You scored ', char_hp, ' hit points')
  elif char_class in ('Fighter', 'Paladin', 'Ranger'):
    hit_die = random.randint(1,10)
    char_hp = mod_con + hit_die
    print('You scored ', char_hp, ' hit points')
  elif char_class in ('Wizard', 'Sorcerer'):
    hit_die = random.randint(1,6)
    char_hp = mod_con + hit_die
    print('You scored ', char_hp, ' hit points')
  else:
    hit_die = random.randint(1,8)
    char_hp = mod_con + hit_die
    print('You scored ', char_hp, ' hit points')
  
def alignment_fn():
  def lawchaos():
    global align_lawchaos
    align_lawchaos = input('Choose (L)awful, (C)haotic, or (N)eutral: ')
    if align_lawchaos in ('L', 'l', 'Lawful', 'lawful'):
      align_lawchaos = 'Lawful'
    elif align_lawchaos in ('C', 'c', 'Chaotic', 'chaotic'):
      align_lawchaos = 'Chaotic'
    elif align_lawchaos in ('N', 'n', 'Neutral', 'neutral'):
      align_lawchaos = 'Neutral'
    else:
      print('Invalid choice')
      lawchaos()
  def goodevil():
    global align_goodevil
    align_goodevil = input('Choose (G)ood, (E)vil, or (N)eutral: ')
    if align_goodevil in ('G', 'g', 'Good', 'good'):
      align_goodevil = 'Good'
    elif align_goodevil in ('E', 'e', 'Evil', 'evil'):
      align_goodevil = 'Evil'
    elif align_goodevil in ('N', 'n', 'Neutral', 'neutral'):
      align_goodevil = 'Neutral'
    else:
      print('Invalid choice')
      goodevil()
  def cont():
    choice = input('Is this correct? (y/n) ')
    if choice in ('Y', 'y', 'Yes', 'yes'):
      pass
    elif choice in ('N', 'n', 'No', 'no'):
      alignment_fn()
    else:
      cont()
  print('Finally choose an alignment.')
  lawchaos()
  goodevil()
  print('The alignment you chose is ', align_lawchaos, '-', align_goodevil)
  cont()

def summary_fn():
  print('##########################################')
  print('#                Summary                 #')
  print('##########################################')
  print(plyr_name, "'s: ", char_race, '-', char_class)
  print(char_name)
  print('##########################################')
  print('Height:         ', char_heightft, "'", char_heightin, '"')
  print('Weight:         ', char_weight, 'lbs.')
  print('Age:            ', char_age, 'years old')
  print('Gender:         ', char_gender)
  print('Alignment:      ', align_lawchaos, '-', align_goodevil)
  print('##########################################')
  print('Max Hit Points: ', char_hp)
  print('Armor Class:    ', char_ac)
  print('Attack Bonus:   ', atk_bonus)
  print('Primary Stat:   ', prim_stat)
  print('##########################################')
  print('Strength:       ', abl_str,  '(', mod_str, ')')
  print('Dexterity:      ', abl_dex,  '(', mod_dex, ')')
  print('Constitution:   ', abl_con,  '(', mod_con, ')')
  print('Intelligence:   ', abl_int,  '(', mod_int, ')')
  print('Wisdom:         ', abl_wis,  '(', mod_wis, ')')
  print('Charisma:       ', abl_cha,  '(', mod_cha, ')')
  
# Script
start()
race_fn()
class_fn()
misc_fn()
name_fn()
abilities_fn()
race_bonus_fn()
modifiers_fn()
hp_fn()
alignment_fn()
summary_fn()