import tkinter as tk
from datetime import datetime

# --- Functions ---
def current_time():
    """Updates the live Gump clock every 10 seconds."""
    now = datetime.now()
    total_minutes = (now.hour * 60) + now.minute
    custom_hours = total_minutes // 142
    remaining_minutes = total_minutes % 142
    custom_hour_fraction = round(custom_hours + (remaining_minutes / 142), 2)

    short_result_text = f"{custom_hour_fraction} Gumps"
    label_result_current.config(text=short_result_text)

    # Schedule again in 10s
    window.after(10000, current_time)


def convert_to_gump_hours(hours, minutes):
    """Converts user input hours + minutes into Gump time."""
    convert_total_minutes = (hours * 60) + minutes
    convert_custom_hours = convert_total_minutes // 142
    convert_remaining_minutes = convert_total_minutes % 142
    convert_custom_hour_fraction = round(convert_custom_hours + (convert_remaining_minutes / 142), 2)

    conv_result_text = f"Converted: {convert_custom_hour_fraction} Gumps"
    label_result_converted.config(text=conv_result_text)


def handle_input():
    """Handles input from entry fields and updates conversion label."""
    try:
        hours = int(hour_entry.get())
        minutes = int(min_entry.get())
        convert_to_gump_hours(hours, minutes)
    except ValueError:
        label_result_converted.config(text="Invalid input! Enter numbers only.")


# --- GUI Setup ---
window = tk.Tk()
window.title("Gump Time Converter")
window.geometry("400x350")
window.config(bg="black")

# Title
label_title = tk.Label(window, text="Gump Mean Time GMT+0", font=("Digital-7", 18),fg="lime", bg="black")
label_title.pack(pady=10)

# Live result label
label_result_current = tk.Label(window, text="", font=("Digital-7", 24),fg="cyan", bg="black")
label_result_current.pack(pady=10)

# Title
convert_title = tk.Label(window, text="Convert hours/mins to Gumps", font=("Digital-7", 10),fg="lime", bg="black")
convert_title.pack(pady=10)

# Input fields
label_hour = tk.Label(window, text="Insert Hour", font=("Digital-7", 10), fg="cyan", bg="black")
label_hour.pack()
hour_entry = tk.Entry(window)
hour_entry.pack()

label_minute = tk.Label(window, text="Insert Minute", font=("Digital-7", 10), fg="cyan", bg="black")
label_minute.pack()
min_entry = tk.Entry(window)
min_entry.pack()

# Button for conversion
btn_update = tk.Button(window, text="Calculate", command=handle_input,font=("Digital-7", 10), fg="black", bg="yellow", relief="solid")
btn_update.pack(pady=10)

# Conversion result label
label_result_converted = tk.Label(window, text="", font=("Digital-7", 14),fg="yellow", bg="black")
label_result_converted.pack(pady=10)


# Start live updating
current_time()

window.mainloop()

