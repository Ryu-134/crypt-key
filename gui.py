import tkinter as tk
from tkinter import ttk, messagebox
import tkinter.font as tkFont
import subprocess
import os
import csv
import sys

# ------------------------------------------------
# FUNCTION: ensure_csv_header_and_write
# ------------------------------------------------
def append_to_csv(website, username, password, filename="user_data.csv"):
    """
    Writes a row [website, username, password] to the CSV file.
    If the CSV does not have the 'Website,Username,Password' header as its first row,
    this function inserts that header row before writing the entry.
    
    Note: CSV files are plain text and do not contain styling like background color.
    """
    # Check if file exists
    file_exists = os.path.isfile(filename)
    
    # Check if the file's first row is already the desired header
    header_needed = True
    if file_exists:
        with open(filename, "r", newline="") as csvfile:
            reader = csv.reader(csvfile)
            first_row = next(reader, None)  # Read the first row
            # If the first row matches our desired header, we don't need to insert it again
            if first_row == ["Website", "Username", "Password"]:
                header_needed = False

    # Now open the file in append mode and conditionally write the header
    with open(filename, "a", newline="") as csvfile:
        writer = csv.writer(csvfile)
        if header_needed:
            writer.writerow(["Website", "Username", "Password"])
        writer.writerow([website, username, password])

# ------------------------------------------------
# FUNCTION: generate_entry
# ------------------------------------------------
def generate_entry():
    """
    Retrieve website, username, and customization options from the GUI,
    then call the backend executable to generate and save a CSV entry directly (no confirmation popup).
    Update the password field with the saved password.
    """
    site = site_entry.get().strip()
    username = username_entry.get().strip()
    if not site or not username:
        messagebox.showerror("Input Error", "Both Website and Username are required!")
        return

    # Retrieve customization options from the dropdowns
    how_val = choose_how_var.get()         # "Custom" or "Random"
    length_val = length_var.get()          # e.g., "16"
    special_val = special_var.get()        # "None", "Some", or "All"
    numbers_val = numbers_var.get()        # "Yes" or "No"
    uppercase_val = uppercase_var.get()    # "Yes" or "No"

    # Construct the path to the backend executable
    executable = "gui/build/CryptKey.app/Contents/MacOS/CryptKey" if os.name != "nt" else "password_manager.exe"

    # Build command with customization flags (no --dry-run, we save directly)
    cmd = [
        executable,
        "--site", site,
        "--username", username,
        "--length", length_val,
        "--how", how_val,
        "--overwrite"
    ]
    if uppercase_val == "No":
        cmd.append("--no-uppercase")
    if numbers_val == "No":
        cmd.append("--no-numbers")
    if special_val == "None":
        cmd.append("--excludeSpecial")
    # If Custom is selected, get the custom password from the password_entry field and pass it
    if how_val == "Custom":
        custom_pwd = password_entry.get().strip()
        if custom_pwd and custom_pwd != "Your Password":
            cmd.extend(["--custom-password", custom_pwd])

    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        final_output = result.stdout.strip()
        parts_final = final_output.split(",")
        final_password = parts_final[2].strip() if len(parts_final) >= 3 else final_output

        # Update "Your Password" field in the main window
        password_entry.delete(0, tk.END)
        password_entry.insert(0, final_password)

        messagebox.showinfo("Entry Added", "Your entry has been saved!")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Backend Error", f"Error: {e.stderr.strip()}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# ------------------------------------------------
