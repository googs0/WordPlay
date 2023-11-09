from colorama import Fore, Back, Style


def printColorfulLetter(letter, isLetterInWord, isLetterInCorrectPlace=False):
  if (not isLetterInWord):
    print(Back.RED + Fore.WHITE + f" {letter} ", end="")
    
  else:
    
    if (isLetterInCorrectPlace):
      print(Back.LIGHTGREEN_EX + Fore.WHITE + f" {letter} ", end="")
    else:
      print(Back.LIGHTYELLOW_EX + Fore.BLACK + f" {letter} ", end="")

def printGuessAccuracy(guess, actual):

  # Loop through each index/position
  for index in range(6):
    letter = guess[index]
    if letter in actual:
      if (letter == actual[index]):
        printColorfulLetter(letter, True, True)
      else:
        printColorfulLetter(letter, True, False)

    else:
      printColorfulLetter(letter, False, False)
    print(Style.RESET_ALL + " ", end="")

def getSixLetterInput():
  userWord = ""
  while (len(userWord) != 6) or (not userWord.isalpha()):
    userWord = input("Enter six letter word: ")
  return userWord

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
  if (userGuess == secretWord):
    print("Congratulations! You're a true wordsmith!")
    break
  attempts -= 1
  if attempts == 0:
    print(f"Game over! Better luck next time! The word was: {secretWord} ")
