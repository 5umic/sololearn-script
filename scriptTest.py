from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver_path = '/Applications/chromedriver'
url = 'https://www.sololearn.com/learn/courses/css-introduction/lesson/1934607001?p=1'  # replace with the URL of the website you're working with
driver = webdriver.Chrome()
driver.get(url)
wait = WebDriverWait(driver, 10)

def click_single_option():

    # Wait until the container is present
    container = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "sl-single-choice-answer")))
    
    # Find all single choice items inside the container
    single_choice_items = container.find_elements(By.CLASS_NAME, 'sl-single-choice-item')

    if single_choice_items:
        # Wait until the first single choice item becomes clickable
        wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'sl-single-choice-item')))
        
        # Click on the first single choice item
        single_choice_items[0].click()
    else:
        print("No single choice items found in the container.")
    

def accept_cookies():
    cookieButton = wait.until(EC.presence_of_element_located((By.ID, "CybotCookiebotDialogBodyLevelButtonAccept")))
    cookieButton.click()

def click_continue_button():
    continueButton = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/div/main/div[1]/div/div/footer/div/button[2]')))
    continueButton.click()


def click_elements_in_container():
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
            loginFunction()  # Rerun the script when the URL changes 
            accept_cookies()
            click_continue_button()
            click_elements_in_container()
            click_single_option()
            click_continue_button()




def loginFunction():

    emailVar = wait.until(EC.presence_of_element_located((By.ID, "email")))
    passVar = wait.until(EC.presence_of_element_located((By.ID, "password")))

    emailVar.send_keys("h23vehsu@du.se")#insert ur login info
    passVar.send_keys("Horunge123")#insert ur password

    signin_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "sol-button-primary")))
    signin_button.click()





watch_url_change(driver)

input("Press Enter to close the browser...")
driver.quit()

