from tkinter import *
from PIL import Image, ImageTk
import subprocess
import os

root = Tk()
root.title("AI-Based Virtual Assistant")
root.geometry("1920x1000")
root.configure(bg="#a6c4d3")

# ========== Navigation Bar ==========
nav_bar = Frame(root, bg="#084b66", height=50)
nav_bar.pack(fill=X)

btn_font = ("Arial", 12, "bold")
btn_fg = "white"
btn_bg = "#084b66"
padx = 30

def go_home():
    pass  # already on home

def open_virtual_assistant():
    script_path = os.path.abspath("gui2.py")
    subprocess.Popen(["python", script_path])  # Launch gui2.py

Label(nav_bar, text="HOME", font=btn_font, fg=btn_fg, bg=btn_bg).pack(side=LEFT, padx=padx, pady=10)
Label(nav_bar, text="HOW IT WORKS", font=btn_font, fg=btn_fg, bg=btn_bg).pack(side=LEFT, padx=padx)
Label(nav_bar, text="ABOUT US", font=btn_font, fg=btn_fg, bg=btn_bg).pack(side=LEFT, padx=padx)

# ========== Main Section ==========
main_frame = Frame(root, bg="#a6c4d3")
main_frame.pack(pady=40, padx=50, fill=BOTH, expand=True)

# -------- Left Panel --------
left_frame = Frame(main_frame, bg="#a6c4d3")
left_frame.grid(row=0, column=0, sticky="n")

Label(left_frame, text="", font=("Arial", 20, "bold"), bg="#a6c4d3", fg="#1a1a1a").pack(anchor="w", pady=(0, 5))
Label(left_frame, text="", font=("Arial", 20, "bold"), bg="#a6c4d3", fg="#1a1a1a").pack(anchor="w", pady=(0, 5))
Label(left_frame, text="AI-Based Virtual Assistant 🤖", font=("Arial", 20, "bold"), bg="#a6c4d3", fg="#1a1a1a").pack(anchor="w", pady=(0, 5))
Label(left_frame, text="Your Smart Companion", font=("Arial", 14), bg="#a6c4d3", fg="#333333").pack(anchor="w", pady=(0, 15))
Label(left_frame, text="💬 Speak or type your command, and let AI handle the rest!", font=("Arial", 12), bg="#a6c4d3").pack(anchor="w")

features = [
    "✔️ What can I do?",
    "✅ Answer your queries",
    "✅ Fetch real-time weather updates ⚙️",
    "✅ Open websites like Google, YouTube, etc. 🌐🎬",
    "✅ Play your favorite music 🎵",
    "✅ More features coming soon!"
]

for line in features:
    Label(left_frame, text=line, font=("Arial", 12), bg="#a6c4d3", anchor="w", justify=LEFT).pack(anchor="w")

Button(left_frame, text="Virtual Assistant", font=("Arial", 12, "bold"), bg="#2c2c2c", fg="white",
       padx=10, pady=5, command=open_virtual_assistant).pack(pady=20, anchor="w")

# -------- Right Panel (Image) --------
right_frame = Frame(main_frame, bg="#a6c4d3")
right_frame.grid(row=0, column=1, padx=(50, 0))

try:
    img = Image.open("IMAGE/gui.jpg")  # Make sure the path is correct
    img = img.resize((700, 400))
    photo = ImageTk.PhotoImage(img)

    Label(right_frame, image=photo, bg="white").pack(pady=10)
    
except Exception as e:
    print("Error loading image:", e)

root.mainloop()
