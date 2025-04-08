import tkinter as tk
from tkinter import ttk, messagebox
import tkinter.font as tkFont
import subprocess
import os

# ------------------------------------------------
# Backend Logic (adapt these for your combos)
# ------------------------------------------------
def generate_entry():
    """Call your backend using 'dry-run' logic, then confirm the result."""
    # Example of reading combo selections:
    how_val = choose_how_var.get()
    length_val = length_var.get()
    special_val = special_var.get()
    numbers_val = numbers_var.get()
    uppercase_val = uppercase_var.get()

    # In your real code, you'd build a command including these flags:
    # e.g. cmd = ["./password_manager", "--how", how_val, "--length", length_val, ...]
    # For now, just show a mock message:
    messagebox.showinfo("Generate Entry", 
        f"Simulating backend call with:\n"
        f"how={how_val}, length={length_val}, special={special_val}, numbers={numbers_val}, uppercase={uppercase_val}"
    )

    # Suppose the backend returned a CSV line: "website, username, password"
    # We'll simulate that for confirm_entry:
    mock_csv_line = f"{how_val}, {length_val}, MyP@ssw0rd!"
    confirm_entry(mock_csv_line)

def confirm_entry(entire_entry):
    """Modal confirmation window showing the CSV entry.
    If confirmed, calls backend again (without --dry-run).
    """
    parts = entire_entry.split(",")
    generated_password = parts[2].strip() if len(parts) >= 3 else entire_entry

    confirm_win = tk.Toplevel(root)
    confirm_win.title("Confirm Entry")
    confirm_win.configure(bg=COLOR_ROOT_BG)
    confirm_win.grab_set()  # Make it modal

    confirm_win.minsize(400, 200)
    confirm_frame = ttk.Frame(confirm_win, style="Dark.TFrame", padding=20)
    confirm_frame.pack(fill=tk.BOTH, expand=True)

    prompt_label = ttk.Label(confirm_frame, text="Entire Entry:", style="Dark.TLabel")
    prompt_label.pack(pady=(10, 5))
    entry_label = ttk.Label(confirm_frame, text=entire_entry, style="Dark.TLabel")
    entry_label.pack(pady=(0, 10))
    question_label = ttk.Label(confirm_frame, text="Does this look correct?", style="Dark.TLabel")
    question_label.pack(pady=(0, 10))

    button_frame = ttk.Frame(confirm_frame, style="Dark.TFrame")
    button_frame.pack(fill=tk.X, pady=10)

    yes_button = ttk.Button(button_frame, text="Yes", command=lambda: on_confirm(generated_password), style="Dark.TButton")
    no_button = ttk.Button(button_frame, text="No", command=lambda: on_cancel(), style="Dark.TButton")

    yes_button.grid(row=0, column=0, padx=10)
    no_button.grid(row=0, column=1, padx=10)
    button_frame.columnconfigure(0, weight=1)
    button_frame.columnconfigure(1, weight=1)

    center_window(confirm_win)

    def on_confirm(generated_pwd):
        confirm_win.destroy()
        # Here you’d call your backend again (w/o --dry-run). For now, just show the final password in the main entry:
        password_entry.delete(0, tk.END)
        password_entry.insert(0, generated_pwd)
        messagebox.showinfo("Entry Added", "Your entry has been saved (simulated)!")

    def on_cancel():
        confirm_win.destroy()
        messagebox.showinfo("Cancelled", "Entry not saved.")

