# 10fastfingers Cheat - OCR-Based Anti-Cheat Analysis and Study

![img_logo](https://10fastfingers.com/img/layout/logo%402x.png)

## Disclaimer

This project is created for educational purposes only.

## Project Objective

The **10fastfingers Cheat** project aims to analyze and study the anti-cheat mechanisms implemented by the popular typing test website [10fastfingers.com](https://10fastfingers.com). By using Optical Character Recognition (OCR), the project explores methods to bypass the anti-cheat system in order to manipulate the recorded words per minute (wpm) score.

## About 10fastfingers.com

[10fastfingers.com](https://10fastfingers.com) is a website designed to test and enhance users' typing skills. It offers various typing tests with different difficulty levels and languages. Users can participate in typing competitions to challenge themselves and compete against others worldwide. The platform also provides valuable typing statistics, such as words per minute (wpm) and accuracy, to help users track their progress.

## How It Works

Once you configure your token and set the desired wpm, the project utilizes **Optical Character Recognition (OCR)** to analyze the second verification step triggered by the website's anti-cheat mechanism. When a user reaches a typing speed of 120wpm, the anti-cheat system challenges them with an image-based verification to prevent cheating attempts. The project explores methods to bypass this verification step using OCR and modify the recorded words per minute (wpm) score.

## Requirements

- Python and Pip installed.
- A browser with your account logged in (to retrieve the token).
- Internet connection.

## Usage Instructions

1. Download the repository and extract its contents.
2. In the `config.json` file, replace `CHANGE_TO_YOUR_SESSION` with your session token.
3. Open CMD or terminal, navigate to the directory where the program is located.
4. Install the required dependencies with the command `pip install -r requirements.txt`.
5. Run the program using `python3 type_test.py`.
6. If an anti-cheat verification is prompted, execute `python3 anti_cheat_bypass.py` (initial run may take longer).

[![Watch the video](https://img.youtube.com/vi/PKN8Vs0xBnw/0.jpg)](https://www.youtube.com/watch?v=PKN8Vs0xBnw)

*Please note that the purpose of this project is purely educational and not intended for any unethical or unauthorized use on the 10fastfingers website.*
