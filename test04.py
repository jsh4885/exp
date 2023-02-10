from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QListView, QMainWindow, QMenuBar, QPushButton,
    QScrollBar, QSizePolicy, QStatusBar, QWidget, QFileDialog)
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(300, 380)
        MainWindow.setMinimumSize(QSize(300, 380))
        MainWindow.setMaximumSize(QSize(300, 380))

        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_3 = QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")


        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)


        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.gridLayout_3.addWidget(self.lineEdit, 0, 1, 1, 1)


        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.clicked.connect(self.btn1_FileLoad)
        self.gridLayout_3.addWidget(self.pushButton_2, 0, 2, 1, 2)


        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.gridLayout_3.addWidget(self.label_2, 1, 0, 1, 1)


        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.gridLayout_3.addWidget(self.lineEdit_2, 1, 1, 1, 1)


        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.clicked.connect(self.btn2_FileLoad)
        self.gridLayout_3.addWidget(self.pushButton_3, 1, 2, 1, 2)


        self.listView = QListView(self.centralwidget)
        self.listView.setObjectName(u"listView")
        self.gridLayout_3.addWidget(self.listView, 2, 0, 1, 3)


        self.verticalScrollBar = QScrollBar(self.centralwidget)
        self.verticalScrollBar.setObjectName(u"verticalScrollBar")
        self.verticalScrollBar.setOrientation(Qt.Vertical)
        self.gridLayout_3.addWidget(self.verticalScrollBar, 2, 3, 1, 1)


        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.gridLayout_3.addWidget(self.pushButton, 3, 1, 1, 1)


        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 300, 22))


        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")


        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)

        self.pushButton_2.clicked.connect(self.file1_name)
        self.pushButton_3.clicked.connect(self.file2_name)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi


    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\uae30\uc900\ud30c\uc77c", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\ud30c\uc77c \ucc3e\uae30", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\ubcd1\ud569\ub300\uc0c1\ud30c\uc77c", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\ud30c\uc77c \ucc3e\uae30", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\ubcd1\ud569\uc2dc\uc791", None))
    # retranslateUi


    def btn1_FileLoad(self):
        fname = QFileDialog.getOpenFileName(self, "File Load", 'D:/ubuntu/disks/',
                                            'All File(*);; Text File(*.txt);; PPtx file(*ppt *pptx)')

        if fname[0]:
            print("파일 경로")
            print(fname[0])
        else:
            print("파일 미선택")

    def btn2_FileLoad(self):
        fname = QFileDialog.getOpenFileName(self, "File Load", 'D:/ubuntu/disks/',
                                            'All File(*);; Text File(*.txt);; PPtx file(*ppt *pptx)')

        if fname[0]:
            print("파일 경로")
            print(fname[0])
        else:
            print("파일 미선택")

    def file1_name(self):
        text = "파일경로"
        self.lineEdit.setText(text)

    def file2_name(self):
        text = "파일경로"
        self.lineEdit_2.setText(text)
    # function