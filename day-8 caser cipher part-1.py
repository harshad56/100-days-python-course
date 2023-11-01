alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
            'Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
            'Z']

direction = input("type 'encode' to encrypt,type 'decode' to decrypt:\n")

text = input("type your message:\n").upper()
shift = int(input("type the shift number:\n"))

#   TODO-1: CREATE A FUNCTION CALLED "encerpt" that takes 'takes' and 'shift' as input


def encrypt(plain_text, shift_amount):
    cipher_text = ""
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        new_letter = alphabet[new_position]
        cipher_text += new_letter

    print(f"the encoded text is {cipher_text} ")
# TODO-1: CREATE  a different function called 'decrypt' that takes the 'text' and 'shift' as input as inputs.


def decrypt(cipher_text, shift_amount):
    plain_text = ""
    for letter in cipher_text:
        position = alphabet.index(letter)
        new_position = position - shift_amount
        new_letter = alphabet[new_position]
        plain_text += new_letter
    print(f"the decoded text is {plain_text} ")


#  TODO-3 :check if the user wanted to encrypt or decrypt the message by checking the 'direction' varaible.then call the correct function based as that 'direction' varaible .you should be able to text the code to encrypt and decrypt  a message.
if direction == "encode":
    encrypt(plain_text=text, shift_amount=shift)
elif direction == "decode":
    decrypt(cipher_text=text, shift_amount=shift)
