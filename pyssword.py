from random import choices
import customtkinter
import pyperclip

password_length = 12


def slider_event(value):
    global password_length
    password_length = int(value)
    password_length_textbox.delete('1.0', 'end')
    password_length_textbox.insert('end', str(password_length))


def copy_button_callback():
    pyperclip.copy(password_textbox.get("0.0", "end"))


def generate_password():
    global password_length

    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '@', '#', '$', '%', '&', '*', '(', ')', '[', ']', '{', '}', '-', ':', ';']
    upper_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
                     'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    lower_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
                     'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    selected_chars = []

    if checkbox_upper_letters.get():
        selected_chars.extend(upper_letters)
    if checkbox_lower_letters.get():
        selected_chars.extend(lower_letters)
    if checkbox_numbers.get():
        selected_chars.extend(numbers)
    if checkbox_symbols.get():
        selected_chars.extend(symbols)

    if selected_chars:
        generated_password = ''.join(choices(selected_chars, k=password_length))
        password_textbox.delete('1.0', 'end')
        password_textbox.insert('end', generated_password)


app = customtkinter.CTk()
app.title("Pyssword")
app.iconbitmap("")
app.geometry("500x550")
app.resizable(False, False)
app.grid_columnconfigure((0, 1, 2, 3), weight=1)


# Password textbox
password_textbox = customtkinter.CTkTextbox(app, height=25, activate_scrollbars=False, border_width=1,
                                            border_color="gray50", font=("Arial", 15))
password_textbox.grid(row=0, column=0, padx=20, pady=(70, 10), sticky="ew", columnspan=4)

# Copy button
copy_button = customtkinter.CTkButton(app, text="Copy", command=copy_button_callback, font=("Arial", 15))
copy_button.grid(row=1, column=1, padx=10, pady=(0, 20), sticky="ew", columnspan=2)

# Characters label
char_label = customtkinter.CTkLabel(app, text="Characters:", fg_color="transparent", font=("Arial", 15))
char_label.grid(row=2, column=0, padx=20, pady=(20, 20), sticky="w")

# Checkbox 1 (upper letters)
checkbox_upper_letters = customtkinter.CTkCheckBox(app, text="ABC")
checkbox_upper_letters.grid(row=3, column=0, padx=(35, 0), pady=(20, 20), sticky="e")
# On by default
checkbox_upper_letters.toggle()

# Checkbox 2 (lower letters)
checkbox_lower_letters = customtkinter.CTkCheckBox(app, text="abc")
checkbox_lower_letters.grid(row=3, column=1, padx=(15, 0), pady=(20, 20), sticky="e")
# On by default
checkbox_lower_letters.toggle()

# Checkbox 3 (numbers)
checkbox_numbers = customtkinter.CTkCheckBox(app, text="123")
checkbox_numbers.grid(row=3, column=2, padx=(15, 0), pady=(20, 20), sticky="e")

# Checkbox 4 (symbols)
checkbox_symbols = customtkinter.CTkCheckBox(app, text="#$&")
checkbox_symbols.grid(row=3, column=3, padx=(15, 15), pady=(20, 20), sticky="e")

# Length label
char_label = customtkinter.CTkLabel(app, text="Length:", fg_color="transparent", font=("Arial", 15))
char_label.grid(row=4, column=0, padx=20, pady=(20, 20), sticky="w")

# Show the current password length
password_length_textbox = customtkinter.CTkTextbox(app, height=25, width=30, activate_scrollbars=False, border_width=1,
                                                   border_color="gray50", font=("Arial", 15))
password_length_textbox.grid(row=5, column=1, padx=99, pady=10, sticky="ew", columnspan=2)
password_length_textbox.insert('end', str(password_length))

# Slider to select a password length
slider = customtkinter.CTkSlider(app, from_=1, to=50, command=slider_event, number_of_steps=49)
slider.grid(row=6, column=0, padx=40, pady=(0, 20), sticky="ew", columnspan=4)
slider.set(password_length)

# Generate button
generate_button = customtkinter.CTkButton(app, text="Generate password", command=generate_password, font=("Arial", 15))
generate_button.grid(row=7, column=1, padx=10, pady=(10, 20), sticky="ew", columnspan=2)

generate_password()


app.mainloop()
