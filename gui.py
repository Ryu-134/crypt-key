import tkinter as tk
from tkinter import ttk, messagebox
import tkinter.font as tkFont
import subprocess
import os

# ================================
# FUNCTION: on_save_click
# -------------------------------
# Placeholder function for your future backend logic.
# You can retrieve the dropdown selections and call the backend here.
# ================================
def on_save_click():
    # For now, just show a message or do nothing.
    messagebox.showinfo("Save Clicked", "You clicked the Save button!\nConnect your backend logic here.")

# ================================
# FUNCTION: center_window
# -------------------------------
# Centers the given window on the screen by calculating appropriate x and y offsets.
# ================================
def center_window(win):
    win.update_idletasks()
    width = win.winfo_width()
    height = win.winfo_height()
    x = (win.winfo_screenwidth() // 2) - (width // 2)
    y = (win.winfo_screenheight() // 2) - (height // 2)
    win.geometry(f"{width}x{height}+{x}+{y}")

# ================================
# SET UP THE MAIN WINDOW (GUI)
# -------------------------------
root = tk.Tk()
root.title("CryptKey")
root.configure(bg="#000000")    # black background
root.minsize(600, 300)
root.resizable(True, True)

# ================================
# DEFINE CUSTOM COLORS
# ----------------===============
COLOR_ROOT_BG   = "#000000"
COLOR_FRAME_BG  = "#1E1E1E"
COLOR_WIDGET_BG = "#555555"
COLOR_FG        = "#FFFFFF"
COLOR_HIGHLIGHT = "#808080"

# ================================
# DEFINE NAMED FONT OBJECTS
# ----------------===============
custom_font = tkFont.Font(family="Segoe UI", size=12, weight="bold")      # For labels, buttons, output
custom_entry_font = tkFont.Font(family="Segoe UI", size=12, weight="normal")  # For Entry widgets

# ================================
# CONFIGURE STYLES FOR THE DARK THEME
# ----------------===============
style = ttk.Style(root)
style.theme_use("clam")

style.configure("Dark.TFrame", background=COLOR_FRAME_BG)
style.configure("Dark.TLabel", background=COLOR_FRAME_BG, foreground=COLOR_FG, font=custom_font)
style.configure("Dark.TButton", background=COLOR_WIDGET_BG, foreground=COLOR_FG,
                borderwidth=0, focusthickness=0, relief="flat", font=custom_font, padding=(6,6))
try:
    style.configure("Dark.TButton", bordercolor=COLOR_FG)
except tk.TclError:
    pass
style.map("Dark.TButton", background=[("active", "#444444")])

style.configure("Dark.TEntry", fieldbackground=COLOR_WIDGET_BG, foreground=COLOR_FG,
                borderwidth=0, font=custom_entry_font)

# ================================
# CREATE A FRAME TO HOLD THE WIDGETS
# -------------------------------
frame = ttk.Frame(root, style="Dark.TFrame", padding=20)
frame.pack(fill=tk.BOTH, expand=True)

# ================================
# TITLE BAR (BIG BLACK BANNER)
# -------------------------------
title_bar = ttk.Label(frame, text="CryptKey", style="Dark.TLabel")
title_bar.config(font=("Arial", 36, "bold"))
title_bar.pack(fill=tk.X, pady=(0, 20))  # extra spacing below

# ================================
# DROPDOWNS
# -------------------------------
def create_dropdown(options, default=None):
    combo = ttk.Combobox(frame, values=options, style="Dark.TEntry", state="readonly")
    combo.set(default if default else options[0])
    return combo

# 1) Choose How, 2) Length, 3) Special Characters
choose_how_combo = create_dropdown(["Custom", "Random"], default="Custom")
length_combo = create_dropdown(["8", "12", "16", "20", "24", "32"], default="16")
special_combo = create_dropdown(["None", "Some", "All"], default="None")

# 4) Numbers, 5) Upper Cases
numbers_combo = create_dropdown(["Yes", "No"], default="Yes")
uppercase_combo = create_dropdown(["Yes", "No"], default="Yes")

# ================================
# CREATE TWO ROWS FOR DROPDOWNS
# -------------------------------
row1 = ttk.Frame(frame, style="Dark.TFrame")
row1.pack(pady=(0, 10), fill=tk.X)

# "Choose How"
choose_how_label = ttk.Label(row1, text="Choose How", style="Dark.TLabel")
choose_how_label.config(font=("Arial", 14, "bold"))
choose_how_label.pack(side=tk.LEFT, padx=(0,10))
choose_how_combo.pack(side=tk.LEFT, padx=(0,30))

# "Length"
length_label = ttk.Label(row1, text="Length", style="Dark.TLabel")
length_label.config(font=("Arial", 14, "bold"))
length_label.pack(side=tk.LEFT, padx=(0,10))
length_combo.pack(side=tk.LEFT, padx=(0,30))

# "Special Characters"
special_label = ttk.Label(row1, text="Special Characters", style="Dark.TLabel")
special_label.config(font=("Arial", 14, "bold"))
special_label.pack(side=tk.LEFT, padx=(0,10))
special_combo.pack(side=tk.LEFT)

row2 = ttk.Frame(frame, style="Dark.TFrame")
row2.pack(pady=(0, 20), fill=tk.X)

# "Numbers"
numbers_label = ttk.Label(row2, text="Numbers", style="Dark.TLabel")
numbers_label.config(font=("Arial", 14, "bold"))
numbers_label.pack(side=tk.LEFT, padx=(0,10))
numbers_combo.pack(side=tk.LEFT, padx=(0,30))

# "Upper Cases"
uppercase_label = ttk.Label(row2, text="Upper Cases", style="Dark.TLabel")
uppercase_label.config(font=("Arial", 14, "bold"))
uppercase_label.pack(side=tk.LEFT, padx=(0,10))
uppercase_combo.pack(side=tk.LEFT)

# ================================
# PASSWORD DISPLAY
# -------------------------------
password_label = ttk.Label(frame, text="Your Password", style="Dark.TLabel")
password_label.config(font=("Arial", 16, "bold"))
password_label.pack(pady=(0, 5))

password_entry = ttk.Entry(frame, style="Dark.TEntry", width=50)
password_entry.insert(0, "Your Password")  # placeholder
password_entry.pack(pady=(0, 20))

# ================================
# SAVE BUTTON
# -------------------------------
save_button = ttk.Button(frame, text="Save", style="Dark.TButton", command=on_save_click)
save_button.pack()

# ================================
# CENTER AND START
# -------------------------------
def finalize_layout():
    center_window(root)

root.after(0, finalize_layout)
root.mainloop()