"""
# the most optimal locators for Amazon Create Account page

# using CSS for the logo
driver.find_element(By.CSS_SELECTOR, "i.a-icon.a-icon-logo")

# using CSS for the Creat account text
driver.find_element(By.CSS_SELECTOR, "div.a-box-inner h1.a-spacing-small")

# Using by ID for your name field
driver.find_element(By.ID, "ap_customer_name")

# Using by ID for Mobile number or email field
driver.find_element(By.ID, "ap_email")

# Using by ID for Password field
driver.find_element(By.ID, "ap_password")


# Using by ID for Re-enter password field
driver.find_element(By.ID, "ap_password_check")

# Using by ID for continue button
driver.find_element(By.ID, "continue")

# using CSS for the Conditions of Use link
driver.find_element(By.CSS_SELECTOR, "a[href *= 'ref=ap_register_notification_condition_of_use?']")

# using CSS for the Privacy Notice link
driver.find_element(By.CSS_SELECTOR, "a[href *= 'ref=ap_register_notification_privacy_notice?']")

# using CSS for the  Sign in link
driver.find_element(By.CSS_SELECTOR, "a.a-link-emphasis[href *= '/ap/signin?openid.pape.max_auth_age']")

# Using by ID for  Create a free business account link
driver.find_element(By.ID, "ab-registration-link.a-link-emphasis")
"""