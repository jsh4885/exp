from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.button = QPushButton(parent=self)
        self.setCentralWidget(self.button)
        self.button.setCheckable(True)
        self.button.clicked.connect(self.button_clicked)
        self.click_count = 0

    def button_clicked(self):
        self.click_count += 1
        self.button.setText(f"{self.click_count}번 클릭함")


app = QApplication()
window = MainWindow()
window.show()
app.exec_()