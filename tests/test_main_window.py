from ui.main_window import MainWindow
from PyQt6.QtWidgets import QMessageBox
from PyQt6.QtCore import QTimer
from PyQt6.QtWidgets import QApplication

from PyQt6.QtCore import Qt


def test_empty_text_validation(qtbot):
    dialog_info = {}

    def handle_dialog():
        dialog = QApplication.activeModalWidget()
        dialog_info["dialog"] = dialog
        assert isinstance(dialog, QMessageBox)
        assert dialog.windowTitle() == "Input Required"
        assert dialog.text() == "Please enter some text before starting."
        assert not window.timer.isActive()
        dialog.accept()

    window = MainWindow()

    qtbot.addWidget(window)
    window.show()

    QTimer.singleShot(0, handle_dialog)
    qtbot.mouseClick(
        window.start_button,
        Qt.MouseButton.LeftButton
    )


def test_valid_text_starts_countdown(qtbot):
    window = MainWindow()
    qtbot.addWidget(window)
    window.show()
    window.text_input.setPlainText("Hello World")
    qtbot.mouseClick(window.start_button, Qt.MouseButton.LeftButton)
    assert window.timer.isActive()
    assert not window.start_button.isEnabled()
