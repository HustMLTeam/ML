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
from PyQt4.QtGui import QMessageBox, QPixmap

import imageViewer


class ImageApp(QtGui.QMainWindow, imageViewer.Ui_MainWindow):
    def __init__(self, parent=None):
        super(self.__class__, self).__init__(parent)
        self.setupUi(self)
        self.action_Open.triggered.connect(self.openImage)
        self.action_Exit.triggered.connect(self.exitApp)
        
    def openImage(self):
        path = QtGui.QFileDialog.getOpenFileName(self, "Please Choose an Image")
        if path:
            try:
                assert imghdr.what(path)
                pixmap = QPixmap(path)
                scaled_pixmap = pixmap.scaled(self.labelImage.size(),
                                              QtCore.Qt.KeepAspectRatio)              
                self.labelImage.setPixmap(scaled_pixmap)
            except:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText("Can't open file {filename}".format(
                    filename = os.path.split(path)[1]))
                msg.setWindowTitle("Wrong!")
                msg.setStandardButtons(QMessageBox.Ok)
                msg.exec_()
    
    def exitApp(self):
        self.close()
        
        
def main():
    app = QtGui.QApplication(sys.argv)
    form = ImageApp()
    form.show()
    app.exec_()
    
    
if __name__ == '__main__':
    main()