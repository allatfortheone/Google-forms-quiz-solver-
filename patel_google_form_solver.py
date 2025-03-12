import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def get_google_form_data(form_url):
    # Initialize Chrome options
    chrome_options = Options()
    # chrome_options.add_argument("--headless")  # Commented out for testing
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--remote-debugging-port=9222")

    # Initialize the WebDriver using the ChromeDriverManager
    service = Service(ChromeDriverManager().install(), log_path="chromedriver.log")
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # Open the Google Form
    driver.get(form_url)
    time.sleep(2)  # Wait for the page to load

    # Extract questions and choices
    questions = driver.find_elements(By.CSS_SELECTOR, '.freebirdFormviewerComponentsQuestionBaseTitle')
    choices = driver.find_elements(By.CSS_SELECTOR, '.freebirdFormviewerComponentsQuestionRadioChoice')

    form_data = {}
    for question in questions:
        question_text = question.text
        choices_text = [choice.text for choice in choices if choice.text]
        form_data[question_text] = choices_text

    # Close the WebDriver
    driver.quit()

    return form_data

def print_form_data(form_data):
    for question, choices in form_data.items():
        print(f"Question: {question}")
        for choice in choices:
            print(f" - {choice}")
        print()

def main():
    # Example Google Form URL
    form_url = input("Enter the Google Form URL: ")

    # Get form data
    form_data = get_google_form_data(form_url)

    # Print form data
    print_form_data(form_data)

if __name__ == "__main__":
    main()
