#!/usr/bin/python
# -*- coding:utf-8 -*-

import sys
from PyQt4 import QtGui

class Example(QtGui.QMainWindow):
	def __init__(self):
		super(Example,self).__init__()
		self.initUI()

	def initUI(self):
		textEdit=QtGui.QTextEdit()
		self.setCentralWidget(textEdit)

		exeAction=QtGui.QAction(QtGui.QIcon('exit.png'),'Exit',self)
		exeAction.setShortcut('Ctrl+Q')
		exeAction.setStatusTip('Exit application')
		exeAction.triggered.connect(self.close)

		self.statusBar()

		menubar=self.menuBar()
		filemenu=menubar.addMenu('&File')
		filemenu.addAction(exeAction)

		toolbar=self.addToolBar('Exit')
		toolbar.addAction(exeAction)

		self.setGeometry(300,300,400,300)
		self.setWindowTitle('Main Window')



def main():
	app=QtGui.QApplication(sys.argv)
	ex=Example()
	ex.show()
	sys.exit(app.exec_())

if __name__=='__main__':
	main()