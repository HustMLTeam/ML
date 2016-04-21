# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'imageViewer.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        MainWindow.showMaximized()
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.scrollArea = QtGui.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 780, 526))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.gridLayout_2 = QtGui.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.labelImage = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.labelImage.setLineWidth(1)
        self.labelImage.setText(_fromUtf8(""))
        self.labelImage.setAlignment(QtCore.Qt.AlignCenter)
        self.labelImage.setObjectName(_fromUtf8("labelImage"))
        self.gridLayout_2.addWidget(self.labelImage, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.line_x = QtGui.QLineEdit(self.centralwidget)
        self.line_x.setObjectName(_fromUtf8("line_x"))
        self.horizontalLayout.addWidget(self.line_x)
        self.line_y = QtGui.QLineEdit(self.centralwidget)
        self.line_y.setObjectName(_fromUtf8("line_y"))
        self.horizontalLayout.addWidget(self.line_y)
        self.line_w = QtGui.QLineEdit(self.centralwidget)
        self.line_w.setObjectName(_fromUtf8("line_w"))
        self.horizontalLayout.addWidget(self.line_w)
        self.line_h = QtGui.QLineEdit(self.centralwidget)
        self.line_h.setObjectName(_fromUtf8("line_h"))
        self.horizontalLayout.addWidget(self.line_h)
        self.btnDrawBox = QtGui.QPushButton(self.centralwidget)
        self.btnDrawBox.setObjectName(_fromUtf8("btnDrawBox"))
        self.horizontalLayout.addWidget(self.btnDrawBox)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menu_File = QtGui.QMenu(self.menubar)
        self.menu_File.setObjectName(_fromUtf8("menu_File"))
        self.menu_Help = QtGui.QMenu(self.menubar)
        self.menu_Help.setObjectName(_fromUtf8("menu_Help"))
        MainWindow.setMenuBar(self.menubar)
        self.action_Open = QtGui.QAction(MainWindow)
        self.action_Open.setObjectName(_fromUtf8("action_Open"))
        self.action_Exit = QtGui.QAction(MainWindow)
        self.action_Exit.setObjectName(_fromUtf8("action_Exit"))
        self.menu_File.addAction(self.action_Open)
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.action_Exit)
        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.menu_Help.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.line_x, QtCore.SIGNAL(_fromUtf8("returnPressed()")), self.btnDrawBox.click)
        QtCore.QObject.connect(self.line_y, QtCore.SIGNAL(_fromUtf8("returnPressed()")), self.btnDrawBox.click)
        QtCore.QObject.connect(self.line_w, QtCore.SIGNAL(_fromUtf8("returnPressed()")), self.btnDrawBox.click)
        QtCore.QObject.connect(self.line_h, QtCore.SIGNAL(_fromUtf8("returnPressed()")), self.btnDrawBox.click)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Image Viewer", None))
        self.line_x.setPlaceholderText(_translate("MainWindow", "起始点横坐标：x", None))
        self.line_y.setPlaceholderText(_translate("MainWindow", "起始点纵坐标：y", None))
        self.line_w.setPlaceholderText(_translate("MainWindow", "方框宽度：w", None))
        self.line_h.setPlaceholderText(_translate("MainWindow", "方框高度：h", None))
        self.btnDrawBox.setText(_translate("MainWindow", "DrawBox", None))
        self.menu_File.setTitle(_translate("MainWindow", "&File", None))
        self.menu_Help.setTitle(_translate("MainWindow", "&Help", None))
        self.action_Open.setText(_translate("MainWindow", "&Open", None))
        self.action_Exit.setText(_translate("MainWindow", "&Exit", None))

