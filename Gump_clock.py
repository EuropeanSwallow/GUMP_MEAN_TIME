import tkinter as tk
from datetime import datetime

def convert_to_gump_hours():
    now = datetime.now()
    current_hour = now.hour
    current_minute = now.minute

    total_minutes = (current_hour * 60) + current_minute
    custom_hours = total_minutes // 142
    remaining_minutes = total_minutes % 142
    custom_hour_fraction = round(custom_hours + (remaining_minutes / 142), 2)

    #long_result_text = (f"It is currently {custom_hours} Gump hours and {remaining_minutes} minutes\n")
    short_result_text = (f"{custom_hour_fraction} Gumps")
    label_result.config(text=short_result_text)

    # Schedule the function to run again after 10,000 ms (10 seconds)
    window.after(10000, convert_to_gump_hours)


# --- GUI Setup ---
window = tk.Tk()
window.title("Gump Time Converter")
window.geometry("400x200")
window.config(bg="black")

label_title = tk.Label(window, text="Gump Mean Time GMT+0", font=("Digital-7", 18), fg="lime", bg="black")
label_title.pack(pady=10)

label_result = tk.Label(window, text="", font=("Digital-7", 24), fg="cyan", bg="black")
label_result.pack(pady=20)

#btn_update = tk.Button(window, text="Update", command=convert_to_gump_hours, font=("Digital-7", 14), fg="black", bg="yellow", relief="solid")
#btn_update.pack(pady=10)

# Start automatic updating
convert_to_gump_hours()

window.mainloop()
