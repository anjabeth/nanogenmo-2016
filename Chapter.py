# -*- coding: utf-8 -*-

import random
import markovify
from textblob import TextBlob 
from Synonym import Synonym 
from Modify import Modify

SENTENCES_PER_CHAPTER = 110

class Chapter(object):
	""" Chapter object represents one chapter in a novel. It has:
	 - id_num: unique id for debugging purposes
	 - banned_chars: list of chars that aren't allowed to be used
	 - model: markovify Text object that generates chapter sentences
	 - syn_gen: Synonym object, generates synonyms for banned words
	 - text: contains text of the chapter
	"""

	
	def __init__(self, id_num, banned_chars, model, syn_gen):
		"""Construct a chapter"""
		self.id_num = id_num
		self.banned_chars = banned_chars
		self.model = model
		self.syn_gen = syn_gen
		self.text = self.create_text()
		
	def create_text(self):
		"""Return the text of the chapter as a string, with all necessary substitutions made"""

		initial_text = self.create_initial_text()
		initial_words = initial_text.split(" ")
		new_words = list()
		mod = Modify()

		
		#determine what happens to 'banned' words
		for word in initial_words:
			#check all chars to see if word contains any, break after it finds one
			banned = False
			for char in self.banned_chars:
				if char in word:
					banned = True
					break

			if banned:
				num = random.randint(0, 10)
				if num <= 7:
					#find synonym
					synonym = self.syn_gen.find_acceptable_synonym(word, self.banned_chars)
					new_words.append(synonym)
					
				elif num <= 9:
					#find letter replacements 
					new_words.append(mod.modify_letters(word, self.banned_chars))
				else:
					#black word out
					new_words.append(mod.black_out(word))
			else:
				new_words.append(word)

		return self.join_words(new_words)

	def create_initial_text(self):
		"""Return original text generated by markov model"""
		initial_text = ""
		for i in range(SENTENCES_PER_CHAPTER):
			try:
				initial_text += str(self.model.make_sentence()).encode('utf-8') + " "
			except UnicodeEncodeError:
				i -= 1

		return initial_text
		
	def join_words(self, words):
		"""Join list of processed words back into one string"""
		return (' ').join(words)
