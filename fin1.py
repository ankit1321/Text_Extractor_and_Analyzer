import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import cv2
import numpy as np
from PIL import Image, ImageTk
import wave
import sphinxbase
import pocketsphinx
import speech_recognition as sr
import pyperclip
from googletrans import Translator
import sys
import os
import pyttsx3
import pytesseract
import pipes
import time
from resizeimage import resizeimage
from playsound import playsound



class mainGui:
    def __init__(self, root):
        self.root = root
        self.finalText = ""
        self.filename = ""
        self.translated_finalText = ""


    def main_window(self):
        self.root.geometry('1366x768')
        self.root.title("Text Extractor & Analyzer")
        self.root.configure(background='gray')
        # self.frame = Frame(root, width=1800, height=900)
        # self.frame.pack()


        self.quite_button = Button(root, text="Quit", width=15, border=5, font='inconsolata 18 bold', bg="red",
                                  fg='white', command=self.quit)
        self.quite_button.pack(padx=2, pady=2)
        self.quite_button.place(x=1130, y=10)
        self.home_button = Button(root, text="Home", width=15, border=5, font='inconsolata 18 bold', bg="red",
                                  fg='white', command=self.goto_home_window)
        self.home_button.pack(padx=2, pady=2)
        self.home_button.place(x=1130, y=80)

        self.image_photo = tk.PhotoImage(file='Image.png')
        self.image_button = Button(root, width=300, height=300, text="Image", border=5, font='inconsolata 18 bold',
                                   image=self.image_photo, bg="skyblue", fg='red', compound=TOP, command=self.imageFunc)
        self.image_button.pack(side=tk.LEFT, padx=5, pady=5)
        self.image_button.place(x=150)
        self.image_button.image = self.image_photo

        self.audio_photo = tk.PhotoImage(file='audio.png')
        self.audio_button = Button(root, width=300, height=300, text="Audio", border=5, font='inconsolata 18 bold',
                                   image=self.audio_photo, bg="skyblue", fg='red', compound=TOP, command=self.audioFunc)
        self.audio_button.pack(side=tk.LEFT, padx=5, pady=5)
        self.audio_button.place(x=465)
        self.audio_button.image = self.audio_photo

        self.video_photo = tk.PhotoImage(file='video.png')
        self.video_button = Button(root, width=300, height=300, text="Video", border=5, font='inconsolata 18 bold',
                                   image=self.video_photo, bg="skyblue", fg='red', compound=TOP)
        self.video_button.pack(side=tk.LEFT, padx=5, pady=5)
        self.video_button.place(x=780)
        self.video_button.image = self.video_photo


    def goto_home_window(self):
        if self.capture_button.winfo_ismapped():
            self.forget_image_window_button()

        self.main_window()





    def imageFunc(self):
        self.forget_main_window_button()

        self.textbox = Text(root, width=45, height=26, borderwidth=25, font=("inconsolata", 14))
        self.scr = Scrollbar(root, orient=VERTICAL, command=self.textbox.yview)
        self.scr.pack()
        self.scr.place(x=1090, y=60)
        self.textbox.config(undo=True, wrap='word')
        self.textbox.pack()
        self.textbox.place(x=560, y=20)
        # self.textbox.insert(END, self.finalText)

        self.imagebox = Text(root, width=45, height=26, borderwidth=25, font=("inconsolata", 14))
        self.imagebox.config(undo=True, wrap='word')
        self.imagebox.pack()
        self.imagebox.place(x=0, y=20)
        self.imagebox.insert(END, self.finalText)

        self.copy_button = Button(root, text="Copy to clipboard", width=15, border=5, font='inconsolata 18 bold', bg="red",
                                  fg='white', command=self.copy_to_clipboard)
        self.copy_button.pack(padx=2, pady=2)
        self.copy_button.place(x=1130, y=150)

        self.export_button = Button(root, text="Export as txt", width=15, border=5, font='inconsolata 18 bold', bg="red",
                                    fg='white', compound=TOP, command=self.export_file)
        self.export_button.pack(padx=2, pady=2)
        self.export_button.place(x=1130, y=220)

        self.translate_button = Button(root, text="Translate", width=15,  border=5, font='inconsolata 18 bold', bg="red",
                                       fg='white', command=self.translate_file)
        self.translate_button.pack(padx=2, pady=2)
        self.translate_button.place(x=1130, y=290)

        self.listen_button = Button(root, text="Listen", width=15, border=5, font='inconsolata 18 bold', bg="red", fg='white',
                                    command=self.listen_as_audio)
        self.listen_button.pack(padx=2, pady=2)
        self.listen_button.place(x=1130, y=360)


        self.text_it_button = Button(root, text="Text it", width=15, border=5, font='inconsolata 18 bold', bg='red', fg='white', command=self.image_to_text)
        self.text_it_button.pack(padx=2, pady=2)
        self.text_it_button.place(x=1130, y=430)

        self.view_original_button = Button(root, text="View Original", width=15, border=5, font='inconsolata 18 bold', bg='red', fg='white', command=self.view_original_text)


        self.capture_button = Button(root, text="Capture", width=15, border=5, font='inconsolata 18 bold', command=self.launch_camera)
        self.capture_button.pack(padx=2, pady=2)
        self.capture_button.place(x=180, y=670)


        self.browse_image_button = Button(root, text="Browse", width=15, border=5, font='inconsolata 18 bold', command=self.browseImageFunc)
        self.browse_image_button.pack(padx=2, pady=2)
        self.browse_image_button.place(x=730, y=670)




    def audioFunc(self):
        self.forget_main_window_button()

        self.textbox = Text(root, width=45, height=26, borderwidth=25, font=("inconsolata", 14))
        self.scr = Scrollbar(root, orient=VERTICAL, command=self.textbox.yview)
        self.scr.pack()
        self.scr.place(x=1090, y=60)
        self.textbox.config(undo=True, wrap='word')
        self.textbox.pack()
        self.textbox.place(x=560, y=20)
        # self.textbox.insert(END, self.finalText)

        self.audiobox = Text(root, width=45, height=26, borderwidth=25, font=("inconsolata", 14))
        self.audiobox.config(undo=True, wrap='word')
        self.audiobox.pack()
        self.audiobox.place(x=0, y=20)
        self.audiobox.insert(END, self.finalText)

        self.copy_button = Button(root, text="Copy to clipboard", width=15, border=5, font='inconsolata 18 bold',
                                  bg="red",
                                  fg='white', command=self.copy_to_clipboard)
        self.copy_button.pack(padx=2, pady=2)
        self.copy_button.place(x=1130, y=150)

        self.export_button = Button(root, text="Export as txt", width=15, border=5, font='inconsolata 18 bold',
                                    bg="red",
                                    fg='white', compound=TOP, command=self.export_file)
        self.export_button.pack(padx=2, pady=2)
        self.export_button.place(x=1130, y=220)

        self.translate_button = Button(root, text="Translate", width=15, border=5, font='inconsolata 18 bold', bg="red",
                                       fg='white', command=self.translate_file)
        self.translate_button.pack(padx=2, pady=2)
        self.translate_button.place(x=1130, y=290)

        self.listen_button = Button(root, text="Listen", width=15, border=5, font='inconsolata 18 bold', bg="red",
                                    fg='white',
                                    command=self.listen_as_audio)
        self.listen_button.pack(padx=2, pady=2)
        self.listen_button.place(x=1130, y=360)

        self.text_it_button = Button(root, text="Text it", width=15, border=5, font='inconsolata 18 bold', bg='red',
                                     fg='white', command=self.audio_to_text)
        self.text_it_button.pack(padx=2, pady=2)
        self.text_it_button.place(x=1130, y=430)

        self.view_original_button = Button(root, text="View Original", width=15, border=5, font='inconsolata 18 bold',
                                           bg='red', fg='white', command=self.view_original_text)

        self.record_audio_button = Button(root, text="Record", width=15, border=5, font='inconsolata 18 bold',
                                     command=self.launch_camera)
        self.record_audio_button.pack(padx=2, pady=2)
        self.record_audio_button.place(x=180, y=670)

        self.browse_image_button = Button(root, text="Browse", width=15, border=5, font='inconsolata 18 bold',
                                          command=self.browseAudioFunc)
        self.browse_image_button.pack(padx=2, pady=2)
        self.browse_image_button.place(x=730, y=670)


    #def of Image to Text
    def image_to_text(self):
        tk.messagebox.showwarning("Processing...", "Please wait")
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
        self.textbox.insert(END, self.finalText)
        print(self.finalText)


    #def of luanch camera and capture the image
    def launch_camera(self):
        cam = cv2.VideoCapture(0)

        cv2.namedWindow("test")

        img_counter = 0

        while True:
            ret, frame = cam.read()
            cv2.imshow("test", frame)
            if not ret:
                break
            k = cv2.waitKey(1)

            if k % 256 == 27:
                # ESC pressed
                print("Escape hit, closing...")
                messagebox.showinfo('Alert', 'Image Capture')
                break
            elif k % 256 == 32:
                # SPACE pressed
                img_name = "opencv_frame_{}.png".format(img_counter)
                cv2.imwrite(img_name, frame)
                print("{} written!".format(img_name))
                img_counter += 1

        cam.release()

        cv2.destroyAllWindows()
        tk.messagebox.showinfo("Alert", "Please select the capture image")




    #def of Audio To Text for file
    def audio_to_text(self):
        tk.messagebox.showwarning("Processing...", "Please wait")
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
        self.textbox.insert(END, self.finalText)


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





    def copy_to_clipboard(self):
        if self.view_original_button.winfo_ismapped():
            pyperclip.copy(self.translated_finalText)
            spam = pyperclip.paste()

        else:
            pyperclip.copy(self.finalText)
            spam = pyperclip.paste()


    def view_original_text(self):
        self.view_original_button.place_forget()
        self.textbox.delete('1.0',END)
        self.textbox.insert(END, self.finalText)


    def export_file(self):
        if self.view_original_button.winfo_ismapped():
            f = open("Translated_Output_text.txt", mode='w+', encoding='utf-8')
            f.write(self.translated_finalText)
            f.close()

        else:
            f = open("Output_text.txt", mode='w+', encoding='utf-8')
            f.write(self.finalText)
            f.close()



    # Translation function
    def translate_file(self):
        self.translator = Translator()
        self.result = self.translator.translate(self.finalText, 'mr')
        print(self.result)
        self.translated_finalText = self.result.text
        self.textbox.delete('1.0', END)
        self.textbox.insert(END, self.translated_finalText)
        self.view_original_button.pack(padx=2, pady=2)
        self.view_original_button.place(x=1130, y=500)




    def listen_as_audio(self):
        engine = pyttsx3.init()
        engine.setProperty('rate', 125)
        engine.say(self.finalText)
        engine.runAndWait()



    def forget_main_window_button(self):
        self.image_button.place_forget()
        self.audio_button.place_forget()
        self.video_button.place_forget()

    def forget_image_window_button(self):
        if self.capture_button.winfo_ismapped():
            self.filename = ""
            self.imagebox.delete('1.0', END)
            self.imagebox.place_forget()
            self.textbox.place_forget()
            self.browse_image_button.place_forget()
            self.capture_button.place_forget()
            self.copy_button.place_forget()
            self.export_button.place_forget()
            self.text_it_button.place_forget()
            self.listen_button.place_forget()
            self.translate_button.place_forget()
            self.view_original_button.place_forget()
            self.scr.place_forget()

        # if self.record_audio_button.winfo_ismapped():
        #     self.filename = ""
        #     self.audiobox.delete('1.0', END)
        #     self.audiobox.place_forget()
        #     self.textbox.place_forget()
        #     self.browse_image_button.place_forget()
        #     self.capture_button.place_forget()
        #     self.copy_button.place_forget()
        #     self.export_button.place_forget()
        #     self.text_it_button.place_forget()
        #     self.listen_button.place_forget()
        #     self.translate_button.place_forget()
        #     self.view_original_button.place_forget()
        #     self.scr.place_forget()


    def quit(self):
        root.destroy()


    def put_imageinto_textbox(self):
        # self.resize_image()
        self.image = tk.PhotoImage(file=self.filename)
        self.imagebox.image_create(tk.END, image=self.image)




    def put_audiointo_textbox(self):
        pass




    def browseImageFunc(self):
        self.filename = filedialog.askopenfilename(initialdir="/", title="Select image file", filetypes=(("png files", "*.png"), ("jpeg files", "*.jpg"), ("all files", "*.*")))
        #print(filename)
        if self.filename:
            if len(self.filename) == 0:
                messagebox.showerror('Error', 'Please select a File')

            else:
                self.put_imageinto_textbox()



    def browseAudioFunc(self):
        self.filename = filedialog.askopenfilename(initialdir="/", title="Select image file", filetypes=(("wav files", "*.wav"), ("mp3 files", "*.mp3"), ("all files", "*.*")))
        #print(filename)
        if self.filename:
            if len(self.filename) == 0:
                messagebox.showerror('Error', 'Please select a File')

            else:
                self.put_audiointo_textbox()







if __name__ == '__main__':
    root = Tk()
    obj = mainGui(root)
    obj.main_window()
    root.wait_window()
