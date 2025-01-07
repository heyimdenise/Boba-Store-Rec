import random

def boba_picker():
    print("Welcome to the Automatic Decision Maker: Boba Picker Edition!")
    print("Please enter a list of boba stores that you are considering. Type 'done' when you are finished.")

    # collect user input of boba store names
    boba_list= []

    while True:
        boba = input("Enter a boba store: ")     # continue to ask for boba store names
        if boba.lower() == 'done':              # done asking questions when user enters 'done'
            break
        elif boba:                              # add user inputs to list of boba store names
            boba_list.append(boba)
        else:                                   # check if input is empty
            print("Please enter a valid name")

    if not boba_list:                           # check if list is empty
        print("No names entered. Please enter a valid name")

    # randomly pick a boba store 
    final_boba = random.choice(boba_list)
    print(f"\nYou should go to: {final_boba}!")


# run program
if __name__ == "__main__":
    boba_picker()