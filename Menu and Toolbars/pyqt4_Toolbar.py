#!/usr/bin/python
# -*- coding:utf-8 -*-

import sys
from PyQt4 import QtGui

#默认支持停靠和悬浮
class Example(QtGui.QMainWindow):
	def __init__(self):
		super(Example,self).__init__()
		self.initUI()

	def initUI(self):
		exeAction=QtGui.QAction(QtGui.QIcon('exit.png'),'Exit',self)
		exeAction.setShortcut('Ctrl+Q')
		exeAction.triggered.connect(QtGui.qApp.quit)

		self.toolbar=self.addToolBar('Exit')
		self.toolbar.addAction(exeAction)

		self.setGeometry(300,300,300,200)
		self.setWindowTitle('Toobar')


def main():
	app=QtGui.QApplication(sys.argv)
	ex=Example()
	ex.show()
	sys.exit(app.exec_())

if __name__=='__main__':
	main()