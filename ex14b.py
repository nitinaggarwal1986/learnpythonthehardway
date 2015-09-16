from sys import argv

script, user_name, company= argv
prompt = 'Your Answer> '

print "Hi %s from %s, I'm the %s script." % (user_name, company, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "Is that where your company at?"
lives_near_company = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, so you said %r about liking me.
You live in %r. You said %r to living near your company, %r.
And you have a %r computer. Nice.
""" % (likes, lives, lives_near_company, company, computer)