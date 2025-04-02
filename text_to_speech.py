import tkinter as tk
import pyttsx3

def speak():
    text = text_entry.get("1.0", tk.END).strip()
    if text:
        engine.say(text)
        engine.runAndWait()

# Initialize text-to-speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Adjust speed if necessary
engine.setProperty('volume', 1.0)  # Adjust volume if necessary

# Create GUI window
root = tk.Tk()
root.title("Text-to-Speech Converter")
root.geometry("400x200")

# Create input text area
text_entry = tk.Text(root, height=5, width=40)
text_entry.pack(pady=20)

# Create button to trigger speech
speak_button = tk.Button(root, text="Speak", command=speak)
speak_button.pack()

# Run the main loop
root.mainloop()
