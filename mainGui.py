import tkinter as tk
from tkinter import *
from tkinter import filedialog
import cv2
import numpy as np
from PIL import Image
import wave
import sphinxbase
import pocketsphinx
import speech_recognition as sr
import pyperclip
import sys
import os
import pyttsx3
import pytesseract


class mainGui(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.filename = ""
        self.finalText = ""
        #Declaring frame
        self.master.geometry('1366x768')
        self.master.title("Text Extractor & Analyzer")
        self.frame = tk.Frame(master, width=1800, height=900)
        self.frame.pack(side=TOP, fill=X)

        #declaring buttons
        self.image_photo = tk.PhotoImage(file='Image.png')
        self.image_button = Button(self.frame, width=300, height=300, text="Image", font='Helvetica 18 bold', image=self.image_photo, bg="skyblue", fg='red', compound=TOP, command=self.imageFunc)
        self.image_button.pack(side=tk.LEFT, padx=2, pady=2)
        self.image_button.image = self.image_photo

        self.audio_photo = tk.PhotoImage(file='audio.png')
        self.audio_button = Button(self.frame, width=300, height=300, text="Audio", font='Helvetica 18 bold', image=self.audio_photo, bg="skyblue", fg='red', compound=TOP,command=self.audioFunc)
        self.audio_button.pack(side=tk.LEFT, padx=2, pady=2)
        self.audio_button.image = self.audio_photo

        self.video_photo = tk.PhotoImage(file='video.png')
        self.video_button = Button(self.frame, width=300, height=300, text="Video", font='Helvetica 18 bold', image=self.video_photo, bg="skyblue", fg='red', compound=TOP, command=self.videoFunc)
        self.video_button.pack(side=tk.LEFT, padx=2, pady=2)
        self.video_button.image = self.video_photo



    def imageFunc(self):
        root = tk.Toplevel(self)
        root.geometry('1366x768')
        root.title("Image to Text")
        self.frame = tk.Frame(root, width=1800, height=900)
        self.frame.pack(side=TOP, fill=X)


        self.capture = tk.PhotoImage(file='capturecam.png')
        self.captureimg_button = Button(self.frame, width=300, height=300, text="capture", font='Helvetica 18 bold', image=self.capture, bg="skyblue", fg='red', compound=TOP)
        self.captureimg_button.pack(side=tk.LEFT, padx=2, pady=2, fill=BOTH)
        self.captureimg_button.image = self.capture


        self.browse_image = tk.PhotoImage(file='select.png')
        self.browse_button = Button(self.frame, width=300, height=300, text='Browse', font='Helvetica 18 bold', image=self.browse_image, bg='skyblue', fg='red', compound=TOP, command=self.browseImageFunc)
        self.browse_button.pack(side=tk.LEFT, padx=2, pady=2, fill=BOTH)
        self.browse_button.image = self.browse_image

        self.textit_button = Button(root, width=10, height=2, text="Text it..", font='Helvetica 18 bold', bg="skyblue", fg='red', compound=BOTTOM, command=self.image_to_text)
        self.textit_button.place(relx=0.3, rely=0.7, anchor=CENTER)
        self.textit_button.pack(side=tk.BOTTOM, padx=2, pady=20)



    def audioFunc(self):
        root = tk.Toplevel(self)
        root.geometry('1366x768')
        root.title("Audio To Text")
        self.frame = tk.Frame(root, width=1800, height=900)
        self.frame.pack(side=TOP, fill=X)

        self.record = tk.PhotoImage(file='audio.png')
        self.recording_button = Button(self.frame, width=300, height=300, text="Record", font='Helvetica 18 bold', image=self.record, bg="skyblue", fg='red', compound=TOP, command=self.audio_to_text_record)
        self.recording_button.pack(side=tk.LEFT, padx=2, pady=2, fill=BOTH)
        self.recording_button.image = self.recording_button

        self.browse_image = tk.PhotoImage(file='select.png')
        self.browse_button = Button(self.frame, width=300, height=300, text='Browse', font='Helvetica 18 bold', image=self.browse_image, bg='skyblue', fg='red', compound=TOP, command=self.browseAudioFunc)
        self.browse_button.pack(side=tk.LEFT, padx=2, pady=2, fill=BOTH)
        self.browse_button.image = self.browse_image

        self.textit_button = Button(root, width=10, height=2, text="Text it..", font='Helvetica 18 bold', bg="skyblue", fg='red', compound=BOTTOM, command=self.audio_to_text)
        self.textit_button.place(relx=0.3, rely=0.7, anchor=CENTER)
        self.textit_button.pack(side=tk.BOTTOM, padx=2, pady=20)


    def videoFunc(self):
        root = tk.Toplevel(self)
        root.geometry('1366x768')
        root.title("Video To Text")
        self.frame = tk.Frame(root, width=1800, height=900)
        self.frame.pack(side=TOP, fill=X)

        self.capture = tk.PhotoImage(file='capturecam.png')
        self.captureimg_button = Button(self.frame, width=300, height=300, text="capture", font='Helvetica 18 bold', image=self.capture, bg="skyblue", fg='red', compound=TOP)
        self.captureimg_button.pack(side=tk.LEFT, padx=2, pady=2, fill=BOTH)
        self.captureimg_button.image = self.capture

        self.browse_image = tk.PhotoImage(file='select.png')
        self.browse_button = Button(self.frame, width=300, height=300, text='Browse', font='Helvetica 18 bold', image=self.browse_image, bg='skyblue', fg='red', compound=TOP, command=self.browseVideoFunc)
        self.browse_button.pack(side=tk.LEFT, padx=2, pady=2, fill=BOTH)
        self.browse_button.image = self.browse_image

        self.textit_button = Button(root, width=10, height=2, text="Text it..", font='Helvetica 18 bold', bg="skyblue", fg='red', compound=BOTTOM)
        self.textit_button.place(relx=0.3, rely=0.7, anchor=CENTER)
        self.textit_button.pack(side=tk.BOTTOM, padx=2, pady=20)


    #Browsing function
    def browseImageFunc(self):
        self.filename = filedialog.askopenfilename(initialdir="/", title="Select image file", filetypes=(("jpeg files", "*.jpg"), ("png files", "*.png"), ("all files", "*.*")))
        #print(filename)


    def browseAudioFunc(self):

        self.filename = filedialog.askopenfilename(initialdir="/", title="Select audio file", filetypes=(("wav files", "*.wav"), ("mp3 files", "*.mp3"), ("all files", "*.*")))
        #print(filename)


    def browseVideoFunc(self):
        self.filename = filedialog.askopenfilename(initialdir="/", title="Select video file", filetypes=(("mp4 files", "*.mp4"), ("3gp files", "*.3gp"), ("all files", "*.*")))
        #print(filename)

    def p_filename(self):
        print(self.filename)


    #def of Image to Text
    def image_to_text(self):
        self.img = cv2.imread(self.filename)

        # Convert to gray
        self.img = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)

        # Apply dilation and erosion to remove some noise

        kernel = np.ones((1, 1), np.uint8)
        # img = cv2.dilate(img, kernel, iterations=1)
        # img = cv2.erode(img, kernel, iterations=1)

        # Write image after removed noise
        cv2.imwrite("removed_noise.png", self.img)

        # Apply threshold to get image with only black and white
        self.img = cv2.adaptiveThreshold(self.img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)

        # Write the image after apply opencv to do some ...
        cv2.imwrite("binary.png", self.img)

        # Recognize text with tesseract for python
        self.finalText = pytesseract.image_to_string(Image.open(self.filename))
        print(self.finalText)

        # Remove template file
        os.remove("removed_noise.png")
        os.remove("binary.png")

        print("----------------- Done -------------------")
        self.result_textbox()




    #def of Audio To Text for file
    def audio_to_text(self):
        r = sr.Recognizer()

        audio = self.filename

        with sr.AudioFile(audio) as source:
            audio = r.listen(source)
            print("Recognizing...\n Please wait....")

            try:
                text = r.recognize_sphinx(audio)
                self.finalText = format(text)
                print("Speech was :\n  " + format(text))
            except Exception as e:
                self.finalText = e
                print(e)
            print("Done... Thank You!!")
        self.result_textbox()


    #def of audio to text for recorded file
    def audio_to_text_record(self):
        r = sr.Recognizer()

        with sr.Microphone() as source:
            print("Say something")
            audio = r.listen(source)

            try:
                text = r.recognize_sphinx(audio)
                self.finalText = format(text)
                print("Speech was :\n  " + format(text))
            except Exception as e:
                self.finalText = e
                print(e)
            print("Done... Thank You!!")
        self.result_textbox()




    #Output text Box window
    def result_textbox(self):
        print("result textbox :",self.finalText)
        root = tk.Toplevel(self)
        root.geometry('1366x768')
        root.title("Text Output")
        self.frame = tk.Frame(root, width=1800, height=900)
        self.frame.pack()

        '''
        #self.scrol_bar = Scrollbar(root)
        frametop = Frame(root)
        framebottom = Frame(root)
        frameleft = Frame(framebottom)
        frameright = Frame(framebottom)

        self.text_box = Text(frametop)
        scroll = Scrollbar(frametop, command=text.yview)
        self.btn1 = Button(frameleft, text="Copy to Clipboard")
        self.btn2 = Button(frameleft, text="Export as pdf")
        self.btn3 = Button(frameright, text="Translate")
        self.btn4 = Button(frameright, text="Return")

        self.text_box['yscrollcommand'] = scroll.set
        frametop.pack(side=TOP, fill=BOTH, expand=1)
        framebottom.pack(side=BOTTOM, fill=BOTH, expand=1)
        frameleft.pack(side=LEFT, fill=BOTH, expand=1)
        frameright.pack(side=RIGHT, fill=BOTH, expand=1)

        self.text_box.pack(side=TOP, fill=BOTH, padx=5, pady=5, expand=1)
        self.text_box.insert(END, self.finalText)
        self.btn1.pack(side=TOP, fill=BOTH, padx=5, pady=5, expand=1)
        self.btn2.pack(side=BOTTOM, fill=BOTH, padx=5, pady=5, expand=1)
        self.btn3.pack(side=TOP, fill=BOTH, padx=5, pady=5, expand=1)
        self.btn4.pack(side=BOTTOM, fill=BOTH, padx=5, pady=5, expand=1)

        '''
        self.textbox = Text(root, width=500, height=150, borderwidth=30)
        self.textbox.config(undo=True, wrap='word')
        self.textbox.place(relx=0.3, rely=0.7)
        self.textbox.pack(side=tk.TOP, padx=2, pady=2, fill=BOTH)
        self.textbox.insert(END, self.finalText)

        self.scrollb = Scrollbar(root, command=self.textbox.yview)
        self.scrollb.pack(side=tk.RIGHT, padx=2, pady=2)
        self.textbox['yscrollcommand'] = self.scrollb.set

        self.copy_button = Button(self.frame, text="Copy to clipboard", font='Helvetica 18 bold', bg="skyblue", fg='red', compound=BOTTOM, command=self.copy_to_clipboard)
        self.copy_button.place(relx=0.3, rely=0.7)
        self.copy_button.pack(padx=2, pady=2, fill=X)

        self.export_button = Button(self.frame, text="Export as txt", font='Helvetica 18 bold', bg="skyblue", fg='red', compound=BOTTOM, command=self.export_file)
        self.export_button.place(relx=0.3, rely=0.7)
        self.export_button.pack(padx=2, pady=2, fill=X)

        self.translate_button = Button(self.frame, text="Translate", font='Helvetica 18 bold', bg="skyblue", fg='red', compound=BOTTOM, command=self.translate_file)
        self.translate_button.place(relx=0.3, rely=0.7)
        self.translate_button.pack(padx=2, pady=2, fill=X)

        self.listen_button = Button(self.frame, text="Listen", font='Helvetica 18 bold', bg="skyblue", fg='red', compound=BOTTOM, command=self.listen_as_audio)
        self.listen_button.place(relx=0.3, rely=0.7)
        self.listen_button.pack(padx=2, pady=2, fill=X)



    def copy_to_clipboard(self):
        pyperclip.copy(self.finalText)
        spam = pyperclip.paste()


    def export_file(self):
        f = open("Output_text.txt", mode='w+',encoding = 'utf-8')
        f.write(self.finalText)
        f.close()

    def translate_file(self):
        pass



    def listen_as_audio(self):
        engine = pyttsx3.init()
        engine.say(self.finalText)
        engine.runAndWait()






if __name__ == '__main__':
    obj = mainGui()
    obj.mainloop()
