
import calendar, datetime
from dateutil import parser
from src.commands import *

class NLP:
	"""
	Parse a message
	"""
	def parse(self, subject):
		print("NLP recv: %s" % subject)

		if subject.startswith("remind"):
			print("NLP det: remind")
			try:
				return (remind, self.get_remind_args(subject))
			except:
				pass

		if self.match_any_ends(subject, ("hello", "hi", "hey", "yo")):
			print("NLP det: hello")
			return (hello, [])

		return (noaction, [])

	"""
	Matches anything in the tuple at the beginning or
	end of a string
	"""
	def match_any_ends(self, subject, match):
		return subject.startswith(match) or subject.endswith(match)


	"""
	Am I the subject of a message?
	"""
	def is_subject(self, nick, message):
		return self.match_any_ends(message, nick)

	"""
	Grabs args for remind
	"""
	def get_remind_args(self, subject):
		parts = subject.split(" ")
		message = " ".join(parts[parts.index("to"):])

		dt = " ".join(parts[3:parts.index("to")])
		print ("DTParse:", dt)

		nowtime = calendar.timegm(datetime.datetime.now().timetuple())

		if parts[2] == 'in':
			epoch = datetime.datetime.utcfromtimestamp(0)
			dt = parser.parse(dt, fuzzy=True, default=epoch)
			thentime = nowtime + calendar.timegm(dt.timetuple())
		elif parts[2] == 'at':
			dt = parser.parse(dt, fuzzy=True)
			thentime = calendar.timegm(dt.timetuple())

		return (parts[1], thentime - nowtime, message)