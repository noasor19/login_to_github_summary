from playwright.sync_api import Locator, Page

from pages.base_page import BasePage
from utilities import config
import re


class LoginPage(BasePage):
    URL = config.GITHUB_URL


    def __init__(self, page: Page):
        super().__init__(page)
        
    # def clickOnSignInButton(self):
    #     self.page.get_by_role("link", name="Sign in").click()

    @property
    def clickOnSignInButton(self) -> None:
      return self.page.get_by_role("link", name="Sign in")

    @property
    def passwordField(self) -> Locator:
        return self.page.get_by_role("textbox", name="Password")

    @property
    def signInButton(self) -> Locator:
        return self.page.get_by_role("link", name="Sign in")


    @property
    def UsernameOrEmailField(self) -> Locator:
        return self.page.get_by_role("textbox", name="Username or email address")

    def signInButtonAfter(self):
        return self.page.get_by_role("button", name="Sign in with your identity")

    def waitForLogingPageToLoad(self):
      self.page.wait_for_url("**/login")
