# -*- coding: utf-8 -*-

import random
import json
from wordnik import *
from PyDictionary import PyDictionary
from Modify import Modify

class Synonym:
	"""Synonym object is a generator for synonyms. Has:
	- apiUrl: url for Wordnik API
	- apiKey: API access key, obtain from wordnik.com
	- client: API client
	- wordApi: query-able API object
	- dictionary: PyDictionary object (for synonym generation)
	- mod: Modify object for redaction if no substitutes found
	- words_without_synonyms: tracking list of words without synonyms to reduce runtime
	"""

	def __init__(self):
		"""Create a Synonym"""
		self.apiUrl = 'http://api.wordnik.com/v4'
		self.apiKey = '789439e487771e1085b261e2bf001749744d0e079512b3549'
		self.client = swagger.ApiClient(self.apiKey, self.apiUrl)
		self.wordApi = WordApi.WordApi(self.client)
		self.dictionary = PyDictionary()
		self.mod = Modify()
		self.words_without_synonyms = dict()

	def find_acceptable_synonym(self, word, banned_chars):
		"""Find a synonym for word that does not contain any of banned_chars"""

		#word already known not to have synonym, misspell instead
		if word in self.words_without_synonyms:
			return self.mod.modify_letters(word, banned_chars)

		#find synonym from Wordnik API
		wordnik_syn = self.get_wordnik_syn(word, banned_chars)
		if wordnik_syn is not None:
			return wordnik_syn

		#didn't find wordnik synonym, try PyDict synonym
		pydict_syn = self.get_pydict_syn(word, banned_chars)
		if pydict_syn is not None:
			return pydict_syn

		#couldn't find a synonym - add to list of words w/o synonyms and respell instead
		self.words_without_synonyms[word] = True
		return self.mod.modify_letters(word, banned_chars)
		
	def get_wordnik_syn(self, word, banned_chars):
		"""Get synonym that does not contain any of banned_chars via Wordnik API. If no synonym found, returns None
		"""

		all_syns = self.wordApi.getRelatedWords(word, relationshipTypes = "synonym")

		if all_syns is not None:
			#find first synonym that does not contain any of the banned chars
			for syn in all_syns:
				banned = False
				for char in banned_chars:
					if char in syn.words[0]:
						banned = True
						break
				if not banned:
					synonym = syn.words[0]
					if synonym is not None:
						return synonym
		return None
	
	def get_pydict_syn(self, word, banned_chars):
		"""Get synonym that does not contain any of banned_chars from PyDictionary. If no synonym found, returns None
		"""
		
		pydict_syns = self.dictionary.synonym(word)

		if pydict_syns is not None:
			for syn in pydict_syns:
				banned = False
				for char in banned_chars:
					if char in syn:
						banned = True
						break
				if not banned:
					synonym = syn
					if synonym is not None:
						return synonym
		return None

		