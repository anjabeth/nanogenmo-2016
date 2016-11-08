class Chapter(object):

	#constructor for a chapter
	def __init__(self, id_num, banned_chars):
		self.id_num = id_num
		self.banned_chars = banned_chars
		self.text = ""

	#don't know if this should go in a separate utils file or in this one - it seems weird to allow a chapter to create itself?? but I think this should work
	def create_chapter()
