from PyQt6.QtCore import QThread
import pyautogui

class TypingWorker(QThread):

    def __init__(self,text,typing_speed):
        super().__init__()
        self.text = text
        self.typing_speed = typing_speed

    def run(self):
        for character in self.text:
            if self.isInterruptionRequested():
                break
            pyautogui.write(character, interval=self.typing_speed)