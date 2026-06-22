import datetime
import time

name = input("Enter Your Name : ")
presentHours = datetime.datetime.now().hour

if 5 <= presentHours <= 11:
    print("Good Morning... ",name)
elif 11 <= presentHours <= 17:
    print("Good Afternoon... ",name)
elif 17 <= presentHours <= 20:
    print("Good evening... ",name)
else:
    print("Good Night...", name)

print("namaste! Welcome to Rlue Based ChatBot...")
print("You can ask me basic question,Type 'bye' to exit from the ChatBot... ")

# chatBot Memory creation [ dictionary of responses ]

responses = {
    "hello" : "hi, welcome. How can help you ??",
    "how are you" : "I am very fine. thank you",
    "who are you" : "I am Smart AI ChatBot...",
    "motivate me" : "Keep going. Every bug of your project makes you a batter devloper...",
    "happy" : "Great to hear that",
    "function kaya hota he" : "chapter 7 dekho"
}

# method/ function  to get response of ChatBot

def getResponseOfBot(userQuestion):
    userQuestion = userQuestion.lower()
    for eachKey in responses:
        if eachKey in userQuestion:
            return responses[eachKey]
    return " Abhi muje vo nahi aata , me abhi sikh raha hu... "

# take user input 

while True:

    userInput = input("Please ask your Question : ")
    reply = getResponseOfBot(userInput)
    print("Bot Response : ", reply)

    if "bye" in userInput.lower():
        break