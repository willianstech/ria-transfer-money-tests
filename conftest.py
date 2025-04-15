import os
import pytest
from datetime import datetime

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    # If failure during the test
    if report.failed and "page" in item.fixturenames:
        page = item.funcargs["page"]
        test_name = item.name
        timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        screenshot_dir = "screenshots"
        os.makedirs(screenshot_dir, exist_ok=True)
        file_name = f"{screenshot_dir}/{test_name}_{timestamp}.png"
        page.screenshot(path=file_name)
        print(f"\n[Screenshot salvo em]: {file_name}")