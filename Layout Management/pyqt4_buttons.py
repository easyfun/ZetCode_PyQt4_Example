#!/usr/bin/python
# -*- coding:utf-8 -*-

import sys
from PyQt4 import QtGui

class Example(QtGui.QWidget):
	"""docstring for Example"""
	def __init__(self):
		super(Example, self).__init__()
		self.initUI()

	def initUI(self):
		okButton=QtGui.QPushButton('OK',self)
		cancelButton=QtGui.QPushButton('Cancel',self)

		hbox=QtGui.QHBoxLayout()
		hbox.addStretch(1)
		hbox.addWidget(okButton)
		hbox.addWidget(cancelButton)

		vbox=QtGui.QVBoxLayout()
		vbox.addStretch(1)
		vbox.addLayout(hbox)

		self.setLayout(vbox)
		self.setGeometry(300,300,300,150)
		self.setWindowTitle('Buttons')


def main():
	app=QtGui.QApplication(sys.argv)
	ex=Example()
	ex.show()
	sys.exit(app.exec_())

if __name__=='__main__':
	main()
		