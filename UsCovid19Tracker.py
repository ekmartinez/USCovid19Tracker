
import os, sys
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
from PyQt5 import QtCore, QtGui, QtWidgets
from textwrap import fill

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1173, 618)
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(12)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.nameLabel = QtWidgets.QLabel(self.centralwidget)
        self.nameLabel.setGeometry(QtCore.QRect(10, 10, 201, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.nameLabel.setFont(font)
        self.nameLabel.setObjectName("nameLabel")
        self.tableTextEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.tableTextEdit.setGeometry(QtCore.QRect(10, 140, 511, 411))
        self.tableTextEdit.setObjectName("tableTextEdit")
        self.selectStateGroupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.selectStateGroupBox.setGeometry(QtCore.QRect(140, 60, 120, 71))
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.selectStateGroupBox.setFont(font)
        self.selectStateGroupBox.setObjectName("selectStateGroupBox")
        self.stateComboBox = QtWidgets.QComboBox(self.selectStateGroupBox)
        self.stateComboBox.setGeometry(QtCore.QRect(10, 30, 101, 31))
        self.stateComboBox.setObjectName("stateComboBox")
        self.selectDataGroupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.selectDataGroupBox.setGeometry(QtCore.QRect(270, 60, 120, 71))
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.selectDataGroupBox.setFont(font)
        self.selectDataGroupBox.setObjectName("selectDataGroupBox")
        self.selectDataComboBox = QtWidgets.QComboBox(self.selectDataGroupBox)
        self.selectDataComboBox.setGeometry(QtCore.QRect(10, 30, 101, 31))
        self.selectDataComboBox.setObjectName("selectDataComboBox")
        self.dataList = ['', 'Daily Cases', 'Daily Deaths', 'Total Cases', 'Total Deaths']
        self.selectDataComboBox.addItems(self.dataList) 
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, 40, 1151, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.getDataGroupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.getDataGroupBox.setGeometry(QtCore.QRect(10, 60, 120, 71))
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.getDataGroupBox.setFont(font)
        self.getDataGroupBox.setObjectName("getDataGroupBox")
        self.getDataButton = QtWidgets.QPushButton(self.getDataGroupBox)
        self.getDataButton.setGeometry(QtCore.QRect(10, 30, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.getDataButton.setFont(font)
        self.getDataButton.setObjectName("getDataButton")
        self.getDataButton.clicked.connect(self.getData)
        self.analyzeDataGroupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.analyzeDataGroupBox.setGeometry(QtCore.QRect(400, 60, 120, 71))
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.analyzeDataGroupBox.setFont(font)
        self.analyzeDataGroupBox.setObjectName("analyzeDataGroupBox")
        self.analyzeDataButton = QtWidgets.QPushButton(self.analyzeDataGroupBox)
        self.analyzeDataButton.setGeometry(QtCore.QRect(10, 30, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.analyzeDataButton.setFont(font)
        self.analyzeDataButton.setObjectName("analyzeDataButton")
        self.analyzeDataButton.clicked.connect(self.displayData)
        self.rightChartGroupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.rightChartGroupBox.setGeometry(QtCore.QRect(540, 70, 621, 481))
        self.rightChartGroupBox.setTitle("")
        self.rightChartGroupBox.setObjectName("rightChartGroupBox")
        self.rightChartLabel = QtWidgets.QLabel(self.rightChartGroupBox)
        self.rightChartLabel.setGeometry(QtCore.QRect(10, 10, 601, 461))
        self.rightChartLabel.setText("")
        self.rightChartLabel.setObjectName("rightChartLabel")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1173, 26))
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(12)
        self.menubar.setFont(font)
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(12)
        self.menuFile.setFont(font)
        self.menuFile.setObjectName("menuFile")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionReadMe = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        self.actionReadMe.setFont(font)
        self.actionReadMe.setObjectName("actionReadMe")
        self.menuFile.addAction(self.actionExit)
        self.menuAbout.addAction(self.actionReadMe)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())
        self.actionExit.triggered.connect(self.close)
        self.actionReadMe.triggered.connect(self.readMe)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.dFrame = pd.DataFrame()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "U.S Covid-19 Tracker"))
        self.nameLabel.setText(_translate("MainWindow", "U.S Covid-19 Tracker"))
        self.selectStateGroupBox.setTitle(_translate("MainWindow", "2 - Select State"))
        self.selectDataGroupBox.setTitle(_translate("MainWindow", "3 - Select Data"))
        self.getDataGroupBox.setTitle(_translate("MainWindow", "1 - Get Data"))
        self.getDataButton.setText(_translate("MainWindow", "Load"))
        self.analyzeDataGroupBox.setTitle(_translate("MainWindow", "4 - Analyze Data"))
        self.analyzeDataButton.setText(_translate("MainWindow", "Run "))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuAbout.setTitle(_translate("MainWindow", "About"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionReadMe.setText(_translate("MainWindow", "Read me"))

    def getData(self):
        try:
            fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, "US COVID TRACKER", "","CSV Files (*.csv);;All Files (*)")
            df = pd.read_csv(fileName)
            self.stateList = set(df['state'])
            self.stateList.add('')
            self.stateComboBox.addItems(sorted(self.stateList))
            self.dFrame = df
            self.statusbar.showMessage(fileName)

        except FileNotFoundError:
            pass

    def displayData(self):
        state = self.stateComboBox.currentText()
        data = self.selectDataComboBox.currentText()

        if state == "" or data =="":
            msg = 'Error: Please choose a state and the type of data to begin the analysis'
            self.warningMsg(msg)

        self.analyzeData(state, data)

    def analyzeData(self, state, data):
            pd.set_option('display.max_rows', None)
            
            dFrame = self.dFrame
            dFrame.rename(columns = {'submission_date':'Date', 'state':'State', 
                            'tot_cases':'Total Cases', 'new_case':'Cases',
                            'new_death':'Deaths', 'tot_death':'Total Deaths'}, inplace=True)

            dFrame['Date'] = pd.to_datetime(dFrame['Date'])
            dFrame = dFrame.set_index('Date')
     
            if data == 'Daily Cases':
                tempTable = dFrame.loc[(dFrame['State'] == state) & (dFrame['Cases'] > 0)]
                tempTable = tempTable[['State', 'Cases']]
                self.tableTextEdit.setHtml(tempTable.to_html())
                self.mainPlotter(tempTable['Cases'], tempTable.index)
            elif data == 'Daily Deaths':
                tempTable = dFrame.loc[(dFrame['State'] == state) & (dFrame['Deaths'] > 0)]
                tempTable = tempTable[['State', 'Deaths']]
                self.tableTextEdit.setHtml(tempTable.to_html())
                self.mainPlotter(tempTable['Deaths'], tempTable.index)
            elif data == 'Total Cases':
                tempTable = dFrame.loc[(dFrame['State'] == state) & (dFrame['Total Cases'] > 0)]
                tempTable = tempTable[['State', 'Total Cases']]
                self.tableTextEdit.setHtml(tempTable.to_html())
                self.mainPlotter(tempTable['Total Cases'], tempTable.index)
            elif data == 'Total Deaths':
                tempTable = dFrame.loc[(dFrame['State'] == state) & (dFrame['Total Deaths'] > 0)]
                tempTable = tempTable[['State', 'Total Deaths']]
                self.tableTextEdit.setHtml(tempTable.to_html())
                self.mainPlotter(tempTable['Total Deaths'], tempTable.index)

    def mainPlotter(self, x, y):
        path = f'{os.path.dirname(__file__)}/mainChart.png'
        fig, ax = plt.subplots(figsize=(6.5, 5.3))
        ax.bar(y, x)
        #TODO:SET MAX DATE TICKS
        ax.xaxis.set_major_locator(mpl.dates.MonthLocator())
        ax.xaxis.set_major_formatter(mpl.dates.DateFormatter('%m-%y'))
        plt.savefig(path)      
        imgChart = QtGui.QPixmap(path)
    
        self.rightChartLabel.setPixmap(imgChart)
        

    def warningMsg(self, msg):
        msgBox = QtWidgets.QMessageBox.warning(None, 'WARNING', msg, QtWidgets.QMessageBox.Ok)
    
    def close(self):
        sys.exit()

    def readMe(self):
        msg = fill('This application will let you track, analyze and visualize Covid-19 data in your state.  \
            To use it just download the historical data CSV file available at https://data.cdc.go, then follow \
                the steps described to view the desired information.',52)
                
        msgBox = QtWidgets.QMessageBox.information(None, 'Read Me', msg, QtWidgets.QMessageBox.Ok)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
