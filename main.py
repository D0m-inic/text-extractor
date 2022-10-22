import cv2
import pytesseract
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from PIL import ImageTk, Image

pytesseract.pytesseract.tesseract_cmd = "/opt/homebrew/bin/tesseract"

root = Tk()
root.title("Text Extractor - Dominic Qu")

def extract():
    textExtracted.set(pytesseract.image_to_string(Image.open(filePath.get())))

def upload():
    try:
        filePath.set(filedialog.askopenfilename())
    except:
        pass


mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N,W,E,S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

filePath = StringVar()
filePath_entry = ttk.Entry(mainframe,textvariable=filePath)
filePath_entry.grid(column=1, row=2, sticky=(W,E))

ttk.Label(mainframe, text="Enter a relative or abolute file path, or click 'Upload Image' and choose the image you would like to convert to text.").grid(column=1, row=1, sticky = (W,E))

textExtracted = StringVar()
ttk.Label(mainframe, textvariable=textExtracted).grid(column=1, row=3, sticky=W)

ttk.Button(mainframe, text="Extract Image", command=extract).grid(column=3,row=3, sticky=E)
ttk.Button(mainframe, text="Upload Image", command=upload).grid(column=2,row=2, sticky = W)

for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

filePath_entry.focus()
root.bind("<Return>", extract)

root.mainloop()