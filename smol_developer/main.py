```python
import sys
import os
from PyQt5 import QtWidgets

from smol_developer import installer, gui, setup

def main():
    app = QtWidgets.QApplication(sys.argv)

    # Setup the application
    setup.setup()

    # Launch the GUI
    gui.launch_gui()

    # Install the application
    installer.install()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
```