# Helper: center_window
# ------------------------------------------------
def center_window(win):
    win.update_idletasks()
    width = win.winfo_width()
    height = win.winfo_height()
    x = (win.winfo_screenwidth() // 2) - (width // 2)
    y = (win.winfo_screenheight() // 2) - (height // 2)
    win.geometry(f"{width}x{height}+{x}+{y}")

# ------------------------------------------------
# MAIN WINDOW SETUP (GUI)
# ------------------------------------------------
root = tk.Tk()
root.title("CryptKey")
root.configure(bg="white")
root.minsize(700, 400)
root.resizable(True, True)

# ------------------------------------------------
# COLORS & FONTS
# ------------------------------------------------
COLOR_ROOT_BG   = "white"  # Confirm window background matches main window
COLOR_FRAME_BG  = "#1E1E1E"
COLOR_WIDGET_BG = "#555555"
COLOR_FG        = "#FFFFFF"  # Dark style for TFrame and TLabels in modals

title_font = ("Arial", 36, "bold")
label_font = ("Arial", 14, "bold")
password_label_font = ("Arial", 16, "bold")
combo_font = ("Arial", 12)

# ------------------------------------------------
# TTK STYLE (Dark theme for confirm modals)
# ------------------------------------------------
style = ttk.Style(root)
style.theme_use("clam")
style.configure("Dark.TFrame", background=COLOR_FRAME_BG)
style.configure("Dark.TLabel", background=COLOR_FRAME_BG, foreground=COLOR_FG, font=label_font)
style.configure("Dark.TButton", background=COLOR_WIDGET_BG, foreground=COLOR_FG,
                borderwidth=0, focusthickness=0, relief="flat", font=label_font, padding=(6,6))
style.map("Dark.TButton", background=[("active", "#444444")])
style.configure("Dark.TEntry", fieldbackground=COLOR_WIDGET_BG, foreground=COLOR_FG,
                borderwidth=0, font=combo_font)

# ------------------------------------------------
# BLACK BANNER (TOP)
# ------------------------------------------------
banner = tk.Frame(root, bg="black", height=60)
banner.pack(fill="x", side="top")
title_label = tk.Label(banner, text="CryptKey", font=title_font, fg="white", bg="black")
title_label.pack(pady=10)

# ------------------------------------------------
# CONTENT FRAME (WHITE BG)
# ------------------------------------------------
content_frame = tk.Frame(root, bg="white")
content_frame.pack(fill="both", expand=True, pady=(10,0))

# ------------------------------------------------
# Helper: create_labeled_dropdown
# ------------------------------------------------
def create_labeled_dropdown(parent, label_text, options, default=None):
    container = tk.Frame(parent, bg="white")
    container.pack(side="left", padx=20)
    lbl = tk.Label(container, text=label_text, font=label_font, bg="white", fg="black")
    lbl.pack(pady=(0,5))
    var = tk.StringVar()
    combo = ttk.Combobox(container, textvariable=var, values=options, state="readonly", font=combo_font)
    combo.set(default if default else options[0])
    combo.pack()
    return var

# ------------------------------------------------
# ROW 1: "Choose How", "Length", "Special Characters"
# ------------------------------------------------
row1 = tk.Frame(content_frame, bg="white")
row1.pack(pady=(0,20))
choose_how_var = create_labeled_dropdown(row1, "Choose How", ["Custom", "Random"], default="Custom")
length_var = create_labeled_dropdown(row1, "Length", ["8", "12", "16", "20", "24", "32"], default="16")
special_var = create_labeled_dropdown(row1, "Special Characters", ["None", "Some", "All"], default="None")

# ------------------------------------------------
# ROW 2: "Numbers", "Upper Cases"
# ------------------------------------------------
row2 = tk.Frame(content_frame, bg="white")
row2.pack(pady=(0,20))
numbers_var = create_labeled_dropdown(row2, "Numbers", ["Yes", "No"], default="Yes")
uppercase_var = create_labeled_dropdown(row2, "Upper Cases", ["Yes", "No"], default="Yes")

# ------------------------------------------------
# ROW 3: Website & Username
# ------------------------------------------------
row3 = tk.Frame(content_frame, bg="white")
row3.pack(pady=(0,20))
website_label = tk.Label(row3, text="Website", font=label_font, bg="white", fg="black")
website_label.pack(side="left", padx=(0,10))
site_entry = tk.Entry(row3, width=30, bg="white", fg="black", font=combo_font, borderwidth=1, relief="flat", insertbackground="black")
site_entry.pack(side="left", padx=(0,30))
username_label = tk.Label(row3, text="Username", font=label_font, bg="white", fg="black")
username_label.pack(side="left", padx=(0,10))
username_entry = tk.Entry(row3, width=30, bg="white", fg="black", font=combo_font, borderwidth=1, relief="flat", insertbackground="black")
username_entry.pack(side="left")

# ------------------------------------------------
# "Your Password" Label & Entry
# ------------------------------------------------
password_label = tk.Label(content_frame, text="Your Password", font=password_label_font, bg="white", fg="black")
password_label.pack(pady=(0,5))
password_entry = tk.Entry(content_frame, width=50, font=combo_font, fg="black", bg="#f0f0f0")
password_entry.insert(0, "Your Password")
password_entry.pack(pady=(0,20))

# ------------------------------------------------
# "Save" Button
# ------------------------------------------------
save_button = tk.Button(content_frame, text="Save", font=combo_font, fg="black", bg="#e0e0e0",
                        relief="raised", bd=2, command=generate_entry)
save_button.pack()

# ------------------------------------------------
# Finalize Layout & Start
# ------------------------------------------------
def finalize_layout():
    center_window(root)
root.after(0, finalize_layout)
root.mainloop()