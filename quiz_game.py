print("Welcome to my computer quizz")

playing = input("Are you ready to play?(yes/no): ")

if playing.lower() != "yes":
    quit()


print("Come on! Let's Play:)")


score = 0

answer = input("What is the Halting Problem in computer science?: ")
if answer.lower() == "The Halting Problem proves that no universal algorithm can determine for every program whether it will eventually stop or run forever.":
    print("You Got it!")
    score += 1

else:
    print("Incorrect!")


answer1 = input("Why is P vs NP considered one of the hardest problems in computing?: ")
if answer1.lower() == "It asks whether every problem whose solution can be verified quickly can also be solved quickly.":
    print("You Got it!")
    score += 1
else:
    print("Incorrect!")
    


answer2 = input("What causes deadlock in operating systems?: ")
if answer2.lower() == "Deadlock occurs when multiple processes wait indefinitely for resources held by each other.":
    print("You Got it!")
    score += 1

else:
    print("Incorrect!")
    



answer3 = input("Why is distributed consensus difficult in distributed systems?: ")
if answer3.lower() == "Network delays and failures make it impossible to guarantee agreement under all conditions.":
    print("You Got it!")
    score += 1

else:
    print("Incorrect!")
    

answer4 = input("What is quantum supremacy in computing?: ")
if answer4.lower() == "Quantum supremacy is the point where a quantum computer performs a task impractical for classical computers.":
    print("You Got it!")
    score += 1

else:
    print("Incorrect!")
    
answer5 = input("Why is cache coherence challenging in multicore processors?: ")
if answer5.lower() == "Multiple cores accessing shared memory simultaneously can create inconsistent cached data.":
    print("You Got it!")
    score += 1

else:
    print("Incorrect!")


answer6 = input("What is the Byzantine Generals Problem?: ")
if answer6.lower() == "It describes the difficulty of achieving trust and agreement in systems with unreliable participants.":
    print("You Got it!")
    score += 1

else:
    print("Incorrect!")
    


answer7 = input("Why is cybersecurity impossible to perfect?: ")
if answer7.lower() == "New vulnerabilities, human error, and evolving attack methods constantly create security risks.":
    print("You Got it!")
    score += 1

else:
    print("Incorrect!")
    



answer8 = input("What makes artificial general intelligence difficult to achieve?: ")
if answer8.lower() == "Human-like reasoning, creativity, and contextual understanding remain beyond current AI systems.":
    print("You Got it!")
    score += 1

else:
    print("Incorrect!")
    

answer9 = input("Why is parallel programming hard?: ")
if answer9.lower() == "Synchronization issues, race conditions, and unpredictable execution order make debugging complex.":
    print("You Got it!")
    score += 1

else:
    print("Incorrect!")


print("You Score is " + str(score) + " Question Correct.")

print("You Score is " + str((score/10)*100) + "% Correct.")

