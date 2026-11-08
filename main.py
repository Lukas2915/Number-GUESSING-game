import random

choice = 0
numbers = random.randint(1, 11)
attempts = 3

lost = 0
won = 0
total_games = 0
history = []

print("""  
            ======= NUMBER GUESSING GAME =======

            1. Start Game
            2. Show History
            4. Exit
    
            ===================================
        """)
while True :
    choice = int(input("Choose an option: "))
    if choice == 4 :
        print("Bey-Bey! Thanks for visit! ")
        print()
        break
    
    elif  choice == 1:
        total_games += 1
        while attempts > 0:
            print()
            num = int(input("Please enter write number :  "))
            print()
            
            if num == numbers : 
                print("You guess number!", numbers)
                print(f"you have left {attempts} attempt" )
                print("You WON!")
                won += 1
                history.append(f"games {total_games}")
            
            elif num > numbers :
                print("Number is too hight! Invalid number! ")
                attempts -= 1
                print(f"you have left {attempts} attempt" )   
                
            elif num < numbers :
                print("Number is too low! Invalid number! ")
                attempts -= 1  
                print(f"you have left {attempts} attempt" )   
                
        if attempts <= 0 :
            print(f'''
            You have left {attempts} attempt
                              
            You Lost..! huh..
                ''')
            print("")
            lost += 1
            history.append(f"games {total_games}")
            
    elif choice == 2 :
        print("\n======= GAME HISTORY =======")

        if len(history) == 0:
            print("NO games played yet")
        else:
            for index, result in enumerate(history):
                print(f"{index}, {result}")
        
        
    else :
        print ("Invalin choice number!")