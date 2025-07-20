# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'homeTab.ui'
##
## Created by: Qt User Interface Compiler version 6.2.4
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QLabel,
    QLineEdit, QMainWindow, QPushButton, QScrollArea,
    QSizePolicy, QWidget)
import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1920, 1080)
        MainWindow.setStyleSheet(u"\n"
"background-color: #F1F1F1;\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label_copy_rights = QLabel(self.centralwidget)
        self.label_copy_rights.setObjectName(u"label_copy_rights")
        self.label_copy_rights.setGeometry(QRect(885, 1035, 181, 20))
        self.label_copy_rights.setStyleSheet(u"font-family: Calibri;\n"
"font-size: 16px;\n"
"font-weight: 400;\n"
"line-height: 19.53px;\n"
"color: #73746B;\n"
"")
        self.label_name = QLabel(self.centralwidget)
        self.label_name.setObjectName(u"label_name")
        self.label_name.setGeometry(QRect(790, 20, 300, 50))
        font = QFont()
        font.setPointSize(30)
        font.setBold(True)
        self.label_name.setFont(font)
        self.label_frame_count = QLabel(self.centralwidget)
        self.label_frame_count.setObjectName(u"label_frame_count")
        self.label_frame_count.setGeometry(QRect(600, 80, 131, 20))
        font1 = QFont()
        font1.setPointSize(15)
        self.label_frame_count.setFont(font1)
        self.pushButton_next = QPushButton(self.centralwidget)
        self.pushButton_next.setObjectName(u"pushButton_next")
        self.pushButton_next.setGeometry(QRect(1090, 550, 80, 80))
        font2 = QFont()
        font2.setPointSize(8)
        self.pushButton_next.setFont(font2)
        self.pushButton_next.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_next.setStyleSheet(u"QPushButton{\n"
"background-color: #2e86de;\n"
"border : None;\n"
"color: rgb(255, 255, 255);\n"
"border: 2px solid #ced4da; \n"
"border-radius: 40px; \n"
"padding: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"        background-color: #0056b3; /* Darker blue on press */\n"
"    }\n"
"")
        icon = QIcon()
        icon.addFile(u":/Home/next1.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_next.setIcon(icon)
        self.pushButton_next.setIconSize(QSize(80, 80))
        self.pushButton_previous = QPushButton(self.centralwidget)
        self.pushButton_previous.setObjectName(u"pushButton_previous")
        self.pushButton_previous.setGeometry(QRect(80, 550, 80, 80))
        self.pushButton_previous.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_previous.setStyleSheet(u"QPushButton{\n"
"background-color: #2e86de;\n"
"border : None;\n"
"color: rgb(255, 255, 255);\n"
"border: 2px solid #ced4da; \n"
"border-radius: 40px; \n"
"padding: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"        background-color: #0056b3; /* Darker blue on press */\n"
"    }\n"
"")
        icon1 = QIcon()
        icon1.addFile(u":/Home/previous1.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_previous.setIcon(icon1)
        self.pushButton_previous.setIconSize(QSize(80, 80))
        self.label_File_path = QLabel(self.centralwidget)
        self.label_File_path.setObjectName(u"label_File_path")
        self.label_File_path.setGeometry(QRect(400, 120, 1120, 20))
        self.label_File_path.setFont(font1)
        self.label_File_path.setStyleSheet(u"")
        self.label_File_path.setAlignment(Qt.AlignCenter)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(470, 80, 131, 20))
        self.label_2.setFont(font1)
        self.pushButton_browse = QPushButton(self.centralwidget)
        self.pushButton_browse.setObjectName(u"pushButton_browse")
        self.pushButton_browse.setGeometry(QRect(1620, 70, 111, 41))
        font3 = QFont()
        font3.setPointSize(13)
        self.pushButton_browse.setFont(font3)
        self.pushButton_browse.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_browse.setStyleSheet(u"QPushButton{\n"
"background-color: #17a2b8;\n"
"border : None;\n"
"color: rgb(255, 255, 255);\n"
"border: 2px solid #ced4da; \n"
"border-radius: 4px; \n"
"padding: 5px;}\n"
"\n"
"QPushButton:pressed {\n"
"        background-color: #0056b3; /* Darker blue on press */\n"
"    }\n"
"")
        self.pushButton_ok_files = QPushButton(self.centralwidget)
        self.pushButton_ok_files.setObjectName(u"pushButton_ok_files")
        self.pushButton_ok_files.setGeometry(QRect(230, 920, 361, 80))
        font4 = QFont()
        font4.setPointSize(20)
        font4.setBold(True)
        self.pushButton_ok_files.setFont(font4)
        self.pushButton_ok_files.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_ok_files.setStyleSheet(u"\n"
"QPushButton {\n"
"background-color: #28a745; \n"
"color: #fff; \n"
"font-weight: bold; \n"
"border: none; \n"
"border-radius: 4px; \n"
"padding: 8px;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(115, 210, 22);\n"
"}")
        self.pushButton_ok_files.setFlat(False)
        self.pushButton_not_ok_files = QPushButton(self.centralwidget)
        self.pushButton_not_ok_files.setObjectName(u"pushButton_not_ok_files")
        self.pushButton_not_ok_files.setGeometry(QRect(680, 920, 351, 80))
        self.pushButton_not_ok_files.setFont(font4)
        self.pushButton_not_ok_files.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_not_ok_files.setStyleSheet(u"QPushButton {\n"
"background-color: #de0a26; \n"
"color: #fff; \n"
"font-weight: bold; \n"
"border: none; \n"
"border-radius: 4px; \n"
"padding: 8px;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(239, 41, 41);\n"
"}\n"
"")
        self.label_frame_number = QLabel(self.centralwidget)
        self.label_frame_number.setObjectName(u"label_frame_number")
        self.label_frame_number.setGeometry(QRect(610, 870, 50, 50))
        self.label_frame_number.setFont(font1)
        self.label_frame_number.setAlignment(Qt.AlignCenter)
        self.pushButton_next_transaction = QPushButton(self.centralwidget)
        self.pushButton_next_transaction.setObjectName(u"pushButton_next_transaction")
        self.pushButton_next_transaction.setGeometry(QRect(1060, 230, 151, 41))
        self.pushButton_next_transaction.setFont(font3)
        self.pushButton_next_transaction.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_next_transaction.setStyleSheet(u"QPushButton{\n"
"background-color: #17a2b8;\n"
"border : None;\n"
"color: rgb(255, 255, 255);\n"
"border: 2px solid #ced4da; \n"
"border-radius: 4px; \n"
"padding: 5px;}\n"
"\n"
"QPushButton:pressed {\n"
"        background-color: #0056b3; /* Darker blue on press */\n"
"    }\n"
"")
        self.pushButton_next_position = QPushButton(self.centralwidget)
        self.pushButton_next_position.setObjectName(u"pushButton_next_position")
        self.pushButton_next_position.setGeometry(QRect(1070, 390, 130, 41))
        self.pushButton_next_position.setFont(font3)
        self.pushButton_next_position.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_next_position.setStyleSheet(u"QPushButton{\n"
"background-color: #17a2b8;\n"
"border : None;\n"
"color: rgb(255, 255, 255);\n"
"border: 2px solid #ced4da; \n"
"border-radius: 4px; \n"
"padding: 5px;}\n"
"\n"
"QPushButton:pressed {\n"
"        background-color: #0056b3; /* Darker blue on press */\n"
"    }\n"
"")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(820, 80, 201, 20))
        self.label_3.setFont(font1)
        self.label_frame_transaction = QLabel(self.centralwidget)
        self.label_frame_transaction.setObjectName(u"label_frame_transaction")
        self.label_frame_transaction.setGeometry(QRect(1020, 80, 131, 20))
        self.label_frame_transaction.setFont(font1)
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(1229, 80, 171, 20))
        self.label_4.setFont(font1)
        self.label_frame_position = QLabel(self.centralwidget)
        self.label_frame_position.setObjectName(u"label_frame_position")
        self.label_frame_position.setGeometry(QRect(1400, 80, 131, 20))
        self.label_frame_position.setFont(font1)
        self.pushButton_prev_position = QPushButton(self.centralwidget)
        self.pushButton_prev_position.setObjectName(u"pushButton_prev_position")
        self.pushButton_prev_position.setGeometry(QRect(40, 390, 151, 41))
        self.pushButton_prev_position.setFont(font3)
        self.pushButton_prev_position.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_prev_position.setStyleSheet(u"QPushButton{\n"
"background-color: #17a2b8;\n"
"border : None;\n"
"color: rgb(255, 255, 255);\n"
"border: 2px solid #ced4da; \n"
"border-radius: 4px; \n"
"padding: 5px;}\n"
"\n"
"QPushButton:pressed {\n"
"        background-color: #0056b3; /* Darker blue on press */\n"
"    }\n"
"")
        self.pushButton_prev_transaction = QPushButton(self.centralwidget)
        self.pushButton_prev_transaction.setObjectName(u"pushButton_prev_transaction")
        self.pushButton_prev_transaction.setGeometry(QRect(30, 230, 170, 41))
        self.pushButton_prev_transaction.setFont(font3)
        self.pushButton_prev_transaction.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_prev_transaction.setStyleSheet(u"QPushButton{\n"
"background-color: #17a2b8;\n"
"border : None;\n"
"color: rgb(255, 255, 255);\n"
"border: 2px solid #ced4da; \n"
"border-radius: 4px; \n"
"padding: 5px;}\n"
"\n"
"QPushButton:pressed {\n"
"        background-color: #0056b3; /* Darker blue on press */\n"
"    }\n"
"")
        self.label_pre_txn_warning = QLabel(self.centralwidget)
        self.label_pre_txn_warning.setObjectName(u"label_pre_txn_warning")
        self.label_pre_txn_warning.setGeometry(QRect(40, 280, 141, 17))
        self.label_pre_txn_warning.setStyleSheet(u"color: rgb(239, 41, 41);")
        self.label_pre_ptn_warning = QLabel(self.centralwidget)
        self.label_pre_ptn_warning.setObjectName(u"label_pre_ptn_warning")
        self.label_pre_ptn_warning.setGeometry(QRect(40, 440, 141, 17))
        self.label_pre_ptn_warning.setStyleSheet(u"color: rgb(239, 41, 41);")
        self.label_last_ptn_warning = QLabel(self.centralwidget)
        self.label_last_ptn_warning.setObjectName(u"label_last_ptn_warning")
        self.label_last_ptn_warning.setGeometry(QRect(1070, 440, 141, 17))
        self.label_last_ptn_warning.setStyleSheet(u"color: rgb(239, 41, 41);")
        self.label_last_txn_warning = QLabel(self.centralwidget)
        self.label_last_txn_warning.setObjectName(u"label_last_txn_warning")
        self.label_last_txn_warning.setGeometry(QRect(1060, 280, 141, 17))
        self.label_last_txn_warning.setStyleSheet(u"color: rgb(239, 41, 41);")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(1260, 200, 611, 141))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 10, 500, 20))
        self.label_5.setFont(font3)
        self.checkBox_lower = QCheckBox(self.frame)
        self.checkBox_lower.setObjectName(u"checkBox_lower")
        self.checkBox_lower.setEnabled(False)
        self.checkBox_lower.setGeometry(QRect(10, 60, 92, 23))
        font5 = QFont()
        font5.setBold(False)
        self.checkBox_lower.setFont(font5)
        self.checkBox_lower.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.checkBox_lower.setCheckable(True)
        self.checkBox_lower.setChecked(False)
        self.checkBox_middle = QCheckBox(self.frame)
        self.checkBox_middle.setObjectName(u"checkBox_middle")
        self.checkBox_middle.setEnabled(False)
        self.checkBox_middle.setGeometry(QRect(160, 60, 92, 23))
        self.checkBox_middle.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.checkBox_middle.setCheckable(True)
        self.checkBox_bottom = QCheckBox(self.frame)
        self.checkBox_bottom.setObjectName(u"checkBox_bottom")
        self.checkBox_bottom.setEnabled(False)
        self.checkBox_bottom.setGeometry(QRect(330, 60, 92, 23))
        self.checkBox_bottom.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.checkBox_bottom.setCheckable(True)
        self.checkBox_top = QCheckBox(self.frame)
        self.checkBox_top.setObjectName(u"checkBox_top")
        self.checkBox_top.setEnabled(False)
        self.checkBox_top.setGeometry(QRect(500, 60, 92, 23))
        self.checkBox_top.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.checkBox_top.setCheckable(True)
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(1260, 440, 611, 141))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.label_6 = QLabel(self.frame_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 10, 390, 21))
        self.label_6.setFont(font3)
        self.lineEdit_reason = QLineEdit(self.frame_2)
        self.lineEdit_reason.setObjectName(u"lineEdit_reason")
        self.lineEdit_reason.setGeometry(QRect(30, 50, 561, 31))
        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(1260, 680, 611, 141))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.label_7 = QLabel(self.frame_3)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(20, 10, 200, 21))
        self.label_7.setFont(font3)
        self.pushButton_zoomIn = QPushButton(self.frame_3)
        self.pushButton_zoomIn.setObjectName(u"pushButton_zoomIn")
        self.pushButton_zoomIn.setGeometry(QRect(50, 60, 141, 41))
        self.pushButton_zoomIn.setFont(font3)
        self.pushButton_zoomIn.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_zoomIn.setStyleSheet(u"QPushButton{\n"
"background-color: #17a2b8;\n"
"border : None;\n"
"color: rgb(255, 255, 255);\n"
"border: 2px solid #ced4da; \n"
"border-radius: 4px; \n"
"padding: 5px;}\n"
"\n"
"QPushButton:pressed {\n"
"        background-color: #0056b3; /* Darker blue on press */\n"
"    }\n"
"")
        self.pushButton_reset = QPushButton(self.frame_3)
        self.pushButton_reset.setObjectName(u"pushButton_reset")
        self.pushButton_reset.setGeometry(QRect(240, 60, 141, 41))
        self.pushButton_reset.setFont(font3)
        self.pushButton_reset.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_reset.setStyleSheet(u"QPushButton{\n"
"background-color: #17a2b8;\n"
"border : None;\n"
"color: rgb(255, 255, 255);\n"
"border: 2px solid #ced4da; \n"
"border-radius: 4px; \n"
"padding: 5px;}\n"
"\n"
"QPushButton:pressed {\n"
"        background-color: #0056b3; /* Darker blue on press */\n"
"    }\n"
"")
        self.pushButton_zoomOut = QPushButton(self.frame_3)
        self.pushButton_zoomOut.setObjectName(u"pushButton_zoomOut")
        self.pushButton_zoomOut.setGeometry(QRect(430, 60, 141, 41))
        self.pushButton_zoomOut.setFont(font3)
        self.pushButton_zoomOut.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_zoomOut.setStyleSheet(u"QPushButton{\n"
"background-color: #17a2b8;\n"
"border : None;\n"
"color: rgb(255, 255, 255);\n"
"border: 2px solid #ced4da; \n"
"border-radius: 4px; \n"
"padding: 5px;}\n"
"\n"
"QPushButton:pressed {\n"
"        background-color: #0056b3; /* Darker blue on press */\n"
"    }\n"
"")
        self.label_allPostions_warning = QLabel(self.centralwidget)
        self.label_allPostions_warning.setObjectName(u"label_allPostions_warning")
        self.label_allPostions_warning.setGeometry(QRect(1270, 350, 170, 17))
        self.label_allPostions_warning.setStyleSheet(u"color: rgb(239, 41, 41);")
        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(270, 150, 709, 709))
        self.scrollArea.setStyleSheet(u"QScrollArea {\n"
"	border : None\n"
"}\n"
"\n"
"QScrollBar {\n"
"    background: #E8E8E8;\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"    width: 7px;\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"    height: 7px;\n"
"}\n"
"\n"
"QScrollBar::handle {\n"
"    background: #787878;\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    min-height: 5px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"    min-width: 5px;\n"
"}\n"
"\n"
"QScrollBar::add-line {\n"
"    border: none;\n"
"    background: none;\n"
"}\n"
"\n"
"QScrollBar::sub-line {\n"
"    border: none;\n"
"    background: none;\n"
"}\n"
"")
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 709, 709))
        self.scrollAreaWidgetContents.setMinimumSize(QSize(0, 0))
        self.scrollAreaWidgetContents.setStyleSheet(u"")
        self.label = QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 700, 700))
        self.label.setStyleSheet(u"border : 1px solid rgb(85, 87, 83);\n"
"")
        self.label.setScaledContents(True)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.pushButton_close = QPushButton(self.centralwidget)
        self.pushButton_close.setObjectName(u"pushButton_close")
        self.pushButton_close.setGeometry(QRect(1870, 10, 40, 40))
        self.pushButton_close.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_close.setStyleSheet(u"border: None")
        icon2 = QIcon()
        icon2.addFile(u":/Home/Close.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_close.setIcon(icon2)
        self.pushButton_close.setIconSize(QSize(40, 40))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_copy_rights.setText(QCoreApplication.translate("MainWindow", u"Copyrights Statement", None))
        self.label_name.setText(QCoreApplication.translate("MainWindow", u"Inspection tool", None))
        self.label_frame_count.setText("")
        self.pushButton_next.setText("")
        self.pushButton_previous.setText("")
        self.label_File_path.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Frame count :: ", None))
        self.pushButton_browse.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.pushButton_ok_files.setText(QCoreApplication.translate("MainWindow", u"OK Files", None))
        self.pushButton_not_ok_files.setText(QCoreApplication.translate("MainWindow", u"Not OK Files", None))
        self.label_frame_number.setText("")
        self.pushButton_next_transaction.setText(QCoreApplication.translate("MainWindow", u"Next Transaction", None))
        self.pushButton_next_position.setText(QCoreApplication.translate("MainWindow", u"Next Position", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Current Transaction :: ", None))
        self.label_frame_transaction.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Current Position :: ", None))
        self.label_frame_position.setText("")
        self.pushButton_prev_position.setText(QCoreApplication.translate("MainWindow", u"Previous Position", None))
        self.pushButton_prev_transaction.setText(QCoreApplication.translate("MainWindow", u"Previous Transaction", None))
        self.label_pre_txn_warning.setText(QCoreApplication.translate("MainWindow", u"First transaction", None))
        self.label_pre_ptn_warning.setText(QCoreApplication.translate("MainWindow", u"First position", None))
        self.label_last_ptn_warning.setText(QCoreApplication.translate("MainWindow", u"Last position", None))
        self.label_last_txn_warning.setText(QCoreApplication.translate("MainWindow", u"Last transaction", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Complete all positions before procedding to next transactions", None))
        self.checkBox_lower.setText(QCoreApplication.translate("MainWindow", u"LOWER", None))
        self.checkBox_middle.setText(QCoreApplication.translate("MainWindow", u"MIDDLE", None))
        self.checkBox_bottom.setText(QCoreApplication.translate("MainWindow", u"BOTTOM", None))
        self.checkBox_top.setText(QCoreApplication.translate("MainWindow", u"TOP", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Reason for OK/Not_OK", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Image Controls", None))
        self.pushButton_zoomIn.setText(QCoreApplication.translate("MainWindow", u"Zoom In", None))
        self.pushButton_reset.setText(QCoreApplication.translate("MainWindow", u"Reset Zoom", None))
        self.pushButton_zoomOut.setText(QCoreApplication.translate("MainWindow", u"Zoom Out", None))
        self.label_allPostions_warning.setText(QCoreApplication.translate("MainWindow", u"Complete all Positions", None))
        self.label.setText("")
        self.pushButton_close.setText("")
    # retranslateUi

