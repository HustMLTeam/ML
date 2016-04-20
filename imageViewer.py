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
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.scrollArea = QtGui.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 780, 557))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.gridLayout_2 = QtGui.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.labelImage = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.labelImage.setLineWidth(1)
        self.labelImage.setText(_fromUtf8(""))
        self.labelImage.setAlignment(QtCore.Qt.AlignCenter)
        self.labelImage.setIndent(0)
        self.labelImage.setObjectName(_fromUtf8("labelImage"))
        self.gridLayout_2.addWidget(self.labelImage, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menu_File = QtGui.QMenu(self.menubar)
        self.menu_File.setObjectName(_fromUtf8("menu_File"))
        self.menu_View = QtGui.QMenu(self.menubar)
        self.menu_View.setObjectName(_fromUtf8("menu_View"))
        self.menu_Help = QtGui.QMenu(self.menubar)
        self.menu_Help.setObjectName(_fromUtf8("menu_Help"))
        MainWindow.setMenuBar(self.menubar)
        self.actionZoom_in = QtGui.QAction(MainWindow)
        self.actionZoom_in.setObjectName(_fromUtf8("actionZoom_in"))
        self.actionZoom_out = QtGui.QAction(MainWindow)
        self.actionZoom_out.setObjectName(_fromUtf8("actionZoom_out"))
        self.action_Normal_Size = QtGui.QAction(MainWindow)
        self.action_Normal_Size.setObjectName(_fromUtf8("action_Normal_Size"))
        self.actionFit_to_Window = QtGui.QAction(MainWindow)
        self.actionFit_to_Window.setObjectName(_fromUtf8("actionFit_to_Window"))
        self.action_About = QtGui.QAction(MainWindow)
        self.action_About.setObjectName(_fromUtf8("action_About"))
        self.action_Open = QtGui.QAction(MainWindow)
        self.action_Open.setObjectName(_fromUtf8("action_Open"))
        self.action_Exit = QtGui.QAction(MainWindow)
        self.action_Exit.setObjectName(_fromUtf8("action_Exit"))
        self.menu_File.addAction(self.action_Open)
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.action_Exit)
        self.menu_View.addAction(self.actionZoom_in)
        self.menu_View.addAction(self.actionZoom_out)
        self.menu_View.addAction(self.action_Normal_Size)
        self.menu_View.addAction(self.actionFit_to_Window)
        self.menu_Help.addAction(self.action_About)
        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.menu_View.menuAction())
        self.menubar.addAction(self.menu_Help.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Image Viewer", None))
        self.menu_File.setTitle(_translate("MainWindow", "&File", None))
        self.menu_View.setTitle(_translate("MainWindow", "&View", None))
        self.menu_Help.setTitle(_translate("MainWindow", "&Help", None))
        self.actionZoom_in.setText(_translate("MainWindow", "Zoom &In", None))
        self.actionZoom_out.setText(_translate("MainWindow", "Zoom &Out", None))
        self.action_Normal_Size.setText(_translate("MainWindow", "&Normal Size", None))
        self.actionFit_to_Window.setText(_translate("MainWindow", "Fit to &Window", None))
        self.action_About.setText(_translate("MainWindow", "&About", None))
        self.action_Open.setText(_translate("MainWindow", "&Open", None))
        self.action_Exit.setText(_translate("MainWindow", "&Exit", None))

