from PyQt5 import QtWidgets
from UI.MainWindow import MainFrame
from Hash_Table import Hash
from UI.PageView import Page
from src.notepad import notepad

### Main ###
if __name__ == "__main__":
    # GUI Initialize
    app = QtWidgets.QApplication([])

    # 객체 생성
    hash_table = Hash(notepad)
    pages = Page(hash_table)
    main_frame = MainFrame(pages)

    # GUI Show
    main_frame.show()

    # GUI Quit
    app.exec_()