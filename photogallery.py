import os
import cv2
from tkinter import *
from PIL import Image,ImageTk

path=r"C:\Users\delso\Desktop\Open Cv with python\imagee"
\Lesson-6 -Image Collage (Video)\images"

image_files =[]

for file in os.listdir(path):
    if file.endswith(",jpg") or file.endswith(".png") or file.endswith(".jpeg"):
        image_files.append(file)

current_image= 0

root=Tk()
root.title("Photo Gallery with opencv")

def load_image():
    global photo

    img_path=os.path.join(path,image_files[current_image])
    img=cv2.imread(img_path)
    img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    img=Image.fromarray(img)
    img=img.resize((500,400))
    photo=ImageTk.PhotoImage(img)

    label.config(image=photo)
    label.image=photo

def grayscale():
    global photo

    img_path = os.path.join(path,image_files[current_image])
    img=cv2.imread(img_path)

    gray=cv2.cvtColor(img,cv2,COLOR_BGR2GRAY)
    gray = cv2.cvtColor(gray, cv2.COLOR_GRAY2RGB)

img = Image.fromarray(gray)
img = img.resize((500, 400))
photo = ImageTk.PhotoImage(img)

label.config(image=photo)
label.image = photo