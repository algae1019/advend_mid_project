from PyQt5 import QtWidgets
from PyQt5 import QtGui
from src.notepad import notepad
from B_Moore import BoyerMoore

### MainFrame ###
class MainFrame(QtWidgets.QWidget):
    def __init__(self, page):
        super().__init__()
        self.page = page

        print("MainFrame initialized!", end="\n")
        self.setupUI()

    def setupUI(self):
        self.setWindowTitle("Viewer")
        self.setGeometry(0, 0, 1200, 600)

        # GUI #
        # Layouts
        HLayout = QtWidgets.QHBoxLayout(self)
        VLayout = QtWidgets.QVBoxLayout(self)
        HLayout2 = QtWidgets.QHBoxLayout(self)
        HLayout3 = QtWidgets.QHBoxLayout(self)
        # PlainText
        self.viewTxt = QtWidgets.QTextBrowser()
        self.viewSort = QtWidgets.QTextBrowser()
        self.searchBox = QtWidgets.QTextEdit("", self)
        self.replaceBox = QtWidgets.QTextEdit("", self)
        self.indexBox = QtWidgets.QLineEdit("", self)
        self.indexBox.setValidator(QtGui.QIntValidator())
        # Buttons
        self.searchBtn = QtWidgets.QPushButton("Search", self)
        self.replaceBtn = QtWidgets.QPushButton("Replace", self)
        self.indexOkBtn = QtWidgets.QPushButton("OK", self)
        self.indexPrevBtn = QtWidgets.QPushButton("< Prev", self)
        self.indexNextBtn = QtWidgets.QPushButton("Next >", self)

        # 이벤트 연결
        self.indexOkBtn.clicked.connect(self.Okbtn_clicked)
        self.indexPrevBtn.clicked.connect(self.Prevbtn_clicked)
        self.indexNextBtn.clicked.connect(self.Nextbtn_clicked)
        self.searchBtn.clicked.connect(self.search_text)
        self.replaceBtn.clicked.connect(self.replace_text)

        # GUI 구성
        HLayout.addWidget(self.viewTxt);         HLayout.addLayout(VLayout)
        HLayout.setStretch(0, 5);                HLayout.setStretch(1, 2)


        VLayout.addWidget(self.searchBox);       VLayout.addWidget(self.replaceBox)
        VLayout.addLayout(HLayout2);             VLayout.addWidget(self.viewSort)
        VLayout.addLayout(HLayout3)

        VLayout.setStretch(0, 1);                VLayout.setStretch(1, 1)
        VLayout.setStretch(2, 1);                VLayout.setStretch(3, 10)
        VLayout.setStretch(4, 1)


        HLayout2.addWidget(self.searchBtn);      HLayout2.addWidget(self.replaceBtn)


        HLayout3.addWidget(self.indexBox);       HLayout3.addWidget(self.indexOkBtn)
        HLayout3.addWidget(self.indexPrevBtn);   HLayout3.addWidget(self.indexNextBtn)


        self.searchBox.setPlaceholderText("Search to...")
        self.replaceBox.setPlaceholderText("Replace to...")
        self.indexBox.setPlaceholderText(f"1 ~ {len(self.page.content)}")
        self.viewTxt.setPlainText("\n".join(notepad))


    ### 페이지 관련 이벤트 ###
    def viewSort_Setpage(self, page, index):
            self.viewSort.setPlainText(page.content[index])

    def Okbtn_clicked(self):
        try:
            index = int(self.indexBox.text()) - 1

            if index < 0:
                self.indexBox.setText('1')
                raise IndexError("입력 범위 초과")

            self.viewSort_Setpage(self.page, index)

        except ValueError:
            QtWidgets.QMessageBox.about(self, "Error", "유효한 정수를 입력하세요.")
            self.indexBox.setText('1')

        except IndexError:
            QtWidgets.QMessageBox.about(self, "Error", "입력 범위 초과")
            self.indexBox.setText(str(len(self.page.content)))


    def Prevbtn_clicked(self):
        try:
            if self.indexBox.text() == '':
                self.indexBox.setText('1')
                raise ValueError("유효한 정수를 입력하세요.")
            
            self.indexBox.setText(str(int(self.indexBox.text()) - 1))
            index = int(self.indexBox.text()) - 1

            if index < 0:
                self.indexBox.setText('1')
                raise ValueError("입력 범위 초과")

            self.viewSort_Setpage(self.page, index)

        except ValueError:
            QtWidgets.QMessageBox.about(self, "Error", "입력 범위 초과")

        except IndexError:
            QtWidgets.QMessageBox.about(self, "Error", "입력 범위 초과")
            self.indexBox.setText(str(len(self.page.content)))

        


    def Nextbtn_clicked(self):
        try:
            if self.indexBox.text() == '':
                self.indexBox.setText(str(len(self.page.content)))
                raise ValueError("유효한 정수를 입력하세요.")
            
            self.indexBox.setText(str(int(self.indexBox.text()) + 1))
            index = int(self.indexBox.text()) - 1

            if index < 0:
                self.indexBox.setText('1')
                raise ValueError("입력 범위 초과")

            self.viewSort_Setpage(self.page, index)

        except ValueError:
            QtWidgets.QMessageBox.about(self, "Error", "입력 범위 초과")

        except IndexError:
            QtWidgets.QMessageBox.about(self, "Error", "입력 범위 초과")
            self.indexBox.setText(str(len(self.page.content)))



    ### 검색 및 대체 관련 이벤트 ###
    def search_text(self):
        pattern = self.searchBox.toPlainText()
        text = self.viewTxt.toPlainText()

        if pattern:
            bm = BoyerMoore(pattern)
            match_index = bm.search(text)
            
            if match_index:
                self.textHighlighting(match_index, len(pattern))
            else:
                QtWidgets.QMessageBox.information(self, "찾을 수 없음", f"'{pattern}' 문서 내에 존재하지 않습니다.")


    def clear_highlight(self):
        cursor = self.viewTxt.textCursor()
        cursor.select(QtGui.QTextCursor.Document)
        format = QtGui.QTextCharFormat()
        cursor.setCharFormat(format)


    def textHighlighting(self, index, length):
        self.clear_highlight()

        cursor = self.viewTxt.textCursor()
        format = QtGui.QTextCharFormat()
        format.setBackground(QtGui.QBrush(QtGui.QColor("yellow")))

        cursor.beginEditBlock()
        for i in index:
            cursor.setPosition(i)
            cursor.movePosition(QtGui.QTextCursor.Right, QtGui.QTextCursor.KeepAnchor, length)
            cursor.mergeCharFormat(format)
        cursor.endEditBlock()



    def replace_text(self):
        pattern = self.searchBox.toPlainText()
        replace = self.replaceBox.toPlainText()
        text = self.viewTxt.toPlainText()

        if pattern:
            bm = BoyerMoore(pattern)
            match_index = bm.search(text)

            # Replace matches in reverse order to maintain indices
            for index in reversed(match_index):
                text = text[:index] + replace + text[index + len(pattern):]

            self.viewTxt.setPlainText(text)