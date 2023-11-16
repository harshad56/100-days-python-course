morse_code = {'A': '•-', 'B': '-•••', 'C': '-•-•', 'D': '-••', 'E': '•', 'F': '••-•', 'G': '--•', 'H': '••••',
              'I': '••', 'J': '•---', 'K': '-•-', 'L': '•-••', 'M': '--', 'N': '-•', 'O': '---', 'P': '•--•',
              'Q': '--•-', 'R': '•-•', 'S': '•••', 'T': '-', 'U': '••-', 'V': '•••-', 'W': '•--', 'X': '-••-',
              'Y': '-•--', 'Z': '--••', '1': '•----', '2': '••---', '3': '•••--', '4': '••••-',
              '5': '•••••', '6': '-••••', '7': '--•••', '8': '---••', '9': '----•', '0': '-----'}

user_input = ""

while user_input.lower() != "end":

    user_input = input("Please enter your string: ")
    morse_string = ""

    if user_input.lower() != "end":
        for letter in user_input:
            if letter.upper() in morse_code:
                morse_string += morse_code[letter.upper()]
            else:
                morse_string += letter
            morse_string += " "
        print(
            f"The string you entered is '{user_input}'.Its morse ciphered version is {morse_string}")