# ------------------------------------------------
# Helper: center a window
# ------------------------------------------------
def center_window(win):
    win.update_idletasks()
    width = win.winfo_width()
    height = win.winfo_height()
    x = (win.winfo_screenwidth() // 2) - (width // 2)
    y = (win.winfo_screenheight() // 2) - (height // 2)
    win.geometry(f"{width}x{height}+{x}+{y}")

# ------------------------------------------------
# Main Window Setup
# ------------------------------------------------
root = tk.Tk()
root.title("CryptKey")
root.configure(bg="white")  # White background
root.minsize(700, 400)
root.resizable(True, True)

# ------------------------------------------------
# Colors & Fonts
# ------------------------------------------------
COLOR_ROOT_BG   = "white"     # so the confirm window also has a white bg
COLOR_FRAME_BG  = "#1E1E1E"
COLOR_WIDGET_BG = "#555555"
COLOR_FG        = "#FFFFFF"

title_font = ("Arial", 36, "bold")
label_font = ("Arial", 14, "bold")
password_label_font = ("Arial", 16, "bold")
combo_font = ("Arial", 12)

# ------------------------------------------------
# TTK Style (Dark-ish for confirmation windows)
# ------------------------------------------------
style = ttk.Style(root)
style.theme_use("clam")

style.configure("Dark.TFrame", background=COLOR_FRAME_BG)
style.configure("Dark.TLabel", background=COLOR_FRAME_BG, foreground=COLOR_FG, font=label_font)
style.configure("Dark.TButton", background=COLOR_WIDGET_BG, foreground=COLOR_FG,
                borderwidth=0, focusthickness=0, relief="flat", font=label_font, padding=(6,6))
style.map("Dark.TButton", background=[("active", "#444444")])

# ------------------------------------------------
# Top Black Banner
# ------------------------------------------------
banner = tk.Frame(root, bg="black", height=60)
banner.pack(fill="x", side="top")

title_label = tk.Label(
    banner, text="CryptKey",
    font=title_font,
    fg="white", bg="black"
)
title_label.pack(pady=10)

# ------------------------------------------------
# Main Content Frame (White)
# ------------------------------------------------
content_frame = tk.Frame(root, bg="white")
content_frame.pack(fill="both", expand=True, pady=(10,0))

# ------------------------------------------------
# Helper: Labeled Combo (white label, normal combos)
# ------------------------------------------------
def create_labeled_dropdown(parent, label_text, options, default=None):
    container = tk.Frame(parent, bg="white")
    container.pack(side="left", padx=40)  # space between groups

    lbl = tk.Label(container, text=label_text, font=label_font, bg="white", fg="black")
    lbl.pack(pady=(0,5))

    var = tk.StringVar()
    combo = ttk.Combobox(container, textvariable=var, values=options, state="readonly", font=combo_font)
    combo.set(default if default else options[0])
    combo.pack()
    return var

# ------------------------------------------------
# Row 1: "Choose How", "Length", "Special Characters"
# ------------------------------------------------
row1 = tk.Frame(content_frame, bg="white")
row1.pack(pady=(0, 20))

choose_how_var = create_labeled_dropdown(row1, "Choose How", ["Custom", "Random"], default="Custom")
length_var = create_labeled_dropdown(row1, "Length", ["8", "12", "16", "20", "24", "32"], default="16")
special_var = create_labeled_dropdown(row1, "Special Characters", ["None", "Some", "All"], default="None")

# ------------------------------------------------
# Row 2: "Numbers", "Upper Cases"
# ------------------------------------------------
row2 = tk.Frame(content_frame, bg="white")
row2.pack(pady=(0, 20))

numbers_var = create_labeled_dropdown(row2, "Numbers", ["Yes", "No"], default="Yes")
uppercase_var = create_labeled_dropdown(row2, "Upper Cases", ["Yes", "No"], default="Yes")

# ------------------------------------------------
# "Your Password" Label & Entry
# ------------------------------------------------
password_label = tk.Label(content_frame, text="Your Password", font=password_label_font, bg="white", fg="black")
password_label.pack(pady=(0, 5))

password_entry = tk.Entry(content_frame, width=50, font=combo_font, fg="black", bg="#f0f0f0")
password_entry.insert(0, "Your Password")
password_entry.pack(pady=(0, 20))

# ------------------------------------------------
# "Save" Button
# ------------------------------------------------
save_button = tk.Button(
    content_frame, text="Save",
    font=combo_font, fg="black", bg="#e0e0e0",
    relief="raised", bd=2,
    command=generate_entry  # Use your backend logic here
)
save_button.pack()

# ------------------------------------------------
# Finalize Layout & Start
# ------------------------------------------------
def finalize_layout():
    center_window(root)

root.after(0, finalize_layout)
root.mainloop()