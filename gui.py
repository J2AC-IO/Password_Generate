import customtkinter as ctk
from tkinter import messagebox
from config import TYPOGRAPHY, FONT_SIZE_DEFAULT, FONT_SIZE_TITLE
import logic


ctk.set_default_color_theme("dark-blue") 
ctk.set_appearance_mode("dark")

frame = ctk.CTk()

frame.title("Gerador de Senhas")

def copy_text():

   if logic.copy_to_clipboard(password_generate.get("1.0", "end")):
      
        messagebox.showinfo("Sucesso", "Senha copiada!")

width_window = 500
height_window = 650

width_window = frame.winfo_screenwidth()
height_window = frame.winfo_screenheight()

pos_x = (width_window // 2) - (width_window // 2)
pos_y = (height_window // 2) - (height_window // 2)

frame.geometry(f'{width_window}x{height_window}+{pos_x}+{pos_y}')
frame.resizable(False, False)

frame.configure(fg_color="#262C3E")

frame_generated_password = ctk.CTkFrame(frame, 
                                  fg_color="#0D1826",
                                  border_width=0,
                                  corner_radius=25
                                  )
frame_generated_password.pack(pady=(20,0), padx=30, fill="both", expand=False)

label_password_generate = ctk.CTkLabel(frame_generated_password, text="Senha Gerada ", font=(TYPOGRAPHY, FONT_SIZE_TITLE, "bold"), text_color="#EEF6FB")
label_password_generate.pack(anchor="center", pady=(20, 15))

password_generate = ctk.CTkTextbox(frame_generated_password, height=50, state="disabled", fg_color="#262C3E", font=(TYPOGRAPHY, FONT_SIZE_DEFAULT, "bold"))
password_generate.pack(fill="both", padx=24)

button = ctk.CTkButton(frame_generated_password, fg_color="#FFA500", hover_color="#FFA500", command=copy_text, text="copiar", font=(TYPOGRAPHY, FONT_SIZE_DEFAULT, "bold"), width=50, height=20)
button.pack(pady=(10, 20),anchor="e" , padx=(0, 30))

frame_options = ctk.CTkFrame(frame, 
                            fg_color="#0D1826",
                            border_width=0,
                            corner_radius=25
                            )
frame_options.pack(pady=(20,0), padx=30, fill="both", expand=False)

label_options = ctk.CTkLabel(frame_options, text="Opções", font=(TYPOGRAPHY, FONT_SIZE_TITLE, "bold"), text_color="#EEF6FB")
label_options.pack(pady=(20,10), anchor="center")

chk_uppercase = ctk.CTkCheckBox(frame_options, text="Incluir letras Maiúsculas", font=(TYPOGRAPHY, FONT_SIZE_DEFAULT), fg_color="#7764F3", text_color="#EEF6FB")
chk_uppercase.pack(anchor="w", padx=15, pady=10)

chk_lowercase = ctk.CTkCheckBox(frame_options, text="Incluir letras Minusculas", font=(TYPOGRAPHY, FONT_SIZE_DEFAULT), fg_color="#7764F3", text_color="#EEF6FB")
chk_lowercase.pack(anchor="w", padx=15, pady=10)

chk_number = ctk.CTkCheckBox(frame_options, text="Incluir Números", font=(TYPOGRAPHY, FONT_SIZE_DEFAULT), fg_color="#7764F3", text_color="#EEF6FB")
chk_number.pack(anchor="w", padx=15, pady=10)

chk_special_char = ctk.CTkCheckBox(frame_options, text="Incluir caractreres Especiais", font=(TYPOGRAPHY, FONT_SIZE_DEFAULT), fg_color="#7764F3", text_color="#EEF6FB")
chk_special_char.pack(anchor="w", padx=15, pady=10)

row = ctk.CTkFrame(frame_options, height=2, fg_color="gray")
row.pack(pady=10)

label_option = ctk.CTkLabel(frame_options, text="Tamanho da Senha:", font=(TYPOGRAPHY, FONT_SIZE_DEFAULT), text_color="#EEF6FB")
label_option.pack(anchor="w", padx=15)

option_menu = ctk.CTkOptionMenu(frame_options, font=(TYPOGRAPHY, FONT_SIZE_DEFAULT), text_color="#EEF6FB", button_color="#7764F3", fg_color="#7764F3", button_hover_color="#7764F3", values=["Selecione uma tamanho...",
                                              "6 caracteres",
                                              "7 caracteres",
                                              "8 caracteres",
                                              "9 caracteres",
                                              "10 caracteres",
                                              "11 caracteres", 
                                              "12 caracteres",
                                              "13 caracteres",
                                              "14 caracteres",
                                              "15 caracteres",
                                              "16 caracteres",
                                              "17 caracteres",
                                              "18 caracteres",
                                              "19 caracteres",
                                              "20 caracteres",
                                              "21 caracteres",
                                              "22 caracteres",
                                              "23 caracteres",
                                              "24 caracteres",
                                              "25 caracteres",
                                              "26 caracteres",
                                              "27 caracteres",
                                              "28 caracteres",
                                              "29 caracteres",
                                              "30 caracteres",
                                              "31 caracteres",
                                              "32 caracteres",
                                              "33 caracteres",
                                              "34 caracteres",
                                              "35 caracteres",
                                              "36 caracteres",
                                              "37 caracteres",
                                              "38 caracteres",
                                              "39 caracteres",
                                              "40 caracteres"
                                              ])

option_menu.pack(anchor="w", padx=15, fill="both", pady=(0, 15))

def processes_data():

    logic.message_config(option_menu.get(), chk_uppercase.get(), chk_lowercase.get(), chk_number.get(), chk_special_char.get(), flash_message, frame, password_generate) 

button = ctk.CTkButton(frame_options, fg_color="#7764F3", hover_color="#7764F3", text="Gerar", command=processes_data, font=(TYPOGRAPHY, FONT_SIZE_DEFAULT, "bold"), width=100, height=35)
button.pack(pady=(5,15))

flash_message = ctk.CTkLabel(frame, text="", font=(TYPOGRAPHY, FONT_SIZE_DEFAULT, "bold"))
flash_message.pack(pady=(10,20))


def run():

    frame.mainloop()
