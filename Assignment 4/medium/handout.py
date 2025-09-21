import random

NUM_ROUNDS = 5

def main():
    print("Welcome to the High-Low Game!")
    print('--------------------------------')
    
    score = 0

    for round_num in range(1, NUM_ROUNDS + 1):
        print(f"\nRound {round_num} of {NUM_ROUNDS}")

        player_num = random.randint(1, 100)
        computer_num = random.randint(1, 100)

        print(f"Your number is: {player_num}")
        
        guess = input("Do you think your number is higher (h) or lower (l) than the computer's? ").lower()
        
        if (guess == "h" and player_num > computer_num) or (guess == "l" and player_num < computer_num):
            print("You guessed right! ✅")
            score += 1
        else:
            print("Wrong guess ❌")
        
        print(f"The computer's number was: {computer_num}")
        print(f"Your current score: {score}")

    print("\nGame Over!")
    print(f"Your final score is: {score} out of {NUM_ROUNDS}")

if __name__ == "__main__":
    main()
