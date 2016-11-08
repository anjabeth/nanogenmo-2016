# -*- coding: utf-8 -*-

import markovify
from Chapter import Chapter
from gutenberg.acquire import load_etext
from gutenberg.cleanup import strip_headers

NUM_CHAPTERS = 5

def main():
		eap_1 = strip_headers(load_etext(2147)).strip() #edgar allan poe vol 1
		eap_2 = strip_headers(load_etext(2148)).strip() #edgar allan poe vol 2
		dickens = strip_headers(load_etext(807)).strip() #charles dickens crime stories
		moonstone = strip_headers(load_etext(155)).strip() #collins: the moonstone
		lerouge = strip_headers(load_etext(3802)).strip() #gaboriau: the lerouge case
		orcival = strip_headers(load_etext(1651)).strip() #gaboriau: the mystery of orcival

		eap_1_model = markovify.Text(eap_1, state_size = 3)
		dickens_model = markovify.Text(dickens, state_size = 3)
		moonstone_model = markovify.Text(moonstone, state_size = 3)
		lerouge_model = markovify.Text(lerouge, state_size = 3)
		orcival_model = markovify.Text(orcival, state_size = 3)

		#NOTE: will need to play around with the weighting based on the text lengths so that I don't get all sentences from one book
		all_model = markovify.combine([eap_1_model, eap_2_model, dickens_model, moonstone_model, lerouge_model, orcival_model])

		#to do: loop to create different chapters - probably make them short (~ten sentences?) at first to make sure that they work properly
		print "\n\n\n Creating Chapters"

		chapters = create_chapters() #this will be a list of all the chapters, they should be complete at this point (all replacement/etc done)
		
		"""
		most of this stuff should probably go in Chapter

		text = ""
		for i in range(3):
			text += str(all_model.make_sentence())

		chapter1 = Chapter(1, ['a'], text)

		print "Chapter 1 banned words"

		all_words = chapter1.text.split(" ") #have to split text into words bc currently it's just one string and otherwise you just get characters, but other than that the "id-ing banned words" code works - it'll be a little more complicated for multiple banned chars because we'll have to loop, and eventually multiple chapters with multiple banned chars - should probably write out the structure of what that should look like
		for word in all_words:
			print word
			if chapter1.banned_chars[0] in word:
				print word + "banned"
"""

def create_chapters():
	all_chapters = list() #list that will hold all the chapters
	for i in range(NUM_CHAPTERS):
		new_chap = Chapter.create_chapter() #this isn't done, create_chapter needs parameters and also you'll have to increment the banned characters every time
		all_chapters.append(new_chap)
	return all_chapters



if __name__ == '__main__':
	main()