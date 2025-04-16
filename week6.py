from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 400)

        self.centralwidget = QtWidgets.QWidget(MainWindow)

        # Label utama yang menampilkan NIM
        self.label = QtWidgets.QLabel("F1D022127", self.centralwidget)
        self.label.setGeometry(QtCore.QRect(100, 50, 300, 100))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setStyleSheet("font-size: 30pt; color: rgb(0, 0, 0); background-color: rgb(255, 255, 255);")
        
        # Nama dan NIM (keaslian tugas)
        self.identity_label = QtWidgets.QLabel("Nama: Kayla Mizanti\nNIM: F1D022127", self.centralwidget)
        self.identity_label.setGeometry(QtCore.QRect(10, 330, 300, 40))
        self.identity_label.setStyleSheet("font-size: 10pt; color: gray;")

        # Slider Font Size
        self.fontSizeLabel = QtWidgets.QLabel("Font Size", self.centralwidget)
        self.fontSizeLabel.setGeometry(QtCore.QRect(30, 160, 100, 20))
        self.fontSlider = QtWidgets.QSlider(QtCore.Qt.Horizontal, self.centralwidget)
        self.fontSlider.setGeometry(QtCore.QRect(130, 160, 300, 20))
        self.fontSlider.setMinimum(20)
        self.fontSlider.setMaximum(60)
        self.fontSlider.setValue(30)
        self.fontSlider.valueChanged.connect(self.updateStyle)

        # Slider Font Color
        self.fontColorLabel = QtWidgets.QLabel("Font Color (Grayscale)", self.centralwidget)
        self.fontColorLabel.setGeometry(QtCore.QRect(30, 200, 150, 20))
        self.fontColorSlider = QtWidgets.QSlider(QtCore.Qt.Horizontal, self.centralwidget)
        self.fontColorSlider.setGeometry(QtCore.QRect(180, 200, 250, 20))
        self.fontColorSlider.setMinimum(0)
        self.fontColorSlider.setMaximum(255)
        self.fontColorSlider.setValue(0)
        self.fontColorSlider.valueChanged.connect(self.updateStyle)

        # Slider Background Color
        self.bgColorLabel = QtWidgets.QLabel("Background Color (Grayscale)", self.centralwidget)
        self.bgColorLabel.setGeometry(QtCore.QRect(30, 240, 180, 20))
        self.bgColorSlider = QtWidgets.QSlider(QtCore.Qt.Horizontal, self.centralwidget)
        self.bgColorSlider.setGeometry(QtCore.QRect(210, 240, 220, 20))
        self.bgColorSlider.setMinimum(0)
        self.bgColorSlider.setMaximum(255)
        self.bgColorSlider.setValue(255)
        self.bgColorSlider.valueChanged.connect(self.updateStyle)

        MainWindow.setCentralWidget(self.centralwidget)

    def updateStyle(self):
        font_size = self.fontSlider.value()
        font_gray = self.fontColorSlider.value()
        bg_gray = self.bgColorSlider.value()

        self.label.setStyleSheet(
            f"font-size: {font_size}pt; "
            f"color: rgb({font_gray}, {font_gray}, {font_gray}); "
            f"background-color: rgb({bg_gray}, {bg_gray}, {bg_gray});"
        )

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.setWindowTitle("PV25 Week 6 - Slider Assignment")
    MainWindow.show()
    sys.exit(app.exec_())
