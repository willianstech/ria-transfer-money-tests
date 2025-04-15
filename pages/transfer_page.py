class TransferPage:
    def __init__(self, page: Page):
        self.page = page
        self.country_selector = "div[role='button']"
        self.amount_input = "input[name='amount']"  
        page.wait_for_load_state("networkidle")

    def select_country(self, country_name: str):
        # Open dropbox Country Selection
        self.page.get_by_role("button", name="Send to Mexico").click()

        # Wait for the search input shows
        search_input = self.page.locator("input[type='text']").first
        search_input.wait_for(timeout=5000)

        # Clear field
        search_input.fill("")
        search_input.type("Brazil")

        # Select Country choosen
        self.page.locator("div.item-container").filter(has_text="Brazil").click()       
        
    def set_amount(self, value: str):
        self.page.locator("input[placeholder='0']").nth(0).fill(value)
        
    def clear_and_type_amount(self, value: str):
        element = self.page.locator(self.amount_input)
        element.clear()
        element.type(value)  

    def get_total_amount(self):
        total_element = self.page.locator("//div[contains(@class, 'details-row')]/span[contains(@class, 'transfer-text')]").first
        return total_element.text_content().split()[0]

