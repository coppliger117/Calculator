from gui2 import *
from Logic2 import *
import sys

def main():
    import sys
    app = QApplication([])
    Dialog = Logic()
    Dialog.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
