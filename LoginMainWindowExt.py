
from PyQt6.QtWidgets import QMessageBox

from LOGIN.lib.dataconnector import DataConnector
from LOGINMainWindow import Ui_MainWindow


class LoginMainWindowExt(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.setupSignalAndSlot()

    def showWindow(self):
        self.MainWindow.show()

    def setupSignalAndSlot(self):
        self.pushButtonLogin.clicked.connect(self.process_login)
        self.pushButtonSign_up.clicked.connect(self.process_signup)
        self.pushButtonClose.clicked.connect(self.closeEvent)

    def process_login(self):
        uid = self.lineEditUserName.text()
        pwd = self.lineEditPassword.text()
        dc = DataConnector()
        emp = dc.login(uid, pwd)
        if emp is None:
            self.show_message("Login Failed", "Invalid username or password.")
        else:
            self.show_message("Login Successful", "Welcome back!")
            # Chuyển sang màn hình chính tại đây

    def process_signup(self):
        uid = self.lineEditUserName.text()
        pwd = self.lineEditPassword.text()
        if not uid or not pwd:
            self.show_message("Signup Failed", "Username and Password cannot be empty.")
            return

        dc = DataConnector()
        if dc.signup(uid, pwd):
            self.show_message("Signup Successful", "Account created successfully.")
            # Chuyển sang màn hình chính tại đây
        else:
            self.show_message("Signup Failed", "An error occurred while signing up.")

    def show_message(self, title, text):
        msg = QMessageBox(self.MainWindow)
        msg.setWindowTitle(title)
        msg.setText(text)
        msg.exec()

    def closeEvent(self, event):
        msg = QMessageBox()
        msg.setText(f"Are you sure you want to exit ?")
        msg.setWindowTitle("Exit Confirmation")
        msg.setIcon(QMessageBox.Icon.Question)
        buttons = QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        msg.setStandardButtons(buttons)
        result = msg.exec()
        if result == QMessageBox.StandardButton.Yes:
            self.MainWindow.close()