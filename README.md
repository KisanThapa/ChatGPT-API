# ChatGPT-API

## Introduction
Recently ChatGPT shake internet with its amazing results. This repository is a simple API for ChatGPT, where you can query many questions and get answers from ChatGPT. I created this repository to make it easier for people who wants to see the ChatGPT response for their many questions. 


## Features
- Query many questions and get answers from ChatGPT
- Save the questions and answers in a file ie. `qna.txt`


## Requirements
- Python 3.6+
- requests and json libraries
- OpenAI API key


## How to get OpenAI API key
Go to [OpenAI API](https://platform.openai.com/account/api-keys) and sign up for an account. You can create an API key by clicking on the `Create new secret key` button. Copy the API key and paste it in the `chatgpt.py` file. Note that the API key is a secret key, so don't share it with anyone and once created you can't see the same key again. So, make sure you copy the key and paste it in the `chatgpt.py` file.


## Before you start
Enter your questions in the `questions.txt` file. Each question should be in a new line. Every question should end within a line. For example, if you want to ask two questions, then your `questions.txt` file should look like this:

  ```bash
  How to send get request in python?
  Transverse waves can propagate: (a) Both in a gas and in a metal (b) In a gas but not in a metal (c) Not in a gas but in a metal (d) Neither in a gas nor in a metal
  ```

## Getting Started
### 1. Clone this repository to your local machine
  ```bash
  git clone https://github.com/KisanThapa/ChatGPT-API.git
  ```

### 2. Change directory to ChatGPT-API
  ```bash
  cd ChatGPT-API
  ```

### 3. Run the script

  If you are on Mac or Linux, run the following command
  ```bash
  python3 chatgpt.py
  ```

  If you are on Windows, run the following command
  ```bash
  python chatgpt.py
  ```

### 4. Check the `qna.txt` file
  You will see the questions and answers in the `qna.txt` file.


## Contributing
If you want to contribute to this repository, feel free to create a pull request. I will review the pull request and merge it if it is good.


## License
This project is licensed under the MIT License. 


## Contact
If you have any questions, feel free to contact me at
- [Email](mailto:kisanthapa33@gmail.com)
- LinkedIn: [Kisan Thapa](https://www.linkedin.com/in/kisan-thapa-860865113/)


## If you like this repository, please give it a star ⭐