alphabet = [
    "a", "b", "c", "d", "e", "f", "g",
    "h", "i", "j", "k", "l", "m",
    "n", "o", "p", "q", "r", "s",
    "t", "u", "v", "w", "x", "y", "z"
]

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

encrypt_words = []
decrypt_words = []

def encrypt(original_text, shift_amount):
    for letter in original_text:
      if letter in alphabet:
        shift_letters = alphabet.index(letter) + shift_amount
        shift_letters = shift_letters % len(alphabet)
        encrypt_words.append(alphabet[shift_letters])
    
    encrypt_string = ""
    for words in encrypt_words:
        encrypt_string += words
    

# encrypt(original_text=text, shift_amount=shift)

def decrypt(original_text, shift_amount):
    for letter in original_text:
      if letter in alphabet:
         shift_letters = alphabet.index(letter) - shift_amount
         shift_letters = shift_letters % len(alphabet)
         decrypt_words.append(alphabet[shift_letters])

    decrypt_string = ""
    for words in decrypt_words:
       decrypt_string += words
    print(f"Here is the decoded result: {decrypt_string}")
         
# decrypt(original_text=text, shift_amount=shift)

def caesar(original_text, shift_amount, encode_or_decode):
    if encode_or_decode == "encode":
      encrypt(original_text=original_text, shift_amount=shift_amount)
    else: 
       decrypt(original_text=original_text, shift_amount=shift_amount)

caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)