"""
Carlos Guzman
2025-2-12
CH8 Excercise 10
Most Frequent Character
"""

# This function is the main function. It gets users input, calls the function to find the most frequent character.
def main():
    while True:
        user_input = input("Enter a string: ").strip()
        if user_input:
            break
        else:
            print("The string cannot be empty. Please try again.")

    try:
        # Find the users most frequent character
        result = most_frequent_character(user_input)
        print(f'The most frequent character in "{user_input}" is "{result}".')
    except Exception as e:
        print(f'An error occurred: {e}')

# This function returns the most frequent character in the string
def most_frequent_character(s):
    # List that holds the unique characters
    unique_characters = []
    for character in s:
        if character not in unique_characters:
            unique_characters.append(character)

    max_count = 0
    most_freq_char = None

    # Loops over each character to check its frequency
    for character in unique_characters:
        count = s.count(character)
        if count > max_count:
            max_count = count
            most_freq_char = character

    return most_freq_char


if __name__ == "__main__":
    main()
