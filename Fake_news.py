import random
import tkinter as tk
from tkinter import messagebox
from datetime import datetime

# ----------------------------
# Category Data (Dictionary)
# ----------------------------

news_data = {
    "Tech": {
        "subjects": ["Elon Musk", "Google CEO", "A hacker", "Microsoft"],
        "actions": ["launches", "destroys", "hacks", "upgrades"],
        "objects": ["AI robot", "the internet", "a secret algorithm", "Windows 15"],
        "reasons": ["to dominate the market", "by mistake", "to save data", "for fun"]
    },

    "Sports": {
        "subjects": ["Virat Kohli", "Cristiano Ronaldo", "Indian Team", "A local player"],
        "actions": ["wins", "loses", "buys", "cancels"],
        "objects": ["World Cup", "a cricket bat", "the stadium", "training camp"],
        "reasons": ["after intense practice", "due to rain", "because of luck", "to surprise fans"]
    },

    "Politics": {
        "subjects": ["Narendra Modi", "A minister", "Parliament", "A political party"],
        "actions": ["announces", "bans", "launches", "removes"],
        "objects": ["new policy", "free WiFi", "national holiday", "tax reform"],
        "reasons": ["for development", "after debate", "to gain support", "for publicity"]
    },

    "Funny": {
        "subjects": ["A local cat", "A student", "A software engineer", "Your neighbor"],
        "actions": ["declares war on", "eats", "throws away", "creates"],
        "objects": ["homework", "the Moon", "all smartphones", "a pizza"],
        "reasons": ["because Monday", "to impress aliens", "for no reason", "after watching YouTube"]
    }
}

# ----------------------------
# Functions
# ----------------------------

headline_count = 0

def generate_headline():
    global headline_count

    category = category_var.get()
    data = news_data[category]

    headline = f"{random.choice(data['subjects'])} {random.choice(data['actions'])} {random.choice(data['objects'])} {random.choice(data['reasons'])}!"

    output_text.insert(tk.END, headline + "\n\n")

    headline_count += 1
    counter_label.config(text=f"Headlines Generated: {headline_count}")


def generate_multiple():
    try:
        count = int(entry_count.get())
        i = 0

        while i < count:
            generate_headline()
            i += 1

    except ValueError:
        messagebox.showerror("Error", "Enter a valid number!")


def clear_text():
    global headline_count
    output_text.delete(1.0, tk.END)
    headline_count = 0
    counter_label.config(text="Headlines Generated: 0")


def save_to_file():
    content = output_text.get(1.0, tk.END)

    if content.strip() == "":
        messagebox.showwarning("Warning", "Nothing to save!")
        return

    with open("fake_news_gui.txt", "a") as file:
        file.write(f"\n{datetime.now()}\n")
        file.write(content)

    messagebox.showinfo("Success", "Saved successfully!")


def exit_app():
    confirm = messagebox.askyesno("Exit", "Are you sure you want to exit?")
    if confirm:
        root.destroy()


# ----------------------------
# GUI Setup
# ----------------------------

root = tk.Tk()
root.title("Fake News Headline Generator")
root.geometry("700x550")
root.configure(bg="#1f2933")

title = tk.Label(root, text="FAKE NEWS HEADLINE GENERATOR",
                 font=("Arial", 18, "bold"),
                 bg="#1f2933", fg="white")
title.pack(pady=10)

# Category Dropdown
category_var = tk.StringVar()
category_var.set("Tech")

category_menu = tk.OptionMenu(root, category_var, *news_data.keys())
category_menu.pack(pady=5)

# Entry
entry_count = tk.Entry(root, width=10)
entry_count.pack(pady=5)
entry_count.insert(0, "1")

# Buttons Frame
button_frame = tk.Frame(root, bg="#1f2933")
button_frame.pack(pady=10)

btn_generate = tk.Button(button_frame, text="Generate One", width=18, command=generate_headline)
btn_generate.grid(row=0, column=0, padx=5, pady=5)

btn_multiple = tk.Button(button_frame, text="Generate Multiple", width=18, command=generate_multiple)
btn_multiple.grid(row=0, column=1, padx=5, pady=5)

btn_clear = tk.Button(button_frame, text="Clear", width=18, command=clear_text)
btn_clear.grid(row=1, column=0, padx=5, pady=5)

btn_save = tk.Button(button_frame, text="Save to File", width=18, command=save_to_file)
btn_save.grid(row=1, column=1, padx=5, pady=5)

btn_exit = tk.Button(root, text="Exit", width=15, command=exit_app)
btn_exit.pack(pady=5)

# Output Text Box
output_text = tk.Text(root, height=15, width=80)
output_text.pack(pady=10)

# Counter Label
counter_label = tk.Label(root, text="Headlines Generated: 0",
                         bg="#1f2933", fg="white")
counter_label.pack()

root.mainloop()
