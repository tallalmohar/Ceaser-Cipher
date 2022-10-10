#imported files
import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
            'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
            's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


# The logo of the Cipher
logo = art.logo
print(logo)


# We can create a single mega function that can combine the last two function
def ceaser(plain_text,shift_amount,direction):
    initial_text = ""
    shift_amount = shift_amount % 26
    if direction.lower() == "decode":
        shift_amount *= -1

    for char in plain_text:
        if char in alphabet:
            letter_pos = alphabet.index(char)
            new_pos = letter_pos + shift_amount
            new_letter = alphabet[new_pos]
            initial_text += new_letter
        else:
            initial_text += char

    print(f"The {direction} text is {initial_text} ")



end_program = False


while end_program is False:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    ceaser(text,shift,direction)

    user_input = input("Type 'yes' if you want to go again. Otherwise type 'no'")
    if user_input.lower() == "no":
        end_program = True



#Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
#def encrypt(plain_text,shift_amount):
    #encryption = ""
    #for letter in plain_text:
        #letter_pos = alphabet.index(letter)
        #new_pos = letter_pos + shift_amount
        #new_letter = alphabet[new_pos]
        #encryption += new_letter
    #print(f"The encoded test is {encryption}")

#Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.
#def decrypt(encryption, shift_amount):
    #decryption = ""
    #for letter in encryption:
        #letter_pos = alphabet.index(letter)
        #new_pos = letter_pos - (shift_amount)
        #new_letter = alphabet[new_pos]
        #decryption += new_letter
    #print(f"The decoded text is {decryption}")




