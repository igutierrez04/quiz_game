print("Welcome to my quiz game!")

playing = input("Would you like to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! let's play a quiz game about marvel movies!")
score = 0

answer = input("Who many spider-man movies is Miles Morales featured in? ")
if answer.lower() == "2":
    print("Yes! that's right!")
    score += 1
else:
    print("that's incorrect.")

answer = input("Who sacrified themselves in order to bring everyone back in avengers end game? ")
if answer.lower() == "iron man":
    print("Yes! that's right!")
    score += 1
else:
    print("that's incorrect.")

answer = input("Who's black panther's little sister? ")
if answer.lower() == "shuri":
    print("Yes! that's right!")
    score += 1
else:
    print("that's incorrect.")

answer = input("What is star lord's real name? ")
if answer.lower() == "peter quill":
    print("Yes! that's right!")
    score += 1
else:
    print("that's incorrect.")

print(f"You got {((score/4) * 100)}% of the questions correct!")


