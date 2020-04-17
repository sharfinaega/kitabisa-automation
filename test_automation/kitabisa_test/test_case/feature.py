from test_automation.kitabisa_test.main_feature import *


def create_donation():
    campaign = browser.driver.find_element_by_xpath("//*[@id='template_horizontal-wide-card-slider']/div/div/a[1]/div/div/figure/img")
    # browser.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='177298-177298']/div[1]/div/span")))
    browser.driver.implicitly_wait(10)
    assert campaign
    campaign.click()

    btn_donation = browser.driver.find_element_by_id("campaign-detail_button_donasi-sekarang")
    browser.driver.implicitly_wait(10)
    assert btn_donation
    btn_donation.click()

    browser.wait.until(EC.visibility_of_element_located((By.ID, "donation-amount")))
    btn_donation_value = browser.driver.find_element_by_xpath("//*[@id='donation-amount']/div[1]")
    browser.driver.implicitly_wait(10)
    assert btn_donation_value
    btn_donation_value.click()


    btn_bca_virtual_account = browser.driver.find_element_by_xpath("//*[@id='__next']/main/div[4]/div[4]/span")
    browser.driver.implicitly_wait(10)
    assert btn_bca_virtual_account
    browser.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='__next']/main/div[4]/div[4]/span")))
    btn_bca_virtual_account.click()

    input_field_name = browser.driver.find_element_by_name("fullname")
    browser.driver.implicitly_wait(10)
    assert input_field_name
    input_field_name.send_keys("Ega Sharfina")

    input_field_phone_number = browser.driver.find_element_by_xpath("//input[@placeholder='Nomor Ponsel']")
    browser.driver.implicitly_wait(10)
    assert input_field_phone_number
    input_field_phone_number.send_keys("0812345678")

    btn_payment_confirmation = browser.driver.find_element_by_id("contribute_button_lanjutkan-pembayaran")
    browser.driver.implicitly_wait(10)
    assert btn_payment_confirmation
    btn_payment_confirmation.click()

    browser.wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='summary-page']/div[8]")))
    banner_btn_close = browser.driver.find_element_by_xpath("//*[@id='summary-page']/div[8]/a[1]/span")
    browser.driver.implicitly_wait(10)
    assert banner_btn_close
    banner_btn_close.click()

    btn_back_to_donation = browser.driver.find_element_by_xpath("//*[@id='summary-page']/div[6]/div[3]/button/span")
    browser.driver.implicitly_wait(10)
    assert btn_back_to_donation
    btn_back_to_donation.click()

    browser.wait.until(EC.invisibility_of_element((By.XPATH, "//*[@id='summary-page']/div[8]")))
    btn_back = browser.driver.find_element_by_xpath("//div[@id='plain-header']/*[name()='svg'][@aria-hidden='true']")
    browser.driver.implicitly_wait(10)
    assert btn_back
    btn_back.click()

