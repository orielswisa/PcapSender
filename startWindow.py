from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from settingWin import *
from forwardPcapClass import *
from scapy.all import *
      


class Ui_MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(Ui_MainWindow,self).__init__()
        self.setupUi(self)
        self.seconedWindow = QtWidgets.QMainWindow()
        self.ui2 = Ui_SettingWindow()
        self.ui2.setupUi(self.seconedWindow)
        self.full_path = None
     


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(373, 456)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Sitka Text")
        self.centralwidget.setFont(font)
        self.centralwidget.setObjectName("centralwidget")
        self.startButton = QtWidgets.QPushButton(self.centralwidget)
        self.startButton.setGeometry(QtCore.QRect(90, 160, 201, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.startButton.setFont(font)
        self.startButton.setObjectName("startButton")
        self.choose_label = QtWidgets.QLabel(self.centralwidget)
        self.choose_label.setGeometry(QtCore.QRect(120, 80, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Sitka Text")
        font.setPointSize(14)
        self.choose_label.setFont(font)
        self.choose_label.setObjectName("choose_label")
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(60, 0, 241, 91))
        font = QtGui.QFont()
        font.setFamily("Sitka Text")
        font.setPointSize(22)
        font.setBold(False)
        font.setWeight(50)
        self.title.setFont(font)
        self.title.setScaledContents(True)
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName("title")
        self.time_lable = QtWidgets.QLabel(self.centralwidget)
        self.time_lable.setGeometry(QtCore.QRect(70, 250, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setFamily("Arial")
        self.time_lable.setFont(font)
        self.time_lable.setAlignment(QtCore.Qt.AlignCenter)
        self.time_lable.setObjectName("time_lable")
        self.packet_label = QtWidgets.QLabel(self.centralwidget)
        self.packet_label.setGeometry(QtCore.QRect(20, 310, 341, 41))
        font = QtGui.QFont()
        font.setFamily("Sitka Text")
        font.setPointSize(8)
        self.packet_label.setFont(font)
        self.packet_label.setObjectName("packet_label")
        font.setPointSize(11)
        self.path_edit = QtWidgets.QTextEdit(self.centralwidget)
        self.path_edit.setGeometry(QtCore.QRect(90, 120, 191, 32))
        self.path_edit.setFont(font)
        self.path_edit.setToolTip("")
        self.path_edit.setWhatsThis("")
        self.path_edit.setAutoFillBackground(False)
        self.path_edit.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.Israel))
        self.path_edit.setObjectName("path_edit")
        self.toolSearchButton = QtWidgets.QToolButton(self.centralwidget)
        self.toolSearchButton.setGeometry(QtCore.QRect(290, 120, 31, 31))
        self.toolSearchButton.setObjectName("toolSearchButton")
        self.packetsnum_label = QtWidgets.QLabel(self.centralwidget)
        self.packetsnum_label.setGeometry(QtCore.QRect(230, 250, 71, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.packetsnum_label.setFont(font)
        self.packetsnum_label.setObjectName("packetsnum_label")
        self.timer_label = QtWidgets.QLabel(self.centralwidget)
        self.timer_label.setGeometry(QtCore.QRect(20, 250, 71, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.timer_label.setFont(font)
        self.timer_label.setObjectName("timer_label")
        self.packetNumber_lable = QtWidgets.QLabel(self.centralwidget)
        self.packetNumber_lable.setGeometry(QtCore.QRect(300, 250, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setFamily("Arial")
        self.packetNumber_lable.setFont(font)
        self.packetNumber_lable.setAlignment(QtCore.Qt.AlignCenter)
        self.packetNumber_lable.setObjectName("packetNumber_lable")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 373, 21))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSettings = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Sitka Text")
        self.actionSettings.setFont(font)
        self.actionSettings.setObjectName("actionSettings")
        self.menuMenu.addAction(self.actionSettings)
        self.menubar.addAction(self.menuMenu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #Clicked functions
        self.toolSearchButton.clicked.connect(self.openFileExplorer)
        self.actionSettings.triggered.connect(self.openSetting)
        self.startButton.clicked.connect(self.startSending)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Pcap sending"))
        self.startButton.setText(_translate("MainWindow", "Start sending"))
        self.choose_label.setText(_translate("MainWindow", "Choose File:"))
        self.title.setText(_translate("MainWindow", "Pcap sender"))
        self.time_lable.setText(_translate("MainWindow", "00"))
        self.packet_label.setText(_translate("MainWindow", "Wait to send..."))
        self.toolSearchButton.setText(_translate("MainWindow", "..."))
        self.packetsnum_label.setText(_translate("MainWindow", "Packets:"))
        self.timer_label.setText(_translate("MainWindow", "Timer:"))
        self.packetNumber_lable.setText(_translate("MainWindow", "00"))
        self.menuMenu.setTitle(_translate("MainWindow", "Menu"))
        self.actionSettings.setText(_translate("MainWindow", "Settings"))
        self.actionSettings.setShortcut(_translate("MainWindow", "Ctrl+S"))

    def openFileExplorer(self):
        qfd = QFileDialog()
        path = ""
        filter = "pcap(*.pcap)"
        f = QFileDialog.getOpenFileName(qfd, "File Explorer", path, filter)
        self.full_path = f[0]
        filename = f[0].split("/")[-1]
        self.path_edit.setText(filename)
        print(f)

    def startSending(self):
        try:
            if self.full_path is None:
                self.pcapFile = open(self.path_edit.toPlainText())
            elif self.path_edit.toPlainText() in self.full_path:
                self.pcapFile = open(self.full_path)
            else:
                self.pcapFile = open(self.path_edit.toPlainText())    
        except:
            self.msg = QMessageBox()
            self.msg.setIcon(QMessageBox.Critical)
            self.msg.setText("The pcacp file not exist")
            self.msg.setInformativeText('Please enter valid file path')
            self.msg.setWindowTitle("Error")
            self.msg.exec_()
            return
        try:
            with open(self.ui2.config_file) as jFile:
                self.config_dict = json.load(jFile)
            print(self.config_dict["dstip"])
        except:
            self.msg = QMessageBox()
            self.msg.setIcon(QMessageBox.Critical)
            self.msg.setText("The config(json) file not exist")
            self.msg.setInformativeText('Please enter valid config file path')
            self.msg.setWindowTitle("Error")
            self.msg.exec_()
            return

        try:
            connect_msg = IP(dst = self.config_dict["dstip"])/UDP(sport= int(self.config_dict["srcport"]),dport = int(self.config_dict["dstport"]))/Raw("Connect")
            send(connect_msg)
            self.config_dict["filename"] = self.path_edit.toPlainText()
            self.config_dict["srcip"] = IP().src
            self.senderClass = Sender(self.config_dict,self)
            self.senderClass.sendPcap()

        except:
            print("ERROR with sender class!")
        




    def openSetting(self):
        self.seconedWindow.show()
        self.ui2.save_button.clicked.connect(self.changeT)

    def changeT(self):
        self.seconedWindow.hide()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = Ui_MainWindow()
    window.show() 
    # MainWindow = QtWidgets.QMainWindow()
    # ui = Ui_MainWindow()
    # ui.setupUi(MainWindow)
    # MainWindow.show()
    sys.exit(app.exec_())
