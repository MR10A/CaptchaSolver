# Selenium Captcha Automation:

This project demonstrates how to automate the process of handling reCAPTCHA using Selenium with Python. The script is designed to handle a reCAPTCHA challenge and includes a browser extension for bypassing reCAPTCHA.
#Availaibe:
ReCaptcha v2
## Prerequisites
```
- Python 3.x
- Google Chrome browser
- ChromeDriver (compatible with your version of Chrome)
```

## Usage:
```
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from captcha import CSDriver
```
# URL of the page with reCAPTCHA
```
url = "https://example.com"
```
# Initialize and run CSDriver
```
driver = CSDriver(url,CaptchaType="ReCAPTCHA2")
```

 


