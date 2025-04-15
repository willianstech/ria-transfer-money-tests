import pytest
import os


from playwright.sync_api import sync_playwright
from pages.transfer_page import TransferPage
from utils.screenshot_helper import save_screenshot


if not os.path.exists("screenshots"):
    os.makedirs("screenshots")

@pytest.fixture(scope="function")
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=300)
        page = browser.new_page()
        page.goto("https://www.riamoneytransfer.com/en-us/")
        yield page
        browser.close()


# BELOW MINIMUM AMOUNT

def test_transfer_amount_min(page):
    transfer = TransferPage(page)
    transfer.select_country("Send to Brazil")
    transfer.set_amount("0.99")  
    error = page.locator("text=Actual costs may vary 1.00 and 14,999.00")
    error.wait_for(timeout=5000)
    assert error.is_visible()
    page.screenshot(path="screenshots/test_transfer_amount_min.png")
    page.close()


# ABOVE MAXIMUM AMOUNT

def test_transfer_amount_max(page):
    transfer = TransferPage(page)
    transfer.select_country("Send to Brazil")
    transfer.set_amount("15,000.00")  
    error = page.locator("text=Actual costs may vary 1.00 and 14,999.00")
    error.wait_for(timeout=5000)
    assert error.is_visible()
    page.screenshot(path="screenshots/test_transfer_amount_max.png")
    page.close()


# TESTING WITH VALUE = 025

def test_transfer_amount_025(page):
    transfer = TransferPage(page)
    transfer.select_country("Brazil")
    transfer.set_amount("025")
    screenshot_path_1 = "screenshots/test_transfer_amount_025_1.png"
    page.screenshot(path=screenshot_path_1) 
    page.wait_for_timeout(6000)      
    formatted_value = transfer.get_total_amount()
    assert formatted_value == "25.00", f"Valor incorreto: {formatted_value}"
    page.wait_for_timeout(9000)    
    screenshot_path_2 = "screenshots/test_transfer_amount_025_2.png"
    page.screenshot(path=screenshot_path_2)     
    page.wait_for_timeout(3000) 
    page.close() 


# TESTING WITH VALUE = 15.000

def test_transfer_amount_15000(page):
    transfer = TransferPage(page)
    transfer.select_country("Brazil")
    transfer.set_amount("15.000")  
    screenshot_path_1 = "screenshots/test_transfer_amount_15000_1.png"
    page.screenshot(path=screenshot_path_1) 
    page.wait_for_timeout(6000)      
    formatted_value = transfer.get_total_amount()
    assert formatted_value == "15.00", f"Valor incorreto: {formatted_value}"
    page.wait_for_timeout(9000)    
    screenshot_path_2 = "screenshots/test_transfer_amount_15000_2.png"
    page.screenshot(path=screenshot_path_2)     
    page.wait_for_timeout(3000) 
    page.close() 
    

# TESTING WITH VALUE = ,7

def test_transfer_invalid_format_7(page):    
    transfer = TransferPage(page)
    transfer.select_country("Send to Brazil")    
    transfer.set_amount(",7") 
    screenshot_path_1 = "screenshots/test_transfer_invalid_format_7_1.png"
    page.screenshot(path=screenshot_path_1) 
    page.wait_for_timeout(6000)      
    formatted_value = transfer.get_total_amount()
    assert formatted_value == "7.00", f"Valor incorreto: {formatted_value}"
    page.wait_for_timeout(9000)    
    screenshot_path_2 = "screenshots/test_transfer_invalid_format_7_2.png"
    page.screenshot(path=screenshot_path_2)      
    page.wait_for_timeout(3000) 
    page.close() 


# TESTING WITH VALUE = 410,7

def test_transfer_invalid_format_410(page):    
    transfer = TransferPage(page)
    transfer.select_country("Send to Brazil")    
    transfer.set_amount("410,7") 
    screenshot_path_1 = "screenshots/test_transfer_invalid_format_410_1.png"
    page.screenshot(path=screenshot_path_1) 
    page.wait_for_timeout(6000)      
    formatted_value = transfer.get_total_amount()
    assert formatted_value == "4,107.00", f"Valor incorreto: {formatted_value}"
    page.wait_for_timeout(9000)    
    screenshot_path_2 = "screenshots/test_transfer_invalid_format_410_2.png"
    page.screenshot(path=screenshot_path_2)      
    page.wait_for_timeout(3000) 
    page.close() 


# TESTING WITH VALUE = 0,99

def test_transfer_invalid_format_099(page):    
    transfer = TransferPage(page)
    transfer.select_country("Send to Brazil")    
    transfer.set_amount("0,99") 
    screenshot_path_1 = "screenshots/test_transfer_invalid_format_099_1.png"
    page.screenshot(path=screenshot_path_1) 
    page.wait_for_timeout(6000)      
    formatted_value = transfer.get_total_amount()
    assert formatted_value == "99.00", f"Valor incorreto: {formatted_value}"
    page.wait_for_timeout(9000)    
    screenshot_path_2 = "screenshots/test_transfer_invalid_format_099_2.png"
    page.screenshot(path=screenshot_path_2)      
    page.wait_for_timeout(3000) 
    page.close() 


# TESTING WITH VALUE = +

def test_transfer_invalid_format_plus(page):    
    transfer = TransferPage(page)
    transfer.select_country("Send to Brazil")    
    transfer.set_amount("+") 
    screenshot_path_1 = "screenshots/test_transfer_invalid_format_plus_1.png"
    page.screenshot(path=screenshot_path_1) 
    page.wait_for_timeout(6000)      
    formatted_value = transfer.get_total_amount()
    assert formatted_value == "0.00", f"Valor incorreto: {formatted_value}"
    page.wait_for_timeout(9000)    
    screenshot_path_2 = "screenshots/test_transfer_invalid_format_plus_2.png"
    page.screenshot(path=screenshot_path_2)      
    page.wait_for_timeout(3000) 
    page.close() 


# TESTING WITH VALUE = ""

def test_transfer_empty_value(page):    
    transfer = TransferPage(page)
    transfer.select_country("Send to Brazil")    
    transfer.set_amount("") 
    screenshot_path_1 = "screenshots/test_transfer_empty_value_1.png"
    page.screenshot(path=screenshot_path_1) 
    page.wait_for_timeout(6000)      
    formatted_value = transfer.get_total_amount()
    assert formatted_value == "0.00", f"Valor incorreto: {formatted_value}"
    page.wait_for_timeout(9000)    
    screenshot_path_2 = "screenshots/test_transfer_empty_value_2.png"
    page.screenshot(path=screenshot_path_2)      
    page.wait_for_timeout(3000) 
    page.close() 






