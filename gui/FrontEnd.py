from PyQt6.QtWidgets import (
    QApplication, QLabel, QComboBox, QPushButton,
    QVBoxLayout, QHBoxLayout, QWidget, QLineEdit
)
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt


class CryptKeyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # Set window title and size
        self.setWindowTitle("CryptKey")
        self.setStyleSheet("background-color: white;")
        self.setGeometry(100, 100, 800, 500)

        # Title Label
        title = QLabel("CryptKey", self)
        title.setFont(QFont("Arial", 30, QFont.Weight.Bold))
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet("background-color: black; color: white; padding: 20px;")

        # Drop-down options (Choose How, Length, Special Characters, Numbers, Upper Cases)
        self.choose_how = self.create_dropdown(["Custom", "Random"])
        self.length = self.create_dropdown(["8", "12", "16", "20", "24", "32"], default="16")
        self.special_chars = self.create_dropdown(["None", "Some", "All"])
        self.numbers = self.create_dropdown(["Yes", "No"])
        self.uppercase = self.create_dropdown(["Yes", "No"])

        # Password Display Box
        self.password_display = QLineEdit()
        self.password_display.setReadOnly(True)
        self.password_display.setPlaceholderText("Your Password")
        self.password_display.setStyleSheet("""
            background-color: lightgray; 
            border-radius: 5px; 
            padding: 10px;
        """)

        # Save Button
        save_button = QPushButton("Save")
        save_button.setStyleSheet("""
            background-color: white; 
            border: 2px solid black; 
            border-radius: 10px; 
            padding: 10px; 
            font-size: 16px;
        """)

        # Layouts
        main_layout = QVBoxLayout()
        main_layout.addWidget(title)

        form_layout = QHBoxLayout()
        form_layout.addLayout(self.create_form_section("Choose How", self.choose_how))
        form_layout.addLayout(self.create_form_section("Length", self.length))
        form_layout.addLayout(self.create_form_section("Special Characters", self.special_chars))

        second_row_layout = QHBoxLayout()
        second_row_layout.addLayout(self.create_form_section("Numbers", self.numbers))
        second_row_layout.addLayout(self.create_form_section("Upper Cases", self.uppercase))

        # Password Box Layout
        password_layout = QVBoxLayout()
        password_label = QLabel("Your Password")
        password_label.setFont(QFont("Arial", 12))
        password_layout.addWidget(password_label)
        password_layout.addWidget(self.password_display)

        # Button Layout
        button_layout = QHBoxLayout()
        button_layout.addWidget(save_button, alignment=Qt.AlignmentFlag.AlignCenter)

        # Add layouts to main layout
        main_layout.addLayout(form_layout)
        main_layout.addLayout(second_row_layout)
        main_layout.addLayout(password_layout)
        main_layout.addLayout(button_layout)

        self.setLayout(main_layout)

    def create_dropdown(self, options, default=None):
        dropdown = QComboBox()
        dropdown.addItems(options)
        if default:
            dropdown.setCurrentText(default)
        dropdown.setStyleSheet("""
            background-color: lightgray; 
            border-radius: 10px; 
            padding: 5px;
        """)
        return dropdown

    def create_form_section(self, label_text, widget):
        layout = QVBoxLayout()
        label = QLabel(label_text)
        label.setFont(QFont("Arial", 12))
        layout.addWidget(label, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(widget, alignment=Qt.AlignmentFlag.AlignCenter)
        return layout


# Run the PyQt App
if __name__ == "__main__":
    app = QApplication([])
    window = CryptKeyApp()
    window.show()
    app.exec()