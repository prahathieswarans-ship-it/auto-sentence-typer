from PyQt6.QtWidgets import (
    QWidget,
    QLabel,
    QTextEdit,
    QVBoxLayout,
    QSpinBox,
    QDoubleSpinBox,
    QPushButton,
    QMessageBox
)

from PyQt6.QtCore import QTimer

from workers.typing_worker import TypingWorker


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.remaining_seconds = 0
        self.setWindowTitle("Auto Sentence Typer")
        self.setGeometry(100, 100, 500, 400)
        self.init_ui()



    def start_typing(self):

        self.text = self.text_input.toPlainText()

        if not self.text.strip():
            QMessageBox.warning(
                self,
                "Input Required",
                "Please enter some text before starting."
            )
            return

        self.start_button.setEnabled(False)
        self.remaining_seconds = self.delay_input.value()
        self.stop_requested = False
        self.countdown_label.setText("Starting in "+ str(self.remaining_seconds) + " seconds")
        self.timer.start(1000)

    def stop_typing(self):
        if self.timer.isActive():
            self.timer.stop()
            self.remaining_seconds = 0
            self.countdown_label.setText("Countdown Stopped")
            self.start_button.setEnabled(True)
        elif self.worker is not None and self.worker.isRunning():
            self.worker.requestInterruption()
            self.stop_requested = True
            self.countdown_label.setText("Stopping...")


    def update_countdown(self):
        self.remaining_seconds -= 1

        if self.remaining_seconds == 0:


            self.countdown_label.setText("Countdown Completed")
            print("Countdown Completed")
            self.timer.stop()

            self.worker = TypingWorker(
                self.text,
                self.speed_input.value()
            )

            self.worker.finished.connect(self.typing_finished)
            self.worker.start()

        else:
            self.countdown_label.setText(
                f"Starting in {self.remaining_seconds} seconds"
            )
            print("Remaining seconds:", self.remaining_seconds)

    def typing_finished(self):
        self.start_button.setEnabled(True)

        if self.stop_requested:
            self.countdown_label.setText("Typing Stopped")
        else:
            self.countdown_label.setText("Typing Completed")

        self.stop_requested = False


    def init_ui(self):
        self.worker = None
        self.stop_requested = False

        self.layout = QVBoxLayout()

        self.title = QLabel("Auto Sentence Typer")

        self.text_input = QTextEdit()

        self.text_input.setPlaceholderText(
            "Enter your sentence or paragraph here..."
        )

        self.delay_label = QLabel("Starting Delay (seconds)")

        self.delay_input = QSpinBox()

        self.delay_input.setMinimum(1)
        self.delay_input.setMaximum(60)
        self.delay_input.setValue(5)

        self.speed_label = QLabel("Typing Interval (seconds)")

        self.speed_input = QDoubleSpinBox()

        self.speed_input.setMinimum(0.01)
        self.speed_input.setMaximum(2.00)
        self.speed_input.setSingleStep(0.01)
        self.speed_input.setValue(0.10)

        self.start_button = QPushButton("Start Typing")
        self.start_button.clicked.connect(self.start_typing)

        self.stop_button = QPushButton("Stop Typing")
        self.stop_button.clicked.connect(self.stop_typing)

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_countdown)

        self.countdown_label = QLabel("Ready to start")

        self.layout.addWidget(self.title)
        self.layout.addWidget(self.text_input)

        self.layout.addWidget(self.delay_label)
        self.layout.addWidget(self.delay_input)

        self.layout.addWidget(self.speed_label)
        self.layout.addWidget(self.speed_input)
        self.layout.addWidget(self.countdown_label)

        self.layout.addWidget(self.start_button)
        self.layout.addWidget(self.stop_button)

        self.setLayout(self.layout)