from scapy.all import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QInputDialog, QLineEdit, QFileDialog,QMessageBox
import json



class Ui_SettingWindow(object):
    def __init__(self):
        super().__init__()
        self.config_file = "config.json"
        

    def setupUi(self, SettingWindow):
        SettingWindow.setObjectName("SettingWindow")
        SettingWindow.resize(442, 593)
        self.centralwidget = QtWidgets.QWidget(SettingWindow)
        font = QtGui.QFont()
        font.setFamily("Sitka Text")
        font.setPointSize(12)
        self.centralwidget.setFont(font)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 0, 441, 571))
        font = QtGui.QFont()
        font.setFamily("Sitka Text")
        font.setPointSize(10)
        self.frame.setFont(font)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.destip_label = QtWidgets.QLabel(self.frame)
        self.destip_label.setGeometry(QtCore.QRect(70, 110, 101, 31))
        self.destip_label.setObjectName("destip_label")
        self.srcip_label = QtWidgets.QLabel(self.frame)
        self.srcip_label.setGeometry(QtCore.QRect(70, 70, 71, 31))
        self.srcip_label.setObjectName("srcip_label")
        self.srcport_label = QtWidgets.QLabel(self.frame)
        self.srcport_label.setGeometry(QtCore.QRect(70, 150, 101, 31))
        self.srcport_label.setObjectName("srcport_label")
        self.dstport_label = QtWidgets.QLabel(self.frame)
        self.dstport_label.setGeometry(QtCore.QRect(70, 190, 111, 31))
        self.dstport_label.setObjectName("dstport_label")
        self.title1_label = QtWidgets.QLabel(self.frame)
        self.title1_label.setGeometry(QtCore.QRect(110, 30, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.title1_label.setFont(font)
        self.title1_label.setAlignment(QtCore.Qt.AlignCenter)
        self.title1_label.setObjectName("title1_label")
        self.title2_label = QtWidgets.QLabel(self.frame)
        self.title2_label.setGeometry(QtCore.QRect(110, 240, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.title2_label.setFont(font)
        self.title2_label.setAlignment(QtCore.Qt.AlignCenter)
        self.title2_label.setObjectName("title2_label")
        self.protocol_comboBox = QtWidgets.QComboBox(self.frame)
        self.protocol_comboBox.setGeometry(QtCore.QRect(70, 440, 91, 31))
        self.protocol_comboBox.setObjectName("protocol_comboBox")
        self.protocol_comboBox.addItem("")
        self.protocol_comboBox.addItem("")
        self.save_button = QtWidgets.QPushButton(self.frame)
        self.save_button.setGeometry(QtCore.QRect(160, 490, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.save_button.setFont(font)
        self.save_button.setObjectName("save_button")
        self.srcip_edit = QtWidgets.QTextEdit(self.frame)
        self.srcip_edit.setGeometry(QtCore.QRect(190, 70, 181, 31))
        self.srcip_edit.setObjectName("srcip_edit")
        self.dstip_edit = QtWidgets.QTextEdit(self.frame)
        self.dstip_edit.setGeometry(QtCore.QRect(190, 110, 181, 31))
        self.dstip_edit.setObjectName("dstip_edit")
        self.srcport_edit = QtWidgets.QTextEdit(self.frame)
        self.srcport_edit.setGeometry(QtCore.QRect(190, 150, 181, 31))
        self.srcport_edit.setObjectName("srcport_edit")
        self.dstport_edit = QtWidgets.QTextEdit(self.frame)
        self.dstport_edit.setGeometry(QtCore.QRect(190, 190, 181, 31))
        self.dstport_edit.setObjectName("dstport_edit")
        self.conv_srcport_edit = QtWidgets.QTextEdit(self.frame)
        self.conv_srcport_edit.setGeometry(QtCore.QRect(190, 360, 181, 31))
        self.conv_srcport_edit.setObjectName("conv_srcport_edit")
        self.conv_dstport_label = QtWidgets.QLabel(self.frame)
        self.conv_dstport_label.setGeometry(QtCore.QRect(70, 400, 111, 31))
        self.conv_dstport_label.setObjectName("conv_dstport_label")
        self.conv_destip_label = QtWidgets.QLabel(self.frame)
        self.conv_destip_label.setGeometry(QtCore.QRect(70, 320, 101, 31))
        self.conv_destip_label.setObjectName("conv_destip_label")
        self.conv_srcport_label = QtWidgets.QLabel(self.frame)
        self.conv_srcport_label.setGeometry(QtCore.QRect(70, 360, 101, 31))
        self.conv_srcport_label.setObjectName("conv_srcport_label")
        self.conv_srcip_edit = QtWidgets.QTextEdit(self.frame)
        self.conv_srcip_edit.setGeometry(QtCore.QRect(190, 280, 181, 31))
        self.conv_srcip_edit.setObjectName("conv_srcip_edit")
        self.conv_dstip_edit = QtWidgets.QTextEdit(self.frame)
        self.conv_dstip_edit.setGeometry(QtCore.QRect(190, 320, 181, 31))
        self.conv_dstip_edit.setObjectName("conv_dstip_edit")
        self.conv_srcip_label = QtWidgets.QLabel(self.frame)
        self.conv_srcip_label.setGeometry(QtCore.QRect(70, 280, 71, 31))
        self.conv_srcip_label.setObjectName("conv_srcip_label")
        self.conv_dstport_edit = QtWidgets.QTextEdit(self.frame)
        self.conv_dstport_edit.setGeometry(QtCore.QRect(190, 400, 181, 31))
        self.conv_dstport_edit.setObjectName("conv_dstport_edit")
        SettingWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(SettingWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 442, 21))
        self.menubar.setObjectName("menubar")
        self.menuLoad_config_file = QtWidgets.QMenu(self.menubar)
        self.menuLoad_config_file.setObjectName("menuLoad_config_file")
        SettingWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(SettingWindow)
        self.statusbar.setObjectName("statusbar")
        SettingWindow.setStatusBar(self.statusbar)
        self.actionLoad_config_file = QtWidgets.QAction(SettingWindow)
        self.actionLoad_config_file.setWhatsThis("")
        self.actionLoad_config_file.setObjectName("actionLoad_config_file")
        self.menuLoad_config_file.addAction(self.actionLoad_config_file)
        self.menubar.addAction(self.menuLoad_config_file.menuAction())

        self.retranslateUi(SettingWindow)
        QtCore.QMetaObject.connectSlotsByName(SettingWindow)
        self.parserJson()

        #Clicked Function
        self.actionLoad_config_file.triggered.connect(self.searchJson)
        self.save_button.clicked.connect(self.saveJson)


    def searchJson(self):
        qfd = QFileDialog()
        path = ""
        filter = "Json(*.json)"
        f = QFileDialog.getOpenFileName(qfd, "File Explorer", path, filter)
        
        self.config_file = f[0]
        self.parserJson()
        print(f)

    def retranslateUi(self, SettingWindow):
        _translate = QtCore.QCoreApplication.translate
        SettingWindow.setWindowTitle(_translate("SettingWindow", "Setting"))
        self.destip_label.setText(_translate("SettingWindow", "Destination ip:"))
        self.srcip_label.setText(_translate("SettingWindow", "Source ip:"))
        self.srcport_label.setText(_translate("SettingWindow", "Source port:"))
        self.dstport_label.setText(_translate("SettingWindow", "Destination port:"))
        self.title1_label.setText(_translate("SettingWindow", "Sending settings"))
        self.title2_label.setText(_translate("SettingWindow", "Conversation settings"))
        self.protocol_comboBox.setItemText(0, _translate("SettingWindow", "UDP"))
        self.protocol_comboBox.setItemText(1, _translate("SettingWindow", "TCP"))
        self.save_button.setText(_translate("SettingWindow", "Save!"))
        self.conv_dstport_label.setText(_translate("SettingWindow", "Destination port:"))
        self.conv_destip_label.setText(_translate("SettingWindow", "Destination ip:"))
        self.conv_srcport_label.setText(_translate("SettingWindow", "Source port:"))
        self.conv_srcip_label.setText(_translate("SettingWindow", "Source ip:"))
        self.menuLoad_config_file.setTitle(_translate("SettingWindow", "Menu"))
        self.actionLoad_config_file.setText(_translate("SettingWindow", "Load config file"))
        self.actionLoad_config_file.setStatusTip(_translate("SettingWindow", "Load a json file that include all the details"))
        self.actionLoad_config_file.setShortcut(_translate("SettingWindow", "Ctrl+O"))

    def parserJson(self):
        try:
            with open(self.config_file) as jFile:
                self.srcip_edit.setText(IP().src)
                self.config_dict = json.load(jFile)
                self.dstip_edit.setText(self.config_dict["dstip"])
                self.srcport_edit.setText(self.config_dict["srcport"])
                self.dstport_edit.setText(self.config_dict["dstport"])


                self.conv_srcip_edit.setText(self.config_dict["conv_srcip"])
                self.conv_dstip_edit.setText(self.config_dict["conv_dstip"])
                self.conv_srcport_edit.setText(self.config_dict["conv_srcport"])
                self.conv_dstport_edit.setText(self.config_dict["conv_dstport"])
                if self.config_dict["protocol"].lower() == "udp":
                    idx = self.protocol_comboBox.findText("UDP") 
                    self.protocol_comboBox.setCurrentIndex(idx)
                    print(idx)
                else:
                    idx = self.protocol_comboBox.findText("TCP") 
                    self.protocol_comboBox.setCurrentIndex(idx)
                print(self.config_dict["dstip"])
        except:
            self.msg = QMessageBox()
            self.msg.setIcon(QMessageBox.Critical)
            self.msg.setText("The config(json) file not exist")
            self.msg.setInformativeText('Please enter valid config file path')
            self.msg.setWindowTitle("Error")
            self.msg.exec_()
            #need open messageBox
            print("error")        
 
    def saveJson(self):
        self.config_dict["dstip"] = self.dstip_edit.toPlainText()
        self.config_dict["srcport"] = self.srcport_edit.toPlainText()
        self.config_dict["dstport"] = self.dstport_edit.toPlainText()

        self.config_dict["conv_srcip"] = self.conv_srcip_edit.toPlainText()
        self.config_dict["conv_dstip"] = self.conv_dstip_edit.toPlainText()
        self.config_dict["conv_srcport"] = self.conv_srcport_edit.toPlainText()
        self.config_dict["conv_dstport"] = self.conv_dstport_edit.toPlainText()
        self.config_dict["protocol"] = self.protocol_comboBox.currentText()

        with open(self.config_file, 'w') as f:
            json.dump(self.config_dict, f)

        print("Saved!")



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SettingWindow = QtWidgets.QMainWindow()
    ui = Ui_SettingWindow()
    ui.setupUi(SettingWindow)
    SettingWindow.show()
    sys.exit(app.exec_())
