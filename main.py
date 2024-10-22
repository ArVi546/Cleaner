import sys
import os
import shutil
from pathlib import Path
from backwork import *
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import *

types_of_count = ["KB", "MB", "GB"]

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CompCleaner")

        self.direct = "."
        self.field = 0
        self.type = 0
        self.paths = paths

        self.dir_enter = QLineEdit(self)
        self.dir_enter.setFixedWidth(300)
        self.dir_enter.move(20, 20)
        self.dir_enter.setPlaceholderText("Enter directory...")
        self.dir_enter.textChanged.connect(self.dir_enter_command)

        self.field_enter = QLineEdit(self)
        self.field_enter.setFixedWidth(100)
        self.field_enter.move(450, 20)
        self.field_enter.setPlaceholderText(f"Enter field in {types_of_count[self.type]}...")
        self.field_enter.textChanged.connect(self.field_enter_command)

        self.type_enter = QComboBox(self)
        self.type_enter.addItems(["KB", "MB", "GB"])
        self.type_enter.setFixedWidth(50)
        self.type_enter.move(575, 20)
        self.type_enter.currentIndexChanged.connect(self.type_enter_command)

        self.start_button = QPushButton(self)
        self.start_button.setText("Start Program")
        self.start_button.setFixedWidth(125)
        self.start_button.move(500, 60)
        self.start_button.clicked.connect(self.start_program)

        self.exit = QListWidget(self)
        self.exit.move(20,100)
        self.exit.setFixedSize(300, 250)

        self.search_button = QPushButton(self)
        self.search_button.setText("Search")
        self.search_button.clicked.connect(self.search_command)
        self.search_button.move(330, 20)

        self.delete_button = QPushButton(self)
        self.delete_button.setText("Delete")
        self.delete_button.clicked.connect(self.delete_file)
        self.delete_button.move(330, 140)

        self.open_button = QPushButton(self)
        self.open_button.setText("Open")
        self.open_button.clicked.connect(self.open_file)
        self.open_button.move(330, 100)

        self.author = QLabel(self)
        self.author.move(600, 370)
        self.author.setText("by ArVi")

        self.setFixedSize(QSize(650, 400))

    def dir_enter_command(self):
        self.direct = self.dir_enter.text()

    def field_enter_command(self):
        self.field = int(self.field_enter.text())

    def type_enter_command(self, s):
        self.type = s

    def start_program(self):
        self.exit.clear()
        files = counting(self.direct, self.type, self.field)
        self.exit.addItems(files)

    def search_command(self):
        self.wb_patch = QFileDialog.getExistingDirectoryUrl()
        self.dir_enter.setText(str(self.wb_patch.url()).replace("file:///", ""))

    def open_file(self):
        os.system(f"explorer {self.paths[self.exit.currentRow()].resolve()}")
    def delete_file(self):
        if Path(self.paths[self.exit.currentRow()].resolve()).is_dir():
            #print(str(self.paths[self.exit.currentRow()].resolve()))
            shutil.rmtree(self.paths[self.exit.currentRow()].resolve())
        else:
            os.remove(self.paths[self.exit.currentRow()].resolve())
        self.start_program()





app = QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()
