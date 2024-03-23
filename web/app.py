import os

# Set the base directory for the pi-velocity-core git repo
base_dir = "./pi-velocity-core"

# Define the main function to run when the app.py script is executed
def main():
    # Print a welcome message and the current working directory
    print("Welcome to the pi-velocity-core app.py script!")
    print(f"Current working directory: {os.getcwd()}")

    # Change the current working directory to the base directory
    os.chdir(base_dir)

    # TODO: Add functionality to the script as needed

    # Print a farewell message and the current working directory
    print("Thanks for using the pi-velocity-core app.py script!")
    print(f"Current working directory: {os.getcwd()}")

# Call the main function to run the app.py script
if __name__ == "__main__":
    main()
