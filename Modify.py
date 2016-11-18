class Modify:

	def __init__(self):
		self.replace_dict = dict()
		self.replace_dict["q"] = ("k")
		self.replace_dict["x"] = ("ks")
		self.replace_dict["j"] = ("g")
		self.replace_dict["v"] = ("ph", "f")
		self.replace_dict["f"] = ("ph")
		self.replace_dict["d"] = ("t")
		self.replace_dict["u"] = ("oo")


	def modify_letters(self, word, banned_chars):
		""" modifies letters of a given word using replace_dict to remove banned characters"""
		return "BANNED-let"

	def black_out(self, word):
		"""redacts a given word"""
		black_out_word = ""
		for char in word:
			black_out_word += u"\u2588"
		return black_out_word
		