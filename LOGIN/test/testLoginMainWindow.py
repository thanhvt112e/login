from PyQt6.QtWidgets import QApplication, QMainWindow

from LoginMainWindowExt import LoginMainWindowExt

app = QApplication([])
myui = LoginMainWindowExt()
mainwindow = QMainWindow()
myui.setupUi(mainwindow)
mainwindow.show()
app.exec()
