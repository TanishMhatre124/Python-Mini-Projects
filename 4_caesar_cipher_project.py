#caesar cipher project

alphabets = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction=input(" type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text=input("type your message:\n").lower()
shift=int(input("type your shift number:\n"))

#encrption
def encrypt(original_text,shift_amount):
    cipher_text=" "
    for letter in original_text:
        shifted_position=alphabets.index(letter)+shift_amount
        shifted_position %=len(alphabets)
        cipher_text +=alphabets[shifted_position]
    

    print(f"here is the encoded results{cipher_text}")
encrypt(original_text=text,shift_amount=shift) 

#decryption 
def decrypt(original_text,shift_amount):
    output_text=" "
    for letter in original_text:
        shifted_position=alphabets.index(letter)- shift_amount
        shifted_position %=len(alphabets)
        output_text +=alphabets[shifted_position]

    print(f"here is the decoded text :{output_text}")
decrypt(original_text=text,shift_amount=shift)

#combining encode and decode both
def caesar(original_text,shift_amount,encode_or_decode):  
    output_text=" "
    for letter in original_text:

        if encode_or_decode== "decode":
            shift_amout *=-1


        shifted_position=alphabets.index(letter)- shift_amount
        shifted_position %=len(alphabets)
        output_text +=alphabets[shifted_position]

    print(f"here is the decoded text :{output_text}")
caesar(original_text=text,shift_amount=shift,encode_or_decode=direction)