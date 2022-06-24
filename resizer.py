from hashlib import new
import os
from tkinter import *
import tkinter as tk
from tkinter import filedialog, messagebox
import cv2

image = ""


def browseimg():
    global img
    fln = filedialog.askopenfilename(
        initialdir=os.getcwd(),
        title="Browse Image File",
        filetypes=(
            ("JPG Image", "*.jpg"),
            ("PNG Image", "*.png"),
            ("All Files", "*.*"),
        ),
    )
    sourceName.set(fln)
    img = cv2.imread(fln, cv2.IMREAD_UNCHANGED)
    h.set(img.shape[0])
    w.set(img.shape[1])


def previewimg():
    cv2.imshow("Source image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def recalculate():
    p = int(perc.get())
    newWidth = int(int(w.get()) * p / 100)
    newHeight = int(int(h.get()) * p / 100)
    w.set(newWidth)
    h.set(newHeight)


def previewResizedImg():
    nw = int(w.get())
    nh = int(h.get())
    newImg = cv2.resize(img, (nw, nh), interpolation=cv2.INTER_AREA)
    cv2.imshow("Preview Resized Image", newImg)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def saveResizedImg():
    fln = filedialog.asksaveasfilename(
        initialdir=os.getcwd(),
        title="Save Image",
        filetypes=(
            ("JPG Image", "*.jpg"),
            ("PNG Image", "*.png"),
            ("All Files", "*.*"),
        ),
    )
    nw = int(w.get())
    nh = int(h.get())
    newImg = cv2.resize(img, (nw, nh), interpolation=cv2.INTER_AREA)
    cv2.imwrite(os.path.basename(fln), newImg)
    messagebox.showinfo(
        "Image Saved",
        "Image has been saved to " + os.path.basename(fln) + " successfully",
    )


root = Tk()

sourceName = StringVar()
w = StringVar()
h = StringVar()
perc = StringVar()


# Source File
sourceWrapper = LabelFrame(root, text="Source File")
sourceWrapper.pack(fill="both", expand="yes", padx=20, pady=20)

sourceLabel = Label(sourceWrapper, text="Source File")
sourceLabel.pack(side=tk.LEFT, padx=10, pady=10)

sourceEntry = Entry(sourceWrapper, textvariable=sourceName)
sourceEntry.pack(side=tk.LEFT, padx=10, pady=10)

sourceBtn = Button(sourceWrapper, text="Browse", command=browseimg)
sourceBtn.pack(side=tk.LEFT, padx=10, pady=10)

previewSrcBtn = Button(sourceWrapper, text="Preview", command=previewimg)
previewSrcBtn.pack(side=tk.LEFT, padx=10, pady=10)

# Image Details
imageWrapper = LabelFrame(root, text="Image Details")
imageWrapper.pack(fill="both", expand="yes", padx=20, pady=20)

dimensionLabel = Label(imageWrapper, text="Dimension")
dimensionLabel.pack(side=tk.LEFT, padx=10, pady=10)

dimensionEntry = Entry(imageWrapper, textvariable=w)
dimensionEntry.pack(side=tk.LEFT, padx=10, pady=10)

xLabel = Label(imageWrapper, text="X")
xLabel.pack(side=tk.LEFT, padx=5, pady=10)

xEntry = Entry(imageWrapper, textvariable=h)
xEntry.pack(side=tk.LEFT, padx=5, pady=10)

# Pixel Safe
pixelWrapper = LabelFrame(root, text="Scale")
pixelWrapper.pack(fill="both", expand="yes", padx=20, pady=20)

pixelLabel = Label(pixelWrapper, text="Percentage")
pixelLabel.pack(side=tk.LEFT, padx=10, pady=10)

pixelEntry = Entry(pixelWrapper, textvariable=perc)
pixelEntry.pack(side=tk.LEFT, padx=10, pady=10)

pixelBtn = Button(pixelWrapper, text="Recalculate Dimension", command=recalculate)
pixelBtn.pack(side=tk.LEFT, padx=10, pady=10)

# Actions
actionWrapper = LabelFrame(root, text="Actions")
actionWrapper.pack(fill="both", expand="yes", padx=20, pady=20)

previewNewBtn = Button(actionWrapper, text="Preview", command=previewResizedImg)
previewNewBtn.pack(side=tk.LEFT, padx=10, pady=10)

saveBtn = Button(actionWrapper, text="Save", command=saveResizedImg)
saveBtn.pack(side=tk.LEFT, padx=10, pady=10)


root.title("Image resizer")
root.geometry("800x600")
root.mainloop()
