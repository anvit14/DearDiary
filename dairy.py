import tkinter as tk
from tkinter import messagebox, ttk
from datetime import datetime

def save_entry():
    entry = entry_text.get("1.0", "end-1c")
    if entry.strip():
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open("diary.txt", "a") as diary_file:
            diary_file.write(f"{date}\n")
            diary_file.write(f"{entry}\n\n")
        entry_text.delete("1.0", "end")
        messagebox.showinfo("Diary Entry Saved", "Your diary entry has been saved!")
    else:
        messagebox.showwarning("Empty Entry", "Please write something before saving.")

app = tk.Tk()
app.title("Cute Diary Journal")

# Style for the notebook tabs
style = ttk.Style()
style.configure("TNotebook.Tab", font=("Helvetica", 12))

notebook = ttk.Notebook(app)
notebook.pack(fill=tk.BOTH, expand=True)

# Create a tab for diary entries
diary_tab = ttk.Frame(notebook)
notebook.add(diary_tab, text="Diary")

label = tk.Label(diary_tab, text="Write your diary entry:", font=("Helvetica", 14))
label.pack(pady=10)

entry_text = tk.Text(diary_tab, height=10, width=40, font=("Helvetica", 12))
entry_text.pack()

save_button = tk.Button(diary_tab, text="Save Entry", command=save_entry, font=("Helvetica", 12))
save_button.pack(pady=10)

# Create a tab for viewing saved entries
view_tab = ttk.Frame(notebook)
notebook.add(view_tab, text="View Entries")

view_text = tk.Text(view_tab, height=10, width=40, font=("Helvetica", 12))
view_text.pack(padx=20, pady=10)

def view_entries():
    with open("diary.txt", "r") as diary_file:
        entries = diary_file.read()
    view_text.delete("1.0", "end")
    view_text.insert("1.0", entries)

view_button = tk.Button(view_tab, text="View Entries", command=view_entries, font=("Helvetica", 12))
view_button.pack(pady=10)

app.mainloop()
