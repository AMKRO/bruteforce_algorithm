from cracker import Cracker

def retrievePassword():
    p = input("Enter password to bruteforce: ")
    return p

def main():
    letters = Cracker.splitter(retrievePassword())
    print(letters)

main()