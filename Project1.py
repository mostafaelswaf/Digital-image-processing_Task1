from tkinter import *
from tkinter import messagebox
import cv2
import numpy as np
from PIL import Image, ImageTk

original_image = cv2.imread("lenna.png")


# --------------------------------
def add_button(text, command):
    button = Button(window, text=text, command=command, bg="#B9B4C7", font=("consle", 11))
    button.pack(pady=6)


# ----------------
def add_buttons():
    add_button(text="original", command=load)

    add_button(text="high pass filter", command=update_hpf)

    add_button(text="Mean filter", command=update_mean_filter)

    add_button(text="median filter", command=update_median_filter)

    add_button(text="prewitt edge detector ", command=apply_prewitt_edge_detector)


# -------------------------------------
def update_image(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = Image.fromarray(img)
    img = ImageTk.PhotoImage(img)
    lable.config(image=img)
    # lablel.pack()
    lable.image = img


# --------------------------------------
def load():
    photo1 = PhotoImage(file="lenna.png")
    lable.config(image=photo1)
    lable.image = photo1


# -----------------------------------------
def update_hpf():
    # Get the selected kernel size from the slider
    kernel_size = int(scale.get())
    if (kernel_size % 2 == 0):
        messagebox.showwarning("Warning", "Kernel size should be an odd number.")
        return
    else:

        # Convert the original image to grayscale
        gray_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
        # Apply Gaussian blur to the grayscale image with the selected kernel size
        blurred_image = cv2.GaussianBlur(gray_image, (kernel_size, kernel_size), 0)
        # Subtract the blurred image from the grayscale image to obtain high-pass filtered image
        hpf_image = cv2.subtract(gray_image, blurred_image)
        # Convert the high-pass filtered image to BGR format and update the image display
        update_image(cv2.cvtColor(hpf_image, cv2.COLOR_GRAY2BGR))


# ----------------------------------
# Update function for mean filter
def update_mean_filter():
    # Get the selected kernel size from the slider
    kernel_size = int(scale.get())
    # Apply mean filter to the original image with the selected kernel size
    mean_image = cv2.blur(original_image, (kernel_size, kernel_size))
    # Update the image display with the mean filtered image
    update_image(mean_image)


# ----------------------------------
def update_median_filter():
    # Get the selected kernel size from the slider
    kernel_size = int(scale.get())
    # Ensure the kernel size is odd
    if (kernel_size % 2 == 0):
        messagebox.showwarning("Warning", "Kernel size should be an odd number.")
        return
    else:
        # Apply median filter to the original image with the selected kernel size
        median_image = cv2.medianBlur(original_image, kernel_size)
        # Update the image display with the median filtered image
        update_image(median_image)


# -------------------------------------------------
# Apply Prewitt edge detector to detect edges in the image
def apply_prewitt_edge_detector():
    # Convert the original image to grayscale
    gray_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
    # Compute the horizontal and vertical gradients using Prewitt operators
    prewitt_x = cv2.Sobel(gray_image, cv2.CV_64F, 1, 0, ksize=3)
    prewitt_y = cv2.Sobel(gray_image, cv2.CV_64F, 0, 1, ksize=3)
    # Compute the magnitude of gradients
    prewitt_image = np.sqrt(prewitt_x ** 2 + prewitt_y ** 2)
    # Normalize the gradient magnitude image
    prewitt_image = cv2.normalize(prewitt_image, None, 0, 255, cv2.NORM_MINMAX, dtype=cv2.CV_8U)
    # Update the image display with the Prewitt edge detected image
    update_image(prewitt_image)


# ----------------------------------------------
window = Tk()
window.geometry("900x900")  # change size of the window
window.config(background="#352F44")

# --------------------------------
photo = PhotoImage(file="lenna.png")
lable = Label(window, image=photo)
lable.pack()
# -------------------------
scale = Scale(window, from_=0, to=20, orient=HORIZONTAL, length=500, bg="#B9B4C7", font=("cosle", 15))
scale.pack(pady=6)
# --------------------------


add_buttons()

window.mainloop()