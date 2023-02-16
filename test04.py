from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)


from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)


from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QListWidget,
    QListWidgetItem, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QWidget, QFileDialog)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(334, 330)
        MainWindow.setMinimumSize(QSize(334, 330))
        MainWindow.setMaximumSize(QSize(334, 330))


        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")


        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(99, 23, 132, 21))


        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(99, 53, 132, 21))


        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(21, 22, 48, 16))


        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(21, 52, 72, 16))


        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.clicked.connect(self.btn1_FileLoad)
        self.pushButton.setGeometry(QRect(240, 22, 75, 24))


        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.clicked.connect(self.btn2_FileLoad)
        self.pushButton_2.setGeometry(QRect(240, 52, 75, 24))


        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.clicked.connect(self.btn_moveup)
        self.pushButton_3.setGeometry(QRect(241, 163, 75, 24))


        self.pushButton_4 = QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.clicked.connect(self.btn_movedown)
        self.pushButton_4.setGeometry(QRect(241, 214, 75, 24))


        self.pushButton_5 = QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.clicked.connect(self.btn_remove)
        self.pushButton_5.setGeometry(QRect(241, 265, 75, 24))


        self.pushButton_6 = QPushButton(self.centralwidget)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.clicked.connect(self.btn_merge)
        self.pushButton_6.setGeometry(QRect(241, 112, 75, 24))


        self.listWidget = QListWidget(self.centralwidget)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(19, 100, 211, 201))


        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 334, 22))


        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")


        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi


    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\uae30\uc900\ud30c\uc77c", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\ubcd1\ud569\ub300\uc0c1\ud30c\uc77c", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\ud30c\uc77c\ucc3e\uae30", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\ud30c\uc77c\ucc3e\uae30", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\u25b3", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"\uc0ad\uc81c", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"\u25bd", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"\ubcd1\ud569\uc2dc\uc791", None))
    # retranslateUi


    def btn1_FileLoad(self):
        fname = QFileDialog.getOpenFileName(self, "File Load", 'D:/ubuntu/disks/',
                                            'All File(*);; Text File(*.txt);; PPtx file(*ppt *pptx)')
        if fname[0]:
            import os
            file_path = os.path.basename(fname[0])
            global file_pathZ
            file_pathZ = os.path.abspath(file_path)
            self.lineEdit.setText(file_path)
        else:
            pass


    def btn2_FileLoad(self):
        global fname
        fname = QFileDialog.getOpenFileNames(self, "File Load", 'D:/ubuntu/disks/',
                                            'All File(*);; Text File(*.txt);; PPtx file(*ppt *pptx)')

        if fname[0]:
            import os

            def convertStringA(arr, sep):
                str_result = ""
                for index, s in enumerate(arr):
                    if index + 1 == len(arr):
                        str_result += os.path.basename(str(s))
                    else:
                        str_result += os.path.basename(str(s) + sep)

                return str_result

            file_pathA = convertStringA(fname[0], ", ")

            self.lineEdit_2.setText(file_pathA)

            def convertStringB(arr, sep):
                str_result = ""
                for index, s in enumerate(arr):
                    if index + 1 == len(arr):
                        str_result += os.path.basename(str(s))
                    else:
                        str_result += os.path.basename(str(s) + sep)

                return str_result

            file_pathB = convertStringB(fname[0], " ")

            a= file_pathB.split()
            i = 0
            while i < len(a):
                self.listWidget.addItem(a[i])
                i += 1

        else:
            pass


    def btn_remove(self):
        rn = self.listWidget.currentRow()
        self.listWidget.takeItem(rn)


    def btn_moveup(self):
        rowIndex = self.listWidget.currentRow()
        currentItem = self.listWidget.takeItem(rowIndex)
        self.listWidget.insertItem(rowIndex - 1, currentItem)
        self.listWidget.setCurrentRow(rowIndex - 1)


    def btn_movedown(self):
        rowIndex = self.listWidget.currentRow()
        currentItem = self.listWidget.takeItem(rowIndex)
        self.listWidget.insertItem(rowIndex + 1, currentItem)
        self.listWidget.setCurrentRow(rowIndex + 1)


    def btn_merge(self):
        import os
        import win32com.client as win32

        hwp = win32.gencache.EnsureDispatch("HWPFrame.HwpObject")
        hwp.RegisterModule("FilePathCheckDLL", "SecurityModule")
        hwp.Open(file_pathZ)

        import os

        BASE_DIR = os.pardir(file_pathZ)
        print(BASE_DIR)
        첨부파일리스트 = fname

        def 첨부삽입(path):
            hwp.HAction.GetDefault("InsertFile", hwp.HParameterSet.HInsertFile.HSet)
            hwp.HParameterSet.HInsertFile.filename = path
            hwp.HParameterSet.HInsertFile.KeepSection = 1
            hwp.HParameterSet.HInsertFile.KeepCharshape = 1
            hwp.HParameterSet.HInsertFile.KeepParashape = 1
            hwp.HParameterSet.HInsertFile.KeepStyle = 1
            hwp.HAction.Execute("InsertFile", hwp.HParameterSet.HInsertFile.HSet)
            return

        hwp.MovePos(3)

        for i in 첨부파일리스트:
            첨부삽입(os.path.join(BASE_DIR, i))
            hwp.MovePos(3)

        hwp.Quit()


        # function