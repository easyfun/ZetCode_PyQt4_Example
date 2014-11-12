#!/usr/bin/python
# -*- coding:utf-8 -*-

import sys
from PyQt4 import QtGui,QtCore

class Example(QtGui.QWidget):
	def __init__(self):
		super(Example,self).__init__()
		self.initUI()

	def initUI(self):
		qbtn=QtGui.QPushButton('Quit',self)
		qbtn.resize(qbtn.sizeHint())
		qbtn.move(50,50)
		qbtn.clicked.connect(QtCore.QCoreApplication.instance().quit)

		self.setGeometry(300,300,250,150)
		self.setWindowTitle('Quit button')

	def closeEvent(self,event):
		reply=QtGui.QMessageBox.question(self,'Message','Are you sure to quit?',
			QtGui.QMessageBox.Yes|QtGui.QMessageBox.No,QtGui.QMessageBox.No)
		if reply==QtGui.QMessageBox.Yes:
			event.accept()
		else:
			event.ignore()

def main():
	app=QtGui.QApplication(sys.argv)
	ex=Example()
	ex.show()
	sys.exit(app.exec_())

if __name__ == '__main__':
	main()