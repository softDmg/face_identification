# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'image_match.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(769, 581)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 771, 541))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.main_frame = QtWidgets.QFrame(self.tab)
        self.main_frame.setGeometry(QtCore.QRect(29, 79, 711, 251))
        self.main_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_frame.setObjectName("main_frame")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.main_frame)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 691, 231))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.original_image = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.original_image.setText("")
        self.original_image.setObjectName("original_image")
        self.horizontalLayout.addWidget(self.original_image)
        self.divider_label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.divider_label.setMaximumSize(QtCore.QSize(100, 16777215))
        self.divider_label.setText("")
        self.divider_label.setObjectName("divider_label")
        self.horizontalLayout.addWidget(self.divider_label)
        self.new_image = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.new_image.setText("")
        self.new_image.setObjectName("new_image")
        self.horizontalLayout.addWidget(self.new_image)
        self.match_image_button = QtWidgets.QPushButton(self.tab)
        self.match_image_button.setGeometry(QtCore.QRect(530, 420, 113, 32))
        self.match_image_button.setObjectName("match_image_button")
        self.MessageLabel = QtWidgets.QLabel(self.tab)
        self.MessageLabel.setGeometry(QtCore.QRect(300, 350, 181, 41))
        self.MessageLabel.setText("")
        self.MessageLabel.setObjectName("MessageLabel")
        self.load_image_button = QtWidgets.QPushButton(self.tab)
        self.load_image_button.setGeometry(QtCore.QRect(110, 420, 113, 32))
        self.load_image_button.setObjectName("load_image_button")
        self.HeaderLabel = QtWidgets.QLabel(self.tab)
        self.HeaderLabel.setGeometry(QtCore.QRect(330, 10, 121, 41))
        self.HeaderLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.HeaderLabel.setObjectName("HeaderLabel")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.main_frame_2 = QtWidgets.QFrame(self.tab_2)
        self.main_frame_2.setGeometry(QtCore.QRect(39, 79, 711, 251))
        self.main_frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_frame_2.setObjectName("main_frame_2")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.main_frame_2)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 10, 691, 231))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.original_image_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.original_image_2.setMaximumSize(QtCore.QSize(250, 16777215))
        self.original_image_2.setText("")
        self.original_image_2.setObjectName("original_image_2")
        self.horizontalLayout_2.addWidget(self.original_image_2)
        self.divider_label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.divider_label_2.setMaximumSize(QtCore.QSize(110, 16777215))
        self.divider_label_2.setText("")
        self.divider_label_2.setObjectName("divider_label_2")
        self.horizontalLayout_2.addWidget(self.divider_label_2)
        self.new_image_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.new_image_2.setMaximumSize(QtCore.QSize(250, 16777215))
        self.new_image_2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.new_image_2.setText("")
        self.new_image_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.new_image_2.setObjectName("new_image_2")
        self.horizontalLayout_2.addWidget(self.new_image_2)
        self.match_image_button_2 = QtWidgets.QPushButton(self.tab_2)
        self.match_image_button_2.setGeometry(QtCore.QRect(540, 420, 113, 32))
        self.match_image_button_2.setObjectName("match_image_button_2")
        self.MessageLabel_2 = QtWidgets.QLabel(self.tab_2)
        self.MessageLabel_2.setGeometry(QtCore.QRect(310, 350, 181, 41))
        self.MessageLabel_2.setText("")
        self.MessageLabel_2.setObjectName("MessageLabel_2")
        self.load_image_button_2 = QtWidgets.QPushButton(self.tab_2)
        self.load_image_button_2.setGeometry(QtCore.QRect(120, 420, 113, 32))
        self.load_image_button_2.setObjectName("load_image_button_2")
        self.HeaderLabel_2 = QtWidgets.QLabel(self.tab_2)
        self.HeaderLabel_2.setGeometry(QtCore.QRect(340, 10, 121, 41))
        self.HeaderLabel_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.HeaderLabel_2.setObjectName("HeaderLabel_2")
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 769, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.match_image_button.setText(_translate("MainWindow", "Match Images"))
        self.load_image_button.setText(_translate("MainWindow", "Load Image"))
        self.HeaderLabel.setText(_translate("MainWindow", "IMAGE MATCHING"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Tab 1"))
        self.match_image_button_2.setText(_translate("MainWindow", "Match Images"))
        self.load_image_button_2.setText(_translate("MainWindow", "Load Image"))
        self.HeaderLabel_2.setText(_translate("MainWindow", "IMAGE MATCHING"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
