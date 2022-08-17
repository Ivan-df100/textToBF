text = input("Enter Text: ")

result = ""

var = 0

for character in text:
	difference = var - ord(character)
	if difference == 0:
		...
		
	elif difference > 0:
		result += "-"*difference
		var -= difference
		
	elif difference < 0:
		result += "+"*(difference*-1)
		var += difference*-1
		
	result += "."
		
print(result)
input()