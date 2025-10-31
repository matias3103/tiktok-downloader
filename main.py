import sys

import os

from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox

from ui_main_window import Ui_MainWindow

from PySide6.QtGui import QPixmap, QIcon

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        base_dir = os.path.dirname(os.path.abspath(__file__))
        image_path = os.path.join(base_dir, "download.gif")
        image_path = os.path.abspath(image_path)

        self.logo.setPixmap(QPixmap(image_path))

        self.link_edit.textChanged.connect(self.normalize_url)
        self.download_button.clicked.connect(self.download_video)


    def normalize_url(self):
        url = self.link_edit.text()
        update_url = url.split('?')[0]
        self.link_edit.setText(update_url)


    def download_video(self):
        link_tiktok = self.link_edit.text()

        if link_tiktok:
            os.system(f'python -m tiktok_downloader --snaptik --url {link_tiktok} --save video.mp4')

        else:
            QMessageBox.warning(self, 'Warning', 'Please enter a link')



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.setWindowTitle('Tiktok')
    window.setWindowIcon(QIcon("logo_aplicacao.webp"))
    window.show()
    app.exec()
