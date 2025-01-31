import time
import tkinter as tk
from tkinter import messagebox
import pygame

def play_sound(sound_file,duration):
    pygame.mixer.init()
    pygame.mixer.music.load("C:\\Users\\Monster\\Desktop\\Python\\Pomodoro2\\alarm.mp3")
    pygame.mixer.music.play()

    time.sleep(duration)
    pygame.mixer.music.stop()


def start_timer():
    global running, time_left
    if not running:
        running = True
        time_left = 60 * 25
        countdown()

def pause_timer():
    global running
    running = False

def reset_timer():
    global running, time_left, current_phase, phase_index
    running = False
    time_left = WORK_DURATION * 60
    current_phase = "Çalışma Zamanı"
    phase_index = 0
    update_display()

def countdown():
    global time_left, running, phase_index, current_phase
    if running and time_left > 0:
        mins, secs = divmod(time_left, 60)
        timer_label.config(text=f"{mins:02d}:{secs:02d}")
        time_left -= 1
        root.after(1000, countdown)
    elif running and time_left == 0 :
        play_sound("C:\\Users\\Monster\\Desktop\\Python\\Pomodoro2\\alarm.mp3",5)
        phase_index += 1
        if phase_index % 2 == 0:
            current_phase = "Çalışma Zamanı"
            time_left = WORK_DURATION * 60
        elif phase_index < (CYCLES * 2) - 1:
            current_phase = "Kısa Mola"
            time_left = SHORT_BREAK * 60
        else:
            current_phase = "Uzun Mola"
            time_left = LONG_BREAK * 60
        messagebox.showinfo("Zaman Doldu!", f"{current_phase} Başlıyor!")
        countdown()
    update_display()

def update_display():
    phase_label.config(text=current_phase)
    mins, secs = divmod(time_left, 60)
    timer_label.config(text=f"{mins:02d}:{secs:02d}")

# Pomodoro Ayarları
WORK_DURATION = 25  # Çalışma süresi (dakika)
SHORT_BREAK = 5  # Kısa mola süresi (dakika)
LONG_BREAK = 15  # Uzun mola süresi (dakika)
CYCLES = 4  # Pomodoro döngü sayısı

time_left = WORK_DURATION * 60
running = False
current_phase = "Çalışma Zamanı"
phase_index = 0

# Tkinter GUI
root = tk.Tk()
root.title("Pomodoro Timer")
root.geometry("300x250")

phase_label = tk.Label(root, text=current_phase, font=("Helvetica", 16))
phase_label.pack(pady=10)

timer_label = tk.Label(root, text="25:00", font=("Helvetica", 36))
timer_label.pack()

start_button = tk.Button(root, text="Başlat", command=start_timer)
start_button.pack(pady=5)

pause_button = tk.Button(root, text="Duraklat", command=pause_timer)
pause_button.pack(pady=5)

reset_button = tk.Button(root, text="Sıfırla", command=reset_timer)
reset_button.pack(pady=5)

update_display()
root.mainloop()
