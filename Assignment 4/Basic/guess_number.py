# import random
# def main():
#     secret_num = random.randint(1 , 99)
#     print("I am thinking a num between 1 and 99")

#     guess = int(input("enter your guess number: "))

#     while guess != secret_num:
#         if guess < secret_num:
#             print("your guess is too low")
#         else:
#             print("your guess is too high")
#         print()

#         guess = int(input("guess again my number :"))
#     print("congrats ! you guess my num the num was :" + str(secret_num))

# if __name__ == "__main__":
#     main()



















import random
def main():
    sec_num = random.randint(1, 99 )
    print("i am thinking a number from 1 to 99 guess what")

    guess = int(input("guess my number :"))

    while sec_num != guess:
        if guess < sec_num:
            print("your num is too low")
        else:
            print("your num is too high")
            print()
        guess = int(input("guess again my num "))
    print("congrats ! you guess my number .the number was " + str(sec_num))

if __name__ == "__main__":
    main()