```python
import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtGui import QIcon

class SmolDeveloperGUI(QtWidgets.QMainWindow):
    def __init__(self):
        super(SmolDeveloperGUI, self).__init__()
        uic.loadUi('assets/gui_layout.ui', self)
        self.setWindowIcon(QIcon('assets/icons/icon.png'))
        self.installButton.clicked.connect(self.on_install_clicked)

    def on_install_clicked(self):
        self.statusLabel.setText("Installation Started")
        # Call the install function from installer.py here
        # Update the progressBar and statusLabel based on the installation status

def launch_gui():
    app = QtWidgets.QApplication(sys.argv)
    window = SmolDeveloperGUI()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    launch_gui()
```