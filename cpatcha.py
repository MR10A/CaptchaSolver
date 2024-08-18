from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

def ReCAPTCHA2(driver):
    try:
        # Switch to the first iframe and click the checkbox
        iframe = driver.find_element(By.TAG_NAME, "iframe")
        driver.switch_to.frame(iframe)
        driver.find_element(By.CLASS_NAME, 'recaptcha-checkbox-border').click()
        driver.implicitly_wait(5)
        driver.switch_to.default_content()
        
        # Switch to the challenge iframe
        iframe = driver.find_element(By.XPATH, '//iframe[@title="recaptcha challenge expires in two minutes"]')
        driver.switch_to.frame(iframe)
        
        try:
            # Click on an element in the challenge
            driver.find_element(By.XPATH, '//*[@id="rc-imageselect"]/div[3]/div[2]/div[1]/div[1]/div[4]').click()
            time.sleep(2)
        except Exception as e:
            print(f"Challenge element click failed: {e}")
        
        driver.switch_to.default_content()
        time.sleep(2)
        
        # Click the submit button
        btn = driver.find_element(By.XPATH, 'html/body/div[1]/div/div/div/div[2]/div/div[2]/form/button')
        driver.execute_script("arguments[0].click();", btn)
        time.sleep(3)
        
    except Exception as e:
        print(f"ReCaptcha handling failed: {e}")
    return driver


def CSDriver(url,CpatchaType):
    options = Options()
    options.add_extension("RecCAPTCHA2.crx")
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    if CaptchaType=="ReCAPTCHA2"
        ReCaptcha(driver)
    return driver




if __name__ == "__main__":
    CSDriver()

    
