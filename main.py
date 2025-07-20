from PySide6 import QtWidgets
from ui import homeTab
import sys



class MainApplicaiton():

    def start(self):
        app = QtWidgets.QApplication(sys.argv)
        self.landing = homeTab.HomeTab()
        self.landing.showFullScreen()
        sys.exit(app.exec())


if __name__ == '__main__':
    MainApplicaiton().start()




