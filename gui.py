import tkinter as tk
from tkinter import ttk, messagebox
import tkinter.font as tkFont
import subprocess
import os

# ================================
# FUNCTION: generate_entry
# -------------------------------
# Retrieves website and username from the GUI.
# Calls the backend in dry-run mode (using --dry-run) so that it only generates the entry 
# (e.g., "website, username, password") without saving.
# Passes the entire CSV entry to confirm_entry() for confirmation.
# ================================
def generate_entry():
    site = site_entry.get().strip()
    username = username_entry.get().strip()

    if not site or not username:
        messagebox.showerror("Input Error", "Both Website and Username are required!")
        return

    executable = "./password_manager" if os.name != "nt" else "password_manager.exe"
    # Include --dry-run so the backend generates but does not save.
    cmd = [executable, "--site", site, "--username", username, "--dry-run"]

    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        entire_entry = result.stdout.strip()  # Expect format: "website, username, password"
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

# ================================
# FUNCTION: confirm_entry
# -------------------------------
# Opens a centered modal confirmation window displaying the entire CSV entry ("website, username, password").
# If the user confirms, the backend is called again (without --dry-run) to save the entry,
# and then the main window's output is updated to show only the generated password.
# If cancelled, nothing is saved.
# ================================
def confirm_entry(entire_entry, site, username, executable):
    parts = entire_entry.split(",")
    generated_password = parts[2].strip() if len(parts) >= 3 else entire_entry

    # Create modal confirmation window.
    confirm_win = tk.Toplevel(root)
    confirm_win.title("Confirm Entry")
    confirm_win.configure(bg=COLOR_ROOT_BG)
    confirm_win.grab_set()  # Modal

    # Set a minimum size and add a frame with extra padding.
    confirm_win.minsize(400, 200)
    confirm_frame = ttk.Frame(confirm_win, style="Dark.TFrame", padding=20)
    confirm_frame.pack(fill=tk.BOTH, expand=True)

    prompt_label = ttk.Label(confirm_frame, text="Entire Entry:", style="Dark.TLabel")
    prompt_label.pack(pady=(10, 5))
    entry_label = ttk.Label(confirm_frame, text=entire_entry, style="Dark.TLabel")
    entry_label.pack(pady=(0, 10))
    question_label = ttk.Label(confirm_frame, text="Does this look correct?", style="Dark.TLabel")
    question_label.pack(pady=(0, 10))

    # Use a frame for buttons and center them.
    button_frame = ttk.Frame(confirm_frame, style="Dark.TFrame")
    button_frame.pack(fill=tk.X, pady=10)
    yes_button = ttk.Button(button_frame, text="Yes", command=lambda: on_confirm(), style="Dark.TButton")
    no_button = ttk.Button(button_frame, text="No", command=lambda: on_cancel(), style="Dark.TButton")
    
    # Grid layout to center buttons:
    yes_button.grid(row=0, column=0, padx=10)
    no_button.grid(row=0, column=1, padx=10)
    button_frame.columnconfigure(0, weight=1)
    button_frame.columnconfigure(1, weight=1)

    def on_confirm():
        confirm_win.destroy()
        # Call backend without --dry-run to save the entry, with --overwrite.
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

    center_window(confirm_win)

# ================================
# SET UP THE MAIN WINDOW (GUI)
# -------------------------------
root = tk.Tk()
root.title("Password Manager GUI")
root.configure(bg="#000000")
root.minsize(600, 250)
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
custom_font = tkFont.Font(family="Segoe UI", size=12, weight="bold")    # For labels, buttons, output.
custom_entry_font = tkFont.Font(family="Segoe UI", size=12, weight="normal")  # For Entry widgets.

# ================================
# CONFIGURE STYLES FOR THE DARK THEME
# ----------------===============
style = ttk.Style(root)
style.theme_use("clam")

