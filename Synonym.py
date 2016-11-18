# -*- coding: utf-8 -*-

from wordnik import *
from PyDictionary import PyDictionary
import random
import json

class Synonym:

	def __init__(self):
		self.apiUrl = 'http://api.wordnik.com/v4'
		self.apiKey = '789439e487771e1085b261e2bf001749744d0e079512b3549'
		self.client = swagger.ApiClient(self.apiKey, self.apiUrl)
		self.wordApi = WordApi.WordApi(self.client)
		self.dictionary = PyDictionary()

	def find_acceptable_synonym(self, word, banned_chars):
		"""finds a synonym for word that does not contain any of banned_chars"""
	
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

		#didn't find wordnik synonym, try PyDict synonym
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
		#couldn't find a synonym
		#eventually call a different function
		#temporarily
		return "NO SYN FOUND" 
		
		
		
		

		