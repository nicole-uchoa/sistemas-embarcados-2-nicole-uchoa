import os
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QWidget
from PyQt5.QtWidgets import QTextEdit, QPushButton, QVBoxLayout, QHBoxLayout, QAction, qApp


class Notepad(QWidget):

    def __init__(self):
        super().__init__()
        self.text = QTextEdit(self)
        # Definindo os botões
        self.clr_btn = QPushButton('Limpar')
        self.sav_btn = QPushButton('Salvar')
        self.opn_btn = QPushButton('Abrir')

        self.init()

    def init(self):
        v_layout = QVBoxLayout()
        h_layout = QHBoxLayout()

        h_layout.addWidget(self.clr_btn)
        h_layout.addWidget(self.sav_btn)
        h_layout.addWidget(self.opn_btn)

        v_layout.addWidget(self.text)
        v_layout.addLayout(h_layout)

        self.sav_btn.clicked.connect(self.save_text)
        self.clr_btn.clicked.connect(self.clear_text)
        self.opn_btn.clicked.connect(self.open_text)

        self.setLayout(v_layout)
        self.setWindowTitle('PyQt5 Bloco de Notas')

        self.show()

    # Função para salvar arquivo de texto
    def save_text(self):
        filename = QFileDialog.getSaveFileName(self, 'Salvar Arquivo', os.getenv('HOME'))
        with open(filename[0], 'w') as f:
            my_text = self.text.toPlainText()
            f.write(my_text)

    # Função para abrir o arquivo de texto
    def open_text(self):
        filename = QFileDialog.getOpenFileName(self, 'Abrir Arquivo', os.getenv('HOME'))
        with open(filename[0], 'r') as f:
            file_text = f.read()
            self.text.setText(file_text)

    # Função para limpar o bloco de notas
    def clear_text(self):
        self.text.clear()


class Writer(QMainWindow):
    def __init__(self):
        super().__init__()

        self.form_widget = Notepad()
        self.setCentralWidget(self.form_widget)

        self.init()

    
    def init(self):
        bar = self.menuBar()
        file = bar.addMenu('Arquivo de Texto')

        new_action = QAction('New', self)
        new_action.setShortcut('Ctrl+N')

        save_action = QAction('&Save', self)
        save_action.setShortcut('Ctrl+S')

        open_action = QAction('&Open', self)

        quit_action = QAction('&Quit', self)

        file.addAction(new_action)
        file.addAction(save_action)
        file.addAction(open_action)
        file.addAction(quit_action)

        quit_action.triggered.connect(self.quit_trigger)
        file.triggered.connect(self.respond)

        self.show()

    def quit_trigger(self):
        qApp.quit()

    def respond(self, q):
        signal = q.text()

        if signal == 'New':
            self.form_widget.clear_text()
        elif signal == '&Open':
            self.form_widget.open_text()
        elif signal == '&Save':
            self.form_widget.save_text()


app = QApplication(sys.argv)
writer = Writer()
sys.exit(app.exec_())