style.configure("Dark.TFrame", background=COLOR_FRAME_BG)
style.configure("Dark.TLabel", background=COLOR_FRAME_BG, foreground=COLOR_FG, font=custom_font)
style.configure("Dark.TButton", background="#555555", foreground=COLOR_FG,
                borderwidth=0, focusthickness=0, relief="flat", font=custom_font, padding=(6,6))
try:
    style.configure("Dark.TButton", bordercolor=COLOR_FG)
except tk.TclError:
    pass
style.map("Dark.TButton", background=[("active", "#444444")])
style.configure("Dark.TEntry", fieldbackground=COLOR_WIDGET_BG, foreground=COLOR_FG,
                borderwidth=0, font=custom_entry_font)

# --- New style for the Exit button with reduced horizontal padding ---
style.configure("Exit.TButton", 
    background="#555555", 
    foreground=COLOR_FG,
    borderwidth=0, 
    focusthickness=0, 
    relief="flat", 
    font=custom_font, 
    padding=(2,4))  # (horizontal, vertical) padding adjusted
style.map("Exit.TButton", background=[("active", "#444444")])

# ================================
# CREATE A FRAME TO HOLD THE WIDGETS
# -------------------------------
frame = ttk.Frame(root, style="Dark.TFrame", padding=20)
frame.pack(fill=tk.BOTH, expand=True)

# ================================
# CREATE AND PLACE THE WIDGETS
# -------------------------------

# Website Label and Entry:
site_label = ttk.Label(frame, text="Website:", style="Dark.TLabel")
site_label.grid(row=0, column=0, sticky=tk.W, pady=8, padx=5)
site_entry = tk.Entry(frame, width=50, bg=COLOR_WIDGET_BG, fg=COLOR_FG, font=custom_entry_font,
                      borderwidth=1, relief="flat", insertbackground="#FFFFFF")
site_entry.grid(row=0, column=1, sticky=tk.W, pady=8, padx=5)

# Username Label and Entry:
username_label = ttk.Label(frame, text="Username:", style="Dark.TLabel")
username_label.grid(row=1, column=0, sticky=tk.W, pady=8, padx=5)
username_entry = tk.Entry(frame, width=50, bg=COLOR_WIDGET_BG, fg=COLOR_FG, font=custom_entry_font,
                          borderwidth=1, relief="flat", insertbackground="#FFFFFF")
username_entry.grid(row=1, column=1, sticky=tk.W, pady=8, padx=5)

# Generate Button (centered):
generate_button = ttk.Button(frame, text="Generate Password", style="Dark.TButton", command=generate_entry)
generate_button.grid(row=2, column=0, columnspan=2, pady=12)

# Output Label and Text Widget:
output_label = ttk.Label(frame, text="Password:", style="Dark.TLabel")
output_label.grid(row=3, column=0, sticky=tk.NW, pady=8, padx=5)
output_text = tk.Text(frame, height=1, width=50, bg=COLOR_WIDGET_BG, fg=COLOR_FG, 
                       font=custom_font,
                       highlightthickness=0, highlightbackground=COLOR_FG,
                       highlightcolor=COLOR_FG, borderwidth=0, relief="flat", state=tk.DISABLED)
output_text.grid(row=3, column=1, pady=8, padx=5)

# Exit Button (centered) in its own frame:
exit_frame = ttk.Frame(frame, style="Dark.TFrame")
exit_frame.grid(row=4, column=0, columnspan=2, pady=12)
exit_button = ttk.Button(exit_frame, text="Exit", style="Exit.TButton", command=root.quit)
exit_button.pack()  # Pack without fill, so the button only takes its natural size

# ================================
# FUNCTION: center_window
# -------------------------------
# Centers the given window on the screen by calculating appropriate x and y offsets.
def center_window(win):
    win.update_idletasks()
    width = win.winfo_width()
    height = win.winfo_height()
    x = (win.winfo_screenwidth() // 2) - (width // 2)
    y = (win.winfo_screenheight() // 2) - (height // 2)
    win.geometry(f"{width}x{height}+{x}+{y}")

# Center the main window.
center_window(root)

# ================================
# START THE MAIN EVENT LOOP
# -------------------------------
root.mainloop()
