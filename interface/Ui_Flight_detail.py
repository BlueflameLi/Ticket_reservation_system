# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e:\OI\sql\ui\Flight_detail.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Flight_detail(object):
    def setupUi(self, Flight_detail):
        Flight_detail.setObjectName("Flight_detail")
        Flight_detail.resize(400, 206)
        self.type_label_2 = QtWidgets.QLabel(Flight_detail)
        self.type_label_2.setGeometry(QtCore.QRect(310, 170, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.type_label_2.setFont(font)
        self.type_label_2.setObjectName("type_label_2")
        self.flight_info_label = QtWidgets.QLabel(Flight_detail)
        self.flight_info_label.setGeometry(QtCore.QRect(40, 60, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.flight_info_label.setFont(font)
        self.flight_info_label.setObjectName("flight_info_label")
        self.model_label_2 = QtWidgets.QLabel(Flight_detail)
        self.model_label_2.setGeometry(QtCore.QRect(130, 170, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.model_label_2.setFont(font)
        self.model_label_2.setObjectName("model_label_2")
        self.arr_prate_label = QtWidgets.QLabel(Flight_detail)
        self.arr_prate_label.setGeometry(QtCore.QRect(60, 140, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.arr_prate_label.setFont(font)
        self.arr_prate_label.setObjectName("arr_prate_label")
        self.model_label = QtWidgets.QLabel(Flight_detail)
        self.model_label.setGeometry(QtCore.QRect(20, 170, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.model_label.setFont(font)
        self.model_label.setObjectName("model_label")
        self.type_label = QtWidgets.QLabel(Flight_detail)
        self.type_label.setGeometry(QtCore.QRect(250, 170, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.type_label.setFont(font)
        self.type_label.setObjectName("type_label")
        self.dep_time_label = QtWidgets.QLabel(Flight_detail)
        self.dep_time_label.setGeometry(QtCore.QRect(210, 110, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.dep_time_label.setFont(font)
        self.dep_time_label.setObjectName("dep_time_label")
        self.flight_label = QtWidgets.QLabel(Flight_detail)
        self.flight_label.setGeometry(QtCore.QRect(10, 10, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.flight_label.setFont(font)
        self.flight_label.setScaledContents(False)
        self.flight_label.setObjectName("flight_label")
        self.arr_time_label_2 = QtWidgets.QLabel(Flight_detail)
        self.arr_time_label_2.setGeometry(QtCore.QRect(290, 140, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.arr_time_label_2.setFont(font)
        self.arr_time_label_2.setObjectName("arr_time_label_2")
        self.deo_label = QtWidgets.QLabel(Flight_detail)
        self.deo_label.setGeometry(QtCore.QRect(20, 110, 31, 21))
        self.deo_label.setAutoFillBackground(False)
        self.deo_label.setStyleSheet("background-color = rgba(183, 226, 255, 153)")
        self.deo_label.setObjectName("deo_label")
        self.dep_prate_label = QtWidgets.QLabel(Flight_detail)
        self.dep_prate_label.setGeometry(QtCore.QRect(60, 110, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.dep_prate_label.setFont(font)
        self.dep_prate_label.setObjectName("dep_prate_label")
        self.dep_prate_label_2 = QtWidgets.QLabel(Flight_detail)
        self.dep_prate_label_2.setGeometry(QtCore.QRect(130, 110, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.dep_prate_label_2.setFont(font)
        self.dep_prate_label_2.setObjectName("dep_prate_label_2")
        self.arr_prate_label_2 = QtWidgets.QLabel(Flight_detail)
        self.arr_prate_label_2.setGeometry(QtCore.QRect(130, 140, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.arr_prate_label_2.setFont(font)
        self.arr_prate_label_2.setObjectName("arr_prate_label_2")
        self.arr_time_label = QtWidgets.QLabel(Flight_detail)
        self.arr_time_label.setGeometry(QtCore.QRect(210, 140, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.arr_time_label.setFont(font)
        self.arr_time_label.setObjectName("arr_time_label")
        self.dep_time_label_2 = QtWidgets.QLabel(Flight_detail)
        self.dep_time_label_2.setGeometry(QtCore.QRect(290, 110, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.dep_time_label_2.setFont(font)
        self.dep_time_label_2.setObjectName("dep_time_label_2")
        self.arr_label = QtWidgets.QLabel(Flight_detail)
        self.arr_label.setGeometry(QtCore.QRect(20, 140, 31, 21))
        self.arr_label.setAutoFillBackground(False)
        self.arr_label.setStyleSheet("")
        self.arr_label.setObjectName("arr_label")

        self.retranslateUi(Flight_detail)
        QtCore.QMetaObject.connectSlotsByName(Flight_detail)

    def retranslateUi(self, Flight_detail):
        _translate = QtCore.QCoreApplication.translate
        Flight_detail.setWindowTitle(_translate("Flight_detail", "Dialog"))
        self.type_label_2.setText(_translate("Flight_detail", "input2"))
        self.flight_info_label.setText(_translate("Flight_detail", "航空信息"))
        self.model_label_2.setText(_translate("Flight_detail", "input1"))
        self.arr_prate_label.setText(_translate("Flight_detail", "准点率："))
        self.model_label.setText(_translate("Flight_detail", "计划机型："))
        self.type_label.setText(_translate("Flight_detail", "类型："))
        self.dep_time_label.setText(_translate("Flight_detail", "平均延误："))
        self.flight_label.setText(_translate("Flight_detail", "航班信息"))
        self.arr_time_label_2.setText(_translate("Flight_detail", "input4_2"))
        self.deo_label.setText(_translate("Flight_detail", "出发"))
        self.dep_prate_label.setText(_translate("Flight_detail", "准点率："))
        self.dep_prate_label_2.setText(_translate("Flight_detail", "input3"))
        self.arr_prate_label_2.setText(_translate("Flight_detail", "input3_2"))
        self.arr_time_label.setText(_translate("Flight_detail", "平均延误："))
        self.dep_time_label_2.setText(_translate("Flight_detail", "input4"))
        self.arr_label.setText(_translate("Flight_detail", "到达"))
