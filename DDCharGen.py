#!/bin/python2.7
# Dungeons & Dragons Character Generator
# Reference - http://pastebin.com/8nTb1h1U
# Refernce - http://www.ibisfightclub.co.uk/dnd/Basics.asp

# Python Imports
import random
import math

# Lists
races = [
"  Dragonborn:  Pride, Honor, Dragon-like Abilities, Mercenaries, Adventurers", 
"  Dwarf:       Tough, Strong Will, Warriors, Master Artisans", 
"  Eladrin:     Graceful, Arcane Magic, Swordplay, Metal / Stoneworking", 
"  Elf:         Kin to Eladrin, Forest Dwellers, Nature Lovers", 
"  Half-Elf:    Human/Elf Offspring, Charasmatic, Versatile", 
"  Halfling:    Quick, Likable, Small, Travelers, Traders", 
"  Human:       Brave, Ambitious", 
"  Tiefling:    Decended from human who bargained for infernal powers, Shadowy, Loners"
]

classes = [
"  Cleric:   Courageous and Devout Holy Warriors and Healers",
"  Fighter:  Armed Combat Experts Relying on Muscle, Training, and Pure Grit",
"  Paladin:  Devout Warriors, Devinely Inspired Knights",
"  Ranger:   Expert Tracker and Scout, Wilderness Warrior, Hit-and-Run Expert",
"  Rogue:    Thieves, Scoundrels, Shadowy, Larceny, Trickery",
"  Warlock:  Mysterious Powers, Curses, Energy Blasts",
"  Warlord:  Hard, Skilled in Close Combat, Brilliant Leaders",
"  Wizard:   Masters of Arcane Power, Disdain Physical Combat, Arcane Blasts"
]

avg_height = [
"  Dragonborn:  6'2\" - 6'8\"",
"  Dwarf:	    4'3\" - 4'9\"",
"  Eladrin:     5'5\" - 6'1\"",
"  Elf:         5'4\" - 6'0\"",
"  Half-elf:    5'5\" - 6'2\"",
"  Halfing:     3'10\" - 4'2\"",
"  Human:       5'6\" - 6'2\"",
"  Tiefling:    5'6\" - 6'-2\"",
]

avg_weight = [
"  Dragonborn:  220 - 230 lbs.",
"  Dwarf:       160 - 220 lbs.",
"  Elf:         130 - 170 lbs.",
"  Half-Elf:    130 - 190 lbs.",
"  Halfling:    75 - 85 lbs.",
"  Human:       135 - 220 lbs.",
"  Tiefling:    140 - 230 lbs."
]
	
roles = [
"  Controller:  Control Control and Area Offense (Wizards)",
"  Defender:    Defense, Good Close Up Offense (Fighter / Paladin)",
"  Leader:      Healing and Support, Good Defenses, Best at Protecting (Cleric / Warlord)",
"  Striker:     Focused Single-Target Offense, Mobile, Tricksters (Ranger / Rogue / Warlock)"
]

law_chaos = [
"  Law:      Honor, trust, obedience, reliabile : lack adaptability",
"  Chaos:    Freedom, adaptability, flexibility :  reckless, irresponsible",
"  Neutral:  Normal respect for authorit and neither compulsion to follow rules or rebel"
]

good_evil = [
"  Good:     Altruistic, respect for life, make personal sacrifices",
"  Evil:     Harming, opressing, killing for sport or without qualms",
"  Neutral:  Object to killing innocents but lack commitment to sacrifice and protect"
]

abilities = [
"  Strength:      Physical Power; Benefits Hand-to-Hand Fighters",
"  Constitution:  Health, Stamina, Vital Force; Benefits All Characters",
"  Dexterity:     Hand-Eye Coordination, Agility, Reflexes, and Balance",
"  Intelligence:  How Well Your Character Learns and Reasons",
"  Wisdom:        Common Sense, Perception, Self-Discipline",
"  Charisma:      Force of Personality, Persuasiveness, Leadership"
]

