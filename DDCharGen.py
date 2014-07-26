#!/bin/python2.7
# Dungeons & Dragons Character Generator
# Reference - http://pastebin.com/8nTb1h1U
# Refernce - http://www.ibisfightclub.co.uk/dnd/Basics.asp
# Reference - http://thenickelscreen.files.wordpress.com/2011/05/dd-alignment-4-flat.png

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

def error_msg():
	print "Opps!  Something went wrong.  Exiting...."
	quit()

# Description
print "Dungeons & Dragons (4th Ed.) Character Generator"
print "	Summary"
print "	  Part 1:  General Information"
print "	  Part 2:  Ability Scores"
print "	  Part 3:  Personality"

def cont():
	cont = raw_input("This section is complete.  Do you want to continue? <y/n>  ")
	if cont in ("N", "n"):
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

if char_class in ("Cleric", "Warlor"):
	if char_role == "Leader":
		pass
	else:
		print "	Clerics and Warlords are best suited as - Leaders"
		role_option = raw_input("	Do you want to continue with this class? <y/n>  ")
		if role_option in ("y", "y"):
			pass
		else:
			char_role = raw_input("	Enter Chosen Role:  ")
elif char_class in ("Fighter", "Paladin"):
	if char_role == "Defender":
		pass
	else:
		print "Fighters and Paladins are best suited as - Defenders"
		role_option = raw_input("	Do you want to continue with this class? <y/n>  ")
		if role_option in ("y", "y"):
			pass
		else:
			char_role = raw_input("	Enter Chosen Role:  ")
elif char_class in ("Ranger", "Rogue", "Warlock"):
	if char_role == "Striker":
		pass
	else:
		print "Rangers, Rogues, and Warlocks are best suited as - Strikers"
		role_option = raw_input("	Do you want to continue with this class? <y/n>  ")
		if role_option in ("y", "y"):
			pass
		else:
			char_role = raw_input("	Enter Chosen Role:  ")
elif char_class == "Wizard":
	if char_role == "Controller":
		pass
	else:
		print "Wizards are best suited as - Controllers"
		role_option = raw_input("	Do you want to continue with this class? <y/n>  ")
		if role_option in ("y", "y"):
			pass
		else:
			char_role = raw_input("	Enter Chosen Role:  ")
else:
	error_msg()

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
		alignment = "Lawful Good"
		examples = "Superman, Captain America"
		comment = "The Knight:  Follows strict moral code and always fights evil"
	elif good_evil_align == "Evil":
		alignment = "Lawful Evil"
		examples = "Magneto, Darth Vader"
		comment = "The Overlord:  Power above all else.  Uses law to maintina control"
	elif good_evil_align == "Neutral":
		alignment = "Lawful Neutral"
		examples = "Silver Surfer, Judge Dred"
		comment = "The Judge:  Believes so strongly in justice, will carry out any order"
	else:
		error_msg()
elif law_chaos_align == "Chaos":
	if good_evil_align == "Good":
		alignment = "Chaotic Good"
		examples = "Robin Hood, Wolverine"
		comment = "The Rebel:  Fight the system to do what you think is right"
	elif good_evil_align == "Evil":
		alignment = "Chaotic Evil"
		examples = "The Joker, Carnage"
		comment = "The Psychopath:  Exists purely to destroy.  Revels in acts of evil"
	elif good_evil_align == "Neutral":
		alignment = "Chaotic Neutral"
		examples = "Capn' Jack Sparrow, Conan the Barbarian"
		comment = "Care only for yourself, ignoring morality and the law"
	else:
		error_msg()
elif law_chaos_align == "Neutral":
	if good_evil_align == "Good":
		alignment = "Neutral Good"
		examples = "Spider-Man, Gandalf"
		comment = "The Hero:  Always do the right thing even if the law is not on your side"
	elif good_evil_align == "Evil":
		alignment = "Neutral Evil"
		examples = "Voldermort, Lex Luthor"
		comment = "The Villain:  Pursues evil at all costs"
	elif good_evil_align == "Neutral":
		alignment = "Neutral Neutral"
		examples = "The Elks"
		comment = "The Outsider:  Unaffected by the petty squabbles of the masses"
	else:
		error_msg()
