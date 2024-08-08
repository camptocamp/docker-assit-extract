import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

REQUEST_PROCESS_WAIT = 20  # Seconds (Selenium default time unit)
EXTRACT_DEMO_LOGIN = ("admin", "motdepasse21")
GEOSHOP_DEMO_LOGIN = ("admin", "Test1234")


class ExtractStatusTest(unittest.TestCase):

    def setUp(self):
        print("Test Execution Started")
        options = webdriver.FirefoxOptions()
        options.add_argument("--web-security=no")
        options.add_argument("--ssl-protocol=any")
        options.add_argument("--ignore-ssl-errors=yes")
        self.driver = webdriver.Remote(
            command_executor="http://selenium:4444/wd/hub", options=options
        )

    def tearDown(self):
        self.driver.close()

    def test_loginWaitFinished(self):
        self.driver.get("http://frontend/extract")
        self.assertEqual(
            self.driver.find_element(By.TAG_NAME, "title").get_attribute("innerText"),
            "Extract",
        )

        # Login
        self.driver.find_element(By.NAME, "username").send_keys(EXTRACT_DEMO_LOGIN[0])
        self.driver.find_element(By.NAME, "password").send_keys(EXTRACT_DEMO_LOGIN[1])
        self.driver.find_element(By.ID, "loginButton").click()
        self.assertEqual(
            self.driver.find_element(By.TAG_NAME, "title")
            .get_attribute("innerText")
            .strip(),
            "Extract – Accueil",
        )

        # Waiting for Geoshop tasks to appear
        WebDriverWait(self.driver, REQUEST_PROCESS_WAIT).until(
            expected_conditions.presence_of_element_located(
                (By.CSS_SELECTOR, "tr.request-row.finished")
            )
        )

        completedRows = self.driver.find_elements(
            By.CSS_SELECTOR, "tr.request-row.finished"
        )
        self.assertEqual(len(completedRows), 3)
        self.assertEqual(
            sum(
                [
                    "Execute script" in row.get_attribute("innerText")
                    for row in completedRows
                ]
            ),
            3,
        )

        self.driver.find_element(By.ID, "logoutLink").click()
        self.assertEqual(
            self.driver.find_element(By.TAG_NAME, "title")
            .get_attribute("innerText")
            .strip(),
            "Extract",
        )


if __name__ == "__main__":
    unittest.main()
