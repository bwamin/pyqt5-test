#imports
from turtle import window_height, window_width
import stored
import os
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QDesktopWidget
from PyQt5.QtCore import QTimer
import sys
import time

#stored.open_program("D:\pytesthub\pyqt5\callbackfiles\OPENME.txt") #should open the text folder

class MyWindow(QWidget):

    def __init__(self):
        super().__init__()
        #i want to define center of screens
        screen_size = QDesktopWidget().screenGeometry()

        screen_width = screen_size.width()
        screen_height = screen_size.height()
        center_x = screen_width // 2
        center_y = screen_height // 2

        window_height = 400
        window_width = 600

        self.setWindowTitle("PYQT5 TEST")  # Set window title
        self.setGeometry(center_x - window_width // 2, center_y - window_height // 2, window_width, window_height) #dimensions should make window open in middle

        #home button creation
        home_button = QPushButton("home", self) #home_button set to equal a qpush button
        home_button.clicked.connect(self.home_function) #connect homebutton to the home function


        self.button = QPushButton("Click Me")
        self.button.clicked.connect(self.on_button_click)  # Connect button click to function

        #home button layout
        layout = QVBoxLayout()
        layout.addWidget(home_button) #adding the widget for home
        # layout for rando buttom
        layout.addWidget(self.button)

        self.setLayout(layout)  # window layout


        #button debounce
        self.debounce_timer = QTimer(self)
        self.debounce_timer.setSingleShot(True)  #will only fire ONCE. so ur not stuck in infinite debounce
        self.debounce_timer.timeout.connect(self.button_offdebounce) #timeout the connection between button and function
        #flag to check if button can be clicked
        self.is_clickable = True

    
    #home buttom function
    def home_function(self):
        if not self.is_clickable:
            print("home IGNORED bcs of debounce") #basicaly if button is on debounce, print this so u know dats y..
            return
        self.is_clickable = False

        self.debounce_timer.start(5000)
        print("im goin home")
        stored.open_program("D:\pytesthub\pyqt5\callbackfiles\OPENME.txt") #should open the text folder


    def button_offdebounce(self):
        self.is_clickable = True #reactivates button after debounce
        print("READY TO CLICK")


    def on_button_click(self):
        print("im clicked")  #buton clicked
        

#std pyqt5 
app = QApplication(sys.argv)
window = MyWindow()
window.show() 
sys.exit(app.exec_()) 
