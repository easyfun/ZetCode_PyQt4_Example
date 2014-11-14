#!/usr/bin/python
# -*- coding:utf-8 -*-

import sys
from PyQt4 import QtGui

class Example(QtGui.QWidget):
	"""docstring for Example"""
	def __init__(self):
		super(Example,self).__init__()
		self.initUI()

	def initUI(self):
		pass

def main():
	app=QtGui.QApplication(sys.argv)
	ex=Example()
	ex.show()
	sys.exit(app.exec_())

if __name__=='__main__':
	main()
		