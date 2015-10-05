# piggetty.py
# 
#
# Joshua Schoonmaker

# Define a function called piggy(string) that returns a string

def piggy(word):
	
	# Magic Happens Here
	# 
# File Header
#

# Define vowels

	vowels = "aeiouAEIOU"

# Ask for word

# Loop through word, one letter at a time

	n = 0
	endword = ""

	for letter in word:
	
	
		# Check if letter is a vowel
		if letter in vowels:
			
			if n == 0:
				
			# True?  We are done
			
				pig = word +  "yay"
				
				return pig
			
			else:
				pig = word[n:] + endword + "ay"
		
				return pig
				
				# False? Consonant
			
		else:
			endword = endword + word[n]
					
			n = n + 1
	

	# Ignore previous line
	
# Open the file *getty.txt* for reading. 

myFile = open("getty.txt","r")

# Open a new file *piggy.txt* for writing.  

newFile = open("piggy.txt","w")

# Read the getty.txt file into a string.  

myString = myFile.read()

# Strip out bad characters (, - .).  

myString = myString.replace(",","")
myString = myString.replace(".","")
myString = myString.replace("-","")


# Split the string into a list of words. 

myList = myString.split()

# Create a new empty string.  

newString = " "

# Loop through the list of words, pigifying each one.  

for word in myList:
 	
# Add the pigified word (and a space) to the new string. 

	newString = newString + str(piggy(word)) + " "
	
# Write the new string to piggy.txt.  

# close the files.

print(newString, file = newFile)

newFile.close()
myFile.close()
