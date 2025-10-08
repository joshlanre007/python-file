import tkinter as tk
from tkinter import messagebox, ttk
from pytubefix import YouTube
import os
from PIL import Image, ImageTk  # for displaying images

# Progress bar update function
def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage = (bytes_downloaded / total_size) * 100
    download_progress.set(percentage)
    window.update_idletasks()

# Download function
def download_video():
    video_url = url.get().strip()
    download_path = os.path.expanduser("~/Downloads")

    if not video_url:
        messagebox.showwarning("Input Error", "Please enter a YouTube URL.")
        return

    try:
        yt = YouTube(video_url, on_progress_callback=on_progress)
        stream = yt.streams.get_highest_resolution()
        stream.download(output_path=download_path)
        messagebox.showinfo("Success", f"Downloaded:\n{yt.title}\n\nSaved to {download_path}")

    except Exception as e:
        error_message = str(e)
        if "404" in error_message:
            messagebox.showerror("Error", "Video not found (HTTP 404). Please try another link.")
        elif "410" in error_message:
            messagebox.showerror("Error", "This video is no longer available (HTTP 410).")
        elif "400" in error_message:
            messagebox.showerror("Error", "Bad request (HTTP 400). Please check the link format:\nhttps://www.youtube.com/watch?v=xxxx")
        else:
            messagebox.showerror("Error", f"Failed to download video.\nReason: {error_message}")

# Create the main window
window = tk.Tk()
window.title("YouTube Video Downloader")

# === Add YouTube Logo ===
try:
    logo_image = Image.open("youtube.png")  # make sure youtube.png is in the same folder
    logo_image = logo_image.resize((120, 70))  # resize for better fit
    logo_photo = ImageTk.PhotoImage(logo_image)

    logo_label = tk.Label(window, image=logo_photo)
    logo_label.image = logo_photo  # keep a reference so it's not garbage-collected
    logo_label.pack(pady=5)
except Exception as e:
    print("Logo not found:", e)

# Widgets
url_label = tk.Label(window, text="YouTube URL:")
url_label.pack(pady=5)

url = tk.Entry(window, width=50)
url.pack(pady=10)

download_button = tk.Button(window, text="Download", command=download_video, bg="red", fg="white")
download_button.pack(pady=15)

# Progress bar
download_progress = tk.DoubleVar()
download_bar = ttk.Progressbar(window, variable=download_progress, maximum=100)
download_bar.pack(pady=10, fill="x")

# Window config
window.geometry("500x300")
window.resizable(False, False)

# Run app
window.mainloop()