socials1 = ["Cheerful", "Charming", "Talkative", "Witty", "Reserved", "Relaxed"]
socials2 = ["Enthusiastic", "Grim", "Hopeful", "Self-assured", "Fatalistic", "Brooding"]
socials3 = ["Gullible", "Suspicious", "Open-minded", "Naive", "Skeptical", "Trusting"]

decisions1 = ["Humble", "Timid", "Adaptable", "Easygoing", "Commanding", "Impatient"]
decisions2 = ["Scrupulous", "Honest", "Pragmatic", "Flexible", "Dutiful", "Wild"]
decisions3 = ["Kind", "Protective", "Stern", "Hard-hearted", "Thoughtful", "Oblivious"]

straits1 = ["Brave", "Cautious", "Competitive", "Reckless", "Steady", "Fierce"]
straits2 = ["Stoic", "Vengeful", "Driven", "Bold", "Happy-go-lucky", "Impassioned"]
straits3 = ["Calm", "Impulsive", "Skittish", "Patient", "Restless", "Unshakable"]

error_msg = "Oops! Something went wrong.  Exiting..."

# Description
print "Dungeons & Dragons (4th Ed.) Character Generator"
print "	Summary"
print "	  Part 1:  General Information"
print "	  Part 2:  Ability Scores"
print "	  Part 3:  Personality"

def cont():
	cont = raw_input("Do you want to continue? y/n  ")
	if cont ==	"n" or cont == "N":
		quit()
	else:
		pass

cont()

# Name
print "Part 1 : General Information"
print "  Section 1.1 : Naming"
char_name = raw_input("	Enter Character Name:  ")
player_name = raw_input("	Enter Player's Name:  ")

# Race
print "  Section 1.2 : Race"
for race in races:
	print "	%s" % (race)
char_race = raw_input("	Enter Chosen Race:  ")

# Class
print "  Section 1.3 : Class"
for c in classes:
	print "	%s" % (c)
char_class = raw_input("	Enter Chosen Class:  ")

# Role
print "  Section 1.4 : Role / Combat Function"
print "  !!Role Availability is Limited by Character Class!!"
for role in roles:
	print "	%s" % (role)
char_role = raw_input("	Enter Chosen Role:  ")

if char_class == "Cleric" or char_class == "Warlord":
	if char_role == "Leader":
		pass
	else:
		print "Clerics and Warlords are best suited as - Leaders"
elif char_class == "Fighter" or char_class == "Paladin":
	if char_role == "Defender":
		pass
	else:
		print "Fighters and Paladins are best suited as - Defenders"
elif char_class == "Ranger" or char_class == "Rogue" or char_class == "Warlock":
	if char_role == "Striker":
		pass
	else:
		print "Rangers, Rogues, and Warlocks are best suited as - Strikers"
elif char_class == "Wizard":
	if char_role == "Controller":
		pass
	else:
		print "Wizards are best suited as - Controllers"
else:
	print error_msg

# Physical Attirbutes
print "  Section 1.5 : Physical Attributes"
gender = raw_input("	Select a Gender (Male / Female):  ")
age = int(input("	Enter Character Age:  "))

print "	Average Height per Race:"
for height in avg_height:
	print "	%s" % (height)
height = int(input("	Enter height in number of inches (6'0\" = 72 inches):  "))
height_ft = height / 12
height_ft = math.trunc(height_ft)
height_in = height % 12
print "	Character Height:  %s ' %s \"" % (height_ft, height_in)

print "	Average Weight per Race:"
for weight in avg_weight:
	print "	%s" % (weight)
wegiht = int(input("	Enter Character Weight:  "))

cont()

# Alignment
print "  Section 1.6 : Alignment (v3.5)"
for alignment in law_chaos:
	print "	%s"	% (alignment)
law_chaos_align = raw_input("Choose 1st Axis Alignment:  ")
for alignment in good_evil:
	print "	%s" % (alignment)
good_evil_align = raw_input("Choose 2nd Axis Alignment:  ")

