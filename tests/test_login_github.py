from pages.login_github import LoginPage
from playwright.sync_api import Page, expect
from utilities.config import TEST_USERNAME, TEST_PASSWORD

def test_sign_in_to_github(page: Page):
    signInPage = LoginPage(page)
    signInPage.open()

# signInPage.clickOnSignInButton()
#or
    page.pause()
    signInPage.clickOnSignInButton()
    signInPage.waitForLogingPageToLoad()

    assert TEST_USERNAME is not None
    assert TEST_PASSWORD is not None 

    
    page.pause()
    signInPage.UsernameOrEmailField.fill(TEST_USERNAME)
    signInPage.passwordField.fill(TEST_PASSWORD)
    expect(signInPage.signInButtonAfter()).to_be_visible()
    pass
