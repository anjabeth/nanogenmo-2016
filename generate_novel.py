# -*- coding: utf-8 -*-

import markovify
from Chapter import Chapter
from gutenberg.acquire import load_etext
from gutenberg.cleanup import strip_headers

NUM_CHAPTERS = 5

def main():
		model = create_model()
		chapters = create_chapters(model) #this will be a list of all the chapters, they should be complete at this point (all replacement/etc done)

		#just to check
		for i in range(NUM_CHAPTERS):
			print "Chapter" + str(i) + "********************************************* \n\n"
			print chapters[i].text
		

def create_chapters(model):
	all_chapters = list() #list that will hold all the chapters
	banned_chars = ("k", "j", "q") #temporary banned chars list for testing purposes
	for i in range(NUM_CHAPTERS):
		new_chap = Chapter(i, banned_chars, model) #this isn't done, it needs to take an increasing list of banned characters (also the constructor in Chpater isn't done yet)
		all_chapters.append(new_chap)
	return all_chapters

def create_model():
	eap_1 = strip_headers(load_etext(2147)).strip() #edgar allan poe vol 1
	eap_2 = strip_headers(load_etext(2148)).strip() #edgar allan poe vol 2
	dickens = strip_headers(load_etext(807)).strip() #charles dickens crime stories
	moonstone = strip_headers(load_etext(155)).strip() #collins: the moonstone
	lerouge = strip_headers(load_etext(3802)).strip() #gaboriau: the lerouge case
	orcival = strip_headers(load_etext(1651)).strip() #gaboriau: the mystery of orcival

	eap_1_model = markovify.Text(eap_1, state_size = 3)
	eap_2_model = markovify.Text(eap_2, state_size = 3)
	dickens_model = markovify.Text(dickens, state_size = 3)
	moonstone_model = markovify.Text(moonstone, state_size = 3)
	lerouge_model = markovify.Text(lerouge, state_size = 3)
	orcival_model = markovify.Text(orcival, state_size = 3)

	#NOTE: will need to play around with the weighting based on the text lengths so that I don't get all sentences from one book
	all_model = markovify.combine([eap_1_model, eap_2_model, dickens_model, moonstone_model, lerouge_model, orcival_model])

	return all_model


if __name__ == '__main__':
	main()