from PyQt5 import QtCore , QtWidgets , QtGui
from PyQt5.QtGui import QMovie
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtCore import Qt , QTimer , QTime , QDate
from MonaLisaui import Ui_MainWindow
import sys
import Main

class MainThread(QThread):

    def __init__(self): 

        super(MainThread,self).__init__()

    def run(self):
        self.Task_Gui()

    def Task_Gui(self):
        Main.TaskExe()

startFunctions = MainThread() 

class Gui_Start(QMainWindow):

    def __init__(self):

        super().__init__()

        self.monalisa_ui = Ui_MainWindow()
        
        self.monalisa_ui.setupUi(self)

        self.monalisa_ui.start_button.clicked.connect(self.startFunc)

        self.monalisa_ui.close_button.clicked.connect(self.close)

    def startFunc(self):

        self.monalisa_ui.movies = QtGui.QMovie(".\\../../../Downloads/matrix.gif")

        self.monalisa_ui.gif_bg.setMovie(self.monalisa_ui.movies)

        self.monalisa_ui.movies.start()




        timer = QTimer(self)

        timer.timeout.connect(self.showtime)

        timer.start(1000)

        startFunctions.start()

    def showtime(self):
        
        current_time = QTime.currentTime()

        label_time = current_time.toString("hh:mm:ss")

        labbel = " Time :  " + label_time 

        self.monalisa_ui.time.setText(labbel)

Gui_App = QApplication(sys.argv)

Gui_MonaLisa = Gui_Start()

Gui_MonaLisa.show()

exit(Gui_App.exec_())
