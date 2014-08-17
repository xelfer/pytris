import re

s = 0
match = re.match(r'[A-Z]', s, flags=0)
if match:
	print "matched something"
