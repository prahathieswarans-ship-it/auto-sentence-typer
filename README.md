# Auto Sentence Typer

A Python desktop application that automatically types user-provided text into the active application after a configurable countdown.

Built using **Python, PyQt6, and PyAutoGUI**.

## Features

- Enter sentences or paragraphs through a graphical interface.
- Configure the starting delay before typing begins.
- Configure the typing interval between characters.
- Start and stop automatic typing.
- View the countdown before typing starts.
- Background typing using a separate worker thread.

## Technologies Used

- **Python** – Core programming language.
- **PyQt6** – Desktop graphical user interface.
- **PyAutoGUI** – Automated keyboard input.
- **Pytest** – Automated testing.

## Project Structure

```text
AutoSentenceTyper/
│
├── main.py
├── ui/
│   ├── __init__.py
│   └── main_window.py
│
├── workers/
│   ├── __init__.py
│   └── typing_worker.py
│
├── tests/
│   ├── test_basic.py
│   └── test_main_window.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/prahathieswarans-ship-it/auto-sentence-typer.git
cd auto-sentence-typer
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the virtual environment

**Windows PowerShell:**

```powershell
.\.venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

## Run the Application

```bash
python main.py
```

## Run Tests

```bash
python -m pytest -v
```

## How to Use

1. Launch the application.
2. Enter the text you want to type.
3. Set the starting delay.
4. Configure the typing interval.
5. Click **Start Typing**.
6. Switch to the target application during the countdown.
7. The application will automatically type your text.
8. Click **Stop Typing** to interrupt the operation.

## Important Notes

- Keep the target application ready before the countdown finishes.
- Avoid interacting with the keyboard or mouse while automatic typing is running.
- PyAutoGUI sends keyboard input to the currently focused application.

## Future Improvements

- Pause and resume typing.
- Keyboard shortcuts.
- Improved error handling.
- Support for additional text input methods.
- More comprehensive automated tests.

## Author

**Prahathieswaran S**

GitHub: [@prahathieswarans-ship-it](https://github.com/prahathieswarans-ship-it)

---

If you find this project useful, consider giving the repository a star!