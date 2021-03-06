# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'estacionamento.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(949, 687)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color: rgb(138, 138, 138);\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btnBuscarCarro = QtWidgets.QPushButton(self.centralwidget)
        self.btnBuscarCarro.setGeometry(QtCore.QRect(440, 530, 121, 51))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btnBuscarCarro.setFont(font)
        self.btnBuscarCarro.setStyleSheet("background:rgb(238, 238, 238)")
        self.btnBuscarCarro.setObjectName("btnBuscarCarro")
        self.btnGerarRelatorio = QtWidgets.QPushButton(self.centralwidget)
        self.btnGerarRelatorio.setGeometry(QtCore.QRect(0, 10, 141, 51))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btnGerarRelatorio.setFont(font)
        self.btnGerarRelatorio.setStyleSheet("background:rgb(238, 238, 238)")
        self.btnGerarRelatorio.setObjectName("btnGerarRelatorio")
        self.btnExcluir = QtWidgets.QPushButton(self.centralwidget)
        self.btnExcluir.setGeometry(QtCore.QRect(440, 580, 121, 51))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btnExcluir.setFont(font)
        self.btnExcluir.setStyleSheet("background:rgb(238, 238, 238)")
        self.btnExcluir.setObjectName("btnExcluir")
        self.btnAdicionar = QtWidgets.QPushButton(self.centralwidget)
        self.btnAdicionar.setGeometry(QtCore.QRect(440, 480, 121, 51))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btnAdicionar.setFont(font)
        self.btnAdicionar.setStyleSheet("background:rgb(238, 238, 238)")
        self.btnAdicionar.setObjectName("btnAdicionar")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(150, 10, 661, 461))
        self.scrollArea.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 659, 459))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame.setStyleSheet("background-color: rgb(88, 88, 88);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.labelestacionamento = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.labelestacionamento.setFont(font)
        self.labelestacionamento.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.labelestacionamento.setText("")
        self.labelestacionamento.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.labelestacionamento.setObjectName("labelestacionamento")
        self.gridLayout.addWidget(self.labelestacionamento, 0, 1, 1, 1)
        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.inputPlaca = QtWidgets.QLineEdit(self.centralwidget)
        self.inputPlaca.setGeometry(QtCore.QRect(320, 480, 113, 20))
        self.inputPlaca.setObjectName("inputPlaca")
        self.inputNome = QtWidgets.QLineEdit(self.centralwidget)
        self.inputNome.setGeometry(QtCore.QRect(320, 510, 113, 20))
        self.inputNome.setObjectName("inputNome")
        self.inputModelo = QtWidgets.QLineEdit(self.centralwidget)
        self.inputModelo.setGeometry(QtCore.QRect(320, 540, 113, 20))
        self.inputModelo.setObjectName("inputModelo")
        self.inputCor = QtWidgets.QLineEdit(self.centralwidget)
        self.inputCor.setGeometry(QtCore.QRect(320, 570, 113, 20))
        self.inputCor.setObjectName("inputCor")
        self.inputConcessionaria = QtWidgets.QLineEdit(self.centralwidget)
        self.inputConcessionaria.setGeometry(QtCore.QRect(320, 600, 113, 20))
        self.inputConcessionaria.setObjectName("inputConcessionaria")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(150, 480, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(150, 510, 61, 20))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(150, 540, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(150, 570, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(150, 590, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(830, 10, 101, 151))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_6 = QtWidgets.QLabel(self.frame_2)
        self.label_6.setGeometry(QtCore.QRect(0, 10, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.labelVagas = QtWidgets.QLabel(self.frame_2)
        self.labelVagas.setGeometry(QtCore.QRect(60, 0, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.labelVagas.setFont(font)
        self.labelVagas.setObjectName("labelVagas")
        self.labelVerificaAdicionado = QtWidgets.QLabel(self.frame_2)
        self.labelVerificaAdicionado.setGeometry(QtCore.QRect(10, 60, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.labelVerificaAdicionado.setFont(font)
        self.labelVerificaAdicionado.setStyleSheet("color: green;")
        self.labelVerificaAdicionado.setText("")
        self.labelVerificaAdicionado.setObjectName("labelVerificaAdicionado")
        self.labelVerificaExluido = QtWidgets.QLabel(self.frame_2)
        self.labelVerificaExluido.setGeometry(QtCore.QRect(10, 100, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.labelVerificaExluido.setFont(font)
        self.labelVerificaExluido.setStyleSheet("color: red;")
        self.labelVerificaExluido.setText("")
        self.labelVerificaExluido.setObjectName("labelVerificaExluido")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(0, 60, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.spinQuantidade = QtWidgets.QSpinBox(self.centralwidget)
        self.spinQuantidade.setGeometry(QtCore.QRect(90, 70, 42, 22))
        self.spinQuantidade.setObjectName("spinQuantidade")
        self.btnReset = QtWidgets.QPushButton(self.centralwidget)
        self.btnReset.setGeometry(QtCore.QRect(610, 600, 75, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btnReset.setFont(font)
        self.btnReset.setStyleSheet("background-color: rgb(198, 0, 0);")
        self.btnReset.setObjectName("btnReset")
        self.spinNumeroDeVagas = QtWidgets.QSpinBox(self.centralwidget)
        self.spinNumeroDeVagas.setGeometry(QtCore.QRect(900, 170, 42, 22))
        self.spinNumeroDeVagas.setObjectName("spinNumeroDeVagas")
        self.btnNumeroDeVagas = QtWidgets.QPushButton(self.centralwidget)
        self.btnNumeroDeVagas.setGeometry(QtCore.QRect(830, 170, 61, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btnNumeroDeVagas.setFont(font)
        self.btnNumeroDeVagas.setStyleSheet("background:rgb(238, 238, 238)")
        self.btnNumeroDeVagas.setObjectName("btnNumeroDeVagas")
        self.btnVerVagas = QtWidgets.QPushButton(self.centralwidget)
        self.btnVerVagas.setGeometry(QtCore.QRect(0, 130, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        self.btnVerVagas.setFont(font)
        self.btnVerVagas.setStyleSheet("background:rgb(238, 238, 238)")
        self.btnVerVagas.setObjectName("btnVerVagas")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Estacionamento"))
        self.btnBuscarCarro.setText(_translate("MainWindow", "Buscar Carro"))
        self.btnGerarRelatorio.setText(_translate("MainWindow", "Gerar relatorio"))
        self.btnExcluir.setText(_translate("MainWindow", "excluir"))
        self.btnAdicionar.setText(_translate("MainWindow", "Adicionar"))
        self.label.setText(_translate("MainWindow", "Placa"))
        self.label_2.setText(_translate("MainWindow", "Nome"))
        self.label_3.setText(_translate("MainWindow", "Modelo"))
        self.label_4.setText(_translate("MainWindow", "Cor"))
        self.label_5.setText(_translate("MainWindow", "Concessionaria"))
        self.label_6.setText(_translate("MainWindow", "Vagas:"))
        self.labelVagas.setText(_translate("MainWindow", "10/10"))
        self.label_7.setText(_translate("MainWindow", "Ultimos:"))
        self.btnReset.setText(_translate("MainWindow", "Reset"))
        self.btnNumeroDeVagas.setText(_translate("MainWindow", "Vagas"))
        self.btnVerVagas.setText(_translate("MainWindow", "Mostrar Vagas ocupadas"))
