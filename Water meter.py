import tkinter as tk
from tkinter import messagebox
#змінна
def add_water():
    global water_intake
    water_intake += 250
    label_var.set(f"Випито: {water_intake} мл")

def reset_water():
    global water_intake
    water_intake = 0
    label_var.set("Випито: 0 мл")

def show_about():
    messagebox.showinfo("Про програму", "Тут ви можете порахувати скількі води випили за день")

def exit_app():
    root.quit()

#Головний екран
root = tk.Tk()
root.title("Трекер води")
root.geometry("2000x2000")
root.configure(bg="#f0f0f0")

# Меню
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Вихід", command=exit_app)
menu_bar.add_cascade(label="Файл", menu=file_menu)
menu_bar.add_command(label="Про програму", command=show_about)

water_intake = 0
label_var = tk.StringVar()
label_var.set("Випито: 0 мл")

#віджети
label = tk.Label(root, textvariable=label_var, font=("Times New Roman", 14), bg="#f0f0f0", fg="#333")
label.pack(pady=10)

add_button = tk.Button(root, text="Випив склянку (250 мл)", command=add_water, font=("Times New Roman", 12), bg="#007BFF", fg="white", relief="raised", bd=3)
add_button.pack(pady=5)

reset_button = tk.Button(root, text="Скинути", command=reset_water, font=("Times New Roman", 12), bg="#DC3545", fg="white", relief="raised", bd=3)
reset_button.pack(pady=5)

root.mainloop()
