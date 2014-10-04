import random

"""
Recieve a hello command
"""
def recv(channel, person, arguments):
	exclaim_responses = ["hey", "hi", "hello"]
	question_responses = ["sup", "how are you", "how's it going"]

	responses = []
	punct = ""
	if (random.choice([1, 2]) == 1):
		punct = "!"
		responses = exclaim_responses
	else:
		punct = "?"
		responses = question_responses

	response = "%s %s%s" %(random.choice(responses), person.name, punct)

	channel.message(response)
