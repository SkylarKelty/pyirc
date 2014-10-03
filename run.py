
from src import bot

server = "irc.kent.ac.uK"
channel = "#skytown"
botnick = "PyIRC"

print("Starting up...\n")

bot.connect(server)
bot.nick(botnick)
bot.join(channel)
bot.run()

print("Shutting down...\n")
