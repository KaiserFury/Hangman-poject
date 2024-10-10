
import random 
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

print("Welcome to the Friend name gussing game.\nYou have to enter the letter which are in Your Friends name.")
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']





name=["abhi","pritam","pinku","durga","devkumar","pawan","roshan","lasan","janu"]
random_letter=random.choice(name)
size_list=["_"]*len(random_letter)


chances=6
while chances!=0 :
    
    user=input("Enter the letter: ").lower()
    clear()
    
    if user in size_list:
        print("you already guessed!")    
        

    for i in range(len(random_letter)):
        if random_letter[i]==user:
            size_list[i]=random_letter[i]
            
    
    print(' '.join(size_list))
 # agar ye dono condition satisfied nhi kar ta hai to direct line 90 pe chala jaega
 
   
    if size_list.count("_")==0:
        print(stages[chances]) 
        print("You won!")
        break

    elif user in random_letter:
        print(f"You guessed {user}")
    
    elif user not in random_letter:
        chances-=1
        print(f"Your gussesd {user}, that's not in the word. You lose a life.")
        if chances==0:
            print("You lose!")
            print(stages[chances]) 
            break
            
    print(stages[chances])     