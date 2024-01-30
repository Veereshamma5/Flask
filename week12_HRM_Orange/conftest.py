from datetime import datetime
from pathlib import Path

import pytest
from selenium import webdriver

BaseUrl = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
Username = "Admin"
Password = "admin123"
SearchText = "Admin"

@pytest.fixture(scope="class", autouse=True)
def browser_setup(request):
    request.cls.driver = webdriver.Chrome()


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    today = datetime.now()
    report_dir = Path("hrmreport", today.strftime("%Y%m%d"))
    report_dir.mkdir(parents=True, exist_ok= True)
    pytest_html = report_dir / f"Report_{today.strftime('%Y%m%d%H%M')}.html"
    print("pytest_html is::::::::::::::::::::::::::", pytest_html)
    config.option.htmlpath = pytest_html
    config.option.self_contained_html = True


def pytest_html_report_title(report):
    report.title = " HRM Report"
