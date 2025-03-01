import pyautogui as pt
import time
import tkinter as tk
from tkinter import messagebox

def start_spam():
    try:
        limit = int(entry_limit.get())
        message = entry_message.get()
        delay = float(entry_delay.get())
        
        if limit <= 0 or delay < 0:
            messagebox.showerror("Error", "Please enter valid positive numbers!")
            return
        
        messagebox.showinfo("Instructions", "Switch to your chat window. Spamming starts in 5 seconds!")
        time.sleep(5)  # Give time to switch
        
        for i in range(limit):
            pt.typewrite(message)
            pt.press("enter")
            time.sleep(delay)
        
        messagebox.showinfo("Success", f"Successfully sent {limit} messages!")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numeric inputs!")

# GUI Setup
root = tk.Tk()
root.title("Message Spammer")
root.geometry("300x200")

tk.Label(root, text="Number of Messages:").pack()
entry_limit = tk.Entry(root)
entry_limit.pack()

tk.Label(root, text="Message:").pack()
entry_message = tk.Entry(root)
entry_message.pack()

tk.Label(root, text="Delay (seconds):").pack()
entry_delay = tk.Entry(root)
entry_delay.pack()

tk.Button(root, text="Start Spamming", command=start_spam).pack()

root.mainloop()
