# Roch Paper Scissor game
# import random library for app random choice
import random

def main():
    
    # say welcom to user
    print("\nHi!\nMy name is Kimia and welcome to my Rock, Paper, Scissor game. :D\n")
    
    # game words
    game_words = ["Rock", "Scissor", "Paper"]
    
    # get user's name
    player_name = input("Enter your name: ").strip().capitalize()
    
    # get final score from user
    final_score = user_input_number()
    
    # definition scores
    player_score = 0
    kimia_score = 0
    
    while player_score != final_score and kimia_score != final_score :
        
        # get user's choice, the user can break and if type another expected word app get choice again
        player_choice = input("Enter your choice: ").strip().capitalize()
        
        if player_choice == "Exit":
            break
        elif player_choice not in game_words:
            print("\n-Wait, what?! :/\n")
            continue
        
        # determine the random word and compare with the player's choice
        kimia_choice = random.choice(game_words)
        print("My choice:",kimia_choice)
    
        if player_choice == "Paper" and kimia_choice == "Rock":
            print("-Lucky :') ")
            player_score += 1
            
        elif player_choice == "Scissor" and kimia_choice == "Paper":
            print("-Lucky :') ")
            player_score += 1
            
        elif player_choice == "Rock" and kimia_choice == "Scissor":
            print("-Lucky :') ")
            player_score += 1
                
        elif player_choice == "Paper" and kimia_choice == "Scissor":
            print("-Loser =)) ")
            kimia_score += 1
            
        elif player_choice == "Rock" and kimia_choice == "Paper":
            print("-Loser =)) ")
            kimia_score += 1
            
        elif player_choice == "Scissor" and kimia_choice == "Rock":
            print("-Loser =)) ")
            kimia_score += 1
            
        else:
            print("-Let's try again :)) ")  
        
        print(f"{player_name}: {player_score}\nKimia: {kimia_score}\n")

    # show resualt to user
    if player_score == final_score:
        print("Winner winner , chicken dinner :))")
    else:
        print("See you next time :)")

def user_input_number():
    while True:
        try:
            final_score = int(input("How many points do you want to play? "))
            return final_score
            
        except ValueError:
            print("\n-Okay smart guy, now give me an integer. :)\n")

if __name__ == "__main__":
    main()