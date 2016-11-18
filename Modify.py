def modify_letters(word, banned_chars):
	return "BANNED-let"

def black_out(word):
	black_out_word = ""
	for char in word:
		black_out_word += u"\u2588"
	return black_out_word
	