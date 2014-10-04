import socket
from src.nlp import NLP
from src.channel import Channel

class PyIRC:
	def __init__(self, hostname, port, channel, nick):
		self.hostname = hostname
		self.port = port
		self.channel = channel
		self.nick = nick
		self.nlp = NLP()

	"""
	Sends a message.
	"""
	def send(self, message):
		print("SEND: %s" % message)
		self.ircsock.send(message.encode())

	"""
	Sends a private message.
	"""
	def privmsg(self, channel, message):
		self.send("PRIVMSG %s :%s\n" % (channel, message))

	"""
	Returns the next available message on the socket.
	"""
	def get_message(self):
		message = self.ircsock.recv(2048).decode()
		message = message.strip('\n\r')

		print("RECV: %s" % message)

		return message

	"""
	Change the bot's nickname
	"""
	def change_nick(self, nick):
		self.send("USER %s 8 * :Skylar\'s Bot\n" % nick)
		self.send("NICK %s\n" % nick)

		# Make sure this is okay.
		while 1:
			message = self.get_message()
			if message.find('004') != -1:
				break

	"""
	Join a channel
	"""
	def join(self, channel):
		self.send("JOIN " + channel + "\n")

	"""
	Run the bot
	"""
	def run(self):
		self.ircsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.ircsock.connect((self.hostname, self.port))

		self.change_nick(self.nick)
		self.join(self.channel)

		while 1:
			message = self.get_message()

			if message.find("PING :") != -1:
				self.send("PONG :Pong\n")
				continue

			if message.find(' PRIVMSG ') !=-1:
				nick = message.split('!')[0][1:]
				person = Channel(self, nick)

				channel = message.split(' PRIVMSG ')[-1].split(' :')[0]
				channel = Channel(self, channel)

				message = message.split(" :", 1)[1]
				message = message.lower()

				botname = self.nick.lower()

				if not self.nlp.is_subject(botname, message):
					print("DET: Not the subject.")
					continue

				# Extract name.
				if message.startswith(botname):
					message = message.lstrip(botname)
				elif message.endswith(botname):
					message = message.rstrip(botname)

				if nick == "sky" and self.nlp.match_any_ends(message, "shutdown"):
					break

				(module, arguments) = self.nlp.parse(message.strip(" "))
				module.recv(channel, person, arguments)
