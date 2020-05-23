# This Python file uses the following encoding: utf-8
import sys
import os


from PySide2.QtWidgets import QApplication, QWidget
from PySide2.QtCore import QFile
from PySide2.QtUiTools import QUiLoader

from PySide2.QtWidgets import QPushButton
from PySide2.QtCore import Slot

xx = QWidget

# Greetings
@Slot()
def say_hello():
    print("Button clicked, Hello!")
    xx.label.setText('xy')


class Test12(QWidget):
    def __init__(self):
        super(Test12, self).__init__()
        self.load_ui()


    def load_ui(self):
        loader = QUiLoader()
        path = os.path.join(os.path.dirname(__file__), "form.ui")
        ui_file = QFile(path)
        ui_file.open(QFile.ReadOnly)

        global xx
        xx = loader.load(ui_file, self)

        xx.btn.clicked.connect(say_hello)
        xx.label.setText('abc')

        ui_file.close()



if __name__ == "__main__":
    app = QApplication([])
    widget = Test12()
    widget.show()
    sys.exit(app.exec_())
