import os
from datetime import datetime

def save_screenshot(page, step_name: str):
    os.makedirs("screenshots", exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    file_name = f"screenshots/{step_name}_{timestamp}.png"
    page.screenshot(path=file_name)
    print(f"[Screenshot manual salvo em]: {file_name}")