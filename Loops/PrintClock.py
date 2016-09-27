hours = 0
minutes = 0
seconds = 0
milliseconds = 0

while hours < 24:
	minutes = 0
	while minutes < 60:
		seconds = 0
		while seconds < 60:
			milliseconds = 0
			while milliseconds < 1000:
				print( (str)(hours) + ":" + (str)(minutes) + ":" + (str)(seconds) + "." + (str)(milliseconds) )
				milliseconds += 1
			seconds += 1
		minutes += 1
	hours += 1
