import tkinter as tk
from tkinter import Tk, Label, Frame, Button
from tkinter import filedialog
from tkinter import *
from math import sqrt
import cv2 as cv
from cv2 import cvtColor, imread, resize
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use("TkAgg") 
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg,NavigationToolbar2Tk
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d import Axes3D 
from tkinter.ttk import *

class main(Tk):
    def __init__(self):
        Tk.__init__(self)

        self.photo1 = PhotoImage(file="photo.png")
        self.photo1 = self.photo1.subsample(8, 8) 

        self.photo2 = PhotoImage(file="color-palette.png")
        self.photo2 = self.photo2.subsample(16, 16) 

        self.photo3 = PhotoImage(file="red.png")
        self.photo3 = self.photo3.subsample(16, 16) 

        self.photo4 = PhotoImage(file="blue.png")
        self.photo4 = self.photo4.subsample(16, 16) 

        self.photo5 = PhotoImage(file="green.png")
        self.photo5 = self.photo5.subsample(16, 16) 

        self.photo6 = PhotoImage(file="diagram.png")
        self.photo6 = self.photo6.subsample(16, 16) 

        self.photo7 = PhotoImage(file="code.png")
        self.photo7 = self.photo7.subsample(16, 16) 

        self.photo8 = PhotoImage(file="cube.png")
        self.photo8 = self.photo8.subsample(8, 8) 

        self.frame = Frame(self)

        self.frame.grid(row=0,column=0,sticky="nsew")

        self.frame.bt1 = Button(self.frame, 
                                text="Load Image",
                                image = self.photo1,
                                compound = tk.TOP, 
                                command = self.LoadImage)
        self.frame.bt1.grid(row=0,column=0, sticky="nswe", rowspan=3)

        self.frame.label_Lab = Label(self,text="")
        self.frame.label_Lab.grid(column=0,row=5,sticky="nw")

        self.frame.bt2 = Button(self.frame, 
                                text = "RGB",
                                image = self.photo2,
                                compound = tk.LEFT,
                                command = self.RGB)
        self.frame.bt2.grid(row=2,column=1, sticky="we", columnspan=2)

        self.frame.bt3 = Button(self.frame, 
                                text = "YCrCb",
                                image = self.photo2,
                                compound = tk.LEFT,
                                command = self.YCrCb)
        self.frame.bt3.grid(row=0,column=1, sticky="we")

        self.frame.bt4 = Button(self.frame, 
                                text = "HSV",
                                image = self.photo2,
                                compound = tk.LEFT,
                                command = self.HSV)
        self.frame.bt4.grid(row=0,column=2, sticky="we")

        self.frame.bt5 = Button(self.frame, 
                                text = "XYZ",
                                image = self.photo2,
                                compound = tk.LEFT,
                                command = self.XYZ)
        self.frame.bt5.grid(row=1,column=1, sticky="we")

        self.frame.bt5 = Button(self.frame, 
                                text = "Lab",
                                image = self.photo2,
                                compound = tk.LEFT,
                                command = self.Lab)
        self.frame.bt5.grid(row=1,column=2, sticky="we")

        self.frame.lb2 = Label(self.frame, text="Color Spaces")
        self.frame.lb2.grid(row=3,column=1, columnspan=2)

        self.frame.bt6 = Button(self.frame,
                                text="Channel 1",
                                image = self.photo3,
                                compound = tk.LEFT,
                                command = lambda: self.changeChannels(ch1))
        self.frame.bt6.grid(row=0,column = 3, sticky="we")

        self.frame.bt7 = Button(self.frame,
                                text="Channel 2",
                                image = self.photo4,
                                compound = tk.LEFT,
                                command = lambda: self.changeChannels(ch2))
        self.frame.bt7.grid(row=1,column = 3, sticky="we")

        self.frame.bt8 = Button(self.frame,
                                text="Channel 3",
                                image = self.photo5,
                                compound = tk.LEFT,
                                command = lambda: self.changeChannels(ch3))
        self.frame.bt8.grid(row=2,column = 3, sticky="we")

        self.frame.lb3 = Label(self.frame, text="Image Channels")
        self.frame.lb3.grid(row=3,column=3, columnspan=1)

        self.frame.bt9 = Button(self.frame,
                                text="Histogram Ch 1", 
                                image = self.photo6,
                                compound = tk.LEFT,
                                command = lambda: self.histogram(ch1))
        self.frame.bt9.grid(row=0,column = 4, sticky="we")

        self.frame.bt10 = Button(self.frame,
                                 text="Histogram Ch 2",
                                 image = self.photo6,
                                 compound = tk.LEFT,
                                 command = lambda: self.histogram(ch2))
        self.frame.bt10.grid(row=1,column = 4, sticky="we")

        self.frame.bt11 = Button(self.frame,
                                 text="Histogram Ch 3",
                                 image = self.photo6,
                                 compound = tk.LEFT,
                                 command = lambda: self.histogram(ch3))
        self.frame.bt11.grid(row=2,column = 4, sticky="we")

        self.frame.lb4 = Label(self.frame, text="Image Histograms")
        self.frame.lb4.grid(row=3,column=4, columnspan=1)

        self.frame.bt12 = Button(self.frame,
                                 text="Threshold Ch 1",
                                 image = self.photo7,
                                 compound = tk.LEFT,
                                 command = lambda: self.threshold(ch1))
        self.frame.bt12.grid(row=0,column = 5, sticky="we")

        self.frame.bt13 = Button(self.frame,
                                 text="Threshold Ch 2",
                                 image = self.photo7,
                                 compound = tk.LEFT,
                                 command = lambda: self.threshold(ch2))
        self.frame.bt13.grid(row=1,column = 5, sticky="we")

        self.frame.bt14 = Button(self.frame,
                                 text="Threshold Ch 3",
                                 image = self.photo7,
                                 compound = tk.LEFT, 
                                 command = lambda: self.threshold(ch3))
        self.frame.bt14.grid(row=2,column = 5, sticky="we")

        self.frame.lb5 = Label(self.frame, text="Image Thresholding")
        self.frame.lb5.grid(row=3,column=5, columnspan=1)

        self.frame.bt15 = Button(self.frame,
                                 text="3D graphic",
                                 image = self.photo8,
                                 compound = tk.TOP, 
                                 command = lambda: self.S3D(ch1,ch2,ch3))
        self.frame.bt15.grid(row=0,column = 6, rowspan=3, sticky="nswe")

    def LoadImage(self):
        path = filedialog.askopenfilename()
        global img
        global color
        img = imread(path)
        h,w,_ = img.shape
        h = int(h/1)
        w = int(w/1)
        img = resize(img, (w,h))
        img = cvtColor(img,cv.COLOR_BGR2RGB)
        color = img
        figure = Figure(figsize=(7,4),dpi=100)
        subplot = figure.add_subplot(111)
        subplot.imshow(img)
        self.frame.canvas = FigureCanvasTkAgg(figure,self)
        self.frame.canvas.get_tk_widget().grid(row=1, column=0)

        toolbarFrame = Frame(master=self)
        toolbarFrame.grid(row=4,column=0,sticky="nswe")
        NavigationToolbar2Tk(self.frame.canvas, toolbarFrame)
        
        self.frame.canvas.callbacks.connect('button_press_event', self.on_click)

        global ch1
        global ch2
        global ch3
        ch1 = color[:,:,0]
        ch2 = color[:,:,1]
        ch3 = color[:,:,2]

        self.frame.label_Lab.config(text="Index Hunter Lab: ")

    def on_click(self,event):
        self.x = int(event.xdata)
        self.y = int(event.ydata)
        img_lab = img[self.y:self.y+3,self.x:self.x+3,:]
        XYZ = cvtColor(img_lab,cv.COLOR_RGB2XYZ)
        sum_lab = 0
        Xn = 95.047
        Yn = 100
        Zn = 108.883
        Ka = (175/198.04)*(Yn+Xn)
        Kb = (70/218.11)*(Yn+Zn)
        for i in range(3):
            for j in range(3):
                X = int(XYZ[i,j,0])
                Y = int(XYZ[i,j,1])
                Z = int(XYZ[i,j,2])
                L = 100*sqrt(Y/Yn)
                a = Ka*((X/Xn-Y/Yn)/sqrt(Y/Yn))
                b = Kb*((Y/Yn-Z/Zn)/sqrt(Y/Yn))
                sum_lab += 100*a/(L*b)
        sum_lab = sum_lab/9
        self.frame.label_Lab.config(text="Index Hunter Lab: "+str(sum_lab))

    def changeChannels(self,ch):
        figure = Figure(figsize=(7,4),dpi=100)
        subplot1 = figure.add_subplot(111)
        subplot1.imshow(ch,'gray')
        self.frame.canvas = FigureCanvasTkAgg(figure)
        self.frame.canvas.get_tk_widget().grid(row=1, column=0)

        toolbarFrame = Frame(master=self)
        toolbarFrame.grid(row=4,column=0,sticky="nswe")
        NavigationToolbar2Tk(self.frame.canvas, toolbarFrame)

    def histogram(self,ch):
        his = cv.calcHist([ch],[0],None,[256],[0,256])
        figure = Figure(figsize=(7,4),dpi=100)
        subplot1 = figure.add_subplot(111)
        subplot1.plot(his)

        self.frame.canvas = FigureCanvasTkAgg(figure)
        self.frame.canvas.get_tk_widget().grid(row=1, column=0)      

        toolbarFrame = Frame(master=self)
        toolbarFrame.grid(row=4,column=0,sticky="nswe")
        NavigationToolbar2Tk(self.frame.canvas, toolbarFrame)

        self.frame.label_Lab.config(text="")

    def threshold(self,ch):
        _, th = cv.threshold(ch,150, 255, cv.THRESH_BINARY + 
                                cv.THRESH_OTSU)
        figure = Figure(figsize=(7,4),dpi=100)
        subplot1 = figure.add_subplot(111)
        subplot1.imshow(th, 'gray')

        self.frame.canvas = FigureCanvasTkAgg(figure)
        self.frame.canvas.get_tk_widget().grid(row=1, column=0)   

        toolbarFrame = Frame(master=self)
        toolbarFrame.grid(row=4,column=0,sticky="nswe")
        NavigationToolbar2Tk(self.frame.canvas, toolbarFrame)
        self.frame.label_Lab.config(text="")

    def S3D(self,ch1,ch2,ch3):
        figure = Figure(figsize=(7,4),dpi=100)
        subplot = figure.add_subplot(projection='3d')
        r = cv.resize(ch1, (0, 0), fx = 0.05, fy = 0.05) 
        g = cv.resize(ch2, (0, 0), fx = 0.05, fy = 0.05) 
        b = cv.resize(ch3, (0, 0), fx = 0.05, fy = 0.05)
        color = []
        for i,j,k in zip(r,g,b):
            for l,m,n in zip(i,j,k):
                color.append([l/255.,m/255.,n/255.])
        subplot.scatter(r, g, b, c=[C for C in color], marker="o",alpha=0.1)
        self.frame.canvas = FigureCanvasTkAgg(figure)
        self.frame.canvas.get_tk_widget().grid(row=1, column=0)  

        toolbarFrame = Frame(master=self)
        toolbarFrame.grid(row=4,column=0,sticky="nswe")
        NavigationToolbar2Tk(self.frame.canvas, toolbarFrame)
        self.frame.label_Lab.config(text="")

    def RGB(self):
        global img
        global color
        color = img  
        figure = Figure(figsize=(7,4),dpi=100)
        subplot = figure.add_subplot(111)
        subplot.imshow(color)
        self.frame.canvas = FigureCanvasTkAgg(figure)
        self.frame.canvas.get_tk_widget().grid(row=1, column=0)

        toolbarFrame = Frame(master=self)
        toolbarFrame.grid(row=4,column=0,sticky="nswe")
        NavigationToolbar2Tk(self.frame.canvas, toolbarFrame)
        self.frame.label_Lab.config(text="Index Hunter Lab: ")
        self.frame.canvas.callbacks.connect('button_press_event', self.on_click)

        global ch1
        global ch2
        global ch3
        ch1 = color[:,:,0]
        ch2 = color[:,:,1]
        ch3 = color[:,:,2]

    def YCrCb(self):
        global img
        global color
        color = cvtColor(img,cv.COLOR_RGB2YCrCb)   
        figure = Figure(figsize=(7,4),dpi=100)
        subplot = figure.add_subplot(111)
        subplot.imshow(color)
        self.frame.canvas = FigureCanvasTkAgg(figure)
        self.frame.canvas.get_tk_widget().grid(row=1, column=0)

        toolbarFrame = Frame(master=self)
        toolbarFrame.grid(row=4,column=0,sticky="nswe")
        NavigationToolbar2Tk(self.frame.canvas, toolbarFrame)
        self.frame.label_Lab.config(text="")

        global ch1
        global ch2
        global ch3
        ch1 = color[:,:,0]
        ch2 = color[:,:,1]
        ch3 = color[:,:,2]

    def HSV(self):
        global img
        global color
        color = cvtColor(img,cv.COLOR_RGB2HSV)   
        figure = Figure(figsize=(7,4),dpi=100)
        subplot = figure.add_subplot(111)
        subplot.imshow(color)
        self.frame.canvas = FigureCanvasTkAgg(figure)
        self.frame.canvas.get_tk_widget().grid(row=1, column=0)

        toolbarFrame = Frame(master=self)
        toolbarFrame.grid(row=4,column=0,sticky="nswe")
        NavigationToolbar2Tk(self.frame.canvas, toolbarFrame)
        self.frame.label_Lab.config(text="")

        global ch1
        global ch2
        global ch3
        ch1 = color[:,:,0]
        ch2 = color[:,:,1]
        ch3 = color[:,:,2]

    def XYZ(self):
        global img
        global color
        color = cvtColor(img,cv.COLOR_RGB2XYZ)   
        figure = Figure(figsize=(7,4),dpi=100)
        subplot = figure.add_subplot(111)
        subplot.imshow(color)
        self.frame.canvas = FigureCanvasTkAgg(figure)
        self.frame.canvas.get_tk_widget().grid(row=1, column=0)

        toolbarFrame = Frame(master=self)
        toolbarFrame.grid(row=4,column=0,sticky="nswe")
        NavigationToolbar2Tk(self.frame.canvas, toolbarFrame)
        self.frame.label_Lab.config(text="")

        global ch1
        global ch2
        global ch3
        ch1 = color[:,:,0]
        ch2 = color[:,:,1]
        ch3 = color[:,:,2]

    def Lab(self):
        global img
        global color
        color = cvtColor(img,cv.COLOR_RGB2Lab)   
        figure = Figure(figsize=(7,4),dpi=100)
        subplot = figure.add_subplot(111)
        subplot.imshow(color)
        self.frame.canvas = FigureCanvasTkAgg(figure)
        self.frame.canvas.get_tk_widget().grid(row=1, column=0)

        toolbarFrame = Frame(master=self)
        toolbarFrame.grid(row=4,column=0,sticky="nswe")
        NavigationToolbar2Tk(self.frame.canvas, toolbarFrame)
        self.frame.label_Lab.config(text="")

        global ch1
        global ch2
        global ch3
        ch1 = color[:,:,0]
        ch2 = color[:,:,1]
        ch3 = color[:,:,2]

root = main()
root.mainloop()
