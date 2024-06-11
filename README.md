# Loto_Checker
## Description
A piece of software that checks if one won the lottery by sending an SMS to a specific phone number using API calls.

This project enables users to be informed if they become millionaires. 

When run periodically, the Lottery Checker saves the users time by letting them know about the lottery results every time new lottery-winning numbers are drawn.

## Features
- A test suite that scrapes the winning lottery numbers from the [EuroJackpot website](https://www.eurojackpot.com/) into a text file, using Robot framework;
- A function that compares the winning numbers, with the numbers the user played, which can be set by the user.
- A function that sends both winning numbers and played numbers to the user's phone number, by calling the [Twillio API](https://www.twilio.com/en-us). 

## Getting Started
### Prerequisites
- Python version 3.10.12 or newer;
- [Python-dotenv library;](https://pypi.org/project/python-dotenv/);
- [os library;](https://docs.python.org/3/library/os.html)
- [twillio.rest library;](https://www.twilio.com/docs)
- [subprocess library;](https://docs.python.org/3/library/subprocess.html)
- Robot framework version 6.0.2;

### Installation
In order to set up the Twilio API, create an account on their website, you will then be provided with 10 USD credit to make calls. Then to the following:

- With the repository cloned locally, rename the file `.env.sample` to `.env`;
- Once logged into the [twilio console](https://console.twilio.com/), generate a twilio phone number, along with an Account SSID and an Auth Token;
- Replace Account SSID and Auth Token;

### Usage
Once all the prerequisites are installed, run the following command from the repository's root directory:
`python3 main.py`

You should get a message like the one shown below. 👇