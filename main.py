# -*- coding:utf-8 -*-

import sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QWidget, QStackedWidget, QTableWidgetItem, QPushButton, \
    QMessageBox, QHeaderView
from PyQt5.QtGui import QPixmap, QPainter
from sip import settracemask
from interface.Ui_adminwindow import Ui_AdminWindow
from interface.Ui_mainwindow import Ui_MainWindow
from interface.Ui_userwindow import Ui_UserWindow
from interface.Ui_Flight_detail import Ui_Flight_detail
from interface.Ui_booking_show import Ui_booing_show
import pyodbc
from datetime import date
import interface.material_rc


def connectdatabase():
    # 连接数据库
    global cnxn, cursor
    cnxn = pyodbc.connect('DRIVER={SQL Server};'
                          'SERVER=localhost\\SQLEXPRESS;'
                          'DATABASE=Ticket_reservation;'
                          'UID=sa;'
                          'PWD=11235813')
    if cnxn:
        cursor = cnxn.cursor()
        return True
    else:
        return False


class MainWindows(QMainWindow, Ui_MainWindow):
    loginwhether = False
    adminlogin = True

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.login_radioButton.setChecked(True)
        self.name_label.hide()
        self.name_lineEdit.hide()
        self.tel_num_label.hide()
        self.tel_num_lineEdit.hide()
        self.setWindowTitle('航空机票预订系统')

        if connectdatabase():
            QtCore.qDebug('Connect database Success!')
        else:
            QMessageBox.about(self, "提示", "无法连接到数据库")

        self.login_radioButton.clicked.connect(self.login_radioButton_clicked)
        self.signup_radioButton.clicked.connect(
            self.signup_radioButton_clicked)
        self.login_signup_pushButton.clicked.connect(
            self.login_signup_pushButton_clicked)
        self.admin_login_pushButton.clicked.connect(
            self.admin_login_pushButton_clicked)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setOpacity(0.9)
        pixmap = QPixmap(":/image/images/background.jpg")
        # 绘制窗口背景，平铺到整个窗口，随着窗口改变而改变
        painter.drawPixmap(self.rect(), pixmap)

    def clearall(self):
        self.tel_num_lineEdit.clear()
        self.name_lineEdit.clear()
        self.Uname_lineEdit.clear()
        self.passwd_lineEdit.clear()

    def login_radioButton_clicked(self):
        self.clearall()
        self.admin_login_pushButton.show()

        if self.loginwhether:
            self.loginwhether = False

            self.login_signup_pushButton.setText('登录')
            self.name_label.hide()
            self.name_lineEdit.hide()
            self.tel_num_label.hide()
            self.tel_num_lineEdit.hide()

    def signup_radioButton_clicked(self):
        self.clearall()
        self.admin_login_pushButton.hide()

        if not self.loginwhether:
            self.loginwhether = True

            self.login_signup_pushButton.setText('注册')
            self.name_label.show()
            self.name_lineEdit.show()
            self.tel_num_label.show()
            self.tel_num_lineEdit.show()

    def admin_login_pushButton_clicked(self):

        self.clearall()
        if self.admin_login_pushButton.text() == "管理员登录":
            self.signup_radioButton.hide()
            self.login_signup_pushButton.setText("管理员登录")
            self.admin_login_pushButton.setText("用户登录")
            self.Uname_label.setText("管理员账号:")
            self.passwd_label.setText("管理员密码:")
            self.name_label.hide()
            self.name_lineEdit.hide()
            self.tel_num_label.hide()
            self.tel_num_lineEdit.hide()
        elif self.admin_login_pushButton.text() == "用户登录":
            self.signup_radioButton.show()
            self.login_signup_pushButton.setText("登录")
            self.admin_login_pushButton.setText("管理员登录")
            self.Uname_label.setText("用户名:")
            self.passwd_label.setText("密码:")
            self.name_label.hide()
            self.name_lineEdit.hide()
            self.tel_num_label.hide()
            self.tel_num_lineEdit.hide()

    def login_signup_pushButton_clicked(self):
        global Uname

        if self.login_signup_pushButton.text() == "登录":

            if not (self.Uname_lineEdit.text() and self.passwd_lineEdit.text()):
                QMessageBox.warning(self, "错误", "输入不能为空")
                self.Uname_lineEdit.setFocus()
            else:
                # 执行查找用户名和密码的存储过程
                cursor.execute("SELECT [Uname] FROM [User] WHERE [Uname] = '{0}' AND [Passwd] = '{1}'".format(
                    self.Uname_lineEdit.text(), self.passwd_lineEdit.text()))
                exist = cursor.fetchall()
                # 如果数据库中存在该用户，则exist为真，否则为空
                if exist:
                    Uname = self.Uname_lineEdit.text()
                    QMessageBox.about(self, "提示", "登陆成功")
                    self.close()
                    self.uw = UserWindow()
                    self.uw.setWindowTitle("用户机票管理")
                    self.uw.show()
                else:
                    QMessageBox.warning(self, "错误", '用户名或密码错误')
                    self.Uname_lineEdit.clear()
                    self.passwd_lineEdit.clear()
                    self.Uname_lineEdit.setFocus()

        elif self.login_signup_pushButton.text() == "管理员登录":
            if not (self.Uname_lineEdit.text() and self.passwd_lineEdit.text()):
                QMessageBox.warning(self, "错误", "输入不能为空")
                self.Uname_lineEdit.setFocus()
            else:
                cursor.execute("SELECT [Uname] FROM [User] WHERE [Uname] = '{0}' AND [Passwd] = '{1}'".format(
                    self.Uname_lineEdit.text(), self.passwd_lineEdit.text()))
                exist = cursor.fetchall()
                # 如果数据库中存在该管理员，则exist为真，否则为空
                if exist and self.Uname_lineEdit.text() == 'admin':
                    Uname = self.Uname_lineEdit.text()
                    QMessageBox.about(self, "提示", "登陆成功")
                    self.close()
                    self.aw = AdminWindow()
                    self.aw.setWindowTitle("系统管理员")
                    self.aw.show()
                else:
                    QMessageBox.warning(self, "错误", '用户名或密码错误')
                    self.Uname_lineEdit.clear()
                    self.passwd_lineEdit.clear()
                    self.Uname_lineEdit.setFocus()
        elif self.login_signup_pushButton.text() == "注册":
            if not (self.Uname_lineEdit.text() and self.passwd_lineEdit.text()):
                QMessageBox.warning(self, "错误", "用户名和密码不能为空")
                self.Uname_lineEdit.setFocus()
            else:
                cursor.execute("SELECT [Uname] FROM [User] WHERE [Uname] = '{0}'".format(
                    self.Uname_lineEdit.text()))
                rows = cursor.fetchall()
                if rows:
                    QMessageBox.warning(self, "错误", "该用户名已存在")
                else:
                    cursor.execute("INSERT INTO [User]([Uname],[Passwd],[Phone],[Name]) VALUES('{0}', '{1}','{2}','{3}')".format(
                        self.Uname_lineEdit.text(), self.passwd_lineEdit.text(), self.tel_num_lineEdit.text(), self.name_lineEdit.text()))
                    # 提交数据进入数据库
                    cnxn.commit()
                    QMessageBox.about(self, "成功", "注册成功")
                    self.clearall()
                    self.login_radioButton.setChecked(True)
                    self.login_radioButton_clicked()


