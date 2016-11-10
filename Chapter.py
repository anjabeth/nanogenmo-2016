import Synonym as syn
import markovify
import Modify as mod
import random

SENTENCES_PER_CHAPTER = 10

class Chapter(object):

	#constructor for a chapter
	def __init__(self, id_num, banned_chars, model):
		self.id_num = id_num
		self.banned_chars = banned_chars
		self.model = model
		print type(model)
		self.text = self.create_text()

	def create_text(self):
		""" should return the text of the chapter as a string, with all necessary substitutions made"""

		#create initial, unmodified text
		initial_text = ""
		for i in range(SENTENCES_PER_CHAPTER):
			initial_text += str(self.model.make_sentence())

		#split words on spaces
		initial_words = initial_text.split(" ")

		#determine what happens to 'banned' words
		for word in iniital_words:
			#check all chars to see if word contains any, break after it finds one
			banned = False
			for char in banned_chars:
				if char in word:
					banned = True
					break

			if banned:
				num = random.randint(0, 10)
				if num <= 7:
					#find synonym
					syn.find_acceptable_synonym(word, banned_chars)
					#if no synonym found, try letter replacements
				elif num <= 9:
					#find letter replacements (MAKE SURE TO CHECK IN LETTER REPLACEMENT METHOD WHICH CHARS ARE CURRENTLY BANNED)
					mod.modify_letters(word, banned_chars)
					#if no suitable replacement, black word out
				else:
					mod.black_out(word)
					#black word out

		#join words back up into one string
		chapter_text = " ".join(initia_words)
		return chapter_text