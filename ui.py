import countries
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QTextEdit, QListView, QMessageBox, QLabel, \
    QCommandLinkButton, QLineEdit, QListWidgetItem
from PyQt5 import uic
import sys
import os
import easygui
import json
from pygal_maps_world.maps import World

countries_list = countries.get_all_countries_by_country()


class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        uic.loadUi("test2.ui", self)

        # declarare label-uri
        self.label_capitala = self.findChild(QLabel, "label_capitala")
        self.label_continent = self.findChild(QLabel, "label_continent")
        self.label_moneda = self.findChild(QLabel, "label_moneda")
        self.label_populatia = self.findChild(QLabel, "label_populatia")
        self.label_suprafata = self.findChild(QLabel, "label_suprafata")
        self.label_timezone = self.findChild(QLabel, "label_timezone")

        # declarare label-uri
        self.label_capitala2 = self.findChild(QLabel, "label_capitala_2")
        self.label_continent2 = self.findChild(QLabel, "label_continent_2")
        self.label_moneda2 = self.findChild(QLabel, "label_moneda_2")
        self.label_populatia2 = self.findChild(QLabel, "label_populatia_2")
        self.label_suprafata2 = self.findChild(QLabel, "label_suprafata_2")
        self.label_timezone2 = self.findChild(QLabel, "label_timezone_2")
        self.label_judete = self.findChild(QLabel, "label_judete")

        # declarare label wiki page si ascundere
        self.label_wiki_page = self.findChild(QLabel, "label_wiki_page")
        self.label_wiki_page.hide()

        # declarare buton care duce spre wiki
        self.commandLinkButton_wiki = self.findChild(QCommandLinkButton, "commandLinkButton_wiki")
        self.commandLinkButton_wiki.clicked.connect(lambda: self.go_to_wiki(self.label_wiki_page.text()))

        # declarare input box search
        self.textedit = self.findChild(QLineEdit, "textEdit_search")
        self.textedit.textChanged.connect(self.sync_lineEdit)
        # declarare buton export
        self.button = self.findChild(QPushButton, "pushButton_export")
        self.button.clicked.connect(self.clickedBtn)

        # declarare list view tari
        self.listView = self.findChild(QListView, "QListWidget_countries")
        self.listView.itemClicked.connect(self.clickedLView)

        # declarare list view judete
        self.qListView_judete = self.findChild(QListView, "qListWidget_judete")

        # initializare labeluri
        self.initialize_interface()

        # populare list cu toate tarile si afisare GUI
        self.populate_view_with_countries()
        self.show()

    def clickedBtn(self):
        try:
            global capitala
            capitala = self.label_capitala.text()
            if capitala:
                path = easygui.filesavebox(msg="", title="Salvati datele", default=selected_country + ".txt",
                                           filetypes=None)


                # salvare date in fisier txt
                file = open(path, "w")
                file.write("Tara: " + tara + "\n")
                file.write("Continent: " + continent + "\n")
                file.write("Capitala: " + capitala + "\n")
                file.write("Populatie: " + populatie + "\n")
                file.write("Suprafata: " + suprafata + "\n")
                file.write("Moneda: " + moneda + "\n")
                file.write("Ora GMT: " + timezone + "\n")
                file.write("Provincii: " + str(provincii) + "\n")
                file.write("All data: " + json.dumps(countries.get_all_info_for_country(tara)) + "\n")
                file.close()

                #desenam harta lumii si o salvam

                worldmap_chart = World()
                worldmap_chart.title = tara
                worldmap_chart.add('Tara aleasa', [countries.get_country_code_from_country(tara)])
                path = path[:len(path)-4]
                print(path)
                worldmap_chart.render_to_file(path + ".svg")
            else:
                self.prompt_message("Trebuie sa selectati o tara!", "Eroare")
        except Exception as ex:
            print(ex)
            # self.textEdit.setPlainText(countries.country_to_continent(item.text()))

    def clickedLView(self, item):
        try:
            global selected_country
            selected_country = item.text()
            self.label_capitala2.show()
            self.label_continent2.show()
            self.label_moneda2.show()
            self.label_populatia2.show()
            self.label_suprafata2.show()
            self.label_timezone2.show()
            self.label_judete.show()

            self.qListView_judete.clear()
            self.label_capitala.setText(str(countries.get_capital_by_country(str(item.text()))))
            self.label_continent.setText(str(countries.get_continent_by_country(str(item.text()))))
            self.label_moneda.setText(str(countries.get_currencies_by_country(str(item.text()))))
            self.label_timezone.setText(str(countries.get_timezone_by_country(str(item.text()))))
            self.label_wiki_page.setText(str(countries.get_wiki_page_by_country(str(item.text()))))
            self.label_populatia.setText(str(countries.get_population_by_country(str(item.text()))))
            self.label_suprafata.setText(str(countries.get_area_by_country(str(item.text()))) + " m2")
            self.qListView_judete.show()
            self.commandLinkButton_wiki.show()
            global tara
            tara = str(item.text())
            global continent
            continent = self.label_continent.text()
            global moneda
            moneda = self.label_moneda.text()
            global populatie
            populatie = self.label_populatia.text()
            global suprafata
            suprafata = self.label_suprafata.text()
            global timezone
            timezone = self.label_timezone.text()
            global wiki_page_url
            wiki_page_url = self.label_wiki_page.text()
            global provincii
            provincii = []
            judete = countries.get_provinces_by_country(str(item.text()))
            for item in judete:
                self.qListView_judete.addItem(item)
                provincii.append(item)


        except:
            self.label_capitala.setText("")
            self.label_continent.setText("")
            self.label_moneda.setText("")
            self.label_timezone.setText("")
            self.label_populatia.setText("")
            self.label_suprafata.setText("")
            self.commandLinkButton_wiki.hide()
            self.qListView_judete.hide()
            self.label_capitala2.hide()
            self.label_continent2.hide()
            self.label_moneda2.hide()
            self.label_populatia2.hide()
            self.label_suprafata2.hide()
            self.label_timezone2.hide()
            self.label_judete.hide()
            self.prompt_message("Nu exista date pentru: " + item.text(), "Eroare")


    def populate_view_with_countries(self):
        for item in countries_list:
            self.listView.addItem(item.capitalize())

    def go_to_wiki(self, wiki_page):
        os.system("start \"\" " + wiki_page)

    # input box pentru cautarea tarii
    def sync_lineEdit(self, text):
        self.listView.clear()
        items = []
        last_item = QListWidgetItem()
        for country in countries_list:
            if country.find(text.lower()) != -1:
                items.append(country)
                item = QListWidgetItem(country.capitalize())
                last_item = item
                self.listView.addItem(item)
        if len(items) == 1:
            self.listView.setCurrentItem(last_item)
            self.clickedLView(last_item)
        else:
            self.initialize_interface()

    def initialize_interface(self):
        # initializare label-uri
        self.label_capitala.setText("")
        self.label_continent.setText("")
        self.label_moneda.setText("")
        self.label_timezone.setText("")
        self.label_populatia.setText("")
        self.label_suprafata.setText("")
        self.commandLinkButton_wiki.hide()
        self.qListView_judete.hide()

        self.label_capitala2.hide()
        self.label_continent2.hide()
        self.label_moneda2.hide()
        self.label_populatia2.hide()
        self.label_suprafata2.hide()
        self.label_timezone2.hide()
        self.label_judete.hide()

    def prompt_message(self, text, title):
        msg = QMessageBox()
        msg.setText(text)
        msg.setWindowTitle(title)
        msg.setIcon(QMessageBox.Information)
        msg.setStyleSheet("QLabel{ color: white}")
        msg.setStyleSheet("text-color: rgb(255, 255, 255);")
        msg.exec_()

app = QApplication(sys.argv)
window = UI()
app.exec_()