else:
	error_msg()

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
reroll = raw_input("  You can reroll one (1) stat, would you like to reroll? <y/n>  ")
if reroll in ("Y", "y"):
	reroll1 = raw_input("Select a stat to reroll: ")
	if reroll1 in ("Strength", "strength", "str"):
		strength = stat_roll()
		print "	  Strength (new):      ", strength
	elif reroll1 in ("Constitution", "constitution", "con"):
		constitution = stat_roll()
		print "	  Constitution (new):  ", constitution
	elif reroll1 in ("Dexterity", "dexterity", "dex"):
		dexterity = stat_roll()
		print "	  Dexterity (new):     ", dexterity
	elif reroll1 in ("Intelligence", "intelligence", "int"):
		intelligence = stat_roll()
		print "	  Intelligence (new):  ", intelligence
	elif reroll1 in ("Wisdom", "wisdom", "wis"):
		wisdom = stat_roll()
		print "	  Wisdom (new):        ", wisdom
	elif reroll1 in ("Charisma", "charisma", "cha"):
		charisma = stat_roll()
		print "	  Charisma (new):      ", charisma
	else:
		error_msg()
elif reroll == "n" or reroll == "N":
	print "	Ability stats have not been changed"
else:
	error_msg()

print "  Certain races generate a bonus to specific abilites.  Calculating..."
if char_race == "Dragonborn":
	print "	Dragonborn Bonus:  +2 Charisma, +2 Strength"
	strength = strength + 2
	charisma = charisma + 2
elif char_race == "Dwarf":
	print "	Dwarf Bonus:  +2 Constitution, +2 Wisdom"
	constitution = constitution + 2
	wisdom = wisdom + 2
elif char_race == "Eladrin":
	print "	Eladrin Bonus:  +2 Dexterity, +2 Intelligence"
	dexterity = dexterity + 2
	intelligence = intelligence + 2
elif char_race == "Elf":
	print "	Elf Bonus:  +2 Dexterity, +2 Wisdom"
	dexterity = dexterity + 2
	wisdom = wisdom + 2
elif char_race == "Half-Elf":
	print "	Half-Elf Bonus:  +2 Constitution, +2 Charisma"
	constitution = constitution + 2
	charisma = charisma + 2
elif char_race == "Halfling":
	print "	Halfling Bonus:  +2 Dexterity, +2 Charisma"
	dexterity = dexterity + 2
	charisma = charisma + 2
elif char_race == "Human":
	print "	Humans can are awarded +2 to an ability of chocie"
	for ability in abilities:
		print "	  %s" % (ability)
	choice = raw_input("Choose an ability:  ")
	if choice == "Strength":
		strength = strength + 2
	elif choice == "Constitution":
		constitution = constitution + 2
	elif chocie == "Dexterity":
		dexterity = dexterity + 2
	elif chocie == "Wisdom":
		wisdom = wisdom + 2
	elif choice == "Intelligence":
		intelligence = intelligence + 2
	elif choice == "Charisma":
		charisma = charisma + 2
	else:
		error_msg()
elif char_race == "Tiefling":
	print "	Tiefling Bonus: +2 Intelligence, +2 Charisma"
	intelligence = intelligence + 2
	charisma = charisma + 2
else:
	error_msg()

if char_class == "Cleric":
	hp = constitution + 12
	pwr_src = "Divine"
	key_ability = "Wisdom, Strength, Charisma"
	armr = "Cloth, Leather, Hide, Chainmail"
	wpn = "Simple Melee, Simple Ranged"
	options = "Battle Clereic, Devoted Cleric"
elif char_class == "Fighter":
	hp = constitution + 15
	pwr_src = "Martial"
	key_ability = "Strength, Dexterity, Wisdom, Constitution"
	armr = "Cloth, Leather, Hide, Chainmail, Scale, Light Shield, Heavy Shield"
	wpn = "Simple Melee, Military Melee, Simple Ranged, Military Ranged"
	options = "Great Weapon Fighter, Guardian Fighter"
elif char_class == "Paladin":
	hp = constitution + 15
	pwr_src = "Divine"
	key_ability = "Strength, Charisma, Wisdom"
	armr = "Cloth, Leather, Hide, Chainmail, Scale, Plate, Light Shield, Heavy Shield"
	wpn = "Simple Melee, Military Melee, Simple Ranged"
	options = "Avenging Paladin, Protecting Paladin"
