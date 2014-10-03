import socket

ircsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def connect(hostname, port = 6667):
	ircsock.connect((hostname, port))

def ircsend(msg):
	ircsock.send(msg.encode())

def getnextmsg():
	msg = ircsock.recv(2048).decode()
	msg = msg.strip('\n\r')
	print(msg)
	return msg

def nick(nick):
	ircsend("USER " + nick + " 8 * :Skylar\'s Bot\r\n")
	ircsend("NICK " + nick + "\n")

	# Make sure this is okay.
	while 1:
		msg = getnextmsg()
		if msg.find('004') != -1:
			break

def join(channel):
	ircsend("JOIN " + channel + "\r\n")

def pong():
	ircsend("PONG :Pong\r\n")  

def run():
	while 1:
		msg = getnextmsg()

		if msg.find("PING :") != -1:
			pong()
			continue

		if msg.find(' PRIVMSG ') !=-1:
			nick = msg.split('!')[0][1:]
			channel = msg.split(' PRIVMSG ')[-1].split(' :')[0]
			message = msg.split(" :", 1)[1]

			if nick == "sky"and message.startswith("shutdown"):
				break