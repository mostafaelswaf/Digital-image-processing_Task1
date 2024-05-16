from tkinter import *
from tkinter import messagebox
import cv2
import numpy as np
from PIL import Image, ImageTk




original_image = cv2.imread("lenna.png")
#---------------------------------------------
def add_button(text,command):
    button = Button(window,text=text,command=command,bg="#B9B4C7",font=("consle",12))
    button.pack(pady=6)

#----------------------------------------------
def add_buttons () :
    add_button(text="original",command=load)
    add_button(text="sobel edge detector",command=apply_sobel_edge_detector)
    add_button(text="Ersion",command=update_erosion)
    add_button(text="Dilation",command=update_dilation)



#-----------------------------------------------
def update_image(img):
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(img)
        img = ImageTk.PhotoImage(img)
        lable.config(image=img)
        #lablel.pack()
        lable.image = img

#-------------------------------------------------
def load ():
    photo1 = PhotoImage(file="lenna.png")
    lable.config(image=photo1)
    lable.image= photo1

#-------------------------------------------------
# Apply Sobel edge detector to detect edges in the image
def apply_sobel_edge_detector():
    # Convert the original image to grayscale
    gray_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
    # Compute the horizontal and vertical gradients using Sobel operators
    sobel_x = cv2.Sobel(gray_image, cv2.CV_64F, 1, 0, ksize=3)
    sobel_y = cv2.Sobel(gray_image, cv2.CV_64F, 0, 1, ksize=3)
    # Compute the magnitude of gradients
    sobel_image = np.sqrt(sobel_x**2 + sobel_y**2)
    # Normalize the gradient magnitude image
    sobel_image = cv2.normalize(sobel_image, None, 0, 255, cv2.NORM_MINMAX, dtype=cv2.CV_8U)
    # Update the image display with the Sobel edge detected image
    update_image(sobel_image)

#-------------------------------------------------------
# Update function for erosion operation
def update_erosion():
    # Get the selected kernel size from the slider
    kernel_size = int(scale.get())
    # Create a kernel for erosion
    kernel = np.ones((kernel_size, kernel_size), np.uint8)
    # Perform erosion on the original image
    erosion_image = cv2.erode(original_image, kernel, iterations=1)
    # Update the image display with the eroded image
    update_image(erosion_image)

#----------------------------------------------------------
# Update function for dilation operation
def update_dilation():
    # Get the selected kernel size from the slider
    kernel_size = int(scale.get())
    # Create a kernel for dilation
    kernel = np.ones((kernel_size, kernel_size), np.uint8)
    # Perform dilation on the original image
    dilation_image = cv2.dilate(original_image, kernel, iterations=1)
    # Update the image display with the dilated image
    update_image(dilation_image)




#----------------------------------------------
window= Tk()
window.geometry("900x900") #change size of the window
window.config(background="#352F44")

#--------------------------------
photo = PhotoImage(file="lenna.png")
lable = Label(window,image=photo)
lable.pack()
#-------------------------
scale = Scale(window,from_=0,to=20,orient=HORIZONTAL,length=500,bg="#B9B4C7",font=("cosle",15))
scale.pack(pady=6)
#--------------------------

add_buttons()

window.mainloop()