from art import logo
print(logo)

alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
             'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n")
    text = input("Type your message: \n").lower()
    shift = int(input("Type the shift number: \n"))

    shift = shift % 26

    def cesar(start_text, shift_amount, cipher_direction):
        end_text = ""
        if cipher_direction == "decode":
                shift_amount *= -1
        for char in start_text:
            if char in alphabets:
                postion = alphabets.index(char)
                new_position = postion + shift_amount
                end_text += alphabets[new_position]
            else:
                end_text += char
        print(f"The {cipher_direction}d text is {end_text}. You message is safe.")

    cesar(start_text=text, shift_amount=shift, cipher_direction=direction)
    
    result = input("Type 'yes' if you want to continue/go again. Otherwise type 'no'. \n")
    if result == "no":
        should_continue = False
        print("Goodbye!")
        