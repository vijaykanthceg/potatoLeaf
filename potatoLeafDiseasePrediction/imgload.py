from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
from tensorflow import keras
from keras.models import load_model
from keras.preprocessing import image
from keras.applications.vgg16 import preprocess_input
import numpy as np
import pyautogui as pag
import warnings

warnings.filterwarnings("ignore")


def openfilename():
    filename = filedialog.askopenfilename(title='"pen')
    return filename


def open_img():
    x = openfilename()
    img = Image.open(x)
    img = img.resize((250, 250), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    panel = Label(root, image=img)
    panel.image = img
    panel.grid(row=2)
    model = keras.models.load_model("potato.h5")
    model.load_weights("potato_weights.h5")
    img1 = image.load_img(x, target_size=(150, 150))
    y = image.img_to_array(img1)
    y = np.expand_dims(y, axis=0)
    img_data = preprocess_input(y)
    img_data /= 255.0
    classes = model.predict(img_data)
    result = classes[0]
    if (result < 0.5):
        print("Healthy Potato")
        pag.alert("Leaf is Healthy")
    else:
        print("Late Blight")
        pag.alert("The Leaf is infected by late blight")


root = Tk()
root.title("Image Loader")
root.geometry("550x300")
root.resizable(width=True, height=True)
btn = Button(root, text='Upload Image', command=open_img).grid(row=1, columnspan=4)
root.mainloop()
