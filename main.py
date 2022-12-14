import time
import timeit
import asyncio

# checks if user input is valid
def validity(varb, type):
    # checks for yes/no questions
    if type == "alpha":
        while varb != 'y' and varb != 'n':
            varb = input("Please enter a valid option (y/n): ").lower()
    # checks if user inputted number between 1-15
    elif type == "digit":
        while varb < 1 or varb > 15:
            varb = int(input("Please enter a valid option (1-15): "))
    return varb

# welcoming user to the library
print("Welcome to the Library!")
print("Here is a list of items you may check out:")
# by using time.sleep(0.5) I wanted it to imitate a loading screen
# to make it feel more realistic
time.sleep(0.5)
for x in range(3):
    print('.')
    time.sleep(0.5)

# categories with list of items that can be checked out
items = {"Textbooks": {1: "Calculus 1", 2: "Physics", 3: "Psychology", 4: "Biology", 5: "US History"},
        "Calculators": {6: "Basic Calculator", 7: "Scientific Calculator", 8: "Graphing Calculator"},
        "Cameras": {9: "Canon EOS Rebel T7", 10: "Canon VIXIA HF R800"},
        "Games": {11: "Playing Cards", 12: "Monopoly", 13: "Connect 4", 14: "Twister", 15: "Jenga"}}

# printing out the list
for x in items:
    print("---------------------------")
    # prints the title of the category
    print(x)
    print("---------------------------")
    # printing out the items in the category
    for y in items[x]:
        print(str(y) + ": " + items[x].get(y))

# checking to see if user wants to check out something or not
continue_program = input("Would you like to check something out (y/n)? ").lower()
continue_program = validity(continue_program, "alpha")

# dictionary with what user checks out
checkedout_dict = {}

# if no then it ends the program
if continue_program == 'n':
    print("Thank you for visiting the Library!")
    quit()
else:
    # while user wants to checkout more items
    while continue_program == 'y':
        print("---------------------------")
        item_checkout = int(input("What would you like to check out (1-15)? "))
        item_checkout = validity(item_checkout, "digit")

        # finding which item it is to add to the dictionary checkedout_dict
        if item_checkout <= 5:
            checkedout_dict[item_checkout] = items["Textbooks"].get(item_checkout)
        elif item_checkout > 5 and item_checkout <= 8:
            checkedout_dict[item_checkout] = items["Calculators"].get(item_checkout)
        elif item_checkout > 8 and item_checkout <= 10:
            checkedout_dict[item_checkout] = items["Cameras"].get(item_checkout)
        elif item_checkout > 10 and item_checkout <= 15:
            checkedout_dict[item_checkout] = items["Games"].get(item_checkout)

        # seeing if user wants to check out more
        continue_program = input("Would you like to check something else out (y/n)? ").lower()
        continue_program = validity(continue_program, "alpha")

print("---------------------------")
# seeing how many items and how long the transaction took
async def async_checkingout():
    print("You have a total of " + str(len(checkedout_dict)) + " items.")
    await asyncio.sleep(5)
    print("Your transaction took: " + str(timeit.timeit('main()', number=1)) + " seconds.")
    print("Your items will be ready in an hour.")

# the main function that shows what the user has checked out
async def main():
    # ensure_future to create task
    asyncio.ensure_future(async_checkingout())
    print("Checking out items. This may take a second.")
    time.sleep(1)
    print("Here is a list of items you have checked out: ")
    for x, y in checkedout_dict.items():
        print(y)
    await asyncio.sleep(5)
    print("You have successfully checked out these items.")

# to run the asynch
loop = asyncio.get_event_loop()
loop.run_until_complete(main())

# end of program prints "Have a nice day!"
print("Have a nice day!")