if law_chaos_align == "Law":
	if good_evil_align == "Good":
		print "	%s 's  %s (%s - %s:%s - Lawful-Good)" % (player_name, char_name, gender, char_class, char_role)
	elif good_evil_align == "Evil":
		print "	%s 's  %s (%s - %s:%s - Lawful-Evil)" % (player_name, char_name, gender, char_class, char_role)
	elif good_evil_align == "Neutral":
		print "	%s 's  %s (%s - %s:%s - Lawful-Neutral)" % (player_name, char_name, gender, char_class, char_role)
	else:
		print error_msg
elif law_chaos_align == "Chaos":
	if good_evil_align == "Good":
		print "	%s 's  %s (%s - %s:%s - Chaotic-Good)" % (player_name, char_name, gender, char_class, char_role)
	elif good_evil_align == "Evil":
		print "	%s 's  %s (%s - %s:%s - Chaotic-Evil)" % (player_name, char_name, gender, char_class, char_role)
	elif good_evil_align == "Neutral":
		print "	%s 's  %s (%s - %s:%s - Chaotic-Neutral)" % (player_name, char_name, gender, char_class, char_role)
	else:
		print error_msg
elif law_chaos_align == "Neutral":
	if good_evil_align == "Good":
		print "	%s 's  %s (%s - %s:%s - Neutral-Good)" % (player_name, char_name, gender, char_class, char_role)
	elif good_evil_align == "Evil":
		print "	%s 's  %s (%s - %s:%s - Neutral-Evil)" % (player_name, char_name, gender, char_class, char_role)
	elif good_evil_align == "Neutral":
		print "	%s 's  %s (%s - %s:%s - Neutral-Neutral)" % (player_name, char_name, gender, char_class, char_role)
	else:
		print error_msg
else:
	print error_msg

cont()

# Abilities
print "Part 2 : Abilities"
print "  Section 1 : Rolling Ability Scores"
for ability in abilities:
	print "	%s" % (ability)

def stat_roll():
        d1 = random.randint (1,6)
        d2 = random.randint (1,6)
        d3 = random.randint (1,6)
        d4 = random.randint (1,6)
        list = [d1,d2,d3,d4]
        list.sort()
        total = sum(list[1:4])
        return total

strength = stat_roll()
print "	Strength:", strength
constitution = stat_roll()
print "	Constitution:", constitution
dexterity = stat_roll()
print "	Dexterity:", dexterity
intelligence = stat_roll()
print "	Intelligence:", intelligence
wisdom = stat_roll()
print "	Wisdom:", wisdom
charisma = stat_roll()
print "	Charisma:", charisma

print "  Section 2.2 : Rerolling"
reroll = raw_input("  You can reroll one (1) stat, would you like to reroll? y/n  ")
if reroll == "y" or reroll == "Y":
	reroll1 = raw_input("Select a stat to reroll: ")
	if reroll1 == "Strength" or reroll1 == "strength" or reroll1 == "str":
		strength = stat_roll()
		print "	New Stats:"
		print "	  Strength:      ", strength
		print "	  Constitution:  ", constitution
		print "	  Dexterity:     ", dexterity
		print "	  Intelligence:  ", intelligence
		print "	  Wisdom:        ", wisdom
		print "	  Charisma:      ", charisma
	elif reroll1 == "Constitution" or reroll1 == "constitution" or reroll1 == "con":
		constitution = stat_roll()
		print "	New Stats:"
		print "	  Strength:      ", strength
		print "	  Constitution:  ", constitution
		print "	  Dexterity:     ", dexterity
		print "	  Intelligence:  ", intelligence
		print "	  Wisdom:        ", wisdom
		print "	  Charisma:      ", charisma
	elif reroll1 == "Dexterity" or reroll1 == "dexterity" or reroll1 == "dex":
		dexterity = stat_roll()
		print "	New Stats:"
		print "	  Strength:      ", strength
		print "	  Constitution:  ", constitution
		print "	  Dexterity:     ", dexterity
		print "	  Intelligence:  ", intelligence
		print "	  Wisdom:        ", wisdom
		print "	  Charisma:      ", charisma
	elif reroll1 == "Intelligence" or reroll1 == "intelligence" or reroll1 == "int":
		intelligence = stat_roll()
		print "	New Stats:"
		print "	  Strength:      ", strength
		print "	  Constitution:  ", constitution
		print "	  Dexterity:     ", dexterity
		print "	  Intelligence:  ", intelligence
		print "	  Wisdom:        ", wisdom
		print "	  Charisma:      ", charisma
	elif reroll1 == "Wisdom" or reroll1 == "wisdom" or reroll1 == "wis":
		wisdom = stat_roll()
		print "	New Stats:"
		print "	  Strength:      ", strength
		print "	  Constitution:  ", constitution
		print "	  Dexterity:     ", dexterity
		print "	  Intelligence:  ", intelligence
		print "	  Wisdom:        ", wisdom
		print "	  Charisma:      ", charisma
	elif reroll1 == "Charisma" or reroll1 == "charisma" or reroll1 == "cha":
		charisma = stat_roll()
		print "	New Stats:"
		print "	  Strength:      ", strength
		print "	  Constitution:  ", constitution
		print "	  Dexterity:     ", dexterity
		print "	  Intelligence:  ", intelligence
		print "	  Wisdom:        ", wisdom
		print "	  Charisma:      ", charisma
	else:
		print error_msg
