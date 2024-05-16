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
    add_button(text="OPEN",command=update_open)
    add_button(text="Close",command=update_close)
    add_button(text="apply hough circle transform",command=apply_hough_circle_transform)


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
#---------------------------------------------------
# Update function for closing operation
def update_close():
    # Get the selected kernel size from the slider
    kernel_size = int(scale.get())
    # Create a kernel for closing
    kernel = np.ones((kernel_size, kernel_size), np.uint8)
    # Perform closing on the original image
    close_image = cv2.morphologyEx(original_image, cv2.MORPH_CLOSE, kernel)
    # Update the image display with the closed image
    update_image(close_image)
#----------------------------------------------------------
# Apply Hough circle transform to detect circles in the image
def apply_hough_circle_transform():
    # Convert the original image to grayscale
    gray_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
    # Detect circles using Hough circle transform with specified parameters
    circles = cv2.HoughCircles(gray_image, cv2.HOUGH_GRADIENT, dp=1, minDist=20, param1=50, param2=30, minRadius=0, maxRadius=0)
    # Check if any circles are detected
    if circles is not None:
        # Convert the circle parameters to integer
        circles = np.uint16(np.around(circles))
        # Create a copy of the original image for drawing circles
        hough_image = original_image.copy()
        # Draw detected circles on the image
        for i in circles[0, :]:
            cv2.circle(hough_image, (i[0], i[1]), i[2], (0, 255, 0), 2)  # Draw the outer circle
            cv2.circle(hough_image, (i[0], i[1]), 2, (0, 0, 255), 3)       # Draw the center of the circle
        # Update the image display with the circles drawn
        update_image(hough_image)

#---------------------------------------------------------
# Update function for opening operation
def update_open():
    # Get the selected kernel size from the slider
    kernel_size = int(scale.get())
    # Create a kernel for opening
    kernel = np.ones((kernel_size, kernel_size), np.uint8)
    # Perform opening on the original image
    open_image = cv2.morphologyEx(original_image, cv2.MORPH_OPEN, kernel)
    # Update the image display with the opened image
    update_image(open_image)


#----------------------------------------------
window= Tk()
window.geometry("900x900") #change size of the window
window.config(background="#352F44")

#--------------------------------
photo = PhotoImage(file="lenna.png")
lable = Label(window,image=photo)
lable.pack()
#-------------------------
scale = Scale(window,from_=0,to=20,orient=HORIZONTAL,length=500,bg="#B9B4C7",font=("cosle",20))
scale.pack(pady=6)
#--------------------------

add_buttons()

window.mainloop()