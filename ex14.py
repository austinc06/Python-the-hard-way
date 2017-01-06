from sys import argv

script, user_name, callsign = argv

prompt = '> '

print("Hi %s, I'm the %s script." % (user_name, script))
print("I'd like to ask you a few questions.")
print("Would you prefer me to call you %s?" % callsign)
Nickname = input(prompt)
if Nickname == 'Yes':
    user = callsign
else:
    user = user_name

print("Do you like me, %s?" % user)
likes = input(prompt)

print("Where do you live, %s?" % user)
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print("""
Alright so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" % (likes, lives, computer))
