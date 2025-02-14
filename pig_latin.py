"""
Carlos Guzman
2025-2-12
CH8 Exercise 12
Pig Latin
"""

# This function prompts the user for input and displays the result
def main():
    # Prompts user to enter a sentence until a sentence is entered
    while True:
        user_input = input("Enter a string to convert to Pig Latin: ").strip()
        if user_input:
            break
        else:
            print("Please enter a string")

    try:
        # Splits the sentence into individual words
        split_string = user_input.split()
        new_string = ""

        # Converts each word into pig latin
        for word in split_string:
            if len(word) == 1:
                new_word = word.upper() + "AY"
            else:
                new_word = word[1:].upper() + word[0].upper() + 'AY'
            new_string += new_word + " "

        # Displays the pig latin sentence
        print(new_string)
    except Exception as e:
        # Handles any errors
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
