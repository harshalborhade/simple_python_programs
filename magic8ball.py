import time
import random
def main():
    responses = ["It is certain",
    "Without a doubt",
    "You may rely on it",
    "Yes definitely",
    "It is decidedly so",
    "As I see it, yes",
    "Most likely","Yes",
    "Outlook good",
    "Signs point to yes",
    "Reply hazy try again",
    "Better not tell you now",
    "Ask again later",
    "Cannot predict now",
    "Concentrate and ask again",
    "Don’t count on it",
    "Outlook not so good",
    "My sources say no",
    "Very doubtful",
    "My reply is no"]
    question = input("What is your question? ")
    print("So you are asking",question)
    for _ in range(2):
        print("thinking.  ",end="\r")
        time.sleep(1)
        print("thinking.. ",end="\r")
        time.sleep(1)
        print("Thinking...",end="\r")
        time.sleep(1)
    print("I have the answer! It is:")
    r = random.randint(0,len(responses) - 1)
    print(responses[r])

main()