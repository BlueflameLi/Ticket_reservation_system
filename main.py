# -*- coding:utf-8 -*-

import sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QStackedWidget, QTableWidgetItem, QPushButton, \
    QMessageBox, QHeaderView
from PyQt5.QtGui import QPixmap, QPainter
from sip import settracemask
from interface.Ui_adminwindow import Ui_AdminWindow
from interface.Ui_mainwindow import Ui_MainWindow
from interface.Ui_userwindow import Ui_UserWindow
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

        self.login_radioButton.clicked.connect(self.login_radioButton_clicked)
        self.signup_radioButton.clicked.connect(
            self.signup_radioButton_clicked)
        self.login_signup_pushButton.clicked.connect(self.login_signup_pushButton_clicked)
        self.admin_login_pushButton.clicked.connect(self.admin_login_pushButton_clicked)

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
        if self.admin_login_pushButton.text()=="管理员登录":
            self.signup_radioButton.hide()
            self.login_signup_pushButton.setText("管理员登录")
            self.admin_login_pushButton.setText("用户登录")
            self.Uname_label.setText("管理员账号:")
            self.passwd_label.setText("管理员密码:")
            self.name_label.hide()
            self.name_lineEdit.hide()
            self.tel_num_label.hide()
            self.tel_num_lineEdit.hide()
        elif self.admin_login_pushButton.text()== "用户登录":
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
                        self.Uname_lineEdit.text(), self.passwd_lineEdit.text(),self.tel_num_lineEdit.text(),self.name_lineEdit.text()))
                    # 提交数据进入数据库
                    cnxn.commit()
                    QMessageBox.about(self, "成功", "注册成功")
                    self.clearall()
                    self.login_radioButton.setChecked(True)
                    self.login_radioButton_clicked()


class UserWindow(QWidget,Ui_UserWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.date_dateEdit.setCalendarPopup(True)
        self.date_dateEdit.setDate(QtCore.QDate.currentDate())
    
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setOpacity(0.9)
        pixmap = QPixmap(":/image/images/userbackground1.jpg")
        # 绘制窗口背景，平铺到整个窗口，随着窗口改变而改变
        painter.drawPixmap(self.rect(), pixmap)
    
class AdminWindow(QWidget,Ui_AdminWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.flight_date_dateEdit.setCalendarPopup(True)
        self.flight_date_dateEdit.setDate(QtCore.QDate.currentDate())

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setOpacity(0.9)
        pixmap = QPixmap(":/image/images/adminbackground.jpg")
        # 绘制窗口背景，平铺到整个窗口，随着窗口改变而改变
        painter.drawPixmap(self.rect(), pixmap)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    if connectdatabase():
        QtCore.qDebug('Connect database Success!')
    else:
        QMessageBox.about(None, "提示", "无法连接到数据库")

    main = MainWindows()
    main.show()
    sys.exit(app.exec_())
