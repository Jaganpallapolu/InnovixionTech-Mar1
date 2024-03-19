import datetime
import winsound
import tkinter as tk
from tkinter import messagebox
import time
import os

alarm_ringing = False


def set_alarm():
    global alarm_ringing
    alarm_time = alarm_entry.get()
    try:
        alarm_hour, alarm_minute = map(int, alarm_time.split(':'))
    except ValueError:
        messagebox.showerror("Error", "Invalid time format. Please use HH:MM")
        return

    now = datetime.datetime.now()
    if now.hour > alarm_hour or (now.hour == alarm_hour and now.minute >= alarm_minute):
        messagebox.showerror("Error", "The entered time is already passed for today.")
        return

    alarm_ringing = True
    alarm_datetime = datetime.datetime(now.year, now.month, now.day, alarm_hour, alarm_minute)
    remaining_time = alarm_datetime - now

    while remaining_time.total_seconds() > 0 and alarm_ringing:
        remaining_time = alarm_datetime - datetime.datetime.now()
        stopwatch_label.config(text=str(remaining_time))
        root.update()
        time.sleep(0.1)

    if alarm_ringing:
        sound_file = "C:/Users/jagan mohan reddy/Downloads/chillin39-20915.wav"
        if os.path.exists(sound_file):
            winsound.PlaySound(sound_file, winsound.SND_FILENAME | winsound.SND_LOOP | winsound.SND_ASYNC)
        else:
            messagebox.showerror("Error", "Sound file not found.")


def stop_alarm():
    global alarm_ringing
    alarm_ringing = False
    winsound.PlaySound(None, winsound.SND_PURGE)


root = tk.Tk()
root.title("Alarm Clock")


window_width = 400
window_height = 300
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2
root.geometry(f"{window_width}x{window_height}+{x}+{y}")


bg_color = "#f0f0f0"
fg_color = "#333333"

root.configure(bg=bg_color)


frame = tk.Frame(root, bg=bg_color)
frame.pack(expand=True, fill='both')

label = tk.Label(frame, text="Enter alarm time (HH:MM):", font=("Arial", 16), bg=bg_color, fg=fg_color)
label.pack(side='top', pady=20)
alarm_entry = tk.Entry(frame, font=("Arial", 16), bg=bg_color, fg=fg_color)
alarm_entry.pack(side='top', pady=10)


def on_enter(event):
    event.widget.config(bg="#cccccc")  # light gray


def on_leave(event):
    event.widget.config(bg=bg_color)


set_alarm_button = tk.Button(frame, text="Set Alarm", command=set_alarm, font=("Arial", 16), bg=bg_color, fg=fg_color)
set_alarm_button.pack(side='top', pady=10)
set_alarm_button.bind("<Enter>", on_enter)
set_alarm_button.bind("<Leave>", on_leave)

stop_alarm_button = tk.Button(frame, text="Stop Alarm", command=stop_alarm, font=("Arial", 16), bg=bg_color, fg=fg_color)
stop_alarm_button.pack(side='top', pady=10)
stop_alarm_button.bind("<Enter>", on_enter)
stop_alarm_button.bind("<Leave>", on_leave)

stopwatch_label = tk.Label(frame, text="", font=("Arial", 16), bg=bg_color, fg=fg_color)
stopwatch_label.pack(side='top', pady=20)

root.mainloop()
