import pyfiglet
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Function to print the PATEL banner
def print_banner():
    ascii_art = pyfiglet.figlet_format("PATEL", font="slant")
    print(ascii_art)

# Function to get the Google Form link from the user
def get_google_form_link():
    form_url = input("Enter the Google Form URL: ")
    return form_url

# Function to fill out and submit the Google Form
def solve_google_form(form_url):
    # Define the answers for the form (modify according to your form structure)
    answers = {
        'question1': 'answer1',
        'question2': 'answer2',
        'question3': 'answer3',
        # Add more questions and answers as needed
    }

    # Initialize the WebDriver
    driver = webdriver.Chrome()  # No need to specify the path if chromedriver is in the project directory

    # Open the Google Form
    driver.get(form_url)
    time.sleep(2)  # Wait for the page to load

    # Fill out the form
    for question, answer in answers.items():
        # Locate the input field (modify according to your form's input structure)
        input_field = driver.find_element(By.XPATH, f"//input[@aria-label='{question}']")
        input_field.send_keys(answer)

    # Submit the form
    submit_button = driver.find_element(By.XPATH, "//span[text()='Submit']")
    submit_button.click()

    # Close the WebDriver
    time.sleep(2)
    driver.quit()

# Main function
def main():
    # Print the PATEL banner
    print_banner()

    # Ask for the Google Form link
    form_url = get_google_form_link()

    # Solve the Google Form
    solve_google_form(form_url)

if __name__ == "__main__":
    main()
