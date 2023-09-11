import tkinter as tk
import os
import ctypes
import cv2

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

window_width = 400
window_height = 80

center_window(root, window_width, window_height)

video_path = "background.mp4"
cap = cv2.VideoCapture(video_path)

def update_video():
    ret, frame = cap.read()
    if ret:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        photo = tk.PhotoImage(data=cv2.imencode('.ppm', frame)[1].tostring())
        video_label.config(image=photo)
        video_label.image = photo
        root.after(30, update_video)
    else:
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
        update_video()

video_label = tk.Label(root)
video_label.pack()

update_video()

button = tk.Button(root, text="ACCESS BIOS", command=access_bios_as_admin, width=50, height=2, bg="black", fg="#00FF00")
button.place(relx=0.5, rely=0.5, anchor="center")

root.mainloop()