class UserWindow(QWidget, Ui_UserWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # 弹出日历
        self.date_dateEdit.setCalendarPopup(True)
        self.date_dateEdit_2.setCalendarPopup(True)

        # 设置为当前日期
        currentdate = QtCore.QDate.currentDate()
        self.date_dateEdit.setDate(currentdate)
        self.date_dateEdit_2.setDate(currentdate)

        self.ticket_tableWidget.setColumnHidden(9, True)

        # 使行列头自适应宽度
        self.flight_tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ticket_tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.order_cen_tableWidget.horizontalHeader(
        ).setSectionResizeMode(QHeaderView.Stretch)
        self.passenger_tableWidget.horizontalHeader(
        ).setSectionResizeMode(QHeaderView.Stretch)

        self.order_show()
        self.my_home_show()

        # 切换界面
        self.menu_my_home_pushButton.clicked.connect(
            self.menu_my_home_pushButton_clicked)
        self.menu_order_pushButton.clicked.connect(
            self.menu_order_pushButton_clicked)
        self.menu_passenger_pushButton.clicked.connect(
            self.menu_passenger_pushButton_clicked)
        self.menu_flight_pushButton.clicked.connect(
            self.menu_flight_pushButton_clicked)
        self.menu_ticket_pushButton.clicked.connect(
            self.menu_ticket_pushButton_clicked)

        # 退出按钮
        self.logout_pushButton.clicked.connect(self.logout_pushButton_clicked)

        self.flight_search_pushButton_2.clicked.connect(
            self.flight_search_pushButton_2_clicked)
        self.flight_search_pushButton.clicked.connect(
            self.flight_search_pushButton_clicked)

        self.order_comboBox.currentIndexChanged.connect(
            self.order_comboBox_currentIndexChanged)

        self.ticket_tableWidget.doubleClicked.connect(
            self.ticket_tableWidget_doubleclicked)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setOpacity(0.9)
        pixmap = QPixmap(":/image/images/userbackground1.jpg")
        # 绘制窗口背景，平铺到整个窗口，随着窗口改变而改变
        painter.drawPixmap(self.rect(), pixmap)

    def menu_my_home_pushButton_clicked(self):
        self.my_home_show()
        self.stackedWidget.setCurrentWidget(self.my_home_page)

    def menu_order_pushButton_clicked(self):
        self.order_show()
        self.stackedWidget.setCurrentWidget(self.order_page)

    def menu_passenger_pushButton_clicked(self):
        self.passenger_show()
        self.stackedWidget.setCurrentWidget(self.passenger_page)

    def menu_flight_pushButton_clicked(self):
        self.stackedWidget.setCurrentWidget(self.flight_page)

    def menu_ticket_pushButton_clicked(self):
        self.stackedWidget.setCurrentWidget(self.ticket_page)

    def logout_pushButton_clicked(self):
        reply = QMessageBox.question(
            self, "提示", "是否退出登录", QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.close()
            self.mw = MainWindows()
            self.mw.setWindowTitle("航空机票预订系统")
            self.mw.show()

    def flight_search_pushButton_2_clicked(self):
        if self.flight_no_search_radioButton_2.isChecked():
            if not self.flight_no_lineEdit_2.text():
                QMessageBox.warning(self, "错误", "请输入航班号！")
            else:
                cursor.execute(
                    "select * from [Flight] WHERE [Flight_NO]='{0}'".format(self.flight_no_lineEdit_2.text()))
                rows = cursor.fetchall()
                if not rows:
                    QMessageBox.warning(self, "错误", "请输入正确的航班号！")
                else:
                    cursor.execute(
                        "select * from [Ticket] WHERE [Plan_departuredate] = '{0}' AND [航班号1]='{1}' AND [Cabin_type] = '{2}' order by [Plan_departuretime],[Plan_arrivaltime]".format(self.date_dateEdit_2.date().toString('yyyy-MM-dd'), self.flight_no_lineEdit_2.text(), self.cabin_comboBox.currentText()))
                    rows = cursor.fetchall()

                    self.ticket_tableWidget.clearContents()
                    self.ticket_tableWidget.setRowCount(len(rows))
                    for index, row in enumerate(rows):
                        newItem = QTableWidgetItem(row.Airline+' '+row.航班号1)
                        newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                        self.ticket_tableWidget.setItem(index, 0, newItem)
                        newItem = QTableWidgetItem(
                            row.Plan_departuretime.strftime('%H:%M'))
                        newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                        self.ticket_tableWidget.setItem(index, 1, newItem)
                        newItem = QTableWidgetItem(
                            row.Plan_arrivaltime.strftime('%H:%M'))
                        newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                        self.ticket_tableWidget.setItem(index, 2, newItem)
                        newItem = QTableWidgetItem(
                            row.出发城市+row.起飞机场名+row.Departure_teminal)
                        newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                        self.ticket_tableWidget.setItem(index, 3, newItem)
                        newItem = QTableWidgetItem(
                            row.到达城市+row.到达机场名+row.Arrival_teminal)
                        newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                        self.ticket_tableWidget.setItem(index, 4, newItem)
                        newItem = QTableWidgetItem(str(row.降落准点率)+'%')
                        newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                        self.ticket_tableWidget.setItem(index, 5, newItem)
                        newItem = QTableWidgetItem(row.Cabin_type)
                        newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                        self.ticket_tableWidget.setItem(index, 6, newItem)
                        newItem = QTableWidgetItem(str(row.Price))
                        newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                        self.ticket_tableWidget.setItem(index, 7, newItem)

                        newItem = QTableWidgetItem(row.行程号)
                        newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                        self.ticket_tableWidget.setItem(index, 9, newItem)

                        # 加入购票按钮
                        book_f = QPushButton()
                        book_f.setText('预订')
                        book_f.clicked.connect(self.book_f_clicked)
                        self.ticket_tableWidget.setCellWidget(index, 8, book_f)
                    self.ticket_tableWidget.horizontalHeader().setSectionResizeMode(0,
                                                                                    QHeaderView.ResizeToContents)
                    self.ticket_tableWidget.horizontalHeader().setSectionResizeMode(1,
                                                                                    QHeaderView.ResizeToContents)
                    self.ticket_tableWidget.horizontalHeader().setSectionResizeMode(2,
                                                                                    QHeaderView.ResizeToContents)
                    self.ticket_tableWidget.horizontalHeader().setSectionResizeMode(3,
                                                                                    QHeaderView.ResizeToContents)
                    self.ticket_tableWidget.horizontalHeader().setSectionResizeMode(4,
                                                                                    QHeaderView.ResizeToContents)

        elif self.city_search_radioButton_2.isChecked():
            if not (self.depcity_lineEdit_2.text() and self.arrcity_lineEdit_2.text()):
                QMessageBox.warning(self, "错误", "请输入起降地！")
            else:
                cursor.execute(
                    "select * from [Airport] WHERE [City] ='{0}'".format(self.depcity_lineEdit_2.text()))
                rows1 = cursor.fetchall()
                cursor.execute(
                    "select * from [Airport] WHERE [City] ='{0}'".format(self.arrcity_lineEdit_2.text()))
                rows2 = cursor.fetchall()
                if not rows1:
                    QMessageBox.warning(self, "错误", "请输入正确的出发城市！")
                    self.depcity_lineEdit_2.clear()
                    self.depcity_lineEdit_2.setFocus()
                elif not rows2:
                    QMessageBox.warning(self, "错误", "请输入正确的到达城市！")
                    self.arrcity_lineEdit_2.clear()
                    self.arrcity_lineEdit_2.setFocus()
                else:
                    cursor.execute(
                        "select * from [Ticket] WHERE [Plan_departuredate] = '{0}' AND [出发城市]='{1}' AND [到达城市] = '{2}' AND [Cabin_type] = '{3}' order by [Plan_departuretime],[Plan_arrivaltime]".format(self.date_dateEdit_2.date().toString('yyyy-MM-dd'), self.depcity_lineEdit_2.text(), self.arrcity_lineEdit_2.text(), self.cabin_comboBox.currentText()))
                    rows = cursor.fetchall()

                    self.ticket_tableWidget.clearContents()
                    self.ticket_tableWidget.setRowCount(len(rows))
                    for index, row in enumerate(rows):
                        newItem = QTableWidgetItem(row.Airline+' '+row.航班号1)
                        newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                        self.ticket_tableWidget.setItem(index, 0, newItem)
                        newItem = QTableWidgetItem(
                            row.Plan_departuretime.strftime('%H:%M'))
                        newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                        self.ticket_tableWidget.setItem(index, 1, newItem)
                        newItem = QTableWidgetItem(
                            row.Plan_arrivaltime.strftime('%H:%M'))
                        newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                        self.ticket_tableWidget.setItem(index, 2, newItem)
                        newItem = QTableWidgetItem(
                            row.出发城市+row.起飞机场名+row.Departure_teminal)
                        newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                        self.ticket_tableWidget.setItem(index, 3, newItem)
                        newItem = QTableWidgetItem(
                            row.到达城市+row.到达机场名+row.Arrival_teminal)
                        newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                        self.ticket_tableWidget.setItem(index, 4, newItem)
                        newItem = QTableWidgetItem(str(row.降落准点率)+'%')
                        newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                        self.ticket_tableWidget.setItem(index, 5, newItem)
                        newItem = QTableWidgetItem(row.Cabin_type)
                        newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                        self.ticket_tableWidget.setItem(index, 6, newItem)
                        newItem = QTableWidgetItem(str(row.Price))
                        newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                        self.ticket_tableWidget.setItem(index, 7, newItem)

                        newItem = QTableWidgetItem(row.行程号)
                        newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                        self.ticket_tableWidget.setItem(index, 9, newItem)

                        # 加入购票按钮
                        book_f = QPushButton()
                        book_f.setText('预订')
                        book_f.clicked.connect(self.book_f_clicked)
                        self.ticket_tableWidget.setCellWidget(index, 8, book_f)
                    self.ticket_tableWidget.horizontalHeader().setSectionResizeMode(0,
                                                                                    QHeaderView.ResizeToContents)
                    self.ticket_tableWidget.horizontalHeader().setSectionResizeMode(1,
                                                                                    QHeaderView.ResizeToContents)
                    self.ticket_tableWidget.horizontalHeader().setSectionResizeMode(2,
                                                                                    QHeaderView.ResizeToContents)
                    self.ticket_tableWidget.horizontalHeader().setSectionResizeMode(3,
                                                                                    QHeaderView.ResizeToContents)
                    self.ticket_tableWidget.horizontalHeader().setSectionResizeMode(4,
                                                                                    QHeaderView.ResizeToContents)

    def flight_search_pushButton_clicked(self):
        if self.flight_no_search_radioButton.isChecked():
            if not self.flight_no_lineEdit.text():
                QMessageBox.warning(self, "错误", "请输入航班号！")
            else:
                cursor.execute(
                    "select * from [Flight] WHERE [Flight_NO]='{0}'".format(self.flight_no_lineEdit.text()))
                rows = cursor.fetchall()
                if not rows:
                    QMessageBox.warning(self, "错误", "请输入正确的航班号！")
                else:
                    cursor.execute(
                        "select * from [Flights] WHERE [Plan_departuredate] = '{0}' AND [航班号]='{1}' order by [Plan_departuretime],[Plan_arrivaltime]".format(self.date_dateEdit.date().toString('yyyy-MM-dd'), self.flight_no_lineEdit.text()))
                    rows = cursor.fetchall()

                    self.flight_tableWidget.clearContents()
                    self.flight_tableWidget.setRowCount(len(rows))
                    for index, row in enumerate(rows):
                        newItem = QTableWidgetItem(row.Airline+' '+row.航班号)
                        newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                        self.flight_tableWidget.setItem(index, 0, newItem)
                        newItem = QTableWidgetItem(
                            row.Plan_departuretime.strftime('%H:%M'))
                        newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                        self.flight_tableWidget.setItem(index, 1, newItem)
                        newItem = QTableWidgetItem(
                            row.Plan_arrivaltime.strftime('%H:%M'))
                        newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                        self.flight_tableWidget.setItem(index, 2, newItem)
                        newItem = QTableWidgetItem(
                            row.出发城市+row.出发机场名+row.Departure_teminal)
                        newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                        self.flight_tableWidget.setItem(index, 3, newItem)
                        newItem = QTableWidgetItem(
                            row.到达城市+row.到达机场名+row.Arrival_teminal)
                        newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                        self.flight_tableWidget.setItem(index, 4, newItem)
                        newItem = QTableWidgetItem(row.Flight_status)
                        newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                        self.flight_tableWidget.setItem(index, 5, newItem)
        elif self.city_search_radioButton.isChecked():
            if not (self.depcity_lineEdit.text() and self.arrcity_lineEdit.text()):
                QMessageBox.warning(self, "错误", "请输入起降地！")
            else:
                cursor.execute(
                    "select * from [Airport] WHERE [City] ='{0}'".format(self.depcity_lineEdit.text()))
                rows1 = cursor.fetchall()
                cursor.execute(
                    "select * from [Airport] WHERE [City] ='{0}'".format(self.arrcity_lineEdit.text()))
                rows2 = cursor.fetchall()
                if not rows1:
                    QMessageBox.warning(self, "错误", "请输入正确的出发城市！")
                    self.depcity_lineEdit.clear()
                    self.depcity_lineEdit.setFocus()
                elif not rows2:
                    QMessageBox.warning(self, "错误", "请输入正确的到达城市！")
                    self.arrcity_lineEdit.clear()
                    self.arrcity_lineEdit.setFocus()
                else:
                    cursor.execute(
                        "select * from [Flights] WHERE [Plan_departuredate] = '{0}' AND [出发城市]='{1}' AND [到达城市] = '{2}' order by [Plan_departuretime],[Plan_arrivaltime]".format(self.date_dateEdit.date().toString('yyyy-MM-dd'), self.depcity_lineEdit.text(), self.arrcity_lineEdit.text()))
                    rows = cursor.fetchall()

                    self.flight_tableWidget.clearContents()
                    self.flight_tableWidget.setRowCount(len(rows))
                    for index, row in enumerate(rows):
                        newItem = QTableWidgetItem(row.Airline+' '+row.航班号)
                        newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                        self.flight_tableWidget.setItem(index, 0, newItem)
                        newItem = QTableWidgetItem(
                            row.Plan_departuretime.strftime('%H:%M'))
                        newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                        self.flight_tableWidget.setItem(index, 1, newItem)
                        newItem = QTableWidgetItem(
                            row.Plan_arrivaltime.strftime('%H:%M'))
                        newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                        self.flight_tableWidget.setItem(index, 2, newItem)
                        newItem = QTableWidgetItem(
                            row.出发城市+row.出发机场名+row.Departure_teminal)
                        newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                        self.flight_tableWidget.setItem(index, 3, newItem)
                        newItem = QTableWidgetItem(
                            row.到达城市+row.到达机场名+row.Arrival_teminal)
                        newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                        self.flight_tableWidget.setItem(index, 4, newItem)
                        newItem = QTableWidgetItem(row.Flight_status)
                        newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                        self.flight_tableWidget.setItem(index, 5, newItem)

    def order_show(self):
        cursor.execute(
            "select * from [Order_Detail] WHERE [Uname] = '{0}' order by [Order_time] DESC".format(Uname))
        rows = cursor.fetchall()
        self.order_cen_tableWidget.clearContents()
        self.order_cen_tableWidget.setRowCount(len(rows))
        for index, row in enumerate(rows):
            newItem = QTableWidgetItem(row.Order_id)
            newItem.setTextAlignment(QtCore.Qt.AlignCenter)
            self.order_cen_tableWidget.setItem(index, 0, newItem)
            newItem = QTableWidgetItem(row.Airline+' '+row.航班号)
            newItem.setTextAlignment(QtCore.Qt.AlignCenter)
            self.order_cen_tableWidget.setItem(index, 1, newItem)
            newItem = QTableWidgetItem(
                row.Plan_departuretime.strftime('%Y-%m-%d %H:%M'))
            newItem.setTextAlignment(QtCore.Qt.AlignCenter)
            self.order_cen_tableWidget.setItem(index, 2, newItem)
            newItem = QTableWidgetItem(
                row.Order_time.strftime('%Y-%m-%d %H:%M'))
            newItem.setTextAlignment(QtCore.Qt.AlignCenter)
            self.order_cen_tableWidget.setItem(index, 3, newItem)
            newItem = QTableWidgetItem(str(row.Order_pay))
            newItem.setTextAlignment(QtCore.Qt.AlignCenter)
            self.order_cen_tableWidget.setItem(index, 4, newItem)
            newItem = QTableWidgetItem(row.Order_status)
            newItem.setTextAlignment(QtCore.Qt.AlignCenter)
            self.order_cen_tableWidget.setItem(index, 5, newItem)

    def order_comboBox_currentIndexChanged(self):
        if self.order_comboBox.currentText() == '全部订单':
            self.order_show()
        elif self.order_comboBox.currentText() == '未出行':
            cursor.execute(
                "select * from [Order_Detail] WHERE [Uname] = '{0}' AND DATEDIFF(hh,GETDATE(),[Plan_departuretime]) > 0 order by [Order_time] DESC".format(Uname))
            rows = cursor.fetchall()
            self.order_cen_tableWidget.clearContents()
            self.order_cen_tableWidget.setRowCount(len(rows))
            for index, row in enumerate(rows):
                newItem = QTableWidgetItem(row.Order_id)
                newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                self.order_cen_tableWidget.setItem(index, 0, newItem)
                newItem = QTableWidgetItem(row.Airline+' '+row.航班号)
                newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                self.order_cen_tableWidget.setItem(index, 1, newItem)
                newItem = QTableWidgetItem(
                    row.Plan_departuretime.strftime('%Y-%m-%d %H:%M'))
                newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                self.order_cen_tableWidget.setItem(index, 2, newItem)
                newItem = QTableWidgetItem(
                    row.Order_time.strftime('%Y-%m-%d %H:%M'))
                newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                self.order_cen_tableWidget.setItem(index, 3, newItem)
                newItem = QTableWidgetItem(str(row.Order_pay))
                newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                self.order_cen_tableWidget.setItem(index, 4, newItem)
                newItem = QTableWidgetItem(row.Order_status)
                newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                self.order_cen_tableWidget.setItem(index, 5, newItem)
        elif self.order_comboBox.currentText() == '未付款':
            cursor.execute(
                "select * from [Order_Detail] WHERE [Uname] = '{0}' AND [Order_status] = '未支付' order by [Order_time] DESC".format(Uname))
            rows = cursor.fetchall()
            self.order_cen_tableWidget.clearContents()
            self.order_cen_tableWidget.setRowCount(len(rows))
            for index, row in enumerate(rows):
                newItem = QTableWidgetItem(row.Order_id)
                newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                self.order_cen_tableWidget.setItem(index, 0, newItem)
                newItem = QTableWidgetItem(row.Airline+' '+row.航班号)
                newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                self.order_cen_tableWidget.setItem(index, 1, newItem)
                newItem = QTableWidgetItem(
                    row.Plan_departuretime.strftime('%Y-%m-%d %H:%M'))
                newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                self.order_cen_tableWidget.setItem(index, 2, newItem)
                newItem = QTableWidgetItem(
                    row.Order_time.strftime('%Y-%m-%d %H:%M'))
                newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                self.order_cen_tableWidget.setItem(index, 3, newItem)
                newItem = QTableWidgetItem(str(row.Order_pay))
                newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                self.order_cen_tableWidget.setItem(index, 4, newItem)
                newItem = QTableWidgetItem(row.Order_status)
                newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                self.order_cen_tableWidget.setItem(index, 5, newItem)

    def my_home_show(self):
        cursor.execute(
            "select * from [User] WHERE [Uname] = '{0}'".format(Uname))
        rows = cursor.fetchall()
        self.Uname_lineEdit.setText(rows[0].Uname)
        self.passwd_lineEdit.setText(rows[0].Passwd)
        self.name_lineEdit.setText(rows[0].Name)
        self.phone_lineEdit.setText(rows[0].Phone)
        self.email_lineEdit.setText(rows[0].Email)
        self.sex_comboBox.setCurrentText(rows[0].Sex)

    def passenger_show(self):
        cursor.execute(
            "select * from [Passenger] WHERE [Uname] = '{0}'".format(Uname))
        rows = cursor.fetchall()
        self.passenger_tableWidget.clearContents()
        self.passenger_tableWidget.setRowCount(len(rows))
        for index, row in enumerate(rows):
            newItem = QTableWidgetItem(row.Pname)
            newItem.setTextAlignment(QtCore.Qt.AlignCenter)
            self.passenger_tableWidget.setItem(index, 1, newItem)
            newItem = QTableWidgetItem(row.IDCard_NO)
            newItem.setTextAlignment(QtCore.Qt.AlignCenter)
            self.passenger_tableWidget.setItem(index, 2, newItem)

            # 插入复选框
            check = QTableWidgetItem()
            check.setCheckState(QtCore.Qt.Unchecked)
            self.passenger_tableWidget.setItem(index, 0, check)

        self.passenger_tableWidget.horizontalHeader().setSectionResizeMode(0,
                                                                           QHeaderView.ResizeToContents)

    def ticket_tableWidget_doubleclicked(self):
        col = self.ticket_tableWidget.selectedItems()[0].column()
        row = self.ticket_tableWidget.selectedItems()[0].row()
        if col == 0:
            self.fd = Flight_detail(self.ticket_tableWidget.item(
                row, 9).text(), self.ticket_tableWidget.selectedItems()[0].text())
            self.fd.setWindowTitle('航班详情')
            self.fd.exec_()

    def book_f_clicked(self):
        sender = self.sender()
        index = self.ticket_tableWidget.indexAt(sender.pos())

        self.bs = Book_show(self.ticket_tableWidget.item(
            index.row(), 9).text(), self.ticket_tableWidget.item(index.row(), 7).text())
        self.bs.exec_()


class AdminWindow(QWidget, Ui_AdminWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # 弹出日历
        self.date_dateEdit.setCalendarPopup(True)
        self.date_dateEdit_2.setCalendarPopup(True)

        # 设置为当前日期
        currentdate = QtCore.QDate.currentDate()
        self.date_dateEdit.setDate(currentdate)
        self.date_dateEdit_2.setDate(currentdate)

        # 使行列头自适应宽度
        self.flight_tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ticket_tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.order_tableWidget.horizontalHeader(
        ).setSectionResizeMode(QHeaderView.Stretch)

        self.flight_no_search_radioButton.setChecked(True)
        self.flight_no_search_radioButton_2.setChecked(True)

        self.date_dateEdit.hide()
        self.date_dateEdit_2.hide()
        self.date_label.hide()
        self.date_label_2.hide()

        self.menu_flight_pushButton.clicked.connect(
            self.menu_flight_pushButton_clicked)
        self.menu_order_pushButton.clicked.connect(
            self.menu_order_pushButton_clicked)
        self.menu_ticket_pushButton.clicked.connect(
            self.menu_ticket_pushButton_clicked)

        self.logout_pushButton.clicked.connect(self.logout_pushButton_clicked)

        self.flight_search_pushButton.clicked.connect(
            self.flight_search_pushButton_clicked)
        self.ticket_pushButton.clicked.connect(self.ticket_pushButton_clicked)

        self.order_search_pushButton.clicked.connect(
            self.order_search_pushButton_clicked)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setOpacity(0.9)
        pixmap = QPixmap(":/image/images/adminbackground.jpg")
        # 绘制窗口背景，平铺到整个窗口，随着窗口改变而改变
        painter.drawPixmap(self.rect(), pixmap)

    def menu_order_pushButton_clicked(self):
        self.stackedWidget.setCurrentWidget(self.order_page)

    def menu_ticket_pushButton_clicked(self):
        self.stackedWidget.setCurrentWidget(self.ticket_page)

    def menu_flight_pushButton_clicked(self):
        self.stackedWidget.setCurrentWidget(self.flight_page)

    def logout_pushButton_clicked(self):
        reply = QMessageBox.question(
            self, "提示", "是否退出登录", QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.close()
            self.mw = MainWindows()
            self.mw.setWindowTitle("航空机票预订系统")
            self.mw.show()

    def flight_search_pushButton_clicked(self):
        if self.flight_no_search_radioButton.isChecked():
            if not self.flight_no_lineEdit.text():
                QMessageBox.warning(self, "错误", "请输入航班号！")
            else:
                cursor.execute(
                    "select * from [Flight] WHERE [Flight_NO]='{0}'".format(self.flight_no_lineEdit.text()))
                rows = cursor.fetchall()
                if not rows:
                    QMessageBox.warning(self, "错误", "请输入正确的航班号！")
                else:
                    cursor.execute(
                        "select * from [Flights] WHERE [航班号]='{0}' order by [Plan_departuretime],[Plan_arrivaltime]".format(self.flight_no_lineEdit.text()))
                    rows = cursor.fetchall()

                    self.flight_tableWidget.clearContents()
                    self.flight_tableWidget.setRowCount(len(rows))
                    for index, row in enumerate(rows):
                        newItem = QTableWidgetItem(row.Airline+' '+row.航班号)
                        newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                        self.flight_tableWidget.setItem(index, 1, newItem)
                        newItem = QTableWidgetItem(
                            row.Plan_departuretime.strftime('%Y-%m-%d %H:%M'))
                        newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                        self.flight_tableWidget.setItem(index, 2, newItem)
                        newItem = QTableWidgetItem(
                            row.Departuretime.strftime('%Y-%m-%d %H:%M'))
                        newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                        self.flight_tableWidget.setItem(index, 3, newItem)
                        newItem = QTableWidgetItem(
                            row.Plan_arrivaltime.strftime('%Y-%m-%d %H:%M'))
                        newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                        self.flight_tableWidget.setItem(index, 4, newItem)
                        newItem = QTableWidgetItem(
                            row.Arrivaltime.strftime('%Y-%m-%d %H:%M'))
                        newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                        self.flight_tableWidget.setItem(index, 5, newItem)
                        newItem = QTableWidgetItem(str(row.Mileage))
                        newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                        self.flight_tableWidget.setItem(index, 6, newItem)
                        newItem = QTableWidgetItem(str(row.Plane_NO))
                        newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                        self.flight_tableWidget.setItem(index, 7, newItem)
                        newItem = QTableWidgetItem(
                            row.出发城市+row.出发机场名+row.Departure_teminal)
                        newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                        self.flight_tableWidget.setItem(index, 8, newItem)
                        newItem = QTableWidgetItem(
                            row.到达城市+row.到达机场名+row.Arrival_teminal)
                        newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                        self.flight_tableWidget.setItem(index, 9, newItem)
                        newItem = QTableWidgetItem(row.Flight_status)
                        newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                        self.flight_tableWidget.setItem(index, 10, newItem)

                        # 插入复选框
                        check = QTableWidgetItem()
                        check.setCheckState(QtCore.Qt.Unchecked)
                        self.flight_tableWidget.setItem(index, 0, check)

                    self.flight_tableWidget.horizontalHeader().setSectionResizeMode(0,
                                                                                    QHeaderView.ResizeToContents)
                    self.flight_tableWidget.horizontalHeader().setSectionResizeMode(1,
                                                                                    QHeaderView.ResizeToContents)
                    self.flight_tableWidget.horizontalHeader().setSectionResizeMode(2,
                                                                                    QHeaderView.ResizeToContents)
                    self.flight_tableWidget.horizontalHeader().setSectionResizeMode(3,
                                                                                    QHeaderView.ResizeToContents)
                    self.flight_tableWidget.horizontalHeader().setSectionResizeMode(4,
                                                                                    QHeaderView.ResizeToContents)
                    self.flight_tableWidget.horizontalHeader().setSectionResizeMode(5,
                                                                                    QHeaderView.ResizeToContents)

        elif self.flight_date_search_radioButton.isChecked():
            cursor.execute(
                "select * from [Flights] WHERE [Plan_departuredate] = '{0}' order by [Plan_departuretime],[Plan_arrivaltime]".format(self.date_dateEdit.date().toString('yyyy-MM-dd')))
            rows = cursor.fetchall()

            self.flight_tableWidget.clearContents()
            self.flight_tableWidget.setRowCount(len(rows))
            for index, row in enumerate(rows):
                newItem = QTableWidgetItem(row.Airline+' '+row.航班号)
                newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                self.flight_tableWidget.setItem(index, 1, newItem)
                newItem = QTableWidgetItem(
                    row.Plan_departuretime.strftime('%Y-%m-%d %H:%M'))
                newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                self.flight_tableWidget.setItem(index, 2, newItem)
                newItem = QTableWidgetItem(
                    row.Departuretime.strftime('%Y-%m-%d %H:%M'))
                newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                self.flight_tableWidget.setItem(index, 3, newItem)
                newItem = QTableWidgetItem(
                    row.Plan_arrivaltime.strftime('%Y-%m-%d %H:%M'))
                newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                self.flight_tableWidget.setItem(index, 4, newItem)
                newItem = QTableWidgetItem(
                    row.Arrivaltime.strftime('%Y-%m-%d %H:%M'))
                newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                self.flight_tableWidget.setItem(index, 5, newItem)
                newItem = QTableWidgetItem(str(row.Mileage))
                newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                self.flight_tableWidget.setItem(index, 6, newItem)
                newItem = QTableWidgetItem(str(row.Plane_NO))
                newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                self.flight_tableWidget.setItem(index, 7, newItem)
                newItem = QTableWidgetItem(
                    row.出发城市+row.出发机场名+row.Departure_teminal)
                newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                self.flight_tableWidget.setItem(index, 8, newItem)
                newItem = QTableWidgetItem(
                    row.到达城市+row.到达机场名+row.Arrival_teminal)
                newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                self.flight_tableWidget.setItem(index, 9, newItem)
                newItem = QTableWidgetItem(row.Flight_status)
                newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                self.flight_tableWidget.setItem(index, 10, newItem)
                # 插入复选框
                check = QTableWidgetItem()
                check.setCheckState(QtCore.Qt.Unchecked)
                self.flight_tableWidget.setItem(index, 0, check)

            self.flight_tableWidget.horizontalHeader().setSectionResizeMode(0,
                                                                            QHeaderView.ResizeToContents)
            self.flight_tableWidget.horizontalHeader().setSectionResizeMode(1,
                                                                            QHeaderView.ResizeToContents)
            self.flight_tableWidget.horizontalHeader().setSectionResizeMode(2,
                                                                            QHeaderView.ResizeToContents)
            self.flight_tableWidget.horizontalHeader().setSectionResizeMode(3,
                                                                            QHeaderView.ResizeToContents)
            self.flight_tableWidget.horizontalHeader().setSectionResizeMode(4,
                                                                            QHeaderView.ResizeToContents)
            self.flight_tableWidget.horizontalHeader().setSectionResizeMode(5,
                                                                            QHeaderView.ResizeToContents)

    def ticket_pushButton_clicked(self):
        if self.flight_no_search_radioButton_2.isChecked():
            if not self.flight_no_lineEdit_2.text():
                QMessageBox.warning(self, "错误", "请输入航班号！")
            else:
                cursor.execute(
                    "select * from [Flight] WHERE [Flight_NO]='{0}'".format(self.flight_no_lineEdit_2.text()))
                rows = cursor.fetchall()
                if not rows:
                    QMessageBox.warning(self, "错误", "请输入正确的航班号！")
                else:
                    cursor.execute(
                        "select * from [Ticket] WHERE [航班号1]='{0}' order by [Plan_departuretime],[Plan_arrivaltime]".format(self.flight_no_lineEdit_2.text()))
                    rows = cursor.fetchall()

                    self.ticket_tableWidget.clearContents()
                    self.ticket_tableWidget.setRowCount(len(rows))
                    for index, row in enumerate(rows):
                        newItem = QTableWidgetItem(row.Airline+' '+row.航班号1)
                        newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                        self.ticket_tableWidget.setItem(index, 1, newItem)
                        newItem = QTableWidgetItem(
                            row.Plan_departuretime.strftime('%Y-%m-%d %H:%M'))
                        newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                        self.ticket_tableWidget.setItem(index, 2, newItem)
                        newItem = QTableWidgetItem(
                            row.Plan_arrivaltime.strftime('%Y-%m-%d %H:%M'))
                        newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                        self.ticket_tableWidget.setItem(index, 3, newItem)
                        newItem = QTableWidgetItem(
                            row.出发城市+row.起飞机场名+row.Departure_teminal)
                        newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                        self.ticket_tableWidget.setItem(index, 4, newItem)
                        newItem = QTableWidgetItem(
                            row.到达城市+row.到达机场名+row.Arrival_teminal)
                        newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                        self.ticket_tableWidget.setItem(index, 5, newItem)
                        newItem = QTableWidgetItem(row.飞机号)
                        newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                        self.ticket_tableWidget.setItem(index, 6, newItem)
                        newItem = QTableWidgetItem(row.舱位代码)
                        newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                        self.ticket_tableWidget.setItem(index, 7, newItem)
                        newItem = QTableWidgetItem(str(row.Price))
                        newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                        self.ticket_tableWidget.setItem(index, 8, newItem)
                        newItem = QTableWidgetItem(str(row.remaining))
                        newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                        self.ticket_tableWidget.setItem(index, 9, newItem)

                        # 插入复选框
                        check = QTableWidgetItem()
                        check.setCheckState(QtCore.Qt.Unchecked)
                        self.ticket_tableWidget.setItem(index, 0, check)

                    self.ticket_tableWidget.horizontalHeader().setSectionResizeMode(0,
                                                                                    QHeaderView.ResizeToContents)
                    self.ticket_tableWidget.horizontalHeader().setSectionResizeMode(1,
                                                                                    QHeaderView.ResizeToContents)
                    self.ticket_tableWidget.horizontalHeader().setSectionResizeMode(2,
                                                                                    QHeaderView.ResizeToContents)
                    self.ticket_tableWidget.horizontalHeader().setSectionResizeMode(3,
                                                                                    QHeaderView.ResizeToContents)
                    self.ticket_tableWidget.horizontalHeader().setSectionResizeMode(4,
                                                                                    QHeaderView.ResizeToContents)

        elif self.flight_date_search_radioButton_2.isChecked():
            cursor.execute(
                "select * from [Ticket] WHERE [Plan_departuredate] = '{0}' order by [Plan_departuretime],[Plan_arrivaltime]".format(self.date_dateEdit_2.date().toString('yyyy-MM-dd')))
            rows = cursor.fetchall()

            self.ticket_tableWidget.clearContents()
            self.ticket_tableWidget.setRowCount(len(rows))
            for index, row in enumerate(rows):
                newItem = QTableWidgetItem(row.Airline+' '+row.航班号1)
                newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                self.ticket_tableWidget.setItem(index, 1, newItem)
                newItem = QTableWidgetItem(
                    row.Plan_departuretime.strftime('%Y-%m-%d %H:%M'))
                newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                self.ticket_tableWidget.setItem(index, 2, newItem)
                newItem = QTableWidgetItem(
                    row.Plan_arrivaltime.strftime('%Y-%m-%d %H:%M'))
                newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                self.ticket_tableWidget.setItem(index, 3, newItem)
                newItem = QTableWidgetItem(
                    row.出发城市+row.起飞机场名+row.Departure_teminal)
                newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                self.ticket_tableWidget.setItem(index, 4, newItem)
                newItem = QTableWidgetItem(
                    row.到达城市+row.到达机场名+row.Arrival_teminal)
                newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                self.ticket_tableWidget.setItem(index, 5, newItem)
                newItem = QTableWidgetItem(row.飞机号)
                newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                self.ticket_tableWidget.setItem(index, 6, newItem)
                newItem = QTableWidgetItem(row.舱位代码)
                newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                self.ticket_tableWidget.setItem(index, 7, newItem)
                newItem = QTableWidgetItem(str(row.Price))
                newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                self.ticket_tableWidget.setItem(index, 8, newItem)
                newItem = QTableWidgetItem(str(row.remaining))
                newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                self.ticket_tableWidget.setItem(index, 9, newItem)

                # 插入复选框
                check = QTableWidgetItem()
                check.setCheckState(QtCore.Qt.Unchecked)
                self.ticket_tableWidget.setItem(index, 0, check)

            self.ticket_tableWidget.horizontalHeader().setSectionResizeMode(0,
                                                                            QHeaderView.ResizeToContents)
            self.ticket_tableWidget.horizontalHeader().setSectionResizeMode(1,
                                                                            QHeaderView.ResizeToContents)
            self.ticket_tableWidget.horizontalHeader().setSectionResizeMode(2,
                                                                            QHeaderView.ResizeToContents)
            self.ticket_tableWidget.horizontalHeader().setSectionResizeMode(3,
                                                                            QHeaderView.ResizeToContents)
            self.ticket_tableWidget.horizontalHeader().setSectionResizeMode(4,
                                                                            QHeaderView.ResizeToContents)

    def order_search_pushButton_clicked(self):
        if not self.order_num_lineEdit.text():
            QMessageBox.warning(self, "错误", "请输入订单号！")
            self.order_num_lineEdit.setFocus()
        else:
            cursor.execute(
                "select * from [Order_Detail] WHERE [Order_id] = '{0}' order by [Order_time] DESC".format(self.order_num_lineEdit.text()))
            rows = cursor.fetchall()
            if not rows:
                QMessageBox.warning(self, "错误", "请输入正确的订单号！")
                self.order_num_lineEdit.clear()
                self.order_num_lineEdit.setFocus()
            else:
                self.order_tableWidget.clearContents()
                self.order_tableWidget.setRowCount(len(rows))
                for index, row in enumerate(rows):
                    newItem = QTableWidgetItem(row.Order_id)
                    newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                    self.order_tableWidget.setItem(index, 1, newItem)
                    newItem = QTableWidgetItem(row.Airline+' '+row.航班号)
                    newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                    self.order_tableWidget.setItem(index, 2, newItem)
                    newItem = QTableWidgetItem(row.Contact_Phone)
                    newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                    self.order_tableWidget.setItem(index, 3, newItem)
                    newItem = QTableWidgetItem(row.Uname)
                    newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                    self.order_tableWidget.setItem(index, 4, newItem)
                    newItem = QTableWidgetItem(
                        row.Plan_departuretime.strftime('%Y-%m-%d %H:%M'))
                    newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                    self.order_tableWidget.setItem(index, 5, newItem)
                    newItem = QTableWidgetItem(
                        row.Plan_arrivaltime.strftime('%Y-%m-%d %H:%M'))
                    newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                    self.order_tableWidget.setItem(index, 6, newItem)
                    newItem = QTableWidgetItem(
                        row.出发城市+row.起飞机场名+row.Departure_teminal)
                    newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                    self.order_tableWidget.setItem(index, 7, newItem)
                    newItem = QTableWidgetItem(
                        row.到达城市+row.到达机场名+row.Arrival_teminal)
                    newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                    self.order_tableWidget.setItem(index, 8, newItem)
                    newItem = QTableWidgetItem(str(row.Order_pay))
                    newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                    self.order_tableWidget.setItem(index, 9, newItem)
                    newItem = QTableWidgetItem(
                        row.Order_time.strftime('%Y-%m-%d %H:%M'))
                    newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                    self.order_tableWidget.setItem(index, 10, newItem)
                    newItem = QTableWidgetItem(row.Order_status)
                    newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                    self.order_tableWidget.setItem(index, 11, newItem)

                    # 插入复选框
                    check = QTableWidgetItem()
                    check.setCheckState(QtCore.Qt.Unchecked)
                    self.order_tableWidget.setItem(index, 0, check)

                self.order_tableWidget.horizontalHeader().setSectionResizeMode(0,
                                                                               QHeaderView.ResizeToContents)
                self.order_tableWidget.horizontalHeader().setSectionResizeMode(1,
                                                                               QHeaderView.ResizeToContents)
                self.order_tableWidget.horizontalHeader().setSectionResizeMode(2,
                                                                               QHeaderView.ResizeToContents)
                self.order_tableWidget.horizontalHeader().setSectionResizeMode(3,
                                                                               QHeaderView.ResizeToContents)
                self.order_tableWidget.horizontalHeader().setSectionResizeMode(5,
                                                                               QHeaderView.ResizeToContents)
                self.order_tableWidget.horizontalHeader().setSectionResizeMode(6,
                                                                               QHeaderView.ResizeToContents)
                self.order_tableWidget.horizontalHeader().setSectionResizeMode(7,
                                                                               QHeaderView.ResizeToContents)
                self.order_tableWidget.horizontalHeader().setSectionResizeMode(8,
                                                                               QHeaderView.ResizeToContents)


class Flight_detail(QDialog, Ui_Flight_detail):
    def __init__(self, itinerary_id, flight_info):
        super().__init__()
        self.setupUi(self)

        self.flight_info_label.setText(flight_info)

        cursor.execute(
            "select [Flight_NO],[Plane_NO] from [Itinerary] WHERE [Itinerary_id] = '{0}'".format(itinerary_id))
        rows = cursor.fetchall()
        Flight_NO = rows[0].Flight_NO
        Plane_NO = rows[0].Plane_NO
        cursor.execute(
            "select * from [Flight_Detail] WHERE [航班号] = '{0}'".format(Flight_NO))
        rows = cursor.fetchall()
        self.dep_prate_label_2.setText(str(rows[0].出发准点率)+'%')
        self.arr_prate_label_2.setText(str(rows[0].降落准点率)+'%')
        self.dep_time_label_2.setText(str(rows[0].出发平均延误时间)+'分钟')
        self.arr_time_label_2.setText(str(rows[0].降落平均延误时间)+'分钟')

        cursor.execute(
            "select * from [Airplane] WHERE [Plane_NO] = '{0}'".format(Plane_NO))
        rows = cursor.fetchall()

        self.model_label_2.setText(rows[0].Plane_model)
        self.type_label_2.setText(rows[0].Plane_type)


class Book_show(QDialog, Ui_booing_show):
    def __init__(self, itinerary_id, price):
        super().__init__()
        self.setupUi(self)

        self.price = price
        self.Itinerary_id=itinerary_id

        cursor.execute(
            "select * from [Ticket] WHERE [行程号] = '{0}' AND [Price] = '{1}' ".format(itinerary_id, price))
        row = cursor.fetchall()[0]
        self.datetime_label.setText(
            row.Plan_departuretime.strftime('%m月%d日 %H:%M出发'))
        self.cabin_type_label.setText(row.Cabin_type)
        self.flight_info_label.setText(row.Airline+' '+row.航班号1)
        self.pay_label.setText('￥'+price)
        self.city_label.setText(row.出发城市+'—'+row.到达城市)

        self.cabin_code=row.舱位代码

        cursor.execute(
            "select * from [Passenger] WHERE [Uname] = '{0}'".format(Uname))
        rows = cursor.fetchall()

        self.passenger_tableWidget.horizontalHeader(
        ).setSectionResizeMode(QHeaderView.Stretch)
        self.passenger_tableWidget.clearContents()
        self.passenger_tableWidget.setRowCount(len(rows))
        for index, row in enumerate(rows):
            newItem = QTableWidgetItem(row.Pname)
            newItem.setTextAlignment(QtCore.Qt.AlignCenter)
            self.passenger_tableWidget.setItem(index, 1, newItem)
            newItem = QTableWidgetItem(row.IDCard_NO)
            newItem.setTextAlignment(QtCore.Qt.AlignCenter)
            self.passenger_tableWidget.setItem(index, 2, newItem)

            # 插入复选框
            check = QTableWidgetItem()
            check.setCheckState(QtCore.Qt.Unchecked)

            self.passenger_tableWidget.setItem(index, 0, check)

        self.passenger_tableWidget.horizontalHeader().setSectionResizeMode(0,
                                                                           QHeaderView.ResizeToContents)

        self.passenger_tableWidget.cellClicked.connect(
            self.passenger_tableWidget_cellclicked)
        self.yes_pushButton.clicked.connect(self.yes_pushButton_clicked)

    def passenger_tableWidget_cellclicked(self, row, col):
        if col == 0:
            self.cnt = 0
            for i in range(self.passenger_tableWidget.rowCount()):
                if self.passenger_tableWidget.item(i, 0).checkState():
                    self.cnt = self.cnt+1
            if self.cnt:
                self.pay_label.setText('￥'+str(self.cnt*int(self.price)))
            else:
                self.pay_label.setText('￥'+self.price)

    def yes_pushButton_clicked(self):
        if not self.tel_num_lineEdit.text():
            QMessageBox.warning(self, "错误", "请输入联系人！")
            self.tel_num_lineEdit.setFocus()
        elif self.cnt == 0:
            QMessageBox.warning(self, "错误", "请选择乘客！")
        else:
            sql="DECLARE @Order_id char(12),@Passenger People;"
            for i in range(self.passenger_tableWidget.rowCount()):
                if self.passenger_tableWidget.item(i, 0).checkState():
                    sql+="INSERT INTO @Passenger VALUES ('{0}','{1}');".format(self.passenger_tableWidget.item(i, 2).text(),self.passenger_tableWidget.item(i, 1).text())
            sql+="EXEC [Create_Order] {0}, @Passenger, {1},'{2}', '{3}','{4}', @Order_id OUTPUT;".format(self.pay_label.text(),self.tel_num_lineEdit.text(),self.Itinerary_id,self.cabin_code,Uname)
            print(sql)
            cursor.execute(sql)
            cursor.commit()
            self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    main = MainWindows()
    main.show()
    sys.exit(app.exec_())
