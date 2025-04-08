import tkinter as tk
from tkinter import ttk, messagebox
import tkinter.font as tkFont
import subprocess
import os
import csv
import sys

# ------------------------------------------------
# FUNCTION: append_to_csv
# ------------------------------------------------
def append_to_csv(website, username, password, filename="user_data.csv"):
    """Append the entry to the CSV file, including column headers if file is new or empty."""
    file_exists = os.path.isfile(filename)
    write_header = (not file_exists) or (os.path.getsize(filename) == 0)
    with open(filename, "a", newline="") as csvfile:
        writer = csv.writer(csvfile)
        if write_header:
            writer.writerow(["Website", "Username", "Password"])
        writer.writerow([website, username, password])

# ------------------------------------------------
# FUNCTION: generate_entry
# ------------------------------------------------
def generate_entry():
    """
    Retrieves website and username from the GUI.
    Calls the backend in dry-run mode using the compiled executable.
    Then passes the CSV-formatted entry to confirm_entry() for confirmation.
    """
    site = site_entry.get().strip()
    username = username_entry.get().strip()
    if not site or not username:
        messagebox.showerror("Input Error", "Both Website and Username are required!")
        return

    # For non-Windows, use the relative path based on the structure:
    #   Project Folder/CryptKey/crypt-key/gui.py  and
    #   Project Folder/CryptKey/gui/CryptKey/build/CryptKey.app/Contents/MacOS/CryptKey
    executable = "gui/CryptKey/build/CryptKey.app/Contents/MacOS/CryptKey" if os.name != "nt" else "password_manager.exe"
    
    # Include --dry-run so the backend only generates the entry.
    cmd = [executable, "--site", site, "--username", username, "--dry-run"]

    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        entire_entry = result.stdout.strip()  # Expected format: "website, username, password"
        confirm_entry(entire_entry, site, username, executable)
    except subprocess.CalledProcessError as e:
        err_msg = e.stderr.strip()
        if "Entry for this site already exists" in err_msg:
            answer = messagebox.askyesno("Duplicate Detected", 
                                         "An entry for this site already exists.\nDo you want to overwrite it?")
            if answer:
                cmd.append("--overwrite")
                try:
                    result = subprocess.run(cmd, capture_output=True, text=True, check=True)
                    entire_entry = result.stdout.strip()
                    confirm_entry(entire_entry, site, username, executable)
                except subprocess.CalledProcessError as e2:
                    messagebox.showerror("Backend Error", f"Error: {e2.stderr.strip()}")
            else:
                messagebox.showinfo("Cancelled", "Operation cancelled.")
        else:
            messagebox.showerror("Backend Error", f"Error: {err_msg}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# ------------------------------------------------
# FUNCTION: confirm_entry
# ------------------------------------------------
def confirm_entry(entire_entry, site, username, executable):
    """
    Opens a modal confirmation window displaying the generated entry.
    If the user confirms, calls the backend again (without --dry-run) to save the entry,
    then updates the main window's output to show the final generated password.
    """
    parts = entire_entry.split(",")
    generated_password = parts[2].strip() if len(parts) >= 3 else entire_entry

    confirm_win = tk.Toplevel(root)
    confirm_win.title("Confirm Entry")
    confirm_win.configure(bg=COLOR_ROOT_BG)
    confirm_win.grab_set()  # Modal

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
        # Call backend again without --dry-run to save the entry, with --overwrite.
        cmd_confirm = [executable, "--site", site, "--username", username, "--overwrite"]
        try:
            result_confirm = subprocess.run(cmd_confirm, capture_output=True, text=True, check=True)
            final_output = result_confirm.stdout.strip()
            parts_final = final_output.split(",")
            final_password = parts_final[2].strip() if len(parts_final) >= 3 else final_output

            output_text.config(state=tk.NORMAL)
            output_text.delete("1.0", tk.END)
            output_text.insert(tk.END, final_password)
            output_text.config(state=tk.DISABLED)

            messagebox.showinfo("Entry Added", "Your entry has been saved!")
        except subprocess.CalledProcessError as e:
            messagebox.showerror("Backend Error", f"Error: {e.stderr.strip()}")

    def on_cancel():
        confirm_win.destroy()
        messagebox.showinfo("Cancelled", "Entry not saved.")

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
# MAIN WINDOW SETUP
# ------------------------------------------------
root = tk.Tk()
root.title("CryptKey")
root.configure(bg="white")  # White background
root.minsize(700, 400)
root.resizable(True, True)

# ------------------------------------------------
# COLORS & FONTS
# ------------------------------------------------
COLOR_ROOT_BG   = "white"     # For confirm window background
COLOR_FRAME_BG  = "#1E1E1E"
COLOR_WIDGET_BG = "#555555"
COLOR_FG        = "#FFFFFF"   # Dark theme for confirm windows

title_font = ("Arial", 36, "bold")
label_font = ("Arial", 14, "bold")
password_label_font = ("Arial", 16, "bold")
combo_font = ("Arial", 12)

# ------------------------------------------------
# TTK STYLE (Dark theme for confirm window)
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
# TOP BLACK BANNER
# ------------------------------------------------
banner = tk.Frame(root, bg="black", height=60)
banner.pack(fill="x", side="top")
title_label = tk.Label(banner, text="CryptKey", font=title_font, fg="white", bg="black")
title_label.pack(pady=10)

# ------------------------------------------------
# MAIN CONTENT FRAME (White)
# ------------------------------------------------
content_frame = tk.Frame(root, bg="white")
content_frame.pack(fill="both", expand=True, pady=(10,0))

# ------------------------------------------------
# Helper: Create Labeled Dropdown in a Container
# ------------------------------------------------
def create_labeled_dropdown(parent, label_text, options, default=None):
    container = tk.Frame(parent, bg="white")
    container.pack(side="left", padx=20)  # Adjust spacing as needed
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
row1.pack(pady=(0,20))
choose_how_var = create_labeled_dropdown(row1, "Choose How", ["Custom", "Random"], default="Custom")
length_var = create_labeled_dropdown(row1, "Length", ["8", "12", "16", "20", "24", "32"], default="16")
special_var = create_labeled_dropdown(row1, "Special Characters", ["None", "Some", "All"], default="None")

# ------------------------------------------------
# Row 2: "Numbers", "Upper Cases"
# ------------------------------------------------
row2 = tk.Frame(content_frame, bg="white")
row2.pack(pady=(0,20))
numbers_var = create_labeled_dropdown(row2, "Numbers", ["Yes", "No"], default="Yes")
uppercase_var = create_labeled_dropdown(row2, "Upper Cases", ["Yes", "No"], default="Yes")

# ------------------------------------------------
# Row 3: Website & Username
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
# Finalize Layout & Start the App
# ------------------------------------------------
def finalize_layout():
    center_window(root)
root.after(0, finalize_layout)
root.mainloop()