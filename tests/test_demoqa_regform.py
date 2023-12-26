from qaguru_tests.data.users import guest
from qaguru_tests.pages.registration_page import HighLevelRegPage


def test_practice_form(setup_browser):
    reg_page = HighLevelRegPage()
    reg_page.register(guest)
    reg_page.should_registered_user_with(guest)
