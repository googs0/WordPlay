from colorama import Fore, Back, Style

# Function that prints out a letter with a colorful background
def printColorfulLetter(letter, isLetterInWord, isLetterInCorrectPlace=False):

  # If it's not in the word, display it with a red background
  if (not isLetterInWord):
    print(Back.RED + Fore.WHITE + f" {letter} ", end="")

  # If it's in the word...
  else:

    # ...and it's also in the right place, display it with a green background
    if (isLetterInCorrectPlace):
      print(Back.LIGHTGREEN_EX + Fore.WHITE + f" {letter} ", end="")

    # ...but in the wrong place, display it with a yellow background
    else:
      print(Back.LIGHTYELLOW_EX + Fore.BLACK + f" {letter} ", end="")


# Display a guess, where each letter is color-coded by it's accuracy
def printGuessAccuracy(guess, actual):

  # Loop through each index/position
  for index in range(6):

    # Grab the letter from the guess
    letter = guess[index]

    # Check if the letter at this index of the user's guess is in the secret word AT ALL or not
    if letter in actual:

      # If the letter is in the secret word, is it also AT THE CURRENT INDEX in the secret word?
      if (letter == actual[index]):

        # Then print it out with a green background
        printColorfulLetter(letter, True, True)

      # If it's not at the current index, we know by this point in the code that it's still used in the secret word somewhere...
      else:
        # ...so we'll print it out with a yellow background
        printColorfulLetter(letter, True, False)

    # ...but if the letter is not in the word at all...
    else:
      # ...print it out with a red background
      printColorfulLetter(letter, False, False)

    # Don't worry about the line of code below, it works. It just handles the transition between colors
    print(Style.RESET_ALL + " ", end="")

# gets 6 letter word from user
def getSixLetterInput():
  userWord = ""
  while (len(userWord) != 6) or (not userWord.isalpha()):
    userWord = input("Enter six letter word: ")
  return userWord

# Create title and directions

title = """


██╗    ██╗ ██████╗ ██████╗ ██████╗     ██████╗ ██╗      █████╗ ██╗   ██╗
██║    ██║██╔═══██╗██╔══██╗██╔══██╗    ██╔══██╗██║     ██╔══██╗╚██╗ ██╔╝
██║ █╗ ██║██║   ██║██████╔╝██║  ██║    ██████╔╝██║     ███████║ ╚████╔╝ 
██║███╗██║██║   ██║██╔══██╗██║  ██║    ██╔═══╝ ██║     ██╔══██║  ╚██╔╝  
╚███╔███╔╝╚██████╔╝██║  ██║██████╔╝    ██║     ███████╗██║  ██║   ██║   
 ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚═════╝     ╚═╝     ╚══════╝╚═╝  ╚═╝   ╚═╝   
                                                                        
"""

directions = """Welcome to Word Play! Test your lexical valor! 

-- You have 6 attempts to guess the secret word
-- The secret word is exactly 6 letters long...no more or less

    -- If the letter is in the correct place it will display green
    -- If the letter is in the secret word but in the incorrect place it will display yellow
    -- If the letter is not in the secret word it will display red

let's get started!
"""

print(title)
print(directions)

# Create secret word for user to guess
secretWord = "answer"

# Initialize number of guesses
attempts = 6


while attempts > 0:
  userGuess = getSixLetterInput()
  printGuessAccuracy(userGuess, secretWord)
  print()

  # If user wins
  if (userGuess == secretWord):
    print("Congratulations! You're a true wordsmith!")
    break
  attempts -= 1

  # if user loses
  if attempts == 0:
    print(f"Game over! Better luck next time! The word was: {secretWord} ")
