import tkinter as tk
from tkinter import messagebox
import random

def move_no_button(button):
    """ Hayır butonunu rastgele bir konuma taşır. """
    new_x = random.randint(50, 250)
    new_y = random.randint(80, 150)
    button.place(x=new_x, y=new_y)

def ask_second_question():
    """ İlk soruya 'Evet' denirse ikinci pencere açılır. """
    first_window.destroy()  # İlk pencereyi kapat

    second_window = tk.Tk()
    second_window.title("Tarih Planı")
    second_window.geometry("400x250")
    second_window.config(bg="lightblue")

    label = tk.Label(second_window, text="Peki first date için tatilde müsait misin? 😊", 
                     font=("Arial", 14, "bold"), bg="lightblue")
    label.pack(pady=40)

    button_frame = tk.Frame(second_window, bg="lightblue")
    button_frame.pack()

    yes_button = tk.Button(button_frame, text="Evet", font=("Arial", 12, "bold"),
                           bg="green", fg="white", width=10, height=2,
                           command=lambda: final_message(second_window))
    yes_button.grid(row=0, column=0, padx=20)

    no_button = tk.Button(button_frame, text="Hayır", font=("Arial", 12, "bold"),
                          bg="red", fg="white", width=10, height=2)
    no_button.grid(row=0, column=1, padx=20)
    no_button.bind("<Enter>", lambda event: move_no_button(no_button))  # Mouse üstüne gelince kaç

    second_window.mainloop()

def final_message(window):
    """ Son mesajı göster ve programı kapat. """
    messagebox.showinfo("Harika!", "Plan yapalım! 🎉")
    window.quit()

# İlk pencereyi oluştur
first_window = tk.Tk()
first_window.title("Çıkma Teklifi")
first_window.geometry("400x250")
first_window.config(bg="pink")

label = tk.Label(first_window, text="Benimle çıkar mısın? 💖", font=("Arial", 16, "bold"), bg="pink")
label.pack(pady=40)

button_frame = tk.Frame(first_window, bg="pink")
button_frame.pack()

yes_button = tk.Button(button_frame, text="Evet", font=("Arial", 12, "bold"),
                       bg="green", fg="white", width=10, height=2,
                       command=ask_second_question)
yes_button.grid(row=0, column=0, padx=20)

no_button = tk.Button(button_frame, text="Hayır", font=("Arial", 12, "bold"),
                      bg="red", fg="white", width=10, height=2)
no_button.grid(row=0, column=1, padx=20)  # Başlangıç pozisyonu

# Mouse "Hayır" butonunun üstüne gelince kaçmasını sağla
no_button.bind("<Enter>", lambda event: move_no_button(no_button))

first_window.mainloop()
