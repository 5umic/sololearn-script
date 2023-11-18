from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def perform_script():

    continueButton = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/div/main/div[1]/div/div/footer/div/button[2]')))
    continueButton.click()


    # Click the "Continue" button
    container_xpath = '//*[@id="main"]/div/main/div[1]/div/div/div[1]/div/div/div/div[3]/div/div[2]'
    container = wait.until(EC.presence_of_element_located((By.XPATH, container_xpath)))

    elements_to_click = container.find_elements(By.CLASS_NAME, 'sl-dnd-options__item')
    for element in elements_to_click:
        element.click()
        



def watch_url_change(current_url):
    while True:
        # Check if the URL has changed
        new_url = driver.current_url
        if new_url != current_url:
            print(f"URL changed to: {new_url}")
            current_url = new_url
            perform_script()  # Rerun the script when the URL changes 


driver_path = '/Applications/chromedriver'
url = 'https://www.sololearn.com/learn/courses/css-introduction/lesson/1934607001?p=1'  # replace with the URL of the website you're working with
driver = webdriver.Chrome()
driver.get(url)
wait = WebDriverWait(driver, 10)

emailVar = wait.until(EC.presence_of_element_located((By.ID, "email")))
passVar = wait.until(EC.presence_of_element_located((By.ID, "password")))

emailVar.send_keys("")#insert ur login info
passVar.send_keys("")#insert ur password

signin_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "sol-button-primary")))
signin_button.click()

cookieButton = wait.until(EC.presence_of_element_located((By.ID, "CybotCookiebotDialogBodyLevelButtonAccept")))
cookieButton.click()

perform_script()

watch_url_change(driver)

input("Press Enter to close the browser...")
driver.quit()
