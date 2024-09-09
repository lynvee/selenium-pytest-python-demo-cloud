# Automation Testing with Selenium Python Behave

## Introduction
This repository is designed for automation testing using Selenium and Python Behave. It aims to provide a robust framework for conducting GUI tests on web applications, ensuring compliance with the specified functional requirements.

## Prerequisites
Before you begin, ensure you have installed the following:
- **Python 3.8+**: Make sure Python is installed on your system.
- **pip**: Python's package installer, used to install the dependencies.
- **Web Browser**: Google Chrome, Firefox, etc.

## Installation
To set up this project on your local machine, follow these steps:
1. Clone the repository:
   ```bash
   git clone https://github.com/lynvee/selenium-python-behave-demo-cloud.git
2. Navigate to the project directory:
    ```bash
    cd your-repository
3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
## Configuration
Configure the test environment by setting the necessary parameters in the `behave.ini` file or through a custom `config.json`. Include parameters such as the base URL and browser preferences.

## Running Tests
Execute the tests using the following commands:
1. To run all tests:
    ```bash
    behave
2. To run a specific feature file:
    ```bash
    behave features/your_feature_file.feature
## Contact
For queries or support, please reach out to us at vtnlinh2909@gmail.com

## View Report
    allure serve [report-name]