elif reroll == "n" or reroll == "N":
	print "	Ability stats have not been changed"
else:
	print error_msg

print "  Certain races generate a bonus to specific abilites"
cont()
if char_race == "Dragonborn":
	strength = strength + 2
	charisma = charisma + 2
	print "	New Stats:"
	print "	  Strength:      ", strength
	print "	  Constitution:  ", constitution
	print "	  Dexterity:     ", dexterity
	print "	  Intelligence:  ", intelligence
	print "	  Wisdom:        ", wisdom
	print "	  Charisma:      ", charisma
elif char_race == "Dwarf":
	constitution = constitution + 2
	wisdom = wisdom + 2
	print "	New Stats:"
	print "	  Strength:      ", strength
	print "	  Constitution:  ", constitution
	print "	  Dexterity:     ", dexterity
	print "	  Intelligence:  ", intelligence
	print "	  Wisdom:        ", wisdom
	print "	  Charisma:      ", charisma
elif char_race == "Eladrin":
	dexterity = dexterity + 2
	intelligence = intelligence + 2
	print "	New Stats:"
	print "	  Strength:      ", strength
	print "	  Constitution:  ", constitution
	print "	  Dexterity:     ", dexterity
	print "	  Intelligence:  ", intelligence
	print "	  Wisdom:        ", wisdom
	print "	  Charisma:      ", charisma
elif char_race == "Elf":
	dexterity = dexterity + 2
	wisdom = wisdom + 2
	print "	New Stats:"
	print "	  Strength:      ", strength
	print "	  Constitution:  ", constitution
	print "	  Dexterity:     ", dexterity
	print "	  Intelligence:  ", intelligence
	print "	  Wisdom:        ", wisdom
	print "	  Charisma:      ", charisma
elif char_race == "Half-Elf":
	constitution = constitution + 2
	charisma = charisma + 2
	print "	New Stats:"
	print "	  Strength:      ", strength
	print "	  Constitution:  ", constitution
	print "	  Dexterity:     ", dexterity
	print "	  Intelligence:  ", intelligence
	print "	  Wisdom:        ", wisdom
	print "	  Charisma:      ", charisma
elif char_race == "Halfling":
	dexterity = dexterity + 2
	charisma = charisma + 2
	print "	New Stats:"
	print "	  Strength:      ", strength
	print "	  Constitution:  ", constitution
	print "	  Dexterity:     ", dexterity
	print "	  Intelligence:  ", intelligence
	print "	  Wisdom:        ", wisdom
	print "	  Charisma:      ", charisma
