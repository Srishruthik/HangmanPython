import random
import string
import time
class game:
    def __init__(self):
        """ 
        Constructor 
        """

        self.game = True
        self.word = ""#selects a randomw word form words.txt
        self.gameWord = [] #this shows the word in dashes(----)
        self.attempts = 0 #total attempts in total for the player to guess
        self.turns = 0 #total attempts it took for the player to guess the word
    
    
    def openTxtFile(self):
        '''
        Reads the txt file
        
        '''
        

        words = None #contains all the words un words.txt in the list(arr)
        with open("words.txt",'r') as f:
            for word in f:
                words = (word.split(" "))

        self.generateWord(words)

    def generateWord(self,words):
        '''
        generates the new word from the list:words
        '''
        randomWord = random.choice(words)
        self.attempts+=len(randomWord)+10
        self.word = randomWord.lower()       
        self.replaceWordtoDash()


    def replaceWordtoDash(self):
        '''
        This replaces the random word chosen from the file to dashes(-)
        if the random word is "Hello" then -> "-----"
        '''

        for i in range(len(self.word)):
            self.gameWord.append("-")
        self.printWord()

    def printWord(self):
        """ 
        prints the word in a string format 
        """

        new_str = ""

        for i in range(len(self.gameWord)):
            new_str+=self.gameWord[i]

        print(new_str)

    def getUserInput(self):
        user = input("Enter: ")
        if len(user) > 1 or len(user) == 0:
            print("Enter only 1 letter!")
            self.getUserInput()
        
        elif user.lower() in string.ascii_lowercase:

            if user in self.gameWord:
                print("You already attempted the letter. Try a new letter")
                self.getUserInput()
            else:
                self.validateInput(user.lower())
            
        elif user.isdigit():
            print("No numbers")
            self.getUserInput()

        else:
            print("No symbols. ONLY LETTERS! ")
            self.getUserInput()


        
        
        

    def validateInput(self,user):
        '''
        Checks if the txt by the user is in the word
        '''
        new_indexs = []
        
        for i in range(len(self.gameWord)):
            if user == self.word[i]:
                #self.gameWord[i] = user
                new_indexs.append(i)

        if len(new_indexs) >= 1:
           
            print(f"{user} is in the word")
            total_turns = self.attempts-self.turns
            print(f"You have {total_turns} attempts left")
            print("\n")

            for index in (new_indexs):
                self.gameWord[index] = user
        else:
            print("\n")
            print(f"{user} is NOT found!.")
            total_turns = self.attempts-self.turns
            print(f"You have {total_turns} attempts left")
            print("Try a new letter")
    

    

    def __main__(self):
        '''
        The main
        '''
        for i in range(10):
            print("\n")
        self.openTxtFile()
        print("Welcome to HANGMAN created by Srishruthik Alle")
        time.sleep(0.7)
        print("Rules are simple. Just guess the words with limited amount of guesses!")
        time.sleep(0.13)
        print("You have",self.attempts,"attempts to guess the word")
        
       
        while self.game:
            
            if "-" in self.gameWord:
                print(*self.gameWord)
                self.turns+=1
                self.getUserInput()
                total_turns = self.attempts-self.turns
                if self.turns == self.attempts:
                    self.game = False
                    print("Game over!")
                    print(f"The word was {self.word}")
                    print("Good luck next time :)")
                elif total_turns < self.gameWord.count("-"):
                    #if the remaining turns left is less than the remaing letters needed then quit
                    self.game = False
                    print("Sorry! You dont have enough attempts to guess the word!")
                    print(f"The word was {self.word}")
                    print("Good luck next time :)")
                
            else:#game is over(The user has guessed the word correctly)
                print("YESSS!!!!! You guessed the word!")
                print(f"The word was {self.word}")
                print("Total attempts: ",self.turns)
                self.game = False
      
g = game()

g.__main__()