elif char_class == "Ranger":
	hp = constitution + 12
	pwr_src = "Martial"
	key_ability = "Strength, Dexterity, Wisdom"
	armr = "Cloth, Leather, Hide"
	wpn = "Simple Melee, Military Melee, Simple Ranged, Military Rnaged"
	options = "Archer Ranger, Two-Blade Ranger"
elif char_class == "Rogue":
	hp = constitution + 12
	pwr_src = "Martial"
	key_ability = "Dexterity, Strength, Charisma"
	armr = "Cloth, Leather"
	wpn = "Dagger, Hand Crossbow, Shuriken, Sling, Short Sword"
	options = "Brawny Rogue, Trickster Rogue"
elif char_class == "Warlock":
	hp = constitution + 12
	pwr_src = "Arcane"
	key_ability = "Charisma, Constitution, Intelligence"
	armr = "Cloth, Leather"
	wpn = "Simple Melee, Simple Ranged"
	options = "Deceptive Warlock, Scourge Warlock"
elif char_class == "Warlord":
	hp = constitution + 12
	pwr_src = "Martial"
	key_ability = "Strength, Intelligence, Charisma"
	armr = "Cloth, Leather, Hide, Chainmail, Light Shield"
	wpn = "Simple Melee, Military Melee, Simple Ranged"
	options = "Inspiring Warlord, Tactical Warlord"
elif char_class == "Wizard":
	hp = constitution + 10
	pwr_src = "Arcane"
	key_ability = "Intelligence, Wisdom, Dexterity"
	armr = "Cloth"
	wpn = "Dagger, Quarterstaff"
	options = "Control Wizard, War Wizard"
else:
	error_msg()

# Ability Modifiers
print "  Section 2.2 : Modifiers"
if strength %2 == 0:
	mod_str = ((strength - 10) / 2)
else:
	mod_str = ((strength - 11) / 2)
if constitution %2 == 0:
	mod_con = ((constitution - 10) / 2)
else:
	mod_con = ((constitution - 11) / 2)
if dexterity %2 == 0:
	mod_dex = ((dexterity - 10) / 2)
else:
	mod_dex = ((dexterity - 11) / 2)
if intelligence %2 == 0:
	mod_int = ((intelligence - 10) / 2)
else:
	mod_int = ((intelligence - 11) / 2)
if wisdom %2 == 0:
	mod_wis = ((wisdom - 10) / 2)
else:
	mod_wis = ((wisdom - 11) / 2)
if charisma %2 == 0:
	mod_cha = ((charisma - 10) / 2)
else:
	mod_cha = ((charisma - 11) / 2)

cont()

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

print "Character 3 Summary:"
print "	%s 's %s:%s:%s" % (player_name, char_race, char_class, char_role)
print "	  Name:                  %s" % (char_name)
print "	  Age:                   %s" % age
print "	  Height:                %s ' %s \"" % (height_ft, height_in)
print "   Weight:                %s" % (weight)
print "	  Gender:                %s" % (gender)
print "	  Alignment:             %s (%s)" % (alignment, examples)
print "	                         %s" % (comment)
print "	  Power Source:          %s" % (pwr_src)
print "	  Armor:                 %s" % (armr)
print "	  Weapons:               %s" % (wpn)
print "	  Prefered Stats:        %s" % (key_ability)
print "		Strength(mod):       %s (%s)" % (strength, mod_str)
print "		Constitution (mod):  %s (%s)" % (constitution, mod_con)
print "		  Hit Points:        %s (%s)" % (hp)
print "		Dexterity (mod):     %s (%s)" % (dexterity, mod_dex)
print "		Intelligence (mod):  %s (%s)" % (intelligence, mod_int)
print "		Wisdom (mod):        %s (%s)" % (wisdom, mod_wis)
print "		Charisma (mod):      %s (%s)" % (charisma, mod_cha)
print "	  Personality:"
print "		Social:        %s" % (social1)
print "		               %s" % (social2)
print "		               %s" % (social3)
print "		Decisions:     %s" % (dec1)
print "		               %s" % (dec2)
print "		               %s" % (dec3)
print "		Dire Straits:  %s" % (dire_strait1)
print "		               %s" % (dire_strait2)
print "		               %s" % (dire_strait3)
print "	  Build Options:   %s" % (options)