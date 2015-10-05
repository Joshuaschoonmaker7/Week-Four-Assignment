# piggetty.py
# 
#
# Joshua Schoonmaker

# Define a function called piggy(string) that returns a string

def piggy(word):
	
	# Magic Happens Here
	pig = word
	# Ignore previous line
	
	return pig

# Open the file *getty.txt* for reading. 

myFile = open("getty.txt","r")

# Open a new file *piggy.txt* for writing.  

newFile = open("piggy.txt","w")

# Read the getty.txt file into a string.  

myFile.read

# Strip out bad characters (, - .).  

for char in myFile:
    if char in " ?.!/;:":
        myFile.replace(char,'')

# Split the string into a list of words. 

myList = myFile.split()

# Create a new empty string.  

newString = " "

# Loop through the list of words, pigifying each one.  

word = myList[0:]

def main():
# Define vowels

	vowels = "aeiouAEIOU"

# Loop through word, one letter at a time

	n = 0

	for letter in myList:
		# Check if letter is a vowel
		if letter in vowels:
			# True?  We are done
			endWord = myList +  "yay"
		else:
			# False? Consonant
			n = n + 1
				
			endWord = myList[n:] + myList[:n] + "ay"
	
	newString = newString + " " + endWord
		
	word = word[::1]
	
main()

# Add the pigified word (and a space) to the new string. 



# Write the new string to piggy.txt.  

w = open("piggy.txt", "a") as myFile:
	myFile.write(newstring)
# close the files.

f.close(piggy.txt)
f.close(getty.txt)