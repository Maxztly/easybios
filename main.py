import tkinter as tk
import os
import ctypes

def access_bios_as_admin():
    ctypes.windll.shell32.ShellExecuteW(
        None, "runas", "cmd.exe", "/K shutdown /r /fw /f /t 0", None, 1)
    
def center_window(root, width, height):

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x = (screen_width - width) // 2
    y = (screen_height - height) // 2

    root.geometry(f"{width}x{height}+{x}+{y}")

root = tk.Tk()
root.title("EasyBIOS")
root.iconbitmap("cmd.ico")
root.configure(bg="black")

window_width = 400
window_height = 80

center_window(root, window_width, window_height)

button = tk.Button(root, text="ACCES BIOS", command=access_bios_as_admin, width=100, height=2, bg="black", fg="#00FF00")
button.pack(padx=20, pady=20)

root.mainloop()