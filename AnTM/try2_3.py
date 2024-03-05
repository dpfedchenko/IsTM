import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QFileDialog
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import time

class Ui_MainWindow(object):

    def __init__(self):
        
        self.omega_x = [i for i in range(500 , 4001, 1)]
        for i in range(0, len(self.omega_x)):
            self.omega_x[i] = self.omega_x[i]/500
        self.U = [0]*len(self.omega_x)
        
        self.epsilon_o_value = 1.1
        self.mu_o_value = 1/1.1
        self.rho_E_value = 1/1.1
        self.rho_H_value = 1.1

        self.Lo_value = 1.0
        self.L_value = 4.0
        self.Ld_value = 0.25

        self.Nd_value = 1.0
        self.Nv_value = 1.0

        self.D_D_value = 90
        self.Theta_value = 45
        self.Phi_value = 45

        self.Xmin_value = 1.0
        self.Xmax_value = 8.0
        self.Ymin_value = -0.05
        self.Ymax_value = 1.1
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 800)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.AngVal_groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.AngVal_groupBox.setGeometry(QtCore.QRect(10, 260, 270, 200))
        self.AngVal_groupBox.setObjectName("AngVal_groupBox")

        self.AoJ_groupBox = QtWidgets.QGroupBox(self.AngVal_groupBox)
        self.AoJ_groupBox.setGeometry(QtCore.QRect(10, 20, 260, 60))
        self.AoJ_groupBox.setObjectName("AoJ_groupBox")

        self.D_D_label = QtWidgets.QLabel(self.AoJ_groupBox)
        self.D_D_label.setGeometry(QtCore.QRect(10, 30, 60, 20))
        self.D_D_label.setObjectName("D_D_label")

        self.D_D_horizontalSlider = QtWidgets.QSlider(self.AoJ_groupBox)
        self.D_D_horizontalSlider.setGeometry(QtCore.QRect(90, 30, 160, 20))
        self.D_D_horizontalSlider.setMaximum(360)
        self.D_D_horizontalSlider.setPageStep(1)
        self.D_D_horizontalSlider.setValue(self.D_D_value)
        self.D_D_horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.D_D_horizontalSlider.setObjectName("D_D_horizontalSlider")

        self.PA_groupBox = QtWidgets.QGroupBox(self.AngVal_groupBox)
        self.PA_groupBox.setGeometry(QtCore.QRect(10, 90, 260, 101))
        self.PA_groupBox.setObjectName("PA_groupBox")

        self.Theta_label = QtWidgets.QLabel(self.PA_groupBox)
        self.Theta_label.setGeometry(QtCore.QRect(10, 30, 60, 20))
        self.Theta_label.setObjectName("Theta_label")

        self.Theta_horizontalSlider = QtWidgets.QSlider(self.PA_groupBox)
        self.Theta_horizontalSlider.setGeometry(QtCore.QRect(90, 30, 160, 20))
        self.Theta_horizontalSlider.setMaximum(360)
        self.Theta_horizontalSlider.setPageStep(1)
        self.Theta_horizontalSlider.setValue(self.Theta_value)
        self.Theta_horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.Theta_horizontalSlider.setObjectName("Theta_horizontalSlider")

        self.Phi_horizontalSlider = QtWidgets.QSlider(self.PA_groupBox)
        self.Phi_horizontalSlider.setGeometry(QtCore.QRect(90, 70, 160, 20))
        self.Phi_horizontalSlider.setMaximum(360)
        self.Phi_horizontalSlider.setPageStep(1)
        self.Phi_horizontalSlider.setValue(self.Phi_value)
        self.Phi_horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.Phi_horizontalSlider.setObjectName("Phi_horizontalSlider")

        self.Phi_label = QtWidgets.QLabel(self.PA_groupBox)
        self.Phi_label.setGeometry(QtCore.QRect(10, 70, 60, 20))
        self.Phi_label.setObjectName("Phi_label")
        
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 20, 270, 235))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")

        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_8.setObjectName("verticalLayout_8")

        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")

        self.EnvV_groupBox = QtWidgets.QGroupBox(self.groupBox)
        self.EnvV_groupBox.setObjectName("EnvV_groupBox")

        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.EnvV_groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")

        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.epsilon_o_label = QtWidgets.QLabel(self.EnvV_groupBox)
        self.epsilon_o_label.setObjectName("epsilon_o_label")

        self.horizontalLayout.addWidget(self.epsilon_o_label)

        self.epsilon_o_doubleSpinBox = QtWidgets.QDoubleSpinBox(self.EnvV_groupBox)
        self.epsilon_o_doubleSpinBox.setMinimum(0.0)
        self.epsilon_o_doubleSpinBox.setMaximum(10.0)
        self.epsilon_o_doubleSpinBox.setSingleStep(0.05)
        self.epsilon_o_doubleSpinBox.setValue(self.epsilon_o_value)
        self.epsilon_o_doubleSpinBox.setObjectName("epsilon_o_doubleSpinBox")

        self.horizontalLayout.addWidget(self.epsilon_o_doubleSpinBox)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)

        self.verticalLayout.addItem(spacerItem)

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        self.mu_o_label = QtWidgets.QLabel(self.EnvV_groupBox)
        self.mu_o_label.setObjectName("mu_o_label")

        self.horizontalLayout_2.addWidget(self.mu_o_label)

        self.mu_o_doubleSpinBox = QtWidgets.QDoubleSpinBox(self.EnvV_groupBox)
        self.mu_o_doubleSpinBox.setMinimum(0.0)
        self.mu_o_doubleSpinBox.setMaximum(10.0)
        self.mu_o_doubleSpinBox.setSingleStep(0.05)
        self.mu_o_doubleSpinBox.setValue(self.mu_o_value)
        self.mu_o_doubleSpinBox.setObjectName("mu_o_doubleSpinBox")

        self.horizontalLayout_2.addWidget(self.mu_o_doubleSpinBox)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)

        self.verticalLayout.addItem(spacerItem1)

        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")

        self.rho_E_label = QtWidgets.QLabel(self.EnvV_groupBox)
        self.rho_E_label.setObjectName("rho_E_label")

        self.horizontalLayout_4.addWidget(self.rho_E_label)

        self.rho_E_doubleSpinBox = QtWidgets.QDoubleSpinBox(self.EnvV_groupBox)
        self.rho_E_doubleSpinBox.setMinimum(0.0)
        self.rho_E_doubleSpinBox.setMaximum(10.0)
        self.rho_E_doubleSpinBox.setSingleStep(0.05)
        self.rho_E_doubleSpinBox.setValue(self.rho_E_value)
        self.rho_E_doubleSpinBox.setObjectName("rho_E_doubleSpinBox")

        self.horizontalLayout_4.addWidget(self.rho_E_doubleSpinBox)
        self.verticalLayout.addLayout(self.horizontalLayout_4)

        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        
        self.verticalLayout.addItem(spacerItem2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
       
        self.rho_H_label = QtWidgets.QLabel(self.EnvV_groupBox)
        self.rho_H_label.setObjectName("rho_H_label")
        
        self.horizontalLayout_3.addWidget(self.rho_H_label)
        
        self.rho_H_doubleSpinBox = QtWidgets.QDoubleSpinBox(self.EnvV_groupBox)
        self.rho_H_doubleSpinBox.setMinimum(0.0)
        self.rho_H_doubleSpinBox.setMaximum(10.0)
        self.rho_H_doubleSpinBox.setSingleStep(0.05)
        self.rho_H_doubleSpinBox.setValue(self.rho_H_value)
        self.rho_H_doubleSpinBox.setObjectName("rho_H_doubleSpinBox")
        
        self.horizontalLayout_3.addWidget(self.rho_H_doubleSpinBox)
        
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        
        self.horizontalLayout_10.addWidget(self.EnvV_groupBox)
        
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        
        self.TV_groupBox = QtWidgets.QGroupBox(self.groupBox)
        self.TV_groupBox.setObjectName("TV_groupBox")
        
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.TV_groupBox)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        
        self.verticalLayout_4.addItem(spacerItem3)
        
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        
        self.Lo_label = QtWidgets.QLabel(self.TV_groupBox)
        self.Lo_label.setObjectName("Lo_label")
        
        self.horizontalLayout_5.addWidget(self.Lo_label)
        
        self.Lo_doubleSpinBox = QtWidgets.QDoubleSpinBox(self.TV_groupBox)
        self.Lo_doubleSpinBox.setMinimum(0.0)
        self.Lo_doubleSpinBox.setMaximum(10.0)
        self.Lo_doubleSpinBox.setSingleStep(0.05)
        self.Lo_doubleSpinBox.setValue(self.Lo_value)
        self.Lo_doubleSpinBox.setObjectName("Lo_doubleSpinBox")
        
        self.horizontalLayout_5.addWidget(self.Lo_doubleSpinBox)
        
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        
        self.verticalLayout_3.addItem(spacerItem4)
        
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        
        self.L_label = QtWidgets.QLabel(self.TV_groupBox)
        self.L_label.setObjectName("L_label")
        
        self.horizontalLayout_6.addWidget(self.L_label)
        
        self.L_doubleSpinBox = QtWidgets.QDoubleSpinBox(self.TV_groupBox)
        self.L_doubleSpinBox.setMinimum(0.0)
        self.L_doubleSpinBox.setMaximum(10.0)
        self.L_doubleSpinBox.setSingleStep(0.05)
        self.L_doubleSpinBox.setValue(self.L_value)
        self.L_doubleSpinBox.setObjectName("L_doubleSpinBox")
        
        self.horizontalLayout_6.addWidget(self.L_doubleSpinBox)
        
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        
        self.verticalLayout_3.addItem(spacerItem5)
        
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        
        self.Ld_label = QtWidgets.QLabel(self.TV_groupBox)
        self.Ld_label.setObjectName("Ld_label")
        
        self.horizontalLayout_7.addWidget(self.Ld_label)
        
        self.Ld_doubleSpinBox = QtWidgets.QDoubleSpinBox(self.TV_groupBox)
        self.Ld_doubleSpinBox.setMinimum(0.0)
        self.Ld_doubleSpinBox.setMaximum(10.0)
        self.Ld_doubleSpinBox.setSingleStep(0.05)
        self.Ld_doubleSpinBox.setValue(self.Ld_value)
        self.Ld_doubleSpinBox.setObjectName("Ld_doubleSpinBox")
        
        self.horizontalLayout_7.addWidget(self.Ld_doubleSpinBox)
        
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        
        self.verticalLayout_4.addItem(spacerItem6)
        
        self.verticalLayout_7.addWidget(self.TV_groupBox)
        
        self.RIV_groupBox = QtWidgets.QGroupBox(self.groupBox)
        self.RIV_groupBox.setObjectName("RIV_groupBox")
        
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.RIV_groupBox)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        
        self.verticalLayout_6.addItem(spacerItem7)
        
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        
        self.Nd_label = QtWidgets.QLabel(self.RIV_groupBox)
        self.Nd_label.setObjectName("Nd_label")
        
        self.horizontalLayout_8.addWidget(self.Nd_label)
        
        self.Nd_doubleSpinBox = QtWidgets.QDoubleSpinBox(self.RIV_groupBox)
        self.Nd_doubleSpinBox.setMinimum(0.5)
        self.Nd_doubleSpinBox.setMaximum(5.0)
        self.Nd_doubleSpinBox.setSingleStep(0.01)
        self.Nd_doubleSpinBox.setValue(self.Nd_value)
        self.Nd_doubleSpinBox.setObjectName("Nd_doubleSpinBox")
        
        self.horizontalLayout_8.addWidget(self.Nd_doubleSpinBox)
        
        self.verticalLayout_5.addLayout(self.horizontalLayout_8)
        
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        
        self.verticalLayout_5.addItem(spacerItem8)
        
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        
        self.Nv_label = QtWidgets.QLabel(self.RIV_groupBox)
        self.Nv_label.setObjectName("Nv_label")
        
        self.horizontalLayout_9.addWidget(self.Nv_label)
        
        self.Nv_doubleSpinBox = QtWidgets.QDoubleSpinBox(self.RIV_groupBox)
        self.Nv_doubleSpinBox.setMinimum(0.5)
        self.Nv_doubleSpinBox.setMaximum(5.0)
        self.Nv_doubleSpinBox.setSingleStep(0.01)
        self.Nv_doubleSpinBox.setValue(self.Nv_value)
        self.Nv_doubleSpinBox.setObjectName("Nv_doubleSpinBox")
        
        self.horizontalLayout_9.addWidget(self.Nv_doubleSpinBox)
        
        self.verticalLayout_5.addLayout(self.horizontalLayout_9)
        
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        
        self.verticalLayout_5.addItem(spacerItem9)
        
        self.verticalLayout_6.addLayout(self.verticalLayout_5)
        
        self.verticalLayout_7.addWidget(self.RIV_groupBox)
        
        self.horizontalLayout_10.addLayout(self.verticalLayout_7)
        
        self.verticalLayout_8.addLayout(self.horizontalLayout_10)
        
        MainWindow.setCentralWidget(self.centralwidget)
        
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        
        MainWindow.setStatusBar(self.statusbar)
        
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1280, 21))
        self.menuBar.setObjectName("menuBar")

        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(300, 20, 960, 600))
        self.widget.setObjectName("widget")
        self.plot_widget = QVBoxLayout(self.widget)

        #plot part
        self.fig_UvsOmega, self.ax_UvsOmega = plt.subplots()
        self.canvas_UvsOmega = FigureCanvas(self.fig_UvsOmega)
        self.plot_widget.addWidget(self.canvas_UvsOmega)
        self.plot_graph()
        
        MainWindow.setMenuBar(self.menuBar)

        ### new
        self.AxisParametres_groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.AxisParametres_groupBox.setGeometry(QtCore.QRect(10, 470, 160, 140))
        self.AxisParametres_groupBox.setTitle("Axis parametres")
        self.AxisParametres_groupBox.setObjectName("AxisParametres_groupBox")

        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.AxisParametres_groupBox)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        
        self.axisX_min_label = QtWidgets.QLabel()
        self.axisX_min_label.setObjectName("axisX_min_label")
        
        self.axisX_min_doubleSpinBox = QtWidgets.QDoubleSpinBox()
        self.axisX_min_doubleSpinBox.setMinimum(-100.0)
        self.axisX_min_doubleSpinBox.setMaximum(100.0)
        self.axisX_min_doubleSpinBox.setSingleStep(0.01)
        self.axisX_min_doubleSpinBox.setValue(self.Xmin_value)
        self.axisX_min_doubleSpinBox.setObjectName("axisX_min_doubleSpinBox")

        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        
        self.horizontalLayout_11.addWidget(self.axisX_min_label)
        self.horizontalLayout_11.addItem(spacerItem10)
        self.horizontalLayout_11.addWidget(self.axisX_min_doubleSpinBox)
        self.verticalLayout_9.addLayout(self.horizontalLayout_11)
        

        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")

        self.axisX_max_label = QtWidgets.QLabel()
        self.axisX_max_label.setObjectName("axisX_max_label")

        self.axisX_max_doubleSpinBox = QtWidgets.QDoubleSpinBox()
        self.axisX_max_doubleSpinBox.setMinimum(-100.0)
        self.axisX_max_doubleSpinBox.setMaximum(100.0)
        self.axisX_max_doubleSpinBox.setSingleStep(0.01)
        self.axisX_max_doubleSpinBox.setValue(self.Xmax_value)
        self.axisX_max_doubleSpinBox.setObjectName("axisX_max_doubleSpinBox")

        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        
        self.horizontalLayout_12.addWidget(self.axisX_max_label)
        self.horizontalLayout_12.addSpacerItem(spacerItem11)
        self.horizontalLayout_12.addWidget(self.axisX_max_doubleSpinBox)
        self.verticalLayout_9.addLayout(self.horizontalLayout_12)

        # Создание объектов
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")

        self.axisY_min_label = QtWidgets.QLabel()
        self.axisY_min_label.setObjectName("axisY_min_label")
        
        self.axisY_min_doubleSpinBox = QtWidgets.QDoubleSpinBox()
        self.axisY_min_doubleSpinBox.setMinimum(-100.0)
        self.axisY_min_doubleSpinBox.setMaximum(100.0)
        self.axisY_min_doubleSpinBox.setSingleStep(0.01)
        self.axisY_min_doubleSpinBox.setValue(self.Ymin_value)
        self.axisY_min_doubleSpinBox.setObjectName("axisY_min_doubleSpinBox")
        
        spacerItem12 =  QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        
        # Расположение объектов
        self.horizontalLayout_13.addWidget(self.axisY_min_label)
        self.horizontalLayout_13.addSpacerItem(spacerItem12)
        self.horizontalLayout_13.addWidget(self.axisY_min_doubleSpinBox)
        self.verticalLayout_9.addLayout(self.horizontalLayout_13)

        # Создание объектов
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")

        self.axisY_max_label = QtWidgets.QLabel()
        self.axisY_max_label.setObjectName("axisY_max_label")

        self.axisY_max_doubleSpinBox = QtWidgets.QDoubleSpinBox()
        self.axisY_max_doubleSpinBox.setMinimum(-100.0)
        self.axisY_max_doubleSpinBox.setMaximum(100.0)
        self.axisY_max_doubleSpinBox.setSingleStep(0.01)
        self.axisY_max_doubleSpinBox.setValue(self.Ymax_value)
        self.axisY_max_doubleSpinBox.setObjectName("axisY_max_doubleSpinBox")

        spacerItem13 =  QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)

        # Расположение объектов
        self.horizontalLayout_14.addWidget(self.axisY_max_label)
        self.horizontalLayout_14.addSpacerItem(spacerItem13)
        self.horizontalLayout_14.addWidget(self.axisY_max_doubleSpinBox)
        self.verticalLayout_9.addLayout(self.horizontalLayout_14)


        # Save and load
        self.SaveLoad_groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.SaveLoad_groupBox.setGeometry(QtCore.QRect(180, 470, 100, 85))
        self.SaveLoad_groupBox.setTitle("Save and Load")
        self.SaveLoad_groupBox.setObjectName("SaveLoad_groupBox")

        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.SaveLoad_groupBox)
        self.verticalLayout_11.setObjectName("verticalLayout_11")

        self.save_txt_button = QtWidgets.QPushButton()
        self.save_txt_button.setObjectName("save_txt_button")

        self.load_txt_button = QtWidgets.QPushButton()
        self.load_txt_button.setObjectName("load_txt_button")

        self.verticalLayout_11.addWidget(self.save_txt_button)
        self.verticalLayout_11.addWidget(self.load_txt_button)



        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.AngVal_groupBox.setTitle(_translate("MainWindow", "Angle values"))
        self.AoJ_groupBox.setTitle(_translate("MainWindow", "Angle of jump"))
        self.D_D_label.setText(_translate("MainWindow", "D_D:  90°"))
        self.PA_groupBox.setTitle(_translate("MainWindow", "Polarization angles "))
        self.Theta_label.setText(_translate("MainWindow", "Theta:  45°"))
        self.Phi_label.setText(_translate("MainWindow", "Phi:  45°"))
        self.EnvV_groupBox.setTitle(_translate("MainWindow", "Env values"))
        self.epsilon_o_label.setText(_translate("MainWindow", "ε_o:"))
        self.mu_o_label.setText(_translate("MainWindow", "μ_o:"))
        self.rho_E_label.setText(_translate("MainWindow", "ρ_E:"))
        self.rho_H_label.setText(_translate("MainWindow", "ρ_H:"))
        self.TV_groupBox.setTitle(_translate("MainWindow", "Thickness values "))
        self.Lo_label.setText(_translate("MainWindow", "Lo:"))
        self.L_label.setText(_translate("MainWindow", "L:"))
        self.Ld_label.setText(_translate("MainWindow", "Ld:"))
        self.RIV_groupBox.setTitle(_translate("MainWindow", "Refractive index values"))
        self.Nd_label.setText(_translate("MainWindow", "Nd:"))
        self.Nv_label.setText(_translate("MainWindow", "Nv:"))
        self.save_txt_button.setText(_translate("MainWindow", "Save as .txt"))
        self.load_txt_button.setText(_translate("MainWindow", "Load.txt"))
        self.axisX_min_label.setText(_translate("MainWindow", "X min:"))
        self.axisX_max_label.setText(_translate("MainWindow", "X max:"))
        self.axisY_min_label.setText(_translate("MainWindow", "Y min:"))
        self.axisY_max_label.setText(_translate("MainWindow", "Y max:"))

        # VALUE CHANGE. doubleSpinBox
        self.epsilon_o_doubleSpinBox.valueChanged.connect(self.update_epsilon_o_value)
        self.mu_o_doubleSpinBox.valueChanged.connect(self.update_mu_o_value)
        self.rho_E_doubleSpinBox.valueChanged.connect(self.update_rho_E_value)
        self.rho_H_doubleSpinBox.valueChanged.connect(self.update_rho_H_value)

        self.Lo_doubleSpinBox.valueChanged.connect(self.update_Lo_value)
        self.L_doubleSpinBox.valueChanged.connect(self.update_L_value)
        self.Ld_doubleSpinBox.valueChanged.connect(self.update_Ld_value)
        self.Nd_doubleSpinBox.valueChanged.connect(self.update_Nd_value)
        self.Nv_doubleSpinBox.valueChanged.connect(self.update_Nv_value)

        self.axisX_min_doubleSpinBox.valueChanged.connect(self.update_Xmin_value)
        self.axisX_max_doubleSpinBox.valueChanged.connect(self.update_Xmax_value)
        self.axisY_min_doubleSpinBox.valueChanged.connect(self.update_Ymin_value)
        self.axisY_max_doubleSpinBox.valueChanged.connect(self.update_Ymax_value)
        

        # VALUE CHANGE. Sliders
        self.D_D_horizontalSlider.valueChanged.connect(self.update_D_D_value)
        self.Theta_horizontalSlider.valueChanged.connect(self.update_Theta_value)
        self.Phi_horizontalSlider.valueChanged.connect(self.update_Phi_value)

        # CLICKED
        self.save_txt_button.clicked.connect(self.save_data_txt)
        self.load_txt_button.clicked.connect(self.load_data)

    def update_epsilon_o_value(self, epsilon_o_value):
        self.epsilon_o_value = epsilon_o_value
        self.plot_graph()

    def update_mu_o_value(self, mu_o_value):
        self.mu_o_value = mu_o_value
        self.plot_graph()

    def update_rho_E_value(self, rho_E_value):
        self.rho_E_value = rho_E_value
        self.plot_graph()

    def update_rho_H_value(self, rho_H_value):
        self.rho_H_value = rho_H_value
        self.plot_graph()

    def update_Lo_value(self, Lo_value):
        self.Lo_value = Lo_value
        self.plot_graph()

    def update_L_value(self, L_value):
        self.L_value = L_value
        self.plot_graph()

    def update_Ld_value(self, Ld_value):
        self.Ld_value = Ld_value
        self.plot_graph()

    def update_Nd_value(self, Nd_value):
        self.Nd_value = Nd_value
        self.plot_graph()

    def update_Nv_value(self, Nv_value):
        self.Nv_value = Nv_value
        self.plot_graph()

    def update_D_D_value(self, D_D_value):
        self.D_D_label.setText(f"D_D:  {D_D_value}°")
        self.D_D_value = D_D_value
        self.plot_graph()
    def update_Theta_value(self, Theta_value):
        self.Theta_label.setText(f"Theta:  {Theta_value}°")
        self.Theta_value = Theta_value
        self.plot_graph()
    def update_Phi_value(self, Phi_value):
        self.Phi_label.setText(f"Phi:  {Phi_value}°")
        self.Phi_value = Phi_value
        self.plot_graph()



    def update_Xmin_value(self, Xmin_value):
        self.Xmin_value = Xmin_value
        self.plot_graph()
    
    def update_Xmax_value(self, Xmax_value):
        self.Xmax_value = Xmax_value
        self.plot_graph()

    def update_Ymin_value(self, Ymin_value):
        self.Ymin_value = Ymin_value
        self.plot_graph()
    
    def update_Ymax_value(self, Ymax_value):
        self.Ymax_value = Ymax_value
        self.plot_graph()

    def save_data_txt(self):
        options1 = QFileDialog.Options()
        file_name1, _ = QFileDialog.getSaveFileName(None, "Save File", "", "Text files (*.txt)", options=options1)
        if file_name1:
            with open(file_name1, "w") as file:
                file.write("Omega \t")
                file.write("Transmission coef \n")
                for i in range(0, len(self.omega_x)):
                    file.write(str(self.omega_x[i]) + "\t")
                    file.write(str(self.U[i]) + "\n")

        options2 = QFileDialog.Options()
        file_name2, _ = QFileDialog.getSaveFileName(None, "Save File", "", "Text files (*.txt)", options=options2)
        
        if file_name2:
            with open(file_name2, "w") as file:
                file.write("Epsilon_o: " + str(self.epsilon_o_value) + "\n")
                file.write("Mu_o: " + str(self.mu_o_value) + "\n")
                file.write("rho_E: " + str(self.rho_E_value) + "\n")
                file.write("rho_H: " + str(self.rho_H_value) + "\n")
                file.write("Lo: " + str(self.Lo_value) + "\n")
                file.write("L: " + str(self.L_value) + "\n")
                file.write("Ld: " + str(self.Ld_value) + "\n")
                file.write("Nd: " + str(self.Nd_value) + "\n")
                file.write("Nv: " + str(self.Nv_value) + "\n")
                file.write("D_D: " + str(self.D_D_value) + "\n")
                file.write("Theta: " + str(self.Theta_value) + "\n")
                file.write("Phi: " + str(self.Phi_value) + "\n")

    # РАБОТАЕТ НЕПРАВИЛЬНО!!! ИСПРАВИТЬ 
    def load_data(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(None, "Open File", "", "Text files (*.txt)", options=options)
        if file_name:
            with open(file_name, "r") as file:
                for line in file:
                    if line.startswith("Epsilon_o"):
                        self.epsilon_o_value = float(line.split(":")[-1].strip())
                    elif line.startswith("Mu_o"):
                        self.mu_o_value = float(line.split(":")[-1].strip())
                    elif line.startswith("rho_E"):
                        self.rho_E_value = float(line.split(":")[-1].strip())
                    elif line.startswith("rho_H"):
                        self.rho_H_value = float(line.split(":")[-1].strip())
                    elif line.startswith("Lo"):
                        self.Lo_value = float(line.split(":")[-1].strip())
                    elif line.startswith("L"):
                        self.L_value = float(line.split(":")[-1].strip())
                    elif line.startswith("Ld"):
                        self.Ld_value = float(line.split(":")[-1].strip())
                    elif line.startswith("Nd"):
                        self.Nd_value = float(line.split(":")[-1].strip())
                    elif line.startswith("Nv"):
                        self.Nv_value = float(line.split(":")[-1].strip())
                    elif line.startswith("D_D"):
                        self.D_D_value = int(line.split(":")[-1].strip())
                    elif line.startswith("Theta"):
                        self.Theta_value = int(line.split(":")[-1].strip())
                    elif line.startswith("Phi"):
                        self.Phi_value = int(line.split(":")[-1].strip())
        self.plot_graph()




    def plot_graph(self):
        start = time.process_time()

        for i in range(0, len(self.omega_x)):
            I = complex(0, 1)
            Pi = np.pi

            epsilon_o = self.epsilon_o_value
            mu_o = self.mu_o_value
            rho_E = self.rho_E_value
            rho_H = self.rho_H_value

            Lo = self.Lo_value
            L = self.L_value
            Ld = self.Ld_value
            Nd = self.Nd_value
            Nv = self.Nv_value

            D_D = self.D_D_value * np.pi / 180
            Theta = self.Theta_value
            Phi = self.Phi_value

            omega = self.omega_x[i]
            
            no = np.sqrt(epsilon_o*mu_o)
            ne = rho_E*rho_H*no
            
            a2 = 1/2*(Lo**2*rho_H**2*rho_E**2*no**2*omega**2+8*Pi**2+Lo**2*no**2*omega**2)/Lo**2/no**2/omega**2
            a1 = np.sqrt(1/4*(Lo**2*no**2*omega**2*rho_E**4*rho_H**4-2*Lo**2*rho_H**2*rho_E**2*no**2*omega**2+16*Pi**2*rho_E**2*rho_H**2+Lo**2*no**2*omega**2+16*Pi**2+16*Pi**2*rho_E**2+16*Pi**2*rho_H**2)/Lo**2/no**2/omega**2)
            
            Lp = L * omega * no

            iota = np.sqrt(a2 - a1, dtype=np.complex128)
            sigma = np.sqrt(a1 + a2)

            CI = np.cos(Lp*iota)
            CS = np.cos(Lp*sigma)
            SI = np.sin(Lp*iota)/iota
            SS = np.sin(Lp*sigma)/sigma

            DifC = CI-CS
            DifS = SI-SS
            SumC = CS+CI
            SumS = SS+SI


            LCM = [[0, 0, 0, 0],
                   [0, 0, 0, 0],
                   [0, 0, 0, 0],
                   [0, 0, 0, 0]]

            LCM[0][0] = 1/8*((-I*rho_H**2*rho_E**4+(-I*rho_H**4-I+2*I*a2-4*I*rho_H**2)*rho_E**2+(-I+2*I*a2)*rho_H**2+4*I*a2)*DifS+2*rho_E**2*rho_H**2*DifC+(4*SumC-4*I*SumS)*a1-2*DifC)/a1
            LCM[0][1] = -1/4*I*(-1/2*rho_E**2*rho_H**2-1/2+a2)*(rho_E+rho_H)*(-rho_H+rho_E)*DifS/a1
            LCM[0][2] = 1/2*(rho_E+rho_H)*Pi*(1/2*rho_H**2*DifS*rho_E**2+rho_H*(DifS+I*DifC)*rho_E-a1*SumS+I*DifC+1/2*DifS)/Lo/rho_H/rho_E/no/omega/a1
            LCM[0][3] = -1/2*(-rho_H+rho_E)*(-1/2*rho_H**2*DifS*rho_E**2+rho_H*(DifS+I*DifC)*rho_E+a1*SumS-1/2*DifS-I*DifC)*Pi/Lo/rho_H/rho_E/no/omega/a1
            LCM[1][0] = 1/4*I*(-1/2*rho_E**2*rho_H**2-1/2+a2)*(rho_E+rho_H)*(-rho_H+rho_E)*DifS/a1
            LCM[1][1] = 1/8*((I*rho_H**2*rho_E**4+(4*I*rho_H**2+I+I*rho_H**4-2*I*a2)*rho_E**2+(I-2*I*a2)*rho_H**2-4*I*a2)*DifS+2*rho_E**2*rho_H**2*DifC+(4*SumC+4*I*SumS)*a1-2*DifC)/a1
            LCM[1][2] = 1/2*Pi*(1/2*rho_H**2*DifS*rho_E**2+rho_H*(-DifS+I*DifC)*rho_E-a1*SumS-I*DifC+1/2*DifS)*(-rho_H+rho_E)/Lo/rho_H/rho_E/no/omega/a1
            LCM[1][3] = -1/2*(rho_E+rho_H)*(-1/2*rho_H**2*DifS*rho_E**2+rho_H*(-DifS+I*DifC)*rho_E-1/2*DifS+a1*SumS+I*DifC)*Pi/Lo/rho_H/rho_E/no/omega/a1
            LCM[2][0] = -1/2*(rho_E+rho_H)*Pi*(1/2*rho_H**2*DifS*rho_E**2+rho_H*(DifS+I*DifC)*rho_E-a1*SumS+I*DifC+1/2*DifS)/Lo/no/omega/a1
            LCM[2][1] = 1/2*(-rho_H+rho_E)*(1/2*rho_H**2*DifS*rho_E**2+rho_H*(-DifS+I*DifC)*rho_E-a1*SumS-I*DifC+1/2*DifS)*Pi/Lo/no/omega/a1
            LCM[2][2] = 1/8*(-I*rho_H**2*rho_E**4*DifS-2*rho_E**3*rho_H**3*DifC+(-I*rho_H**4*DifS+((-4*I+4*I*a2)*DifS-4*I*SumS*a1)*rho_H**2+2*I*(-1/2+a2)*DifS)*rho_E**2+4*(1/2*DifC+SumC*a1)*rho_H*rho_E+2*I*(-1/2+a2)*rho_H**2*DifS)/rho_E/rho_H/a1
            LCM[2][3] = 1/4*I*(rho_E+rho_H)*(-rho_H+rho_E)*DifS*(-1/2*rho_E**2*rho_H**2-1/2+a2)/rho_E/rho_H/a1
            LCM[3][0] = -1/2*Pi*(-1/2*rho_H**2*DifS*rho_E**2+rho_H*(DifS+I*DifC)*rho_E+a1*SumS-1/2*DifS-I*DifC)*(-rho_H+rho_E)/Lo/no/omega/a1
            LCM[3][1] = 1/2*Pi*(rho_E+rho_H)*(-1/2*rho_H**2*DifS*rho_E**2+rho_H*(-DifS+I*DifC)*rho_E-1/2*DifS+a1*SumS+I*DifC)/Lo/no/omega/a1
            LCM[3][2] = -1/4*I*(-rho_H+rho_E)*(rho_E+rho_H)*DifS*(-1/2*rho_E**2*rho_H**2-1/2+a2)/rho_E/rho_H/a1
            LCM[3][3] = 1/8*(I*rho_H**2*rho_E**4*DifS-2*rho_E**3*rho_H**3*DifC+(I*rho_H**4*DifS+((4*I-4*I*a2)*DifS+4*I*SumS*a1)*rho_H**2-2*I*(-1/2+a2)*DifS)*rho_E**2+4*(1/2*DifC+SumC*a1)*rho_H*rho_E-2*I*(-1/2+a2)*rho_H**2*DifS)/rho_E/rho_H/a1

 
            LDM = [[0, 0, 0, 0],
                   [0, 0, 0, 0],
                   [0, 0, 0, 0],
                   [0, 0, 0, 0]]

            LDM[0][0] = 1 / 4 * ((2 * Nd * mu_o ** (1 / 2) * epsilon_o ** (1 / 2) + Nd ** 2 * mu_o + epsilon_o) * np.exp(-I * Nd * Ld * omega) - np.exp(I * Nd * Ld * omega) * (epsilon_o - 2 * Nd * mu_o ** (1 / 2) * epsilon_o ** (1 / 2) + Nd ** 2 * mu_o)) / epsilon_o ** (1 / 2) / mu_o ** (1 / 2) / Nd
            LDM[0][1] = 1 / 2 * I * np.sin(Nd * Ld * omega) / Nd / mu_o ** (1 / 2) / epsilon_o ** (1 / 2) * (-epsilon_o + Nd ** 2 * mu_o)
            LDM[0][2] = 0
            LDM[0][3] = 0
            LDM[1][0] = -1 / 2 * I * np.sin(Nd * Ld * omega) / Nd / mu_o ** (1 / 2) / epsilon_o ** (1 / 2) * (-epsilon_o + Nd ** 2 * mu_o)
            LDM[1][1] = -1 / 4 * ((epsilon_o - 2 * Nd * mu_o ** (1 / 2) * epsilon_o ** (1 / 2) + Nd ** 2 * mu_o) * np.exp(-I * Nd * Ld * omega) - np.exp(I * Nd * Ld * omega) * (2 * Nd * mu_o ** (1 / 2) * epsilon_o ** (1 / 2) + Nd ** 2 * mu_o + epsilon_o)) / epsilon_o ** (1 / 2) / mu_o ** (1 / 2) / Nd
            LDM[1][2] = 0
            LDM[1][3] = 0
            LDM[2][0] = 0
            LDM[2][1] = 0
            LDM[2][2] = 1 / 4 / mu_o ** (1 / 2) / epsilon_o ** (1 / 2) * ((rho_E ** 2 * epsilon_o + 2 * Nd * rho_H * mu_o ** (1 / 2) * rho_E * epsilon_o ** (1 / 2) + Nd ** 2 * rho_H ** 2 * mu_o) * np.exp(-I * Nd * Ld * omega) - np.exp(I * Nd * Ld * omega) * (Nd ** 2 * rho_H ** 2 * mu_o - 2 * Nd * rho_H * mu_o ** (1 / 2) * rho_E * epsilon_o ** (1 / 2) + rho_E ** 2 * epsilon_o)) / Nd / rho_H / rho_E
            LDM[2][3] = 1 / 2 * I * np.sin(Nd * Ld * omega) / Nd / rho_H / mu_o ** (1 / 2) / rho_E / epsilon_o ** (1 / 2) * (-rho_E ** 2 * epsilon_o + Nd ** 2 * rho_H ** 2 * mu_o)
            LDM[3][0] = 0
            LDM[3][1] = 0
            LDM[3][2] = -1 / 2 * I * np.sin(Nd * Ld * omega) / Nd / rho_H / mu_o ** (1 / 2) / rho_E / epsilon_o ** (1 / 2) * (-rho_E ** 2 * epsilon_o + Nd ** 2 * rho_H ** 2 * mu_o)
            LDM[3][3] = -1 / 4 / mu_o ** (1 / 2) / epsilon_o ** (1 / 2) * ((Nd ** 2 * rho_H ** 2 * mu_o - 2 * Nd * rho_H * mu_o ** (1 / 2) * rho_E * epsilon_o ** (1 / 2) + rho_E ** 2 * epsilon_o) * np.exp(-I * Nd * Ld * omega) - np.exp(I * Nd * Ld * omega) * (rho_E ** 2 * epsilon_o + 2 * Nd * rho_H * mu_o ** (1 / 2) * rho_E * epsilon_o ** (1 / 2) + Nd ** 2 * rho_H ** 2 * mu_o)) / Nd / rho_H / rho_E

            RBM = [[0, 0, 0, 0],
                   [0, 0, 0, 0],
                   [0, 0, 0, 0],
                   [0, 0, 0, 0]]

            RBM[0][0] = 1 / 2 * (mu_o ** (1 / 2) * Nv + epsilon_o ** (1 / 2)) / Nv
            RBM[0][1] = 1 / 2 * (mu_o ** (1 / 2) * Nv - epsilon_o ** (1 / 2)) / Nv
            RBM[0][2] = 0
            RBM[0][3] = 0
            RBM[1][0] = 1 / 2 * (mu_o ** (1 / 2) * Nv - epsilon_o ** (1 / 2)) / Nv
            RBM[1][1] = 1 / 2 * (mu_o ** (1 / 2) * Nv + epsilon_o ** (1 / 2)) / Nv
            RBM[1][2] = 0
            RBM[1][3] = 0
            RBM[2][0] = 0
            RBM[2][1] = 0
            RBM[2][2] = 1 / 2 * (rho_H * mu_o ** (1 / 2) * Nv + rho_E * epsilon_o ** (1 / 2)) / Nv
            RBM[2][3] = 1 / 2 * (rho_H * mu_o ** (1 / 2) * Nv - rho_E * epsilon_o ** (1 / 2)) / Nv
            RBM[3][0] = 0
            RBM[3][1] = 0
            RBM[3][2] = 1 / 2 * (rho_H * mu_o ** (1 / 2) * Nv - rho_E * epsilon_o ** (1 / 2)) / Nv
            RBM[3][3] = 1 / 2 * (rho_H * mu_o ** (1 / 2) * Nv + rho_E * epsilon_o ** (1 / 2)) / Nv

            LBM = [ [0, 0, 0, 0],
                    [0, 0, 0, 0],
                    [0, 0, 0, 0],
                    [0, 0, 0, 0]]

            LBM[0][0] = 1/2*(mu_o**(1/2)*Nv+epsilon_o**(1/2))/mu_o**(1/2)/epsilon_o**(1/2)
            LBM[0][1] = 1/2*(-mu_o**(1/2)*Nv+epsilon_o**(1/2))/mu_o**(1/2)/epsilon_o**(1/2)
            LBM[0][2] = 0
            LBM[0][3] = 0
            LBM[1][0] = 1/2*(-mu_o**(1/2)*Nv+epsilon_o**(1/2))/mu_o**(1/2)/epsilon_o**(1/2)
            LBM[1][1] = 1/2*(mu_o**(1/2)*Nv+epsilon_o**(1/2))/mu_o**(1/2)/epsilon_o**(1/2)
            LBM[1][2] = 0
            LBM[1][3] = 0
            LBM[2][0] = 0
            LBM[2][1] = 0
            LBM[2][2] = 1/2*(rho_H*mu_o**(1/2)*Nv+rho_E*epsilon_o**(1/2))/rho_H/mu_o**(1/2)/rho_E/epsilon_o**(1/2)
            LBM[2][3] = 1/2*(-rho_H*mu_o**(1/2)*Nv+rho_E*epsilon_o**(1/2))/rho_H/mu_o**(1/2)/rho_E/epsilon_o**(1/2)
            LBM[3][0] = 0
            LBM[3][1] = 0
            LBM[3][2] = 1/2*(-rho_H*mu_o**(1/2)*Nv+rho_E*epsilon_o**(1/2))/rho_H/mu_o**(1/2)/rho_E/epsilon_o**(1/2)
            LBM[3][3] = 1/2*(rho_H*mu_o**(1/2)*Nv+rho_E*epsilon_o**(1/2))/rho_H/mu_o**(1/2)/rho_E/epsilon_o**(1/2)

            TAJM = [[0, 0, 0, 0],
                    [0, 0, 0, 0],
                    [0, 0, 0, 0],
                    [0, 0, 0, 0]]

            TAJM[0][0] = np.cos(D_D)
            TAJM[0][1] = 0
            TAJM[0][2] = -1 / 2 * (rho_H + rho_E) * np.sin(D_D) / rho_E / rho_H
            TAJM[0][3] = -1 / 2 * (-rho_H + rho_E) * np.sin(D_D) / rho_E / rho_H
            TAJM[1][0] = 0
            TAJM[1][1] = np.cos(D_D)
            TAJM[1][2] = -1 / 2 * (-rho_H + rho_E) * np.sin(D_D) / rho_E / rho_H
            TAJM[1][3] = -1 / 2 * (rho_H + rho_E) * np.sin(D_D) / rho_E / rho_H
            TAJM[2][0] = 1 / 2 * (rho_H + rho_E) * np.sin(D_D)
            TAJM[2][1] = -1 / 2 * (-rho_H + rho_E) * np.sin(D_D)
            TAJM[2][2] = np.cos(D_D)
            TAJM[2][3] = 0
            TAJM[3][0] = -1 / 2 * (-rho_H + rho_E) * np.sin(D_D)
            TAJM[3][1] = 1 / 2 * (rho_H + rho_E) * np.sin(D_D)
            TAJM[3][2] = 0
            TAJM[3][3] = np.cos(D_D)

            Vo = [-np.cos(Theta),
                  0,
                  np.sin(Theta) * np.exp(I * Phi),
                  0]
            

            Ve = [0,
                  0,
                  0,
                  0]

            ######### Resulting matrix  #########

            Tw = np.dot(np.dot(LBM, LCM), RBM)

            Rx = (-Tw[1][0] * Vo[2] * Tw[0][2] + Tw[1][0] * Tw[2][2] * Vo[0] - Tw[1][2] * Vo[0] * Tw[2][0] + Tw[1][2] *
                  Tw[0][0] * Vo[2]) / (Tw[0][0] * Tw[2][2] - Tw[0][2] * Tw[2][0])
            Ry = -(Tw[3][0] * Vo[2] * Tw[0][2] + Tw[3][0] * Tw[2][2] * Vo[0] + Tw[3][2] * Vo[0] * Tw[2][0] - Tw[3][2] *
                   Tw[0][0] * Vo[2]) / (Tw[0][0] * Tw[2][2] - Tw[0][2] * Tw[2][0])

            Tx = (-Vo[2] * Tw[0][2] + Tw[2][2] * Vo[0]) / (Tw[0][0] * Tw[2][2] - Tw[0][2] * Tw[2][0])
            Ty = -(Vo[0] * Tw[2][0] - Tw[0][0] * Vo[2]) / (Tw[0][0] * Tw[2][2] - Tw[0][2] * Tw[2][0])

            self.U[i] = abs(Tx) ** 2 + abs(Ty) ** 2

        try:
            self.ax_UvsOmega.clear()
            self.ax_UvsOmega.grid(True)
            self.ax_UvsOmega.set_xlim(self.Xmin_value, self.Xmax_value)
            self.ax_UvsOmega.set_ylim(self.Ymin_value, self.Ymax_value)
            self.ax_UvsOmega.plot(self.omega_x, self.U)
            self.canvas_UvsOmega.draw()
        except Exception as e:
            print("Error:", str(e))
        
        finish = time.process_time()
        print("dt = " + str(finish - start))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
