# 
# File Header
#

def main():
# Define vowels

	vowels = "aeiouAEIOU"

# Ask for word

	word = input("Please enter a word: ")

# Loop through word, one letter at a time

	n = 0

	for letter in word:
		# Check if letter is a vowel
		if letter in vowels:
			# True?  We are done
			endWord = word +  "yay"
		else:
			# False? Consonant
			n = n + 1
				
			endWord = word[n:] + word[:n] + "ay"
		break
		
		
	print(endWord)
	
main()