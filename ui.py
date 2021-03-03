import excel
import countries
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QTextEdit, QListView, QMessageBox, QLabel
from PyQt5 import uic
import sys
import os
import easygui


class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        uic.loadUi("test2.ui", self)

        # find the widgets in the xml file
        self.label_capitala = self.findChild(QLabel,"label_capitala")
        self.label_continent = self.findChild(QLabel,"label_continent")
        self.label_moneda = self.findChild(QLabel,"label_moneda")
        self.label_populatia = self.findChild(QLabel,"label_populatia")
        self.label_judete = self.findChild(QLabel,"label_judete")
        self.label_suprafata = self.findChild(QLabel,"label_suprafata")
        self.label_imezone = self.findChild(QLabel,"label_imezone")
        self.label_wiki_page = self.findChild(QLabel,"label_wiki_page")
        self.textedit = self.findChild(QTextEdit, "textEdit_search")
        self.button = self.findChild(QPushButton, "pushButton_export")
        self.listView = self.findChild(QListView, "QListWidget_countries")
        self.button.clicked.connect(self.clickedBtn)
        self.listView.itemClicked.connect(self.clickedLView)
        self.populate_view_with_countries()
        self.show()

    def clickedBtn(self):
        desk_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'desktop')
        path = easygui.fileopenbox(msg="", title="Alege fisierul", default=desk_path, filetypes=["*.xlsx"],
                                   multiple=False)
        wb = excel.open_xl(path)
        countries = excel.countries_list(wb)
        for keys, item in countries.items():
            self.listView.addItem(item)

    def clickedLView(self, item):
        # QMessageBox.information(self, "ListWidget", "ListWidget: " + item.text())
        self.textEdit.setPlainText(countries.country_to_continent(item.text()))

    def populate_view_with_countries(self):
        desk_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'desktop')

        countries_list = countries.get_all_countries_by_country()
        for item in countries_list:
            self.listView.addItem(item)

app = QApplication(sys.argv)
window = UI()
app.exec_()
