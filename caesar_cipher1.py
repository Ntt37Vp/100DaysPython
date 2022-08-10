# Day 8 Output - Caesar Cipher
from art_works import caesar

print(caesar)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def caesar(input_text, input_shift, input_direction):
    end_text = ""
    # Common bug is having the if block inside the for loop
    if input_direction == "decode":
        input_shift *= -1
    for char in input_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + input_shift
            end_text += alphabet[new_position]
        else:
            end_text += char
    print(f"The {input_direction}d text is {end_text}")


should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26

    caesar(input_text=text, input_shift=shift, input_direction=direction)

    replay = input("Type yes if you want to continue. Otherwise, type no. ")
    if replay == "No" or "no":
        should_end = False
        print("Goodbye.")

# def encrypt(plain_text, shift_amount):
#     cipher_text = ""
#     for letter in plain_text:
#         position = alphabet.index(letter)
#         new_position = position + shift_amount
#         if new_position > 25:
#             new_position = new_position - 26
#         new_letter = alphabet[new_position]
#         cipher_text += new_letter
#     print(f"The encrypted text is {cipher_text}")
#
# def decrypt(cipher_text, shift_amount):
#     plain_text = ""
#     for letter in cipher_text:
#         position = alphabet.index(letter)
#         new_position = position - shift_amount
#         new_letter = alphabet[new_position]
#         plain_text += new_letter
#     print(f"The decrypted text is {plain_text}")
