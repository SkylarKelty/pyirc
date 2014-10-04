
class Channel:
	def __init__(self, conn, name):
		self.conn = conn
		self.name = name

	def message(self, message):
		self.conn.privmsg(self.name, message)