# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e:\OI\sql\ui\addflight.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Add_flight(object):
    def setupUi(self, Add_flight):
        Add_flight.setObjectName("Add_flight")
        Add_flight.resize(400, 347)
        self.flight_comboBox = QtWidgets.QComboBox(Add_flight)
        self.flight_comboBox.setGeometry(QtCore.QRect(120, 50, 161, 31))
        self.flight_comboBox.setObjectName("flight_comboBox")
        self.date_label = QtWidgets.QLabel(Add_flight)
        self.date_label.setGeometry(QtCore.QRect(30, 50, 61, 30))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.date_label.setFont(font)
        self.date_label.setStyleSheet("")
        self.date_label.setObjectName("date_label")
        self.date_label_2 = QtWidgets.QLabel(Add_flight)
        self.date_label_2.setGeometry(QtCore.QRect(30, 90, 71, 30))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.date_label_2.setFont(font)
        self.date_label_2.setStyleSheet("")
        self.date_label_2.setObjectName("date_label_2")
        self.date_dateEdit = QtWidgets.QDateEdit(Add_flight)
        self.date_dateEdit.setGeometry(QtCore.QRect(120, 90, 201, 31))
        self.date_dateEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(2021, 6, 21), QtCore.QTime(0, 0, 0)))
        self.date_dateEdit.setObjectName("date_dateEdit")
        self.date_label_3 = QtWidgets.QLabel(Add_flight)
        self.date_label_3.setGeometry(QtCore.QRect(30, 210, 61, 30))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.date_label_3.setFont(font)
        self.date_label_3.setStyleSheet("")
        self.date_label_3.setObjectName("date_label_3")
        self.plane_comboBox = QtWidgets.QComboBox(Add_flight)
        self.plane_comboBox.setGeometry(QtCore.QRect(120, 210, 161, 31))
        self.plane_comboBox.setObjectName("plane_comboBox")
        self.yes_pushButton = QtWidgets.QPushButton(Add_flight)
        self.yes_pushButton.setGeometry(QtCore.QRect(40, 280, 111, 41))
        self.yes_pushButton.setStyleSheet("QPalette{background:#D7DBE4;}QGroupBox#gboxDevicePanel>QLabel{color:#E7ECF0;}\n"
"\n"
"QWidget#frmMain,QWidget[Form=\"true\"]{\n"
"border:1px solid #738393;\n"
"border-radius:0px;\n"
"}\n"
"\n"
".QFrame{\n"
"border:1px solid #C2CCD8;\n"
"border-radius:5px;\n"
"}\n"
"\n"
"QLabel,QLineEdit,QTextEdit,QPlainTextEdit,QSpinBox,QGroupBox,QComboBox,QDateEdit,QTimeEdit,QDateTimeEdit,QSpinBox,QTreeView,QListView,QTableView,QTabWidget::pane{\n"
"color:#3D3E42;\n"
"}\n"
"\n"
"QWidget#widget_title{\n"
"background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #667481,stop:1 #566373);\n"
"}\n"
"\n"
"QLabel#lab_Ico,QLabel#lab_Title{\n"
"border-radius:0px;\n"
"color:#E7ECF0;\n"
"background-color:rgba(0,0,0,0);\n"
"border-style:none;\n"
"}\n"
"\n"
"QToolButton::menu-indicator{\n"
"image:None;\n"
"}\n"
"\n"
"QToolButton,QWidget#widget_frm>QLabel{\n"
"border-style:none;\n"
"padding:10px;\n"
"color:#E7ECF0;\n"
"background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #667481,stop:1 #566373);\n"
"}\n"
"\n"
"QToolButton:hover,QWidget#widget_frm>QLabel:hover{\n"
"background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #778899,stop:1 #708090);\n"
"}\n"
"\n"
"QLabel[labVideo=\"true\"]{\n"
"color:#E7ECF0;\n"
"border:1px solid #738393;\n"
"background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #667481,stop:1 #566373);\n"
"}\n"
"\n"
"QLabel[labVideo=\"true\"]:focus{\n"
"border:1px solid #FF0000;\n"
"background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #778899,stop:1 #708090);\n"
"}\n"
"\n"
"QLineEdit,QTextEdit,QPlainTextEdit,QSpinBox{\n"
"border:1px solid #C2CCD8;\n"
"border-radius:5px;\n"
"padding:2px;\n"
"background:none;\n"
"selection-background-color:#667481;\n"
"selection-color:#E7ECF0;\n"
"}\n"
"\n"
"QLineEdit[echoMode=\"2\"]{\n"
"lineedit-password-character:9679;\n"
"}\n"
"\n"
".QGroupBox{\n"
"border:1px solid #C2CCD8;\n"
"border-radius:5px;\n"
"}\n"
"\n"
".QPushButton{\n"
"border-style:none;\n"
"border:1px solid #C2CCD8;\n"
"color:#E7ECF0;\n"
"padding:5px;\n"
"min-height:20px;\n"
"border-radius:5px;\n"
"background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #667481,stop:1 #566373);\n"
"}\n"
"\n"
".QPushButton:hover{\n"
"background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #778899,stop:1 #708090);\n"
"}\n"
"\n"
".QPushButton:pressed{\n"
"background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #667481,stop:1 #566373);\n"
"}\n"
"\n"
".QPushButton:disabled{\n"
"color:#838383;\n"
"background:#F4F4F4;\n"
"}\n"
"\n"
"QPushButton#btnSplitterH{\n"
"padding:2px;\n"
"min-height:8px;\n"
"}\n"
"\n"
"QPushButton#btnMenu,QPushButton#btnMenu_Min,QPushButton#btnMenu_Max,QPushButton#btnMenu_Close,QPushButton#btnSplitterV,QPushButton#btnSplitterH{\n"
"border-radius:0px;\n"
"color:#E7ECF0;\n"
"background-color:rgba(0,0,0,0);\n"
"border-style:none;\n"
"}\n"
"\n"
"QPushButton#btnMenu:hover,QPushButton#btnMenu_Min:hover,QPushButton#btnMenu_Max:hover,QPushButton#btnSplitterV:hover,QPushButton#btnSplitterH:hover{\n"
"background-color:qlineargradient(spread:pad,x1:0,y1:1,x2:0,y2:0,stop:0 rgba(25,134,199,0),stop:1 #778899);\n"
"}\n"
"\n"
"QPushButton#btnMenu_Close:hover{\n"
"background-color:qlineargradient(spread:pad,x1:0,y1:1,x2:0,y2:0,stop:0 rgba(238,0,0,128),stop:1 rgba(238,44,44,255));\n"
"}\n"
"\n"
"QCheckBox{\n"
"color:#3D3E42;\n"
"spacing:2px;\n"
"}\n"
"\n"
"QCheckBox::indicator{\n"
"width:20px;\n"
"height:20px;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked{\n"
"image:url(:/image/checkbox_unchecked.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked{\n"
"image:url(:/image/checkbox_checked.png);\n"
"}\n"
"\n"
"QRadioButton{\n"
"color:#3D3E42;\n"
"spacing:2px;\n"
"}\n"
"\n"
"QRadioButton::indicator{\n"
"width:15px;\n"
"height:15px;\n"
"}\n"
"\n"
"QRadioButton::indicator::unchecked{\n"
"image:url(:/image/radio_normal.png);\n"
"}\n"
"\n"
"QRadioButton::indicator::checked{\n"
"image:url(:/image/radio_selected.png);\n"
"}\n"
"\n"
"QSpinBox::up-button,QDateEdit::up-button,QTimeEdit::up-button,QDateTimeEdit::up-button{\n"
"image:url(:/image/add_top.png);\n"
"}\n"
"\n"
"QSpinBox::down-button,QDateEdit::down-button,QTimeEdit::down-button,QDateTimeEdit::down-button{\n"
"image:url(:/image/add_bottom.png);\n"
"}\n"
"\n"
"QComboBox,QDateEdit,QTimeEdit,QDateTimeEdit,QSpinBox{\n"
"border-radius:3px;\n"
"padding:3px 5px 3px 5px;\n"
"border:1px solid #C2CCD8;\n"
"background:none;\n"
"selection-background-color:#667481;\n"
"selection-color:#E7ECF0;\n"
"}\n"
"\n"
"QComboBox::drop-down,QDateEdit::drop-down,QTimeEdit::drop-down,QDateTimeEdit::drop-down{\n"
"subcontrol-origin:padding;\n"
"subcontrol-position:top right;\n"
"width:15px;\n"
"border-left-width:1px;\n"
"border-left-style:solid;\n"
"border-top-right-radius:3px;\n"
"border-bottom-right-radius:3px;\n"
"border-left-color:#C2CCD8;\n"
"}\n"
"\n"
"QComboBox::down-arrow,QDateEdit::down-arrow,QTimeEdit::down-arrow,QDateTimeEdit::down-arrow{\n"
"image:url(:/image/add_bottom.png);\n"
"}\n"
"\n"
"QMenu{\n"
"color:#E7ECF0;\n"
"background-color:#667481;\n"
"margin:2px;\n"
"}\n"
"\n"
"QMenu::item{\n"
"padding:3px 20px 3px 20px;\n"
"}\n"
"\n"
"QMenu::indicator{\n"
"width:13px;\n"
"height:13px;\n"
"}\n"
"\n"
"QMenu::item:selected{\n"
"color:#E7ECF0;\n"
"border:0px solid #738393;\n"
"background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #667481,stop:1 #566373);\n"
"}\n"
"\n"
"QMenu::separator{\n"
"height:1px;\n"
"background:#738393;\n"
"}\n"
"\n"
"QProgressBar{\n"
"background:#C2CCD8;\n"
"border-radius:5px;\n"
"text-align:center;\n"
"border:1px solid #C2CCD8;\n"
"}\n"
"\n"
"QProgressBar::chunk{\n"
"width:5px;\n"
"margin:0.5px;\n"
"background-color:#667481;\n"
"}\n"
"\n"
"QSlider::groove:horizontal,QSlider::add-page:horizontal{\n"
"height:8px;\n"
"border-radius:3px;\n"
"background:#C2CCD8;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal{\n"
"height:8px;\n"
"border-radius:3px;\n"
"background:#708090;\n"
"}\n"
"\n"
"QSlider::handle:horizontal{\n"
"width:13px;\n"
"margin-top:-3px;\n"
"margin-bottom:-3px;\n"
"border-radius:6px;\n"
"background:qradialgradient(spread:pad,cx:0.5,cy:0.5,radius:0.5,fx:0.5,fy:0.5,stop:0.6 #667481,stop:0.8 #778899);\n"
"}\n"
"\n"
"QSlider::groove:vertical,QSlider::sub-page:vertical{\n"
"width:8px;\n"
"border-radius:3px;\n"
"background:#C2CCD8;\n"
"}\n"
"\n"
"QSlider::add-page:vertical{\n"
"width:8px;\n"
"border-radius:3px;\n"
"background:#708090;\n"
"}\n"
"\n"
"QSlider::handle:vertical{\n"
"height:13px;\n"
"margin-left:-2px;\n"
"margin-right:-3px;\n"
"border-radius:6px;\n"
"background:qradialgradient(spread:pad,cx:0.5,cy:0.5,radius:0.5,fx:0.5,fy:0.5,stop:0.6 #667481,stop:0.8 #778899);\n"
"}\n"
"\n"
"QScrollBar:vertical{\n"
"width:10px;\n"
"background-color:rgba(0,0,0,0%);\n"
"padding-top:10px;\n"
"padding-bottom:10px;\n"
"}\n"
"\n"
"QScrollBar:horizontal{\n"
"height:10px;\n"
"background-color:rgba(0,0,0,0%);\n"
"padding-left:10px;\n"
"padding-right:10px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical,QScrollBar::handle:horizontal{\n"
"width:10px;\n"
"background:#708090;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover,QScrollBar::handle:horizontal:hover{\n"
"width:10px;\n"
"background:#566373;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical{\n"
"height:10px;\n"
"width:10px;\n"
"subcontrol-position:bottom;\n"
"subcontrol-origin:margin;\n"
"border-image:url(:/image/add_bottom.png);\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal{\n"
"height:10px;\n"
"width:10px;\n"
"subcontrol-position:right;\n"
"subcontrol-origin:margin;\n"
"border-image:url(:/image/add_right.png);\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical{\n"
"height:10px;\n"
"width:10px;\n"
"subcontrol-position:top;\n"
"subcontrol-origin:margin;\n"
"border-image:url(:/image/add_top.png);\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal{\n"
"height:10px;\n"
"width:10px;\n"
"subcontrol-position:left;\n"
"subcontrol-origin:margin;\n"
"border-image:url(:/image/add_left.png);\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical,QScrollBar::sub-page:vertical,QScrollBar::add-page:horizontal,QScrollBar::sub-page:horizontal{\n"
"width:10px;\n"
"background:#C2CCD8;\n"
"}\n"
"\n"
"QScrollArea{\n"
"border:0px;\n"
"}\n"
"\n"
"QTreeView,QListView,QTableView,QTabWidget::pane{\n"
"border:1px solid #C2CCD8;\n"
"selection-background-color:#778899;\n"
"selection-color:#E7ECF0;\n"
"alternate-background-color:#DDE0E7;\n"
"}\n"
"\n"
"QTableView::item:selected,QListView::item:selected,QTreeView::item:selected{\n"
"color:#E7ECF0;\n"
"background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #667481,stop:1 #566373);\n"
"}\n"
"\n"
"QTableView::item:hover,QListView::item:hover,QTreeView::item:hover{\n"
"color:#E7ECF0;\n"
"background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #778899,stop:1 #708090);\n"
"}\n"
"\n"
"QTableView::item,QListView::item,QTreeView::item{\n"
"padding:5px;\n"
"margin:0px;\n"
"}\n"
"\n"
"QHeaderView::section,QTableCornerButton:section{\n"
"padding:3px;\n"
"margin:0px;\n"
"color:#E7ECF0;\n"
"border:1px solid #C2CCD8;\n"
"background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #778899,stop:1 #708090);\n"
"}\n"
"\n"
"QTabBar::tab{\n"
"border-radius:5px;\n"
"border:1px solid #C2CCD8;\n"
"color:#E7ECF0;\n"
"min-width:55px;\n"
"min-height:20px;\n"
"padding:3px 8px 3px 8px;\n"
"margin:1px;\n"
"background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #778899,stop:1 #708090);\n"
"}\n"
"\n"
"QTabBar::tab:selected,QTabBar::tab:hover{\n"
"background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #667481,stop:1 #566373);\n"
"}\n"
"\n"
"QStatusBar::item{\n"
"border:0px solid #667481;\n"
"border-radius:3px;\n"
"}\n"
"\n"
"QToolBox::tab,QToolTip,QGroupBox#gboxDevicePanel{\n"
"padding:3px;\n"
"border-radius: 5px;\n"
"color:#E7ECF0;\n"
"background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #667481,stop:1 #566373);\n"
"}\n"
"\n"
"QToolBox::tab:selected{\n"
"background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #778899,stop:1 #708090);\n"
"}\n"
"")
        self.yes_pushButton.setObjectName("yes_pushButton")
        self.no_pushButton = QtWidgets.QPushButton(Add_flight)
        self.no_pushButton.setGeometry(QtCore.QRect(220, 280, 111, 41))
        self.no_pushButton.setStyleSheet("QPalette{background:#D7DBE4;}QGroupBox#gboxDevicePanel>QLabel{color:#E7ECF0;}\n"
"\n"
"QWidget#frmMain,QWidget[Form=\"true\"]{\n"
"border:1px solid #738393;\n"
"border-radius:0px;\n"
"}\n"
"\n"
".QFrame{\n"
"border:1px solid #C2CCD8;\n"
"border-radius:5px;\n"
"}\n"
"\n"
"QLabel,QLineEdit,QTextEdit,QPlainTextEdit,QSpinBox,QGroupBox,QComboBox,QDateEdit,QTimeEdit,QDateTimeEdit,QSpinBox,QTreeView,QListView,QTableView,QTabWidget::pane{\n"
"color:#3D3E42;\n"
"}\n"
"\n"
"QWidget#widget_title{\n"
"background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #667481,stop:1 #566373);\n"
"}\n"
"\n"
"QLabel#lab_Ico,QLabel#lab_Title{\n"
"border-radius:0px;\n"
"color:#E7ECF0;\n"
"background-color:rgba(0,0,0,0);\n"
"border-style:none;\n"
"}\n"
"\n"
"QToolButton::menu-indicator{\n"
"image:None;\n"
"}\n"
"\n"
"QToolButton,QWidget#widget_frm>QLabel{\n"
"border-style:none;\n"
"padding:10px;\n"
"color:#E7ECF0;\n"
"background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #667481,stop:1 #566373);\n"
"}\n"
"\n"
"QToolButton:hover,QWidget#widget_frm>QLabel:hover{\n"
"background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #778899,stop:1 #708090);\n"
"}\n"
"\n"
"QLabel[labVideo=\"true\"]{\n"
"color:#E7ECF0;\n"
"border:1px solid #738393;\n"
"background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #667481,stop:1 #566373);\n"
"}\n"
"\n"
"QLabel[labVideo=\"true\"]:focus{\n"
"border:1px solid #FF0000;\n"
"background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #778899,stop:1 #708090);\n"
"}\n"
"\n"
"QLineEdit,QTextEdit,QPlainTextEdit,QSpinBox{\n"
"border:1px solid #C2CCD8;\n"
"border-radius:5px;\n"
"padding:2px;\n"
"background:none;\n"
"selection-background-color:#667481;\n"
"selection-color:#E7ECF0;\n"
"}\n"
"\n"
"QLineEdit[echoMode=\"2\"]{\n"
"lineedit-password-character:9679;\n"
"}\n"
"\n"
".QGroupBox{\n"
"border:1px solid #C2CCD8;\n"
"border-radius:5px;\n"
"}\n"
"\n"
".QPushButton{\n"
"border-style:none;\n"
"border:1px solid #C2CCD8;\n"
"color:#E7ECF0;\n"
"padding:5px;\n"
"min-height:20px;\n"
"border-radius:5px;\n"
"background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #667481,stop:1 #566373);\n"
"}\n"
"\n"
".QPushButton:hover{\n"
"background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #778899,stop:1 #708090);\n"
"}\n"
"\n"
".QPushButton:pressed{\n"
"background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #667481,stop:1 #566373);\n"
"}\n"
"\n"
".QPushButton:disabled{\n"
"color:#838383;\n"
"background:#F4F4F4;\n"
"}\n"
"\n"
"QPushButton#btnSplitterH{\n"
"padding:2px;\n"
"min-height:8px;\n"
"}\n"
"\n"
"QPushButton#btnMenu,QPushButton#btnMenu_Min,QPushButton#btnMenu_Max,QPushButton#btnMenu_Close,QPushButton#btnSplitterV,QPushButton#btnSplitterH{\n"
"border-radius:0px;\n"
"color:#E7ECF0;\n"
"background-color:rgba(0,0,0,0);\n"
"border-style:none;\n"
"}\n"
"\n"
"QPushButton#btnMenu:hover,QPushButton#btnMenu_Min:hover,QPushButton#btnMenu_Max:hover,QPushButton#btnSplitterV:hover,QPushButton#btnSplitterH:hover{\n"
"background-color:qlineargradient(spread:pad,x1:0,y1:1,x2:0,y2:0,stop:0 rgba(25,134,199,0),stop:1 #778899);\n"
"}\n"
"\n"
"QPushButton#btnMenu_Close:hover{\n"
"background-color:qlineargradient(spread:pad,x1:0,y1:1,x2:0,y2:0,stop:0 rgba(238,0,0,128),stop:1 rgba(238,44,44,255));\n"
"}\n"
"\n"
"QCheckBox{\n"
"color:#3D3E42;\n"
"spacing:2px;\n"
"}\n"
"\n"
"QCheckBox::indicator{\n"
"width:20px;\n"
"height:20px;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked{\n"
"image:url(:/image/checkbox_unchecked.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked{\n"
"image:url(:/image/checkbox_checked.png);\n"
"}\n"
"\n"
"QRadioButton{\n"
"color:#3D3E42;\n"
"spacing:2px;\n"
"}\n"
"\n"
"QRadioButton::indicator{\n"
"width:15px;\n"
"height:15px;\n"
"}\n"
"\n"
"QRadioButton::indicator::unchecked{\n"
"image:url(:/image/radio_normal.png);\n"
"}\n"
"\n"
"QRadioButton::indicator::checked{\n"
"image:url(:/image/radio_selected.png);\n"
"}\n"
"\n"
"QSpinBox::up-button,QDateEdit::up-button,QTimeEdit::up-button,QDateTimeEdit::up-button{\n"
"image:url(:/image/add_top.png);\n"
"}\n"
"\n"
"QSpinBox::down-button,QDateEdit::down-button,QTimeEdit::down-button,QDateTimeEdit::down-button{\n"
"image:url(:/image/add_bottom.png);\n"
"}\n"
"\n"
"QComboBox,QDateEdit,QTimeEdit,QDateTimeEdit,QSpinBox{\n"
"border-radius:3px;\n"
"padding:3px 5px 3px 5px;\n"
"border:1px solid #C2CCD8;\n"
"background:none;\n"
"selection-background-color:#667481;\n"
"selection-color:#E7ECF0;\n"
"}\n"
"\n"
"QComboBox::drop-down,QDateEdit::drop-down,QTimeEdit::drop-down,QDateTimeEdit::drop-down{\n"
"subcontrol-origin:padding;\n"
"subcontrol-position:top right;\n"
"width:15px;\n"
"border-left-width:1px;\n"
"border-left-style:solid;\n"
"border-top-right-radius:3px;\n"
"border-bottom-right-radius:3px;\n"
"border-left-color:#C2CCD8;\n"
"}\n"
"\n"
"QComboBox::down-arrow,QDateEdit::down-arrow,QTimeEdit::down-arrow,QDateTimeEdit::down-arrow{\n"
"image:url(:/image/add_bottom.png);\n"
"}\n"
"\n"
"QMenu{\n"
"color:#E7ECF0;\n"
"background-color:#667481;\n"
"margin:2px;\n"
"}\n"
"\n"
"QMenu::item{\n"
"padding:3px 20px 3px 20px;\n"
"}\n"
"\n"
"QMenu::indicator{\n"
"width:13px;\n"
"height:13px;\n"
"}\n"
"\n"
"QMenu::item:selected{\n"
"color:#E7ECF0;\n"
"border:0px solid #738393;\n"
"background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #667481,stop:1 #566373);\n"
"}\n"
"\n"
"QMenu::separator{\n"
"height:1px;\n"
"background:#738393;\n"
"}\n"
"\n"
"QProgressBar{\n"
"background:#C2CCD8;\n"
"border-radius:5px;\n"
"text-align:center;\n"
"border:1px solid #C2CCD8;\n"
"}\n"
"\n"
"QProgressBar::chunk{\n"
"width:5px;\n"
"margin:0.5px;\n"
"background-color:#667481;\n"
"}\n"
"\n"
"QSlider::groove:horizontal,QSlider::add-page:horizontal{\n"
"height:8px;\n"
"border-radius:3px;\n"
"background:#C2CCD8;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal{\n"
"height:8px;\n"
"border-radius:3px;\n"
"background:#708090;\n"
"}\n"
"\n"
"QSlider::handle:horizontal{\n"
"width:13px;\n"
"margin-top:-3px;\n"
"margin-bottom:-3px;\n"
"border-radius:6px;\n"
"background:qradialgradient(spread:pad,cx:0.5,cy:0.5,radius:0.5,fx:0.5,fy:0.5,stop:0.6 #667481,stop:0.8 #778899);\n"
"}\n"
"\n"
"QSlider::groove:vertical,QSlider::sub-page:vertical{\n"
"width:8px;\n"
"border-radius:3px;\n"
"background:#C2CCD8;\n"
"}\n"
"\n"
"QSlider::add-page:vertical{\n"
"width:8px;\n"
"border-radius:3px;\n"
"background:#708090;\n"
"}\n"
"\n"
"QSlider::handle:vertical{\n"
"height:13px;\n"
"margin-left:-2px;\n"
"margin-right:-3px;\n"
"border-radius:6px;\n"
"background:qradialgradient(spread:pad,cx:0.5,cy:0.5,radius:0.5,fx:0.5,fy:0.5,stop:0.6 #667481,stop:0.8 #778899);\n"
"}\n"
"\n"
"QScrollBar:vertical{\n"
"width:10px;\n"
"background-color:rgba(0,0,0,0%);\n"
"padding-top:10px;\n"
"padding-bottom:10px;\n"
"}\n"
"\n"
"QScrollBar:horizontal{\n"
"height:10px;\n"
"background-color:rgba(0,0,0,0%);\n"
"padding-left:10px;\n"
"padding-right:10px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical,QScrollBar::handle:horizontal{\n"
"width:10px;\n"
"background:#708090;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover,QScrollBar::handle:horizontal:hover{\n"
"width:10px;\n"
"background:#566373;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical{\n"
"height:10px;\n"
"width:10px;\n"
"subcontrol-position:bottom;\n"
"subcontrol-origin:margin;\n"
"border-image:url(:/image/add_bottom.png);\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal{\n"
"height:10px;\n"
"width:10px;\n"
"subcontrol-position:right;\n"
"subcontrol-origin:margin;\n"
"border-image:url(:/image/add_right.png);\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical{\n"
"height:10px;\n"
"width:10px;\n"
"subcontrol-position:top;\n"
"subcontrol-origin:margin;\n"
"border-image:url(:/image/add_top.png);\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal{\n"
"height:10px;\n"
"width:10px;\n"
"subcontrol-position:left;\n"
"subcontrol-origin:margin;\n"
"border-image:url(:/image/add_left.png);\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical,QScrollBar::sub-page:vertical,QScrollBar::add-page:horizontal,QScrollBar::sub-page:horizontal{\n"
"width:10px;\n"
"background:#C2CCD8;\n"
"}\n"
"\n"
"QScrollArea{\n"
"border:0px;\n"
"}\n"
"\n"
"QTreeView,QListView,QTableView,QTabWidget::pane{\n"
"border:1px solid #C2CCD8;\n"
"selection-background-color:#778899;\n"
"selection-color:#E7ECF0;\n"
"alternate-background-color:#DDE0E7;\n"
"}\n"
"\n"
"QTableView::item:selected,QListView::item:selected,QTreeView::item:selected{\n"
"color:#E7ECF0;\n"
"background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #667481,stop:1 #566373);\n"
"}\n"
"\n"
"QTableView::item:hover,QListView::item:hover,QTreeView::item:hover{\n"
"color:#E7ECF0;\n"
"background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #778899,stop:1 #708090);\n"
"}\n"
"\n"
"QTableView::item,QListView::item,QTreeView::item{\n"
"padding:5px;\n"
"margin:0px;\n"
"}\n"
"\n"
"QHeaderView::section,QTableCornerButton:section{\n"
"padding:3px;\n"
"margin:0px;\n"
"color:#E7ECF0;\n"
"border:1px solid #C2CCD8;\n"
"background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #778899,stop:1 #708090);\n"
"}\n"
"\n"
"QTabBar::tab{\n"
"border-radius:5px;\n"
"border:1px solid #C2CCD8;\n"
"color:#E7ECF0;\n"
"min-width:55px;\n"
"min-height:20px;\n"
"padding:3px 8px 3px 8px;\n"
"margin:1px;\n"
"background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #778899,stop:1 #708090);\n"
"}\n"
"\n"
"QTabBar::tab:selected,QTabBar::tab:hover{\n"
"background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #667481,stop:1 #566373);\n"
"}\n"
"\n"
"QStatusBar::item{\n"
"border:0px solid #667481;\n"
"border-radius:3px;\n"
"}\n"
"\n"
"QToolBox::tab,QToolTip,QGroupBox#gboxDevicePanel{\n"
"padding:3px;\n"
"border-radius: 5px;\n"
"color:#E7ECF0;\n"
"background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #667481,stop:1 #566373);\n"
"}\n"
"\n"
"QToolBox::tab:selected{\n"
"background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #778899,stop:1 #708090);\n"
"}\n"
"")
        self.no_pushButton.setObjectName("no_pushButton")
        self.p_timeEdit = QtWidgets.QTimeEdit(Add_flight)
        self.p_timeEdit.setGeometry(QtCore.QRect(120, 130, 201, 31))
        self.p_timeEdit.setObjectName("p_timeEdit")
        self.date_label_4 = QtWidgets.QLabel(Add_flight)
        self.date_label_4.setGeometry(QtCore.QRect(30, 130, 71, 30))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.date_label_4.setFont(font)
        self.date_label_4.setStyleSheet("")
        self.date_label_4.setObjectName("date_label_4")
        self.a_timeEdit = QtWidgets.QTimeEdit(Add_flight)
        self.a_timeEdit.setGeometry(QtCore.QRect(120, 170, 201, 31))
        self.a_timeEdit.setObjectName("a_timeEdit")
        self.date_label_5 = QtWidgets.QLabel(Add_flight)
        self.date_label_5.setGeometry(QtCore.QRect(30, 170, 71, 30))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.date_label_5.setFont(font)
        self.date_label_5.setStyleSheet("")
        self.date_label_5.setObjectName("date_label_5")

        self.retranslateUi(Add_flight)
        self.no_pushButton.clicked.connect(Add_flight.reject)
        QtCore.QMetaObject.connectSlotsByName(Add_flight)

    def retranslateUi(self, Add_flight):
        _translate = QtCore.QCoreApplication.translate
        Add_flight.setWindowTitle(_translate("Add_flight", "Dialog"))
        self.date_label.setText(_translate("Add_flight", "?????????"))
        self.date_label_2.setText(_translate("Add_flight", "????????????"))
        self.date_label_3.setText(_translate("Add_flight", "?????????"))
        self.yes_pushButton.setText(_translate("Add_flight", "??????"))
        self.no_pushButton.setText(_translate("Add_flight", "??????"))
        self.date_label_4.setText(_translate("Add_flight", "????????????"))
        self.date_label_5.setText(_translate("Add_flight", "????????????"))

