import random

##====================USER INPUTS====================##

# Add terms and definitions here
# Make sure there are the same amt of terms as there are defs

terms = ["Ammonium", "Hydroxide", "Cyanide", "Nitrate", "Sulfate", "Phosphate", "Chromate", "Carbonate", "Acetate", "Permanganate", "Nitrite", "Sulfite", "Phosphite", "Dichromate"]

defs = ["NH_4^+", "OH^-", "CN^-", "NO_3^-", "SO_4^2-", "PO_4^3-", "CrO_4^2-", "CO_3^2-", "C_2H_3O_2^-", "MnO_4^-", "NO_2^-", "SO_3^2-", "PO_3^3-", "Cr_2O_7^2-"]

##========================================##


# print title logo function
def title():
    print(" _____      _        _                _ _ _____ _   ")
    print("|  __ \    | |      (_)         /\   | | |_   _| |")
    print("| |__) |___| |_ __ _ _ _ __    /  \  | | | | | | |_")
    print("|  _  // _ \ __/ _` | | '_ \  / /\ \ | | | | | | __|")
    print("| | \ \  __/ || (_| | | | | |/ ____ \| | |_| |_| |_ ")
    print("|_|  \_\___|\__\__,_|_|_| |_/_/    \_\_|_|_____|\__|")
    print()
    print()


prevChoice = ""

# copy inputs into a list so it can be modified without modifiying original
terms_cpy = terms
defs_cpy = defs
learned = []

# welcome screen
print("Hello! Welcome to")
print()
title()

# ask user for what mode they want to do
ans = input(
    "What mode would you like to learn in? (Type small, medium, large): ")
ans = ans.lower()
if ans == "small":
    length = 50
elif ans == "medium":
    length = 100
elif ans == "large":
    length = 200
else:
    length = 100

# create the chances to weight the random selections
chance = []
for i in range(len(terms_cpy)):
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
        rIndex = random.choices(range(len(terms_cpy)), weights=chance, k=2)
        rIndex = int(rIndex[0])
        if len(terms_cpy) > 1:
            while terms_cpy[rIndex] == prevChoice:
                rIndex = random.choices(range(len(terms_cpy)),
                                        weights=chance,
                                        k=2)
                rIndex = int(rIndex[0])
            prevChoice = terms_cpy[rIndex]

        print(chance)
        ans = input(">> " + terms_cpy[rIndex] + " ")

        # check if question is right
        # if right, subtract the weight by 5, if wrong, add weight by 5
        if ans == defs_cpy[rIndex]:
            chance[rIndex] -= 10
        else:
            chance[rIndex] += 10
            print("no that wrong.")
            ans = input("Type \"" + terms_cpy[rIndex] + " is " +
                        defs_cpy[rIndex] + "\" to continue: ")

        # remove any items that have a weight of 0
        toremove = []
        for i in range(len(terms_cpy)):
            if chance[i] == 0:
                toremove.append(i)
        if len(terms_cpy) >= 1:
            for j in range(len(toremove)):
                learned.append(
                    terms_cpy.pop(toremove[j]) + " -> " +
                    defs_cpy.pop(toremove[j]))
                chance.pop(toremove[j])
        else:
            break

        # increment question counter
        questions += 1

    # continue out of the nested loop if all terms are completed
    if len(terms_cpy) < 1:
        break

    # generate summary
    tolearn = []
    for i in range(len(terms_cpy)):
        tolearn.append(terms_cpy[i] + " -> " + defs_cpy[i])

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
