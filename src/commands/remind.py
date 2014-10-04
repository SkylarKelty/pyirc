
import time, datetime

def recv(channel, person, args):
	(subject, seconds, message) = args

	dt = datetime.datetime.fromtimestamp(
        time.time() + seconds
    ).strftime('%Y-%m-%d %H:%M:%S')

	channel.message("%s: okay, I will remind you at %s" % (subject, dt))