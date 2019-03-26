from tkinter import*
import tkinter as tk
from tkinter import filedialog
import cv2
import numpy as np
import pytesseract
from PIL import Image
import os


def imageToText(filename):
    # Read image with opencv
    img = cv2.imread(filename)

    # Convert to gray
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply dilation and erosion to remove some noise

    kernel = np.ones((1, 1), np.uint8)
    # img = cv2.dilate(img, kernel, iterations=1)
    # img = cv2.erode(img, kernel, iterations=1)

    # Write image after removed noise
    cv2.imwrite("removed_noise.png", img)

    # Apply threshold to get image with only black and white
    img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)

    # Write the image after apply opencv to do some ...
    cv2.imwrite("binary.png", img)

    # Recognize text with tesseract for python
    result = pytesseract.image_to_string(Image.open("binary.png"))
    print(result)

    # Remove template file
    os.remove("removed_noise.png")
    os.remove("binary.png")

    print("----------------- Done -------------------")


class image:

    def __init__(self, root):
        self.root = root
        #global button_flag
        frame = Frame(root, width=1800, height=1400)
        frame.pack(side=TOP, fill=X)
        root.geometry("1000x600")
        root.title("Image ")

        self.capture = tk.PhotoImage(file='capturecam.png')
        self.captureimg_button = Button(frame, width=300, height=300, text="capture", font='Helvetica 18 bold',
                                   image=self.capture, bg="skyblue", fg='red', compound=TOP)
        self.captureimg_button.pack(side=tk.LEFT, padx=2, pady=2, fill=BOTH)
        self.captureimg_button.image = self.capture


        self.browse_image = tk.PhotoImage(file='select.png')
        self.browse_button = Button(frame, width=300,height=300, text='Browse',  font='Helvetica 18 bold',image=self.browse_image, bg='skyblue', fg='red', compound=TOP, command=lambda :self.browsefunc())
        self.browse_button.pack(side=tk.LEFT, padx=2, pady=2, fill=BOTH)
        self.browse_button.image = self.browse_image


        self.textit_button = Button(root,text = "Text it..",font='Helvetica 18 bold',bg="skyblue",fg='red',compound=TOP, command=lambda:imageToText(filename))
        self.textit_button.place(relx=0.3,rely=0.7,anchor=CENTER)


    def browsefunc(self):
        global filename
        filename = filedialog.askopenfilename(initialdir="/", title="Select image file", filetypes=(
           ("all files", "*.*"), ("jpeg files", "*.jpg"), ("png files", "*.png")))




root = Tk()
img = image(root)

root.mainloop()