elif char_race == "Human":
	print "	Humans can are awarxed +2 to an ability of chocie"
	for ability in abilities:
		print "	  %s" % (ability)
	choice = raw_input("Choose an ability:  ")
	if choice == "Strength":
		strength = strength + 2
		print "	New Stats:"
		print "	  Strength:      ", strength
		print "	  Constitution:  ", constitution
		print "	  Dexterity:     ", dexterity
		print "	  Intelligence:  ", intelligence
		print "	  Wisdom:        ", wisdom
		print "	  Charisma:      ", charisma
	elif choice == "Constitution":
		constitution = constitution + 2
		print "	New Stats:"
		print "	  Strength:      ", strength
		print "	  Constitution:  ", constitution
		print "	  Dexterity:     ", dexterity
		print "	  Intelligence:  ", intelligence
		print "	  Wisdom:        ", wisdom
		print "	  Charisma:      ", charisma
	elif chocie == "Dexterity":
		dexterity = dexterity + 2
		print "	New Stats:"
		print "	  Strength:      ", strength
		print "	  Constitution:  ", constitution
		print "	  Dexterity:     ", dexterity
		print "	  Intelligence:  ", intelligence
		print "	  Wisdom:        ", wisdom
		print "	  Charisma:      ", charisma
	elif chocie == "Wisdom":
		wisdom = wisdom + 2
		print "	New Stats:"
		print "	  Strength:      ", strength
		print "	  Constitution:  ", constitution
		print "	  Dexterity:     ", dexterity
		print "	  Intelligence:  ", intelligence
		print "	  Wisdom:        ", wisdom
		print "	  Charisma:      ", charisma
	elif choice == "Intelligence":
		intelligence = intelligence + 2
		print "	New Stats:"
		print "	  Strength:      ", strength
		print "	  Constitution:  ", constitution
		print "	  Dexterity:     ", dexterity
		print "	  Intelligence:  ", intelligence
		print "	  Wisdom:        ", wisdom
		print "	  Charisma:      ", charisma
	elif choice == "Charisma":
		charisma = charisma + 2
		print "	New Stats:"
		print "	  Strength:      ", strength
		print "	  Constitution:  ", constitution
		print "	  Dexterity:     ", dexterity
		print "	  Intelligence:  ", intelligence
		print "	  Wisdom:        ", wisdom
		print "	  Charisma:      ", charisma
	else:
		error_msg
elif char_race == "Tiefling":
	intelligence = intelligence + 2
	charisma = charisma + 2
	print "	New Stats:"
	print "	  Strength:      ", strength
	print "	  Constitution:  ", constitution
	print "	  Dexterity:     ", dexterity
	print "	  Intelligence:  ", intelligence
	print "	  Wisdom:        ", wisdom
	print "	  Charisma:      ", charisma
else:
	error_msg

# Social Descriptors
print "Part 3 : Personality"
print "  Section 3.1 : Social Interactions (Influence on others out-of-combat)"
print "	How do others percieve you in social interactions?"
for interaction in socials1:
	print "	  %s" % (interaction)
social1 = raw_input("	Answer:  ")

print "	How optimistic are you?"
for interaction in socials2:
	print "	  %s" % (interaction)
social2 = raw_input("	Answer:  ")

print "	How trusting are you?"
for interaction in socials3:
	print "	  %s" % (interaction)
social3 = raw_input("	Answer:  ")

# Decision Points
print "  Section 3.2 : Decision Points (Personallity's influence on tough decisions)"
print "	How assertive are youat a decision point?"
for point in decisions1:
	print "	  %s" % (point)
dec1 = raw_input("	Answer:  ")

print "	How assertive are youat a decision point?"
for point in decisions2:
	print "	  %s" % (point)
dec2 = raw_input("	Answer:  ")

print "	How assertive are youat a decision point?"
for point in decisions3:
	print "	  %s" % (point)
dec3 = raw_input("	Answer:  ")

# Dire Straits
print "  Section 3.3 : Dire Straits (Reactions to dire situations)"
print "  How courageous are you in dire straits?"
for ds in straits1:
	print "	  %s" % (ds)
dire_strait1 = raw_input("	Answer:  ")

print "How do you feel when faced by setbacks?"
for ds in straits2:
	print "	  %s" % (ds)
dire_strait2 = raw_input("	Answer:  ")

print "How are your nerves?"
for ds in straits3:
	print "	  %s" % (ds)
dire_strait3 = raw_input("	Answer:  ")