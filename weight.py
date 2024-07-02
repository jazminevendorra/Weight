## This program will display a menu with options to
## 1. Display “10 ways to cut 500 calories” guideline.
## 2. Generate next semester expected weight table.
## 3. Quit.

def main():
    # Intro
    print ("500 Less a Day Makes the Weight Go Away ...")

    # Initialize Quit constant
    QUIT = 3

    # Intialize control variable
    option = 0

    while option != QUIT:

        # Display menu and prompt user for choice
        print("\nChoose one of the following options:")
        print("\t1. Dispaly \"10 ways to cut 500 calories\" guideline.")
        print("\t2. Generate next semester expected weight table.")
        print("\t3. Quit")
        option = int(input("Option: "))

        
        if(option == 1):    # Display 10 ways
            print("\nTry these 10 ways to cut 500 calories every day.")
            print("\t* Swap you snack.")
            print("\t* Cut one high-calorie treat.")
            print("\t* DO NOT drink your calories.")
            print("\t* Make low calorie substitutions.")
            print("\t* Ask for a doggie bag.")
            print("\t* Just say \"no\" to friend food.")
            print("\t* Build a thinner pizza.")
            print("\t* Use a smaller plate.")
            print("\t* Avoid alcohol")
            print("Source: US National Library of Medicine")

        elif(option == 2):  # Display weight

            # Prompt user for starting weight
            weight = int(input("\nPlease enter staring weight in pounds (>=100): "))

            # Validate
            while weight <= 100:

                # Error message
                print("\tError ... Invalid weight. Try again\n")

                # Prompt user for weight input
                weight = int(input("Please enter staring weight in pounds (>=100): "))

            # Display table
            print("-----------------")
            print("Month\tWeight")
            print("-----------------")

            for num in [1,2,3,4,5,6]:
                weight = weight - 4
                print(" ", num,"\t",weight,"lb.")

                
        elif(option == QUIT):  # Quit
            print("\nGood Bye ...")
            print()
        else:   # Invalid option
            print("\nError ... Invalid option. Try Again")


main()
