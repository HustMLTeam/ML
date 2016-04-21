# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 23:19:52 2016

@author: 逸川
"""
import sys
import os
import imghdr

from PyQt4 import QtCore
from PyQt4 import QtGui
from PyQt4.QtGui import QMessageBox, QPixmap, QPainter, QPen

import imageViewer


class ImageApp(QtGui.QMainWindow, imageViewer.Ui_MainWindow):
    def __init__(self, parent=None):
        super(self.__class__, self).__init__(parent)
        self.setupUi(self)
        self.action_Open.triggered.connect(self.openImage)
        self.action_Exit.triggered.connect(self.exitApp)
        self.btnDrawBox.clicked.connect(self.drawBox)
        self.pixmap = None
        
    def showErrMsg(self, text=None, infoText=None):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        if text:
            msg.setText(str(text))
        if infoText:
            msg.setInformativeText(str(infoText))
        msg.setWindowTitle('Error!')
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()
        
    def openImage(self):
        path = QtGui.QFileDialog.getOpenFileName(self, "Choose an Image")
        if path:
            try:
                assert imghdr.what(path), 'Not an image'
                self.pixmap = QPixmap(path)
                self.pixmap = self.pixmap.scaled(self.labelImage.size(),
                                              QtCore.Qt.KeepAspectRatio)
                self.labelImage.setPixmap(self.pixmap)
            except Exception as e:
                text = "Can't open file {filename}".format(
                    filename = os.path.split(path)[1])
                info = str(e)
                self.showErrMsg(text, info)
                
    def drawBox(self):
        '''handle errors'''
        if not self.pixmap:
            self.showErrMsg('Please choose an image first!')
            return
            
        x, y, w, h = self.line_x.text(), self.line_y.text(), self.line_w.text(),\
            self.line_h.text()
        if not (x.isdigit() and y.isdigit() and w.isdigit() and h.isdigit()):
            self.showErrMsg('Please input integer!')
            return
        
        x, y, w, h = int(x), int(y), int(w), int(h)
        if not 0 <= x <= self.pixmap.width():
            self.showErrMsg('Value Error', 'x should be an integer between 0 and %d' 
                % self.pixmap.width())
            return
        if not 0 <= y <= self.pixmap.height():
            self.showErrMsg('Value Error', 'y should be an integer between 0 and %d'
                % self.pixmap.height())
            return
        if not 0 <= w <= (self.pixmap.width() - x):
            self.showErrMsg('Value Error', 'x+w should be an integer between 0 and %d'
                % self.pixmap.width())
            return
        if not 0 <= h <= (self.pixmap.height() - y):
            self.showErrMsg('Value Error', 'y+h should be an integer between 0 and %d'
                % self.pixmap.height())
            return
        
        painter = QPainter()
        painter.begin(self.pixmap)
        pen = QPen(QtCore.Qt.red, 5, QtCore.Qt.SolidLine)
        painter.setPen(pen)
        painter.drawRect(x, y, w, h)
        painter.end()
        self.labelImage.setPixmap(self.pixmap)
    
    def exitApp(self):
        self.close()
        
        
def main():
    app = QtGui.QApplication(sys.argv)
    form = ImageApp()
    form.show()
    sys.exit(app.exec_())
    
    
if __name__ == '__main__':
    main()