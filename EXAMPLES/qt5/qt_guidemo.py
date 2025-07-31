#!/usr/bin/env python

import sys

from PyQt5.QtWidgets import QMainWindow, QApplication
from ui_guidemo import Ui_GuiDemo

class GuiDemoMain(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        # Set up the user interface from Designer.
        self.ui = Ui_GuiDemo()
        self.ui.setupUi(self)

#        self.ui.cbGoats.isChecked()
        self.ui.btLoad.clicked.connect(self._btload_clicked)
        self.ui.btDestroy.clicked.connect(self._btdestroy_clicked)

        # Connect up menu actions
        # self.ui.actionQuit.triggered.connect(self.close)

        # Connect up buttons.
        # self.ui.BUTTON_NAME.clicked.connect(self._pushed)

    def _btload_clicked(self):
        sender = self.sender()
        print(f"{sender = }")

        self.ui.leLoad.setText("You clicked it!")

    def _btdestroy_clicked(self):
        self.ui.leLoad.setText("")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = GuiDemoMain()
    main.show()
    app.exec()


