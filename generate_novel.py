# -*- coding: utf-8 -*-

import sys
import io
import textwrap
import markovify
from gutenberg.acquire import load_etext
from gutenberg.cleanup import strip_headers
from Chapter import Chapter

NUM_CHAPTERS = 25
OUTPUT_LOC = "novel.txt"

CHAR_REMOVE_ORDER = ("z", "q", "x", "j", "k", "v", "b", "p", "y", "g", "f", "w", "m", "u", "c", "l", "d", "r", "h", "s", "n", "i", "o", "a", "t", "e")

def main():
	model = create_model()
	chapters = create_chapters(model) 
	
	clearfile()

	f = open(OUTPUT_LOC, "a")
	write_chapters(f, chapters)
	f.close()
	
	print "Novel written to " + str(OUTPUT_LOC)
	
	


def create_chapters(model):
	all_chapters = list() #list that will hold all the chapters
	for i in range(NUM_CHAPTERS):
		new_chap = Chapter(i, CHAR_REMOVE_ORDER[0:i+1], model) #this isn't done, it needs to take an increasing list of banned characters (also the constructor in Chpater isn't done yet)
		all_chapters.append(new_chap)
	return all_chapters

def create_model():
	eap_1 = strip_headers(load_etext(2147)).strip() #edgar allan poe vol 1
	eap_2 = strip_headers(load_etext(2148)).strip() #edgar allan poe vol 2
	dickens = strip_headers(load_etext(807)).strip() #charles dickens crime stories
	moonstone = strip_headers(load_etext(155)).strip() #collins: the moonstone
	lerouge = strip_headers(load_etext(3802)).strip() #gaboriau: the lerouge case
	orcival = strip_headers(load_etext(1651)).strip() #gaboriau: the mystery of orcival
	calais = strip_headers(load_etext(16339)).strip() #griffiths: the passenger from calais\
	leavenworth = strip_headers(load_etext(4047)).strip() #griffiths: the passenger from calais
	agent = strip_headers(load_etext(974)).strip() #conrad: the secret agent
	thirtynine = strip_headers(load_etext(558)).strip() #conrad: the secret agent

	eap_1_model = markovify.Text(eap_1, state_size = 3)
	eap_2_model = markovify.Text(eap_2, state_size = 3)
	dickens_model = markovify.Text(dickens, state_size = 3)
	moonstone_model = markovify.Text(moonstone, state_size = 3)
	lerouge_model = markovify.Text(lerouge, state_size = 3)
	orcival_model = markovify.Text(orcival, state_size = 3)
	calais_model = markovify.Text(calais, state_size = 3)
	leavenworth_model = markovify.Text(leavenworth, state_size = 3)
	agent_model = markovify.Text(agent, state_size=3)
	thirtynine_model = markovify.Text(thirtynine, state_size = 3)

	#NOTE: will need to play around with the weighting based on the text lengths so that I don't get all sentences from one book
	all_model = markovify.combine([eap_1_model, eap_2_model, dickens_model, moonstone_model, lerouge_model, orcival_model, calais_model, leavenworth_model, agent_model, thirtynine_model])

	return all_model

def write_chapters(file, chapters):
	"""writes chapters to file using textwrap to make lines readable length"""

	for i in range(NUM_CHAPTERS):
		file.write("Chapter" + str(i + 1) + "******************************************* \n")
		lines = textwrap.wrap(chapters[i].text)
		for line in lines:
			file.write((line).encode("utf-8") + "\n")
		file. write("\n\n\n\n")

def clearfile():
	"""clears input file, utility for when running script multiple times"""
	f = open(OUTPUT_LOC, "w")
	f.write("A Procedurally Generated Novel By Anja Beth\n\n")
	f.close()

if __name__ == '__main__':
	main()