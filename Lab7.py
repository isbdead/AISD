#Требуется для своего варианта второй части л.р. №6 (усложненной программы) разработать реализацию с использованием графического интерфейса.
# Допускается использовать любую графическую библиотеку питона. Рекомендуется использовать внутреннюю библиотеку питона  tkinter.
# В программе должны быть реализованы минимум одно окно ввода, одно окно вывода (со скролингом), одно текстовое поле, одна кнопка.
# Вариант 1. Пароль состоит из К символов - латинские буквы или цифры. Составьте все возможные пароли.

import tkinter as tk
from tkinter import scrolledtext, messagebox
import string
import itertools

chars = string.ascii_letters + string.digits  # a-zA-Z0-9

def check_password(password):
    return any(ch.isdigit() for ch in password) and any(ch.isalpha() for ch in password)

def generate_passwords_algo(k, prefix=""):
    if k == 0:
        if check_password(prefix):
            yield prefix
    else:
        for ch in chars:
            yield from generate_passwords_algo(k - 1, prefix + ch)

def center_window(root, width=600, height=500):
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    root.geometry(f"{width}x{height}+{x}+{y}")

class PasswordApp:
    def __init__(self, root):
        self.root = root
        root.title("Генератор паролей с ограничениями")
        center_window(root, 600, 500)

        # Ввод длины
        self.label = tk.Label(root, text="Введите длину пароля K (натуральное число, лучше не больше 4):")
        self.label.pack(pady=5)

        self.entry = tk.Entry(root, width=10)
        self.entry.pack()

        # Кнопка
        self.btn_generate = tk.Button(root, text="Сгенерировать (алгоритмический)", command=self.generate_algo)
        self.btn_generate.pack(pady=5)

        # Текстовое поле с прокруткой для вывода
        self.text_area = scrolledtext.ScrolledText(root, width=70, height=25)
        self.text_area.pack(padx=10, pady=10)

    def generate_algo(self):
        self.text_area.delete('1.0', tk.END)
        try:
            k = int(self.entry.get())
            if k < 1:
                messagebox.showerror("Ошибка", "Введите натуральное число больше 0")
                return
            if k > 4:
                if not messagebox.askyesno("Предупреждение",
                                           "Генерация паролей для K>4 займет очень много времени и памяти. Продолжить?"):
                    return
        except ValueError:
            messagebox.showerror("Ошибка", "Введите корректное число")
            return

        filename = "password_6.txt"
        count = 0
        self.text_area.insert(tk.END, f"Генерация паролей длины {k} с ограничением (минимум 1 цифра и 1 буква)...\n\n")
        with open(filename, 'w', encoding='utf-8') as f:
            for pwd in generate_passwords_algo(k):
                count += 1
                self.text_area.insert(tk.END, pwd + '\n')
                f.write(pwd + '\n')
                if count % 1000 == 0:
                    self.text_area.update()

        self.text_area.insert(tk.END, f"\nВсего паролей: {count}\n")
        self.text_area.insert(tk.END, f"Пароли сохранены в файл: {filename}\n")

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordApp(root)
    root.mainloop()