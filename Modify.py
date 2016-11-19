class Modify:\

	#order of eliminations: ("z", "q", "x", "j", "k", "v", "b", "p", "y", "g", "f", "w", "m", "u", "c", "l", "d", "r", "h", "s", "n", "i", "o", "a", "t", "e")

	#note - maybe look into letters you can eliminate in certain contexts? abstract -> abstrat, painting -> paining (maybe like 2-consonant pairs?)

	def __init__(self):
		self.replace_dict = dict()
		self.replace_dict["q"] = ("k")
		self.replace_dict["x"] = ("ks")
		self.replace_dict["j"] = ("g")
		self.replace_dict["k"] = ("g")
		self.replace_dict["v"] = ("f")
		self.replace_dict["b"] = ("p")
		self.replace_dict["y"] = ("i")
		self.replace_dict["f"] = ("ph")
		self.replace_dict["d"] = ("t")
		self.replace_dict["u"] = ("oo")


	def modify_letters(self, word, banned_chars):
		""" modifies letters of a given word using replace_dict to remove banned characters"""
		word = word.decode("utf-8")
		new_word = ""

		#replace chars as needed
		for char in word:
			if char in banned_chars:
				if char in self.replace_dict:
					new_word += self.replace_dict[char]
				else:
					#char isn't in replacement dict and can't be replaced, so black out word instead
					return self.black_out(word)
			else:
				#characters successfully replaced, return new_word
				new_word += char
		
		
		return new_word

	

	def black_out(self, word):
		"""redacts a given word"""
		black_out_word = ""
		for char in word:
			black_out_word += u"\u2588"
		return black_out_word
		