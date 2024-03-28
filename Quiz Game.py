print("Welcome to my computer quiz!")

play = input("Do you want to play")

if play != "yes":
    quit()

print("Okay! let's play")
score = 0
question = input("What does ram stand for").lower()
if question == "random access memory":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")

question = input("What does css stand for").lower()
if question == "cascading style sheet":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")

question = input("What does rom stand for").lower()
if question == "read only memory":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")

print(f"You got {score} questions correct")
print(f"You got {(score /  3 ) * 100}%")