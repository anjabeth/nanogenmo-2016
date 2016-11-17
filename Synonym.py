# -*- coding: utf-8 -*-

from wordnik import *
from textblob import Word
import random
import json

class Synonym:

	def __init__(self):
		self.apiUrl = 'http://api.wordnik.com/v4'
		self.apiKey = '789439e487771e1085b261e2bf001749744d0e079512b3549'
		self.client = swagger.ApiClient(self.apiKey, self.apiUrl)
		self.wordApi = WordApi.WordApi(self.client)

	def find_acceptable_synonym(self, word, banned_chars):
		
		all_syns = self.wordApi.getRelatedWords(word, relationshipTypes = "synonym")
		if all_syns is not None:
			#temporary 
			synonym = all_syns[0].words[0]
			for syn in all_syns:
				print syn.words
		else: #couldn't find a synonym
			#call a different function
			return "NO SYN FOUND" #for now
		
		return "Orig: " + word + "SYNONYM:" + synonym
		
		

		