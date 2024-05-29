import sys
from PyQt5.QtWidgets import QApplication

import commandline.terminal_loop as terminal_loop
from gui.MainWindow import MainWindow


def main():
    #terminal_loop.start()
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()