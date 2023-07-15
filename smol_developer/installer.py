```python
import os
import sys
from PyQt5.QtWidgets import QApplication, QMessageBox

def install():
    try:
        # Assuming the installation process involves copying files to a specific directory
        os.system("cp -r /path/to/smol_developer /path/to/installation/directory")
        return "installationCompleted"
    except Exception as e:
        print(e)
        return "installationFailed"

def main():
    app = QApplication(sys.argv)

    # Show a message box to confirm installation
    msgBox = QMessageBox()
    msgBox.setText("Do you want to install Smol Developer?")
    msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
    returnValue = msgBox.exec()

    if returnValue == QMessageBox.Yes:
        installation_status = install()
        if installation_status == "installationCompleted":
            msgBox.setText("Installation completed successfully.")
        else:
            msgBox.setText("Installation failed.")
        msgBox.exec()

if __name__ == "__main__":
    main()
```