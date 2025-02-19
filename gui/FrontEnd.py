from PyQt6.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget

def on_click():
    label.setText("Hello, PyQt Desktop App!")

app = QApplication([])
window = QWidget()
window.setWindowTitle("My PyQt App")

layout = QVBoxLayout()

label = QLabel("Welcome!")
layout.addWidget(label)

button = QPushButton("Click Me")
button.clicked.connect(on_click)
layout.addWidget(button)

window.setLayout(layout)
window.show()
app.exec()