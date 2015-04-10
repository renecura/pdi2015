# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwin.ui'
#
# Created: Fri Apr 10 10:26:08 2015
#      by: PyQt4 UI code generator 4.10.4
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
        MainWindow.resize(742, 582)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.imgA = QtGui.QGraphicsView(self.centralwidget)
        self.imgA.setObjectName(_fromUtf8("imgA"))
        self.verticalLayout.addWidget(self.imgA)
        self.loadImgA = QtGui.QPushButton(self.centralwidget)
        self.loadImgA.setObjectName(_fromUtf8("loadImgA"))
        self.verticalLayout.addWidget(self.loadImgA)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_2.addWidget(self.label_2)
        self.imgB = QtGui.QGraphicsView(self.centralwidget)
        self.imgB.setObjectName(_fromUtf8("imgB"))
        self.verticalLayout_2.addWidget(self.imgB)
        self.loadImgB = QtGui.QPushButton(self.centralwidget)
        self.loadImgB.setObjectName(_fromUtf8("loadImgB"))
        self.verticalLayout_2.addWidget(self.loadImgB)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout_3.addWidget(self.label_3)
        self.imgC = QtGui.QGraphicsView(self.centralwidget)
        self.imgC.setObjectName(_fromUtf8("imgC"))
        self.verticalLayout_3.addWidget(self.imgC)
        self.calcular = QtGui.QPushButton(self.centralwidget)
        self.calcular.setObjectName(_fromUtf8("calcular"))
        self.verticalLayout_3.addWidget(self.calcular)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.operacion = QtGui.QComboBox(self.centralwidget)
        self.operacion.setObjectName(_fromUtf8("operacion"))
        self.verticalLayout_4.addWidget(self.operacion)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 742, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpenImgA = QtGui.QAction(MainWindow)
        self.actionOpenImgA.setObjectName(_fromUtf8("actionOpenImgA"))
        self.actionOpenImgB = QtGui.QAction(MainWindow)
        self.actionOpenImgB.setObjectName(_fromUtf8("actionOpenImgB"))
        self.actionOperate = QtGui.QAction(MainWindow)
        self.actionOperate.setObjectName(_fromUtf8("actionOperate"))

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.loadImgA, QtCore.SIGNAL(_fromUtf8("clicked()")), self.actionOpenImgA.trigger)
        QtCore.QObject.connect(self.loadImgB, QtCore.SIGNAL(_fromUtf8("clicked()")), self.actionOpenImgB.trigger)
        QtCore.QObject.connect(self.calcular, QtCore.SIGNAL(_fromUtf8("clicked()")), self.actionOperate.trigger)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Operador Imágenes", None))
        self.label.setText(_translate("MainWindow", "Imagen A", None))
        self.loadImgA.setText(_translate("MainWindow", "Cargar A", None))
        self.label_2.setText(_translate("MainWindow", "Imagen B", None))
        self.loadImgB.setText(_translate("MainWindow", "Cargar B", None))
        self.label_3.setText(_translate("MainWindow", "Imagen C", None))
        self.calcular.setText(_translate("MainWindow", "Calcular", None))
        self.actionOpenImgA.setText(_translate("MainWindow", "openImgA", None))
        self.actionOpenImgB.setText(_translate("MainWindow", "openImgB", None))
        self.actionOperate.setText(_translate("MainWindow", "operate", None))

