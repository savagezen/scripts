#!/bin/python2.7
# Dungeons & Dragons Character Generator
# Reference - http://pastebin.com/8nTb1h1U

# Python Imports
import random

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

roles = [
"  Controller:  Control Control and Area Offense",
"  Defender:    Defense, Good Close Up Offense,",
"  Leader:      Healing and Support, Good Defenses, Best at Protecting",
"  Striker:     Focused Single-Target Offense, Mobile, Tricksters"
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

error_msg = "Oops! Something went wrong.  Exiting..."

# Description
print "Dungeons & Dragons (4th Ed.) Character Generator"

# Name
print "Part 1.1 : Name"
char_name = raw_input("	Enter Character Name:  ")
player_name = raw_input("	Enter Player's Name:  ")

# Race
print "Part 1.2 : Race"
for race in races:
	print "	%s" % (race)
char_race = raw_input("	Enter Chosen Race:  ")

# Class
print "Part 1.3 : Class"
for c in classes:
	print "	%s" % (c)
char_class = raw_input("	Enter Chosen Class:  ")

# Role
print "Part 1.4 : Roles / Combat Functions:"
print "	!!Role Availability is Limited by Character Class!!"
for role in roles:
	print "	%s" % (role)
char_role = raw_input("	Enter Chosen Role:  ")

if char_class == "Cleric" or char_class == "Warlord":
	if char_role == "Leader":
		print "	%s 's  %s - %s : %s" % (player_name, char_name, char_class, char_role)
	else:
		print "Clerics and Warlords are best suited as - Leaders"
elif char_class == "Fighter" or char_class == "Paladin":
	if char_role == "Defender":
		print "	%s 's  %s - %s : %s" % (player_name, char_name, char_class, char_role)
	else:
		print "Fighters and Paladins are best suited as - Defenders"
elif char_class == "Ranger" or char_class == "Rogue" or char_class == "Warlock":
	if char_role == "Striker":
		print "	%s 's  %s - %s : %s" % (player_name, char_name, char_class, char_role)
	else:
		print "Rangers, Rogues, and Warlocks are best suited as - Strikers"
elif char_class == "Wizard":
	if char_role == "Controller":
		print "	%s 's  %s - %s : %s" % (player_name, char_name, char_class, char_role)
	else:
		print "Wizards are best suited as - Controllers"
else:
	print error_msg

# Alignment
print "Part 1.5 : Alignment (v3.5)"
for alignment in law_chaos:
	print "	%s"	% (alignment)
law_chaos_align = raw_input("Choose 1st Axis Alignment:  ")
for alignment in good_evil:
	print "	%s" % (alignment)
good_evil_align = raw_input("Choose 2nd Axis Alignment:  ")

if law_chaos_align == "Law":
	if good_evil_align == "Good":
		print "	%s 's Lawful-Good %s - %s : %s" % (player_name, char_name, char_class, char_role)
	elif good_evil_align == "Evil":
		print "	%s 's  Lawful-Evil %s - %s : %s" % (player_name, char_name, char_class, char_role)
	elif good_evil_align == "Neutral":
		print "	%s 's  Lawful-Neutral %s - %s : %s" % (player_name, char_name, char_class, char_role)
	else:
		print error_msg
elif law_chaos_align == "Chaos":
	if good_evil_align == "Good":
		print "	%s 's Chaotic-Good %s - %s : %s" % (player_name, char_name, char_class, char_role)
	elif good_evil_align == "Evil":
		print "	%s 's  Chaotic-Evil %s - %s : %s" % (player_name, char_name, char_class, char_role)
	elif good_evil_align == "Neutral":
		print "	%s 's  Chaotic-Neutral %s - %s : %s" % (player_name, char_name, char_class, char_role)
	else:
		print error_msg
elif law_chaos_align == "Neutral":
	if good_evil_align == "Good":
		print "	%s 's Neutral-Good %s - %s : %s" % (player_name, char_name, char_class, char_role)
	elif good_evil_align == "Evil":
		print "	%s 's  Neutral-Evil %s - %s : %s" % (player_name, char_name, char_class, char_role)
	elif good_evil_align == "Neutral":
		print "	%s 's  Neutral-Neutral %s - %s : %s" % (player_name, char_name, char_class, char_role)
	else:
		print error_msg
else:
	print error_msg

# Abilities
print "Part 2.1 : Ability Scores"
print "	These will be radom rolled scores.  See Player Handbook for more information."
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

reroll = raw_input("You can reroll one (1) stat, would you like to reroll? y/n  ")
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
	print "Ability stats have not been changed"
else:
	print error_msg