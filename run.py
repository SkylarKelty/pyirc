
from src.bot import PyIRC

server = "irc.kent.ac.uK"
channel = "#skytown"
botnick = "pyrc"

print("Starting up...\n")

bot = PyIRC(server, 6667, channel, botnick)
bot.run()

print("Shutting down...\n")
