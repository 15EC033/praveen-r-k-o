l = input("Input an letter of the alphabet: ")

if l in ('a', 'e', 'i', 'o', 'u'):
	print("%s it is a vowel." % l)
elif l == 'y':
	print("Sometimes letter y stand for vowel, sometimes stand for consonant.")
else:
	print("%s it is a consonant." % l) 
