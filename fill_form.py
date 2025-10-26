from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://docs.google.com/forms/d/e/1FAIpQLSdUCd3UWQ3VOgeg0ZzNeT-xzNawU8AJ7Xidml-w1vhfBcvBWQ/viewform")

wait = WebDriverWait(driver, 10)

# Better version of helper functions
def input_by_label(label_text):
    xpath = f'//div[contains(., "{label_text}") and @role="listitem"]//input'
    return wait.until(EC.presence_of_element_located((By.XPATH, xpath)))

def textarea_by_label(label_text):
    xpath = f'//div[contains(., "{label_text}") and @role="listitem"]//textarea'
    return wait.until(EC.presence_of_element_located((By.XPATH, xpath)))


# ---------- Fill the form ----------
input_by_label("Full Name").send_keys("Sahil Ahmad")
input_by_label("Contact Number").send_keys("8423******")
input_by_label("Email ID").send_keys("sahilahmad****@gmail.com")
textarea_by_label("Full Address").send_keys("Ka*****, Lucknow")
input_by_label("Pin Code").send_keys("2261**")
input_by_label("Date of Birth").send_keys("17/**/20**")

# Gender (text or radio)
try:
    input_by_label("Gender").send_keys("Male")
except:
    gender_option = driver.find_element(By.XPATH, '//div[@role="radio" and .="Male"]')
    gender_option.click()

# Code field
input_by_label("GNFPYC").send_keys("GNFPYC")

# Submit button
submit_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//span[text()="Submit"]')))
submit_button.click()

print("✅ Form submitted successfully!")
driver.quit()