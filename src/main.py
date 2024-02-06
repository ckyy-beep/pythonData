def main():
    # Game Introduction
    print("Welcome to the Adventure Game!")
    print("In this game, you will be exploring a mysterious world full of challenges.")
    
    # Character Creation
    player_name = input("Enter your character's name: ")
    print(f"Welcome, {player_name}! Your adventure begins now.")

    # Starting the main game loop
    while True:
        print("\nYou are in a dark forest. You can go left, right, or forward.")
        choice = input("What do you want to do? (left/right/forward/quit): ").lower()

        if choice == "quit":
            print("Thanks for playing!")
            break
        elif choice == "left":
            print("You went left and found a treasure chest!")
            # Here, you can add more logic, like opening the chest, finding items, etc.
        elif choice == "right":
            print("You went right and encountered a monster!")
            # This can lead to a combat system or a puzzle to escape.
        elif choice == "forward":
            print("You move forward and find a mysterious door.")
            # This can lead to a new area or a puzzle.
        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()
