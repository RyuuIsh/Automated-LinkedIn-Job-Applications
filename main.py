import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

URL = "https://www.linkedin.com/jobs/search/?keywords=python&f_AL=true&f_E=1&f_JT=I&f_WT=2&sortBy=R"
ACCOUNT_EMAIL = os.getenv("LINKEDIN_EMAIL")
ACCOUNT_PASSWORD = os.getenv("LINKEDIN_PASSWORD")
LOCATION = "India"
PHONE = os.getenv("PHONE_NUMBER")

# Set up Chrome WebDriver options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

driver.get(URL)
time.sleep(5)

# Click Sign in Button
try:
    sign_in_button = driver.find_element(By.LINK_TEXT, "Sign in")
    sign_in_button.click()
except NoSuchElementException:
    print("Sign-in button not found.")

# Enter login credentials
time.sleep(5)
email_field = driver.find_element(By.ID, "username")
email_field.send_keys(ACCOUNT_EMAIL)
password_field = driver.find_element(By.ID, "password")
password_field.send_keys(ACCOUNT_PASSWORD)
password_field.send_keys(Keys.ENTER)

# Manual CAPTCHA solving
input("Solve CAPTCHA if prompted, then press Enter to continue...")

# Find job listings
time.sleep(5)
job_listings = driver.find_elements(By.CSS_SELECTOR, ".job-card-container--clickable")

for job in job_listings:
    try:
        job.click()
        time.sleep(2)

        # Click Apply Button
        apply_button = driver.find_element(By.CSS_SELECTOR, ".jobs-s-apply button")
        apply_button.click()
        time.sleep(2)

        # Check if phone number is required
        try:
            phone_field = driver.find_element(By.CSS_SELECTOR, "input[id*=phoneNumber]")
            if phone_field.get_attribute("value") == "":
                phone_field.send_keys(PHONE)
        except NoSuchElementException:
            print("Phone field not found. Skipping...")

        # Submit the application
        submit_button = driver.find_element(By.CSS_SELECTOR, "footer button")
        submit_button.click()
        time.sleep(2)

        print("✅ Application submitted successfully!")

    except (NoSuchElementException, ElementClickInterceptedException):
        print("⚠️ Could not apply to this job. Skipping...")

driver.quit()
