import random

# declare term and def lists
terms = []

defs = []

# variable for the default length of session
DEFAULT_LENGTH = 100

# reads file
inputF = open('INPUT_TERMS_AND_DEFS_HERE.txt', 'r')
Lines = inputF.readlines()

# variable to store the line number where the instructions end in the input file
END_OF_INSTRUCTIONS_LINE_NUM = 6

# reads terms and defs from file into list, skipping the "how to use" lines
ct = 1
for line in Lines:
    if ct <= END_OF_INSTRUCTIONS_LINE_NUM:
        ct += 1
    else:
        termt, deft = line.split("-")
        terms.append(termt.strip())
        defs.append(deft.strip())

# print title logo function
def title():
    print(" _____      _        _                _ _ _____ _   ")
    print("|  __ \    | |      (_)         /\   | | |_   _| |")
    print("| |__) |___| |_ __ _ _ _ __    /  \  | | | | | | |_")
    print("|  _  // _ \ __/ _` | | '_ \  / /\ \ | | | | | | __|")
    print("| | \ \  __/ || (_| | | | | |/ ____ \| | |_| |_| |_ ")
    print("|_|  \_\___|\__\__,_|_|_| |_/_/    \_\_|_|_____|\__| Alpha v1.5")
    print()
    print()

# preve choice so you don't get the same question 
prevChoice = ""

# for storing terms completely learned
learned = []

# welcome screen
print("Hello! Welcome to")
print()
title()

# ask user for what mode they want to do
ans = input("What mode would you like to learn in? (Type small, medium, large): ")
ans = ans.lower()
if ans == "small":
    length = 30
elif ans == "medium":
    length = 100
elif ans == "large":
    length = 200
else:
    print("Invalid input - setting length to default")
    length = DEFAULT_LENGTH

print()

ans = input("Would you like the questions to ask for (a) the corresponding definition to the given term, or (b) the correspodning term to the given definition? (a) terms or (b) definitions? (type a or b)")
ans = ans.lower()
if ans == "a":
    questionsList = terms
    answers = defs
elif ans == "b":
    questionsList = defs
    answers = terms
else:
    print("Invalid input - defaulting to choice a")
    questionsList = terms
    answers = defs

# create the chances to weight the random selections
chance = []
for i in range(len(questionsList)):
    chance.append(length)

questions = 0

# loop until all terms are learned
while True:
    while questions < 8:
        # clear console and print title
        print(chr(27) + '[2j')
        print('\033c')
        print('\x1bc')
        title()

        ## pick question and ask it
        # make sure question isnt the same as the immediate last one
        rIndex = random.choices(range(len(questionsList)), weights=chance, k=2)
        rIndex = int(rIndex[0])
        if len(questionsList) > 1:
            while questionsList[rIndex] == prevChoice:
                rIndex = random.choices(range(len(questionsList)),
                                        weights=chance,
                                        k=2)
                rIndex = int(rIndex[0])
            prevChoice = questionsList[rIndex]

        print(chance)
        ans = input(">> " + questionsList[rIndex] + " ")

        # check if question is right
        # if right, subtract the weight by 5, if wrong, add weight by 5
        if ans == answers[rIndex]:
            chance[rIndex] -= 10
        else:
            chance[rIndex] += 10
            print("no that wrong.")
            ans = input("Type \"" + questionsList[rIndex] + " is " +
                        answers[rIndex] + "\" to continue: ")

        # remove any items that have a weight of 0
        toremove = []
        for i in range(len(questionsList)):
            if chance[i] == 0:
                toremove.append(i)
        if len(questionsList) >= 1:
            for j in range(len(toremove)):
                learned.append(
                    questionsList.pop(toremove[j]) + " -> " +
                    answers.pop(toremove[j]))
                chance.pop(toremove[j])
        else:
            break

        # increment question counter
        questions += 1

    # continue out of the nested loop if all terms are completed
    if len(questionsList) < 1:
        break

    # generasmte summary
    tolearn = []
    for i in range(len(questionsList)):
        tolearn.append(questionsList[i] + " -> " + answers[i])

    learning = []
    for j in range(len(tolearn)):
        k = 0
        if chance[j] < length:
            learning.append(tolearn.pop(k))
            k -= 1
        k += 1

    # print sectional summary to user
    print(chr(27) + '[2j')
    print('\033c')
    print('\x1bc')
    title()
    print("Great Progress!")
    print()
    print("Here's a summary of everything thus far:")
    print("==========================================")
    print("Terms learned: " + str(learned))
    print()
    print("Terms still being learned: " + str(learning))
    print()
    print("Terms to learn: " + str(tolearn))
    print("==========================================")
    print()
    input("Enter any character or just press enter to continue: ")
    questions = 0

# you win
print(chr(27) + '[2j')
print('\033c')
print('\x1bc')
title()
print("Congrats!  You've studied the terms pretty well!")
