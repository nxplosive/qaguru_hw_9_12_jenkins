from selene import browser, have, be, by
from selene.support.shared.jquery_style import s
import allure
from qaguru_tests.controls import resource
from qaguru_tests.data.users import User, guest


class HighLevelRegPage:

    @allure.step("Open page")
    def open(self):
        browser.open('/automation-practice-form')
        s('.pattern-backgound').should(have.exact_text('Practice Form'))
        return self

    @allure.step(f"User first name {guest.firstName}")
    def fill_first_name(self, guest):
        s('#firstName').click().should(be.blank).type(guest.firstName)

    @allure.step(f"User last name {guest.lastName}")
    def fill_last_name(self, guest):
        s('#lastName').click().should(be.blank).type(guest.lastName)

    @allure.step(f"User email {guest.userEmail}")
    def fill_email(self, guest):
        s('#userEmail').click().should(be.blank).type(guest.userEmail)

    @allure.step(f"User sex {guest.userGender}")
    def fill_gender(self, guest):
        s('#gender-radio-1').double_click()

    @allure.step(f"User phone number {guest.userPhoneNumber}")
    def fill_phone_number(self, guest):
        s('#userNumber').click().type(guest.userPhoneNumber)

    @allure.step("User date of birth")
    def user_birthday(self, guest):
        s('#dateOfBirthInput').click()
        s('.react-datepicker__month-select').element(by.text(guest.month)).click()
        s('.react-datepicker__year-select').element(by.text(guest.year)).click()
        s(f'.react-datepicker__day--0{guest.day}').click()

    @allure.step(f"User subject {guest.userSubject}")
    def user_subject(self, guest):
        s('#subjectsInput').click().should(be.blank).type(guest.userSubject).press_tab()

    @allure.step("User hobby")
    def user_hobby(self):
        s('[for="hobbies-checkbox-1"]').click()

    @allure.step("Upload photo")
    def fill_picture(self, guest):
        s('#uploadPicture').send_keys(resource.path(guest.userPicture))

    @allure.step(f"User address {guest.userCurrentAddress}")
    def fill_address(self, guest):
        s('#currentAddress').should(be.blank).type(guest.userCurrentAddress)

    @allure.step(f"User state {guest.userState}")
    def fill_state(self, guest):
        s('#react-select-3-input').type(guest.userState).press_enter()

    @allure.step(f"User city {guest.userCity}")
    def fill_city(self, guest):
        s('#react-select-4-input').type(guest.userCity).press_enter()

    @allure.step("Click submit button")
    def fill_submit(self):
        s('#submit').press_enter()

    def register(self, user: User):
        self.open()
        self.fill_first_name(user)
        self.fill_last_name(user)
        self.fill_email(user)
        self.fill_gender(user)
        self.fill_phone_number(user)
        self.user_birthday(user)
        self.user_subject(user)
        self.user_hobby()
        self.fill_picture(user)
        self.fill_address(user)
        self.fill_state(user)
        self.fill_city(user)
        self.fill_submit()

    @allure.step("Comparing result")
    def should_registered_user_with(self, user):
        s('.table-responsive').all('td').even.should(
            have.exact_texts(
                f'{user.firstName} {user.lastName}',
                user.userEmail,
                user.userGender,
                user.userPhoneNumber,
                f'{user.day} {user.month},{user.year}',
                user.userSubject,
                user.userHobby,
                user.userPicture,
                user.userCurrentAddress,
                f'{user.userState} {user.userCity}',
            )
        )
        return self