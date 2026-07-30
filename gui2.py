#chat page , it displays the chat and you can give command,type the command, and then go for execution.

from tkinter import *
from PIL import Image, ImageTk
import speechtotext
import action


def ask():
    user_val = speechtotext.speech_to_text()
    action_val = action.action(user_val)

    text.insert(END, 'User: ' + user_val + "\n")
    if action_val is not None:
        text.insert(END, "Answer: " + str(action_val) + "\n")

    if str(action_val).lower() == "okay sir":
        root.destroy()


def send():
    user_input = entry.get()
    if user_input.strip() == "":
        return
    bot_response = action.action(user_input)

    text.insert(END, 'User: ' + user_input + "\n")
    if bot_response is not None:
        text.insert(END, "Answer:" + str(bot_response) + "\n")

    if str(bot_response).lower() == "okay sir":
        root.destroy()


def del_text():
    text.delete('1.0', END)


# GUI Setup
root = Tk()
root.title("AI Virtual Assistant")
root.geometry("1920x1000")
root.configure(bg="#ffffff")

# Sidebar
sidebar = Frame(root, width=300, bg="#00588A")
sidebar.pack(side="left", fill="y")

chat_label = Label(sidebar, text="CHAT", fg="white", bg="#00588A", font=("Arial", 12, "bold"))
chat_label.pack(pady=10)

# Frame for chat + scrollbar
chat_frame = Frame(sidebar, bg="#00588A")
chat_frame.pack(fill="both", expand=True, padx=10, pady=5)

scrollbar = Scrollbar(chat_frame)
scrollbar.pack(side="right", fill="y")

text = Text(
    chat_frame,
    height=30,
    width=28,
    font=("Arial", 10),
    bg="#00588A",
    wrap=WORD,
    yscrollcommand=scrollbar.set
)
text.pack(side="left", fill="both", expand=True)
scrollbar.config(command=text.yview)


# Topbar
topbar = Frame(root, height=50, bg="#006E8A")
topbar.pack(side="top", fill="x")

title_label = Label(topbar, text="AI BASED VIRTUAL ASSISTANT", fg="white", bg="#00588A", font=("Arial", 14, "bold"))
title_label.pack(pady=10)

# Content
content = Frame(root, bg="white")
content.pack(expand=True, fill="both")

# Image
try:
    img = Image.open("IMAGE/gui22.jpg")  # Make sure the path is correct
    img = img.resize((915, 400))
    photo = ImageTk.PhotoImage(img)
    img_label = Label(content, image=photo, bg="white")
    img_label.image = photo
    img_label.pack(pady=(10, 20))  # adds bottom margin below image
except Exception as e:
    print("Error loading image:", e)


# Entry + Buttons

entry_frame = Frame(content, bg="white")
entry_frame.pack(pady=(40, 10))  # adds top margin before entry


entry = Entry(entry_frame, font=("Arial", 12), width=85, bg="#fdf1e7", bd=0)
entry.pack(side="left", ipady=8, padx=(0, 5))

send_btn = Button(entry_frame, text="➤", font=("Arial", 12, "bold"), bg="#007ACC", fg="white", command=send)
send_btn.pack(side="left", padx=2)

# Load mic image
mic_img = Image.open("IMAGE/voice1.png")  # Make sure path and case are correct
mic_img = mic_img.resize((30, 30))
mic_photo = ImageTk.PhotoImage(mic_img)

# Button with image
mic_btn = Button(entry_frame, image=mic_photo, bg="black", command=ask, bd=0)
mic_btn.image = mic_photo  # Prevent garbage collection
mic_btn.pack(side="left", padx=2)


#load del image
del_img = Image.open("IMAGE/delete.png")  # Make sure path and case are correct
del_img = del_img.resize((30, 30))
del_photo = ImageTk.PhotoImage(del_img)

# del Button with image
del_btn = Button(entry_frame, image=del_photo, bg="black", command=del_text, bd=0)
del_btn.image = del_photo  # Prevent garbage collection
del_btn.pack(side="left", padx=2)



root.mainloop()
