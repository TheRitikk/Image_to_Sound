import pytesseract
from PIL import Image, ImageTk
import pyttsx3
import tkinter as tk
from tkinter import filedialog

def is_image_file(file_path):
    image_extensions = {".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".ico", ".webp"}
    return any(file_path.lower().endswith(ext) for ext in image_extensions)

def say_text(image_label):
    # image_path = filedialog.askopenfilename()  # Open a file dialog to select an image
    image_path = filedialog.askopenfilename(
        title="Select an Image",
        filetypes=[("Image Files", "*.jpg *.jpeg *.png *.gif *.bmp *.tiff *.ico *.webp")]
    )
    if image_path:
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Replace with the actual path
        
        # Open and resize the image to your desired size
        img = Image.open(image_path)
        img = img.resize((200, 150))  
        
        # Convert the PIL image to a PhotoImage object for display in tkinter
        img = ImageTk.PhotoImage(img)
        image_label.config(image=img)
        image_label.image = img

        text = pytesseract.image_to_string(Image.open(image_path))
        
        def say_after_display():
            say(text)
        
        root.after(100, say_after_display)

def say(text, speed=100):
    engine = pyttsx3.init()
    engine.setProperty('rate', speed)
    for char in text:
        engine.say(char)
        engine.runAndWait()

# Create the main window
root = tk.Tk()
root.title("Text-to-Speech")
root.geometry("400x400")

# Create a button to select an image and initiate the text-to-speech process
select_button = tk.Button(root, text="Select Image", command=lambda: say_text(image_label))
select_button.pack(pady=20)

# Create a label to display the image
image_label = tk.Label(root)
image_label.pack()


# Start the GUI main loop
root.mainloop()
