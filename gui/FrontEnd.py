from PyQt6.QtWidgets import (
    QApplication, QLabel, QComboBox, QPushButton,
    QVBoxLayout, QHBoxLayout, QWidget, QLineEdit, QSpacerItem, QSizePolicy
)
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt
import subprocess


class CryptKeyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # Set window properties
        self.setWindowTitle("CryptKey")
        self.setStyleSheet("background-color: white;")
        self.setGeometry(100, 100, 900, 600)

        # Title Bar (Ensures Full Width)
        title_bar = QLabel("CryptKey", self)
        title_bar.setFont(QFont("Arial", 36, QFont.Weight.Bold))
        title_bar.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title_bar.setStyleSheet("""
            background-color: black;
            color: white;
            padding: 20px;
            width: 100%;
        """)

        # Dropdown Styling (Rounded Edges & Improved Visibility)
        dropdown_style = """
            QComboBox {
                background-color: lightgray;
                border-radius: 15px;  /* Rounded edges */
                padding: 5px 15px;
                font-size: 16px;
                color: black;
                min-width: 100px;
                border: 1px solid black;
            }
            QComboBox::drop-down {
                border: 0px;
            }
            QComboBox QAbstractItemView {
                background-color: white;
                border: 1px solid black;
                selection-background-color: lightgray;
                color: black;
            }
        """

        # Create dropdowns
        self.choose_how = self.create_dropdown(["Custom", "Random"], dropdown_style)
        self.length = self.create_dropdown(["8", "12", "16", "20", "24", "32"], dropdown_style, default="16")
        self.special_chars = self.create_dropdown(["None", "Some", "All"], dropdown_style)
        self.numbers = self.create_dropdown(["Yes", "No"], dropdown_style)
        self.uppercase = self.create_dropdown(["Yes", "No"], dropdown_style)

        # Create Labels Above Dropdowns (Increase Text Size, Reduce Spacing)
        row1_layout = QHBoxLayout()
        row1_layout.addLayout(self.create_form_section("Choose How", self.choose_how))
        row1_layout.addLayout(self.create_form_section("Length", self.length))
        row1_layout.addLayout(self.create_form_section("Special Characters", self.special_chars))

        row2_layout = QHBoxLayout()
        row2_layout.addLayout(self.create_form_section("Numbers", self.numbers))
        row2_layout.addLayout(self.create_form_section("Upper Cases", self.uppercase))

        # Password Display Box
        self.password_display = QLineEdit()
        self.password_display.setReadOnly(True)
        self.password_display.setPlaceholderText("Your Password")
        self.password_display.setStyleSheet("""
            background-color: lightgray; 
            color: black;
            border-radius: 5px; 
            padding: 15px;
            font-size: 18px;
        """)

        # Darker "Your Password" Text
        password_label = QLabel("Your Password")
        password_label.setFont(QFont("Arial", 16, QFont.Weight.Bold))  # Increased font size
        password_label.setStyleSheet("color: black; padding-bottom: 5px;")  # Reduced spacing below label

        # Save Button (Clickable with Visual Feedback)
        self.save_button = QPushButton("Save")
        self.save_button.setStyleSheet("""
            background-color: white; 
            border: 2px solid black; 
            border-radius: 20px; 
            padding: 12px 20px; 
            font-size: 16px;
            color: black;
        """)
        self.save_button.pressed.connect(self.on_save_click)

        # Main Layout
        main_layout = QVBoxLayout()
        main_layout.addWidget(title_bar)

        main_layout.addSpacing(10)  # Reduce spacing after the title
        main_layout.addLayout(row1_layout)
        main_layout.addSpacing(10)  # Reduce spacing between rows
        main_layout.addLayout(row2_layout)
        main_layout.addSpacing(30)  # Reduce space before password box

        # Password Layout
        password_layout = QVBoxLayout()
        password_layout.addWidget(password_label, alignment=Qt.AlignmentFlag.AlignCenter)
        password_layout.addWidget(self.password_display)
        main_layout.addLayout(password_layout)

        main_layout.addSpacing(10)  # Reduce space before button

        # Save Button Layout (Centered)
        button_layout = QHBoxLayout()
        button_layout.addItem(QSpacerItem(40, 10, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum))
        button_layout.addWidget(self.save_button)
        button_layout.addItem(QSpacerItem(40, 10, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum))
        main_layout.addLayout(button_layout)

        self.setLayout(main_layout)

    def create_dropdown(self, options, style, default=None):
        dropdown = QComboBox()
        dropdown.addItems(options)
        dropdown.setStyleSheet(style)
        if default:
            dropdown.setCurrentText(default)
        return dropdown

    def create_form_section(self, label_text, widget):
        layout = QVBoxLayout()
        label = QLabel(label_text)
        label.setFont(QFont("Arial", 14, QFont.Weight.Bold))  # Increase text size
        label.setStyleSheet("color: black; padding-bottom: 2px;")  # Reduce spacing below label
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(label)
        layout.addWidget(widget, alignment=Qt.AlignmentFlag.AlignCenter)
        return layout

    def on_save_click(self):
        """Handles the save button click event and generates password via C++ backend"""
        self.save_button.setStyleSheet("""
            background-color: lightgray; 
            border: 2px solid black; 
            border-radius: 20px; 
            padding: 12px 20px; 
            font-size: 16px;
            color: black;
        """)

        length = self.length.currentText()
        use_upper = self.uppercase.currentText() == "Yes"
        use_numbers = self.numbers.currentText() == "Yes"
        use_special = self.special_chars.currentText() != "None"

        try:
            result = subprocess.run([
                "../build/CryptKey",
                "--length", length,
                "--upper", str(use_upper).lower(),
                "--numbers", str(use_numbers).lower(),
                "--special", str(use_special).lower()
            ], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

            if result.returncode == 0:
                self.password_display.setText(result.stdout.strip())
            else:
                self.password_display.setText("Error: " + result.stderr.strip())

        except Exception as e:
            self.password_display.setText("Execution failed")
            print("Error:", e)


# Run the PyQt App
if __name__ == "__main__":
    app = QApplication([])
    window = CryptKeyApp()
    window.show()
    app.exec()