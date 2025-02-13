import string
import random
import pyperclip

def message_config(option, upper_char, lowercase_char, number, special_char, frame_message, display, text_password):

    if('Selecione' in option):

        flash_message(frame_message, display, "Selecione um tamanho!")
        return
    
    if(not (upper_char or lowercase_char or number or special_char)):
        flash_message(frame_message, display, "Escolha pelo menos uma opção.")  
        return 
    
    flash_message(frame_message, display, "Senha Gerada com sucesso.", "green")

    size = int(option.split()[0])

    generate_password(text_password, option, upper_char, lowercase_char, number, special_char, size)
    return


def flash_message(frame_message, display, message, color="red"):

    time = 2000

    frame_message.configure(text=message , text_color=color)  

    frame_message.pack() 

    display.after(time, frame_message.pack_forget)


def generate_password(text_password, option, upper_char, lowercase_char, number, special_char, size):

    char = ''

    if upper_char: 

        char += string.ascii_uppercase
    
    if lowercase_char:

        char += string.ascii_lowercase
    
    if number:

        char += string.digits

    if special_char:

        char += string.punctuation

    password = ''.join(random.choice(char) for _ in range(size))

    text_password.configure(state="normal")
    text_password.delete('1.0', 'end')
    text_password.insert('1.0', password )
    text_password.configure(state="disabled")

    return password



def copy_to_clipboard(password):

    if password.strip():
        
        pyperclip.copy(password)

        return True
    
    return False
